# iBizAIFactory


#### 系统模块

|    模块名称col200   | 代码名col200      |  模型组col200   |   备注col400  |
| --------  |------------| -----    |-------- |
|[智能](module/ai)|ai|||
|[知识管理](module/Wiki)|Wiki||主要包含知识空间相关业务实体的管理，如：空间、页面等。|
|[基础管理](module/Base)|Base||主要包含基础类、通用类业务实体的管理，如目录、评论、关注、人员等。|
|[全文检索](module/FTR)|FTR||全文检索相关业务实体管理。|
|[系统管理](module/ibizsysmgr)|ibizsysmgr|ibizsysmgr[^ibizsysmgr]|部门及人员业务实体的映射。|
|[ebsx系统管理](module/ebsx)|ebsx|ebsx模型组[^ebsx]|ebsx部门及人员业务实体的映射。|
|[模型扩展](module/extension)|extension||主要包含模型扩展类实体。|
|[效能度量](module/Insight)|Insight||主要包含效能度量相关业务实体的管理，如仪表盘、报表等。|
|[meta](module/meta)|meta|||


#### 服务接口

|  中文名col200      |   代码名col200 |   备注col600  |
|  --------   |------------  |  -----   |
|[ServiceAPI](api/ServiceAPI/ServiceAPI)|ServiceAPI||

#### 对接外部接口

|  中文名col200      |   代码名col200  |    备注col600  |
|  --------   |------------|    -----   |
|[ebsx系统管理](client/iBizRTClient/iBizRTClient)|iBizRTClient||
|[模型扩展](client/extension/extension)|extension||
|[系统管理](client/ibizsysmgr/ibizsysmgr)|ibizsysmgr||

#### 系统应用

|  中文名col200      |   代码名col200  |   备注col600  |
|  --------   |------------ |  -----   |
|[<i class="fa-solid fa-desktop"></i>AI Factory](app/aifactoryweb)|aifactoryweb||


#### 国际化支持

|  中文名col200      |   代码名col200  |   资源项col100    |   备注col500  |
|  --------   |------------ |  ----- |  :-----:   |
|[简体中文](i18n/ZH_CN)|ZH_CN|5||

#### 数据库支持

|  中文名col200      |   代码名col200  |   备注col600  |
|  --------   |------------|  -----   |
|[POSTGRESQL](db/POSTGRESQL)|POSTGRESQL||
|[MYSQL5](db/MYSQL5)|MYSQL5||
[^ibizsysmgr]: ibizsysmgr系统模型组
[^ebsx]: allinone模型组
