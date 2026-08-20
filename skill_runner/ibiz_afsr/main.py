import os
import logging
from logging.handlers import RotatingFileHandler # 👈 引入按大小切分的 Handler

pid = os.getpid()

# 使用 RotatingFileHandler 替换普通的 FileHandler
file_handler = RotatingFileHandler(
    filename=f"afsr_{pid}.log",
    maxBytes=10 * 1024 * 1024,  # 单个文件最大 10 MB
    backupCount=5,               # 最多保留 5 个历史备份 (app.log.1, app.log.2 ...)
    encoding="utf-8"
)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    handlers=[
        file_handler,            # 👈 使用按大小切分的文件处理器
        logging.StreamHandler()  # 同时控制台输出
    ],
    force=True  # 强制生效
)

# 2. 创建主入口的 logger
logger = logging.getLogger(__name__)

# main.py
try:
    from .skill_runner import ToolCallHandler
except ImportError:
    from skill_runner import ToolCallHandler

import argparse
import re
from urllib.parse import urlparse, urlunparse
import io
import shutil
import zipfile
import requests
from pathlib import Path

import logging

# 2. 创建主入口的 logger
logger = logging.getLogger(__name__)


def normalize_aifactory_env():
    """规范化 AIFACTORY_URL"""
    raw_url = os.environ.get('AIFACTORY_URL') or os.environ.get('AIFACTORY_BASE_URL')
    if not raw_url:
        raise Exception("错误：请设置环境变量 AIFACTORY_URL 如 https://aifactory.ibizlab.cn/api/ibizaifactory__aifactoryweb/factories/ai.iBizIntelligence/skill_runners")
    raw_url = raw_url.strip().rstrip('/')

    parsed = urlparse(raw_url)
    scheme = parsed.scheme or "http"
    netloc = parsed.netloc or parsed.path.split('/')[0]

    full_path = parsed.path if parsed.scheme else "/" + "/".join(parsed.path.split('/')[1:])
    full_path = full_path.rstrip('/')

    match = re.search(r'(.*)(/factories/.+?/skill_runners)', full_path)

    if match:
        prefix = match.group(1).rstrip('/')
        core_path = match.group(2)
        final_path = f"{prefix}{core_path}"
    else:
        default_suffix = "/api/ibizaifactory__aifactoryweb/factories/ai.iBizIntelligence/skill_runners"
        final_path = f"{full_path}{default_suffix}"

    normalized_url = urlunparse((scheme, netloc, final_path, '', '', ''))
    os.environ['AIFACTORY_URL'] = normalized_url
    logger.info(f"🔄 AIFACTORY_URL 环境变量已规范化为: {normalized_url}")


def load_env_file(env_file: str):
    """加载 .env 配置文件"""
    if not env_file:
        return

    path = Path(env_file)
    if not path.exists():
        logger.warning(f"⚠️  配置文件 {env_file} 不存在")
        return

    try:
        from dotenv import load_dotenv
        load_dotenv(dotenv_path=env_file, override=True)
        logger.info(f"✅ 从 .env 配置文件加载: {env_file}")
    except ImportError:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        key, _, value = line.partition('=')
                        os.environ[key.strip()] = value.strip()
            logger.info(f"✅ 从 .env 配置文件加载: {env_file}")
        except Exception as e:
            logger.error(f"❌ 读取配置文件失败: {e}")

def set_env_from_args(args):
    """将命令行参数写入环境变量（优先级最高）"""
    mapping = {
        'aifactory_url': 'AIFACTORY_URL',
        'aifactory_token': 'AIFACTORY_TOKEN',
        'aifactory_mqtt': 'AIFACTORY_MQTT',
        'aifactory_skills': 'AIFACTORY_SKILLS',
        'aifactory_workspace': 'AIFACTORY_SKILL_WORKSPACE',
        'bot_plugins': 'BOT_PLUGINS',
        'skill_repo': 'AIFACTORY_SKILLREPO',
    }

    for arg_name, env_name in mapping.items():
        value = getattr(args, arg_name, None)
        if value is not None:
            os.environ[env_name] = value
            logger.info(f"[命令行] {env_name} = {value}")


