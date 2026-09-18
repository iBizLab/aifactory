#!/usr/bin/env python3
"""
看守进程 (Watchdog) 用于监控 SkillRunner 是否假死。
每隔 30 秒检查心跳文件，若超过 120 秒未更新则重启 Runner。

用法:
  # 使用默认配置
  afsr-daemon

  # 指定环境文件
  afsr-daemon -f .envprod

  # 传递完整参数给子进程（推荐）
  afsr-daemon -- afsr -e KEY=value -f .envprod

  # 使用 Python 脚本 + 参数
  afsr-daemon -c skill_runner.py -- -e KEY=value
"""

import os
import sys
import time
import subprocess
import argparse
import signal
import logging
from pathlib import Path

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("Watchdog")

# 默认参数
DEFAULT_RUNNER_SCRIPT = "afsr"          # 你的 SkillRunner 主脚本
DEFAULT_HEARTBEAT_FILE = ".skillrunner_heartbeat"
CHECK_INTERVAL = 30                          # 秒
HEARTBEAT_TIMEOUT = 150                      # 秒

class Watchdog:
    def __init__(self, runner_cmd, heartbeat_file, env_file=None, runner_args=None):
        self.runner_cmd = runner_cmd
        self.heartbeat_file = Path(heartbeat_file).resolve()
        self.env_file = env_file
        self.runner_args = runner_args or []
        self.process = None
        self.stop_requested = False

    def start_runner(self):
        """启动子进程"""
        if self.process is not None:
            self.stop_runner()

        runner_cmd_str = str(self.runner_cmd)

        # 构建启动命令
        cmd = []

        # 如果是 .py 文件且存在，用 python 执行
        if Path(runner_cmd_str).exists() and runner_cmd_str.endswith('.py'):
            cmd = [sys.executable, runner_cmd_str]
        else:
            cmd = [runner_cmd_str]

        # 添加透传参数
        if self.runner_args:
            cmd.extend(self.runner_args)



        logger.info(f"启动 SkillRunner: {' '.join(cmd)}")

        try:
            self.process = subprocess.Popen(cmd)
        except FileNotFoundError:
            logger.error(f"命令或脚本未找到: {runner_cmd_str}")
            logger.error("请确保 afsr 已安装 (pip install -e .) 或使用 -c 指定脚本路径")
            self.process = None
        except Exception as e:
            logger.error(f"启动失败: {e}")
            self.process = None

    def stop_runner(self):
        """终止子进程"""
        if self.process is None:
            return
        if self.process.poll() is None:  # 仍在运行
            logger.info("终止 SkillRunner 进程...")
            self.process.terminate()
            try:
                self.process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                logger.warning("进程未响应 SIGTERM，强制 kill")
                self.process.kill()
                self.process.wait()
        self.process = None

    def is_heartbeat_alive(self):
        """检查心跳文件是否新鲜"""
        if not self.heartbeat_file.exists():
            logger.warning("心跳文件不存在")
            return False
        try:
            with open(self.heartbeat_file, 'r') as f:
                timestamp_str = f.read().strip()
            if not timestamp_str:
                logger.warning("心跳文件为空")
                return False
            last_beat = float(timestamp_str)
            age = time.time() - last_beat
            if age > HEARTBEAT_TIMEOUT:
                logger.warning(f"心跳超时: {age:.1f}s > {HEARTBEAT_TIMEOUT}s")
                return False
            logger.debug(f"心跳正常, 距今 {age:.1f}s")
            return True
        except Exception as e:
            logger.error(f"读取心跳文件失败: {e}")
            return False

    def run(self):
        """主循环"""
        # 首次启动
        self.start_runner()
        time.sleep(5)

        while not self.stop_requested:
            # 检查子进程是否意外退出
            if self.process is not None and self.process.poll() is not None:
                logger.warning("SkillRunner 进程意外退出，将重新启动")
                self.process = None

            # 如果进程不在运行，则启动它
            if self.process is None:
                self.start_runner()
                time.sleep(5)

            # 检查心跳
            if not self.is_heartbeat_alive():
                logger.warning("心跳检测失败，重启 SkillRunner")
                self.stop_runner()
                self.start_runner()
                time.sleep(5)

            # 等待下一次检查
            for _ in range(CHECK_INTERVAL):
                if self.stop_requested:
                    break
                time.sleep(1)

        # 循环结束，清理
        self.stop_runner()
        logger.info("看守进程退出")

    def signal_handler(self, signum, frame):
        """信号处理，用于优雅退出"""
        logger.info(f"收到信号 {signum}，准备退出...")
        self.stop_requested = True


def main():
    global CHECK_INTERVAL, HEARTBEAT_TIMEOUT

    parser = argparse.ArgumentParser(
        description="SkillRunner 看守进程",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # 使用默认配置
  afsr-daemon

  # 指定环境文件
  afsr-daemon -f .envprod

  # 传递完整参数给子进程（推荐）
  afsr-daemon -- afsr -e KEY=value -f .envprod

  # 使用 Python 脚本 + 参数
  afsr-daemon -c skill_runner.py -- -e KEY=value

  # 自定义心跳超时
  afsr-daemon --timeout 120 -f .envprod
        """
    )

    parser.add_argument(
        "--runner-script","-c",
        dest="runner_script",
        default=DEFAULT_RUNNER_SCRIPT,
        help=f"SkillRunner 主脚本路径 (默认: {DEFAULT_RUNNER_SCRIPT})"
    )

    parser.add_argument(
        "--env-file", "-f",
        dest="env_file",
        default=".env",
        help=".env 配置文件路径 (默认: .env)"
    )

    parser.add_argument(
        "--interval",
        type=int,
        default=CHECK_INTERVAL,
        help=f"检查间隔秒数 (默认: {CHECK_INTERVAL})"
    )

    parser.add_argument(
        "--timeout",
        type=int,
        default=HEARTBEAT_TIMEOUT,
        help=f"心跳超时秒数 (默认: {HEARTBEAT_TIMEOUT})"
    )

    # 解析已知参数，剩余参数透传给子进程
    args, remaining_args = parser.parse_known_args()

    # 根据 env-file 生成心跳文件名
    heartbeat_file = Path.cwd() / DEFAULT_HEARTBEAT_FILE
    if args.env_file and args.env_file != '.env':
        heartbeat_file = Path.cwd() / f"{Path(args.env_file).name}_heartbeat"

    # 更新全局常量
    CHECK_INTERVAL = args.interval
    HEARTBEAT_TIMEOUT = args.timeout

    logger.info(f"启动看守进程")
    logger.info(f"  启动命令: {args.runner_script}")
    logger.info(f"  环境文件: {args.env_file}")
    logger.info(f"  透传参数: {remaining_args}")
    logger.info(f"  心跳文件: {heartbeat_file}")
    logger.info(f"  检查间隔: {CHECK_INTERVAL}s")
    logger.info(f"  心跳超时: {HEARTBEAT_TIMEOUT}s")



    # 如果没有，且 env_file 有值且不是默认 .env，自动添加
    if args.env_file and args.env_file != '.env' :
        remaining_args.extend(['-f', args.env_file])

    watchdog = Watchdog(
        runner_cmd=args.runner_script,
        heartbeat_file=heartbeat_file,
        env_file=args.env_file,
        runner_args=remaining_args
    )

    # 注册信号处理
    signal.signal(signal.SIGINT, watchdog.signal_handler)
    signal.signal(signal.SIGTERM, watchdog.signal_handler)

    watchdog.run()


if __name__ == "__main__":
    main()