### **安装说明**

#### 前提条件

- CPU >= 4 核
- RAM >= 16 GB
- Disk >= 50 GB
- Docker >= 24.0.0 & Docker Compose >= v2.26.1

> 如果你并没有在本机安装 Docker（Windows、Mac，或者 Linux）, 可以参考文档 [Install Docker Engine](https://docs.docker.com/engine/install/) 自行安装。

#### 启动AIFACTORY服务

1. 克隆仓库：

```bash
$ git clone https://gitee.com/ibizlab/aifactory.git
```

2. 进入 **compose** 文件夹，利用提前编译好的 Docker 镜像启动服务器：

```bash
$ cd aifactory/deploy/compose
$ docker compose -f docker-compose.yml --env-file .env up -d

# ARM64架构启动:
# docker-compose -f docker-compose-arm64.yml --env-file=.env up -d

# 如果使用实验室模式，根据变量注释提示调整**.lab**文件内对应参数,和在线实验室联动:
# docker compose -f docker-compose-lab.yml --env-file .lab up -d
```

> [!TIP]
> 如果你遇到 Docker 镜像拉不下来的问题，可以在 **deploy/compose/.env** 文件内根据变量 `IMAGE_URL` 的注释提示选择华为云或者阿里云的相应镜像。
>
> - 华为云镜像名：`swr.ap-southeast-1.myhuaweicloud.com/find1024/`
> - 阿里云镜像名：`registry.cn-shanghai.aliyuncs.com/1024find/`
>
> 如果你想修改MySQL、ZooKeeper、Redis、Nacos、EMQX服务为本地服务（开发模式不支持），可以在 **deploy/compose/.env** 文件内根据变量注释提示调整对应参数。

4. 服务器启动成功后再次确认服务器状态：

```bash
$ docker logs -f aifactoryservice
```

_出现以下界面提示说明服务器启动成功：_

```bash
[DEBUG] n.i.central.cloud.core.ServiceHubBase    : 系统[ibizaifactory]已经注册
[DEBUG] n.i.central.cloud.core.ServiceHubBase    : Heap Memory Usage:
[DEBUG] n.i.central.cloud.core.ServiceHubBase    : Init: 786432000
[DEBUG] n.i.central.cloud.core.ServiceHubBase    : Used: 1489565680
[DEBUG] n.i.central.cloud.core.ServiceHubBase    : Committed: 4904714240
[DEBUG] n.i.central.cloud.core.ServiceHubBase    : Max: 11169955840
[DEBUG] n.i.central.cloud.core.ServiceHubBase    : Non-Heap Memory Usage:
[DEBUG] n.i.central.cloud.core.ServiceHubBase    : Init: 2555904
[DEBUG] n.i.central.cloud.core.ServiceHubBase    : Used: 222739928
[DEBUG] n.i.central.cloud.core.ServiceHubBase    : Committed: 231342080
[DEBUG] n.i.central.cloud.core.ServiceHubBase    : Max: -1
```

等待启动完成访问

假定本机使用localhost访问，如果跨机器访问请将localhost更换为服务器ip地址或域名：

**iBizAifactory桌面端**：http://localhost:30280/aifactoryweb/

**UAA系统管理**：http://localhost:32666

#### 数据卷

> [!CAUTION]
> 请注意，本次更新替换文件映射为Docker数据卷，升级前请做好数据备份。

- mysql_data：MySQL数据库的数据卷
- allinone_data：ibiz-ebsx-allinone服务存放文件的数据卷，例如：图片，附件等
- postgres_data：PostgreSQL数据库的数据卷

### 常见错误

##### 问题1、资源不足

本系统部署模式走微服务和前后分离，启动需要有多个独立服务，流畅运行建议16G或以上，如果启动后看到有容器未能启动成功或者启动成功又自行退出，许多人反映是mysql和nacos服务，这种情况下基本都是资源不足。

另外虽然主机资源充足，但是Windows或MacOS上使用了DockerDesktop，docker虚拟机的资源阈值分配不够，也烦请提高分配额。