def fetch_and_save_config():

    base_url = os.environ.get('AIFACTORY_URL')
    config_url = f"{base_url}/get_config"

    logger.info(f"使用基础URL: {base_url}")
    logger.info(f"请求配置地址: {config_url}")

    try:
        resp = requests.get(config_url, timeout=30)
        resp.raise_for_status()
        config = resp.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"❌ 请求失败: {e}")
        return False

    added_count = 0
    for key, value in config.items():
        str_key = str(key).strip().upper()
        str_val = str(value).strip() if value is not None else ""

        if os.environ.get(str_key) is not None:
            logger.info(f"ℹ️  跳过已存在环境变量: {str_key}")
        else:
            os.environ[str_key] = str_val
            logger.info(f"➕ 注入新环境变量: {str_key}={str_val}")
            added_count += 1

    if added_count > 0:
        logger.info(f"✅ 成功向当前进程注入 {added_count} 个新环境变量")
    else:
        logger.info("ℹ️  无新环境变量需要注入")


    return True

def fetch_openai_env():
    if not os.getenv('OPENAI_BASE_URL'):
        os.environ['OPENAI_BASE_URL'] = os.environ['AIFACTORY_URL'].replace("/skill_runners","/compatible-mode/v1")
    if not os.getenv('OPENAI_API_KEY'):
        os.environ['OPENAI_API_KEY'] = os.environ['AIFACTORY_TOKEN']
    if not os.getenv('OPENAI_CHAT_MODEL_ID'):
        os.environ['OPENAI_CHAT_MODEL_ID'] = "kb_switch@DynamicAgent"

def sync_git_skills():
    """同步技能仓库"""
    repo_url = os.getenv('AIFACTORY_SKILLREPO')
    skills_dir = os.getenv('AIFACTORY_SKILLS')

    if not repo_url or not skills_dir:
        return

    repo_url = repo_url.strip().rstrip('/')
    if not (repo_url.startswith('http://') or repo_url.startswith('https://')):
        logger.warning("⚠️  AIFACTORY_SKILLREPO 不是有效的 HTTP(S) 地址，跳过下载")
        return

    skills_path = Path(skills_dir)
    skills_path.mkdir(parents=True, exist_ok=True)

    clean_url = repo_url[:-4] if repo_url.endswith('.git') else repo_url
    if repo_url.lower().endswith('.zip'):
        zip_url = repo_url
    elif "github.com" in clean_url.lower():
        zip_url = f"{clean_url}/archive/refs/heads/main.zip"
    elif "gitee.com" in clean_url.lower():
        zip_url = f"{clean_url}/repository/archive/master.zip"
    else:
        zip_url = f"{clean_url}/-/archive/master/archive.zip"

    logger.info(f"🚀 开始从 {zip_url} 下载/更新技能包...")
    try:
        resp = requests.get(zip_url, timeout=60)
        resp.raise_for_status()

        with zipfile.ZipFile(io.BytesIO(resp.content)) as zip_ref:
            namelist = zip_ref.namelist()
            if not namelist:
                logger.warning("⚠️  下载的 Zip 包为空")
                return

            for member in zip_ref.infolist():
                original_path = member.filename

                if '/skills/' in original_path:
                    relative_path = original_path.split('/skills/', 1)[1]

                    if not relative_path.strip():
                        continue

                    member.filename = relative_path

                    target_file_path = skills_path / member.filename

                    if member.is_dir():
                        target_file_path.mkdir(parents=True, exist_ok=True)
                    else:
                        target_file_path.parent.mkdir(parents=True, exist_ok=True)
                        with zip_ref.open(original_path) as source, open(target_file_path, "wb") as target:
                            shutil.copyfileobj(source, target)

        logger.info(f"✅ 成功提取 Git 仓库中 [skills] 目录下的所有内容，已平铺覆盖至: {skills_path}")

    except requests.exceptions.RequestException as e:
        logger.error(f"❌ 技能包下载失败: {e}")
    except zipfile.BadZipFile:
        logger.error("❌ 下载的文件不是有效的 Zip 格式")


