# 基础管理(Base) <!-- {docsify-ignore-all} -->

主要包含基础类、通用类业务实体的管理，如目录、评论、关注、人员等。

### 实体

|    名称col200   | 代码名col150      |  实体类型col150   | 存储模式col100 | 表名称col200   |    联合主键col100   |  主状态col100   |  权限控制col150  |  启用审计col100    |  备注col500  |
| --------  |------------| -----   |  --------|  --------|  --------|    -------- | -------- | -------- |-------- |
|[活动(ACTIVITY)](module/Base/activity)|activity|主实体|SQL|ACTIVITY|否|否|自控制|否|记录系统中用户或系统行为的日志，可以是实体属性更新、状态变更等。|
|[附件(ATTACHMENT)](module/Base/attachment)|attachment|动态附属实体|SQL|ATTACHMENT|否|否|附属主实体控制（未映射自控）|否|与工作项或文档、需求等实体关联的文件，用于提供额外信息。|
|[关注(ATTENTION)](module/Base/attention)|attention|主实体|SQL|ATTENTION|是|否|附属主实体控制|否|允许用户标记重要的项目或信息，以便于跟踪和及时获取更新。|
|[类别(CATEGORY)](module/Base/category)|category|主实体|SQL|CATEGORY|否|否|自控制|否|逻辑上用于分类存储其他实体的容器。|
|[类别设置(CATEGORY_SETTINGS)](module/Base/category_settings)|category_settings|主实体|SQL|CATEGORY_SETTINGS|否|否|自控制|否||
|[评论(COMMENT)](module/Base/comment)|comment|主实体|SQL|COMMENT|否|否|附属主实体控制|否|用于存储用户在需求、工单、工作项、页面、等内容上发布的评论。|
|[通用规则(COMMON_FLOW)](module/Base/common_flow)|common_flow|主实体|SQL|COMMON_FLOW|否|否|自控制|否||
|[部门(DEPARTMENT)](module/Base/department)|department|主实体|无存储||否|否|自控制|否|用于查看和管理企业的部门信息。|
|[数据字典(DICTIONARY)](module/Base/dictionary_data)|dictionary_data|主实体|SQL|DICTIONARY|否|否|自控制|否|用于记录基础数据字典。|
|[动态数据看板(DYNADASHBOARD)](module/Base/dyna_dashboard)|dyna_dashboard|主实体|SQL|DYNADASHBOARD|否|否|附属主实体控制（未映射自控）|否|配置动态数据看板功能必备。|
|[扩展日志(EXTEND_LOG)](module/Base/extend_log)|extend_log|主实体|SQL|EXTEND_LOG|否|否|自控制|否|记录扩展日志|
|[扩展执行计划(EXTEND_SCHEDULE)](module/Base/extend_schedule)|extend_schedule|主实体|SQL|EXTEND_SCHEDULE|否|否|自控制|否||
|[扩展计划任务(EXTEND_SCHEDULED_TASK)](module/Base/extend_scheduled_task)|extend_scheduled_task|主实体|SQL|EXTEND_SCHEDULED_TASK|否|否|自控制|否||
|[扩展计划任务历史(EXTEND_SCHEDULED_TASK_HIS)](module/Base/extend_scheduled_task_his)|extend_scheduled_task_his|主实体|SQL|EXTEND_SCHEDULED_TASK_HIS|否|否|自控制|否||
|[扩展任务类型(EXTEND_TASK_TYPE)](module/Base/extend_task_type)|extend_task_type|主实体|SQL|EXTEND_TASK_TYPE|否|否|自控制|否||
|[收藏(FAVORITE)](module/Base/favorite)|favorite|主实体|SQL|FAVORITE|是|否|自控制|否|用户自定义的收藏记录，方便快速访问常用的实体或页面。|
|[团队(GROUP)](module/Base/group)|group|主实体|SQL|USER_GROUP|否|否|自控制|否|记录团队信息。|
|[岗位(JOB)](module/Base/job)|job|主实体|无存储||否|否|自控制|否|记录人员岗位信息。|
|[后台管理(MANAGEMENT)](module/Base/management)|management|主实体|无存储||否|否|自控制|否|用于后台管理界面展示。|
|[成员(MEMBER)](module/Base/member)|member|主实体|SQL|MEMBER|是|否|附属主实体控制（未映射自控）|否|公共成员实体。|
|[通知设置(NOTIFY_SETTING)](module/Base/notify_setting)|notify_setting|主实体|无存储||否|否|自控制|否|记录个人通知设置信息|
|[组织(ORGANIZATION)](module/Base/organization)|organization|主实体|无存储||否|否|自控制|否|用于查看和管理企业的组织信息。|
|[文件夹(PORTFOLIO)](module/Base/portfolio)|portfolio|主实体|SQL|PORTFOLIO|否|否|自控制|否|用于项目集查看及管理，可以统一协调项目工作，把控整体进度。|
|[文件夹成员(PORTFOLIO_MEMBER)](module/Base/portfolio_member)|portfolio_member|关系实体|SQL|PORTFOLIO_MEMBER|是|否|附属主实体控制（未映射自控）|否|记录项目集团队中各个成员的角色·，方便管理和协作。|
|[职位(POSITION)](module/Base/position)|position|主实体|SQL|POSITION|否|否|自控制|否|管理人员职位信息|
|[最近访问(RECENT)](module/Base/recent)|recent|主实体|SQL|RECENT|是|否|自控制|否|记录用户最近访问过的实体记录，便于快速回溯和提高工作效率。|
|[分组(SECTION)](module/Base/section)|section|主实体|SQL|SECTION|否|否|自控制|否|用于结构化管理需求、工单等。|
|[序列(SEQUENCE_GENERATOR)](module/Base/sequence_generator)|sequence_generator|主实体|SQL|SEQUENCE_GENERATOR|否|否|自控制|否|生成并存储唯一的序列号。|
|[企业用户(USER)](module/Base/user)|user|主实体|无存储||否|否|自控制|否|记录使用PLM系统的用户信息。（无存储，通过外部服务获取用户数据）|
|[版本(VERSION)](module/Base/version)|version|主实体|SQL|VERSION|否|否|附属主实体控制（未映射自控）|否|用于管理和记录软件的版本历史和变更。|