def parse_args():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(
        description="AI Factory Skill Runner - Cloud-edge collaborative agent",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # 使用默认 .env
  afsr

  # 使用指定的 .env 配置文件
  afsr --env-file .envprod

  # 命令行参数覆盖配置文件
  afsr --env-file .envprod --url https://another.example.com --token new-token

  # 全部使用命令行参数
  afsr --url https://aifactory.example.com --token your-token \\
      --mqtt wss://mqtt.example.com/mqtt \\
      --skills /path/to/skills \\
      --workspace /path/to/workspace \\
      --plugins '[{"type":"qq","bot_id":"xxx"}]'
        """
    )

    parser.add_argument(
        "--env-file", "-f",
        dest="env_file",
        default=".env",
        help=".env 配置文件路径 (默认: .env)"
    )

    parser.add_argument(
        "--url", "-u",
        dest="aifactory_url",
        help="AI Factory 服务地址 (AIFACTORY_URL)，优先级高于配置文件"
    )

    parser.add_argument(
        "--token", "-t",
        dest="aifactory_token",
        help="认证 Token (AIFACTORY_TOKEN)，优先级高于配置文件"
    )

    parser.add_argument(
        "--mqtt", "-m",
        dest="aifactory_mqtt",
        help="MQTT WebSocket 服务器地址 (AIFACTORY_MQTT)，优先级高于配置文件"
    )

    parser.add_argument(
        "--skills", "-s",
        dest="aifactory_skills",
        help="技能目录路径 (AIFACTORY_SKILLS)，优先级高于配置文件"
    )

    parser.add_argument(
        "--workspace", "-w",
        dest="aifactory_workspace",
        help="工作区路径 (AIFACTORY_SKILL_WORKSPACE)，优先级高于配置文件"
    )

    parser.add_argument(
        "--plugins", "-p",
        dest="bot_plugins",
        help='机器人插件配置 JSON 字符串 (BOT_PLUGINS)，优先级高于配置文件'
    )

    parser.add_argument(
        "--skill-repo",
        dest="skill_repo",
        help="技能仓库地址 (AIFACTORY_SKILLREPO)，优先级高于配置文件"
    )

    parser.add_argument(
        "-e", "--env",
        dest="env_vars",
        action="append",
        help="设置额外环境变量，格式: KEY=VALUE (可多次使用)"
    )

    parser.add_argument(
        "--no-sync",
        dest="no_sync",
        action="store_true",
        help="跳过技能仓库同步"
    )

    return parser.parse_args()


def print_config_summary():
    """打印配置摘要"""
    logger.info("=" * 50)
    logger.info("AI Factory Skill Runner 启动")
    logger.info("=" * 50)
    logger.info(f"  AIFACTORY_URL:      {os.environ.get('AIFACTORY_URL', '未设置')}")
    if os.environ.get('AIFACTORY_TOKEN'):
        logger.info(f"  AIFACTORY_TOKEN:     {'*' * 8}...")
    else:
        logger.info(f"  AIFACTORY_TOKEN:     未设置")
    logger.info(f"  AIFACTORY_MQTT:      {os.environ.get('AIFACTORY_MQTT', '未设置')}")
    logger.info(f"  AIFACTORY_SKILLS:    {os.environ.get('AIFACTORY_SKILLS', '未设置')}")
    logger.info(f"  AIFACTORY_WORKSPACE: {os.environ.get('AIFACTORY_SKILL_WORKSPACE', '未设置')}")
    if os.environ.get('AIFACTORY_SKILLREPO'):
        logger.info(f"  AIFACTORY_SKILLREPO: {os.environ.get('AIFACTORY_SKILLREPO')}")
    if os.environ.get('BOT_PLUGINS'):
        logger.info(f"  BOT_PLUGINS:         {os.environ.get('BOT_PLUGINS')}")
    logger.info("=" * 50)


def prompt_for_missing_env(missing_keys):
    """只提示缺失的环境变量"""
    print("\n" + "=" * 50)
    print(f"⚠️  缺少必需的环境变量: {', '.join(missing_keys)}")
    print("=" * 50)
    print("请手动输入以下配置：\n")

    config = {}

    for key in missing_keys:
        if key == 'AIFACTORY_URL':
            default = "https://aifactory.ibizlab.cn/api/ibizaifactory__aifactoryweb/factories/ai.iBizIntelligence/skill_runners"
            value = input(f"请输入 {key} [{default}]: ").strip()
            config[key] = value if value else default

        elif key == 'AIFACTORY_TOKEN':
            while True:
                value = input(f"请输入 {key}: ").strip()
                if value:
                    config[key] = value
                    break
                print("❌ AIFACTORY_TOKEN 不能为空，请重新输入")

        elif key in ['AIFACTORY_MQTT', 'AIFACTORY_SKILLREPO']:
            defaults = {
                'AIFACTORY_MQTT': 'wss://mqtt.ibizlab.cn/mqtt',
                'AIFACTORY_SKILLREPO': 'https://code.ibizlab.cn/product_catalog/aifactory/aifactory-skill'
            }
            default = defaults.get(key)
            value = input(f"请输入 {key} [{default}]: ").strip()
            config[key] = value if value else default

    print("\n✅ 配置录入完成\n")
    return config


def save_env_file(config, env_file=".env"):
    """
    保存配置到 .env 文件
    - 如果 key 已存在，覆盖其值
    - 如果 key 不存在，追加到文件末尾
    """
    try:
        env_path = Path(env_file)

        # 1. 如果文件存在，读取现有配置
        existing_config = {}
        if env_path.exists():
            with open(env_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        key, _, value = line.partition('=')
                        # 去掉引号
                        value = value.strip().strip('"').strip("'")
                        existing_config[key.strip()] = value

        # 2. 用新配置覆盖（或追加）
        existing_config.update(config)

        # 3. 写回文件
        with open(env_path, 'w', encoding='utf-8') as f:
            for key, value in existing_config.items():
                # 如果值包含特殊字符，用引号包裹
                if any(c in value for c in [' ', '#', '=']):
                    f.write(f'{key}="{value}"\n')
                else:
                    f.write(f'{key}={value}\n')

        logger.info(f"✅ 配置已保存到 {env_file}")
        return True

    except Exception as e:
        logger.error(f"⚠️  保存配置文件失败: {e}")
        return False


def main():
    """主入口"""
    args = parse_args()

    # 1. 加载 .env 配置文件
    load_env_file(args.env_file)

    # 2. 处理 -e 参数（类似 docker -e）
    if args.env_vars:
        for env_str in args.env_vars:
            try:
                key, value = env_str.split('=', 1)
                key = key.strip().upper()
                value = value.strip()
                os.environ[key] = value
                logger.info(f"[ -e ] {key}={value}")
            except ValueError:
                logger.warning(f"⚠️  忽略无效的环境变量格式: {env_str} (应为 KEY=VALUE)")
                continue

    # 2. 命令行参数覆盖（优先级最高）
    set_env_from_args(args)

    required = ['AIFACTORY_URL', 'AIFACTORY_TOKEN']
    missing = [k for k in required if k not in os.environ or not os.environ[k]]

    if missing:
        config = prompt_for_missing_env(missing)

        # 写入环境变量
        for key, value in config.items():
            os.environ[key] = value

        # 询问是否保存到 .env（只保存刚输入的配置）
        save_choice = input("\n是否将配置保存到 .env 文件？(y/n) [y]: ").strip().lower()
        if save_choice != 'n':
            save_env_file(config, args.env_file)

        logger.info("✅ 配置已加载，继续启动...")

    normalize_aifactory_env()
    fetch_openai_env()

    logger.info("=== 开始获取配置 ===")
    success = fetch_and_save_config()
    if success:
        logger.info("=== 配置获取完成 ===")

    # 1. 处理 AIFACTORY_SKILL_WORKSPACE
    workspace_env = os.getenv('AIFACTORY_SKILL_WORKSPACE')

    # 如果环境变量未设置，默认取当前工作目录 os.getcwd()
    base_path = workspace_env if workspace_env else os.getcwd()

    # 规范化路径（去除结尾斜杠等）
    base_path = os.path.normpath(base_path)

    # 判断目录含 workspace (忽略大小写)
    if base_path.lower().index('workspace')>=0:
        target_workspace = base_path
    else:
        target_workspace = os.path.join(base_path, 'workspace')

    # 自动创建目录（如果不存在）
    if not os.path.exists(target_workspace):
        os.makedirs(target_workspace, exist_ok=True)
        logger.info(f"📁 目标工作区目录不存在，已自动创建: {target_workspace}")

    # 更新/写回环境变量
    os.environ['AIFACTORY_SKILL_WORKSPACE'] = target_workspace
    logger.info(f"📁 最终确定的 AIFACTORY_SKILL_WORKSPACE 为: {target_workspace}")

    # 2. 处理 AIFACTORY_SKILLS：如果未设置，取 target_workspace 的同级 (上级目录/skills) 文件夹
    if not os.getenv('AIFACTORY_SKILLS'):
        parent_dir = os.path.dirname(target_workspace)
        os.environ['AIFACTORY_SKILLS'] = os.path.join(parent_dir, 'skills')
        logger.info(f"📁 自动初始化 AIFACTORY_SKILLS 为: {os.environ['AIFACTORY_SKILLS']}")

    # 3. 验证必需的环境变量
    required = ['AIFACTORY_MQTT', 'AIFACTORY_SKILLREPO']
    missing = [k for k in required if k not in os.environ or not os.environ[k]]

    if missing:
        config = prompt_for_missing_env(missing)

        # 写入环境变量
        for key, value in config.items():
            os.environ[key] = value

        # 询问是否保存到 .env（只保存刚输入的配置）
        save_choice = input("\n是否将配置保存到 .env 文件？(y/n) [y]: ").strip().lower()
        if save_choice != 'n':
            save_env_file(config, args.env_file)

        logger.info("✅ 配置已加载，继续启动...")

    print_config_summary()

    if not args.no_sync:
        sync_git_skills()

    logger.info("=== 启动技能处理器 ===")
    handler = ToolCallHandler()
    handler.start_listening()


if __name__ == "__main__":
    main()