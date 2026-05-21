# 处理逻辑 <!-- {docsify-ignore-all} -->


## [智能体(AI_AGENT)](module/ai/ai_agent.md) :id=ai_agent

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[reload_aiagents](module/ai/ai_agent/logic/reload_aiagents)|reload_aiagents|无||重载AI代理对象|



## [智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context.md) :id=ai_agent_context

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[agent_flow_clone](module/ai/ai_agent_context/logic/agent_flow_clone)|agent_flow_clone|无||克隆flow智能体|
|[agent_flow_templ](module/ai/ai_agent_context/logic/agent_flow_templ)|agent_flow_templ|AI交谈逻辑||智能体处理流(模板)|
|[dynamic_agent_dataset](module/ai/ai_agent_context/logic/dynamic_agent_dataset)|dynamic_agent_dataset|无|||
|[fill_with_agent](module/ai/ai_agent_context/logic/fill_with_agent)|fill_with_agent|无||由插件补充填充，此配置仅作为填充入口|
|[get_by_code](module/ai/ai_agent_context/logic/get_by_code)|get_by_code|无|||
|[reload_aiagents](module/ai/ai_agent_context/logic/reload_aiagents)|reload_aiagents|无||重载AI代理对象|
|[交谈全文内容推理](module/ai/ai_agent_context/logic/chat_fulltext_reason)|chat_fulltext_reason|AI交谈逻辑|||
|[交谈分析文档](module/ai/ai_agent_context/logic/chat_analyze_documents)|chat_analyze_documents|AI交谈逻辑|||
|[交谈执行技能](module/ai/ai_agent_context/logic/chat_execute_skill)|chat_execute_skill|AI交谈逻辑|||
|[交谈执行行为](module/ai/ai_agent_context/logic/chat_execute_action)|chat_execute_action|AI交谈逻辑|||
|[创建之前](module/ai/ai_agent_context/logic/beforefile)|beforefile|无|||
|[创建智能体](module/ai/ai_agent_context/logic/create_ai_agent_context)|create_ai_agent_context|AI交谈逻辑|||
|[删除logic扩展模型](module/ai/ai_agent_context/logic/delete_extend_model)|delete_extend_model|无|||
|[建立默认flow交谈逻辑](module/ai/ai_agent_context/logic/create_default_flow_logic)|create_default_flow_logic|无|||
|[批量执行](module/ai/ai_agent_context/logic/batch_execution)|batch_execution|无|||
|[查表审查](module/ai/ai_agent_context/logic/lookup)|lookup|AI交谈逻辑|||
|[深度研究](module/ai/ai_agent_context/logic/deep_research)|deep_research|AI交谈逻辑|||
|[绑定智能体](module/ai/ai_agent_context/logic/bind)|bind|无|||
|[辅助生成引导提示词（停用）](module/ai/ai_agent_context/logic/guided_prompt)|guided_prompt|AI交谈逻辑|||


## [智能体会话(AI_AGENT_CONVERSATION)](module/ai/ai_agent_conversation.md) :id=ai_agent_conversation

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[delete](module/ai/ai_agent_conversation/logic/delete)|delete|无||设置结束状态|
|[提取session前缀并存储](module/ai/ai_agent_conversation/logic/extract_session_type)|extract_session_type|无|||
|[清空消息](module/ai/ai_agent_conversation/logic/clear_message)|clear_message|无|||
|[除指定外清空会话](module/ai/ai_agent_conversation/logic/clear_all_except)|clear_all_except|无|||




## [智能体记忆任务实例(AI_AGENT_MEMORY_TASK)](module/ai/ai_agent_memory_task.md) :id=ai_agent_memory_task

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[保存记忆分块](module/ai/ai_agent_memory_task/logic/save_chunk)|save_chunk|无|||
|[填充默认文档标识](module/ai/ai_agent_memory_task/logic/fill_default_doc_id)|fill_default_doc_id|无|||
|[更新每日记忆文档](module/ai/ai_agent_memory_task/logic/update_daily_log)|update_daily_log|无|||
|[获取记忆分块](module/ai/ai_agent_memory_task/logic/get_chunk)|get_chunk|无|||
|[获取记忆文档](module/ai/ai_agent_memory_task/logic/get_document)|get_document|无|||
|[记忆提取并存储](module/ai/ai_agent_memory_task/logic/extract_and_store)|extract_and_store|无|||


## [智能体会话消息(AI_AGENT_MESSAGE)](module/ai/ai_agent_message.md) :id=ai_agent_message

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[取消点赞或点踩](module/ai/ai_agent_message/logic/cancel_feedback)|cancel_feedback|无|||
|[点赞](module/ai/ai_agent_message/logic/like)|like|无|||
|[点踩](module/ai/ai_agent_message/logic/dislike)|dislike|无|||


## [智能体会话(AI_AGENT_SESSION)](module/ai/ai_agent_session.md) :id=ai_agent_session

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[get_info](module/ai/ai_agent_session/logic/get_info)|get_info|无|||



## [AI客户端凭证(AI_CLIENT_CREDENTIAL)](module/ai/ai_client_credential.md) :id=ai_client_credential

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[exrouter](module/ai/ai_client_credential/logic/exrouter)|exrouter|无|||


## [AI凭证(AI_CREDENTIAL)](module/ai/ai_credential.md) :id=ai_credential

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[获取Cloud配置](module/ai/ai_credential/logic/get_cloud_config)|get_cloud_config|无|||


## [知识库文档分块(AI_KB_CHUNK)](module/ai/ai_kb_chunk.md) :id=ai_kb_chunk

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[检索测试](module/ai/ai_kb_chunk/logic/retrieval_test)|retrieval_test|无|||
|[获取pageIndex信息](module/ai/ai_kb_chunk/logic/get_page_index_info)|get_page_index_info|无|||



## [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document.md) :id=ai_kb_document

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[ai_kb_document_type_counters](module/ai/ai_kb_document/logic/ai_kb_document_type_counters)|ai_kb_document_type_counters|无|||
|[全文推理](module/ai/ai_kb_document/logic/reason)|reason|无|||
|[参考引用](module/ai/ai_kb_document/logic/references)|references|无|||
|[文档批量解析](module/ai/ai_kb_document/logic/batch_parse)|batch_parse|无|||
|[文档解析处理](module/ai/ai_kb_document/logic/parse)|parse|无||恢复文件类文档解析时仅变更状态|
|[文档重新解析](module/ai/ai_kb_document/logic/reparse)|reparse|无|||
|[未切片数据集](module/ai/ai_kb_document/logic/unparsed)|unparsed|无|||
|[构建切片](module/ai/ai_kb_document/logic/build_chunk)|build_chunk|无|||
|[构建索引](module/ai/ai_kb_document/logic/build_index)|build_index|无|||
|[统计文档类型并更新知识库](module/ai/ai_kb_document/logic/cal_source_type)|cal_source_type|无|||
|[统计评论数](module/ai/ai_kb_document/logic/comment_counters)|comment_counters|无||统计知识库文档评论数|
|[获取fullText信息](module/ai/ai_kb_document/logic/get_full_text_info)|get_full_text_info|无|||
|[获取pageIndex信息](module/ai/ai_kb_document/logic/get_page_index_info)|get_page_index_info|无|||
|[获取关联信息](module/ai/ai_kb_document/logic/retrieve_ref_info)|retrieve_ref_info|无|||


## [知识库文档同步(AI_KB_DOCUMENT_SYNC)](module/ai/ai_kb_document_sync.md) :id=ai_kb_document_sync

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[准备建立](module/ai/ai_kb_document_sync/logic/prepare_create)|prepare_create|无|||
|[同步创建知识库文档](module/ai/ai_kb_document_sync/logic/sync_create_doc)|sync_create_doc|无|||
|[同步删除文档和分块](module/ai/ai_kb_document_sync/logic/sync_remove_doc_chunk)|sync_remove_doc_chunk|无|||
|[空间文档解析处理](module/ai/ai_kb_document_sync/logic/space_parsing)|space_parsing|无|||


## [知识库文档向导(AI_KB_DOCUMENT_WIZARD)](module/ai/ai_kb_document_wizard.md) :id=ai_kb_document_wizard

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[创建知识库文档](module/ai/ai_kb_document_wizard/logic/create_ai_kb_doc)|create_ai_kb_doc|无|||


## [知识库图谱实体(AI_KB_GRAPH_ENTITY)](module/ai/ai_kb_graph_entity.md) :id=ai_kb_graph_entity

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[获取图谱实体/关系信息](module/ai/ai_kb_graph_entity/logic/graph_info)|graph_info|无|||







## [知识库成员(AI_KB_MEMBER)](module/ai/ai_kb_member.md) :id=ai_kb_member

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[变更角色](module/ai/ai_kb_member/logic/change_role)|change_role|无||批量设置角色身份（role_id）|
|[无操作](module/ai/ai_kb_member/logic/nothing)|nothing|无||无操作逻辑，用于替换表单的获取数据行为|






## [知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base.md) :id=ai_knowledge_base

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[all_doc_reason](module/ai/ai_knowledge_base/logic/all_doc_reason)|all_doc_reason|无||通过传入知识库标识、智能体，对知识库下文档逐个进行推理|
|[get_by_code](module/ai/ai_knowledge_base/logic/get_by_code)|get_by_code|无|||
|[keywords计算](module/ai/ai_knowledge_base/logic/keywords)|keywords|无|||
|[ls](module/ai/ai_knowledge_base/logic/ls)|ls|无|||
|[全文内容推理](module/ai/ai_knowledge_base/logic/fulltext_reason)|fulltext_reason|无|||
|[创建默认成员](module/ai/ai_knowledge_base/logic/create_member)|create_member|无|||
|[删除](module/ai/ai_knowledge_base/logic/delete)|delete|无||知识库数据的逻辑删除，修改知识库的是否删除属性值|
|[取消星标](module/ai/ai_knowledge_base/logic/un_favorite)|un_favorite|无||空间取消星标|
|[变更管理员角色](module/ai/ai_knowledge_base/logic/change_admin_role)|change_admin_role|无||批量变更管理员角色身份（role_id）|
|[填充分类配置](module/ai/ai_knowledge_base/logic/fill_category_config)|fill_category_config|无|||
|[恢复](module/ai/ai_knowledge_base/logic/recover)|recover|无||恢复已删除状态知识库数据，修改知识库的是否删除属性值|
|[推理](module/ai/ai_knowledge_base/logic/reason)|reason|无|||
|[查找知识库首页模版](module/ai/ai_knowledge_base/logic/find_template)|find_template|无|||
|[深度研究](module/ai/ai_knowledge_base/logic/deep_research)|deep_research|无|||
|[生成引导提示词](module/ai/ai_knowledge_base/logic/generate_guided_prompts)|generate_guided_prompts|无|||
|[知识库切换（对话窗口）](module/ai/ai_knowledge_base/logic/switch_set)|switch_set|无|||
|[获取summary信息](module/ai/ai_knowledge_base/logic/get_summary)|get_summary|无|||
|[获取参考资料](module/ai/ai_knowledge_base/logic/query_references)|query_references|无|||
|[计算解析数完成知识库状态处理](module/ai/ai_knowledge_base/logic/calc_parsed_cnt)|calc_parsed_cnt|无|||
|[设置星标](module/ai/ai_knowledge_base/logic/favorite)|favorite|无||设置为星标产品|
|[重置分片索引数据](module/ai/ai_knowledge_base/logic/reset_all_chunk)|reset_all_chunk|无|||



## [AI大模型(AI_MODEL)](module/ai/ai_model.md) :id=ai_model

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[生成提供商模型](module/ai/ai_model/logic/generate_provider_model)|generate_provider_model|无|||
|[获取Cloud配置](module/ai/ai_model/logic/get_cloud_config)|get_cloud_config|无|||
|[获取模型提供商版本](module/ai/ai_model/logic/provider_model_version)|provider_model_version|无|||


## [模型提供商(AI_MODEL_PROVIDER)](module/ai/ai_model_provider.md) :id=ai_model_provider

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[生成AI凭证](module/ai/ai_model_provider/logic/create_ai_credential)|create_ai_credential|无|||
|[获取已登记AI凭证](module/ai/ai_model_provider/logic/get_ai_default_credential)|get_ai_default_credential|无|||


## [智能审查报告(AI_REVIEW_REPORT)](module/ai/ai_review_report.md) :id=ai_review_report

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[upsert](module/ai/ai_review_report/logic/upsert)|upsert|无|||
|[获取转换html](module/ai/ai_review_report/logic/ConvertedHTML)|ConvertedHTML|无|||




## [关注(ATTENTION)](module/Base/attention.md) :id=attention

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[取消关注](module/Base/attention/logic/un_attention)|un_attention|无|||


## [类别(CATEGORY)](module/Base/category.md) :id=category

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[删除类别及子类别](module/Base/category/logic/delete_child_category)|delete_child_category|无||删除类别及其下子类别（测试）|
|[新建类别排序](module/Base/category/logic/sort)|sort|无|||
|[设置默认分组](module/Base/category/logic/set_section)|set_section|属性逻辑||设置默认分组|
|[默认设定](module/Base/category/logic/default_setting)|default_setting|无|||


## [类别设置(CATEGORY_SETTINGS)](module/Base/category_settings.md) :id=category_settings

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[get_aifactory_sys_env](module/Base/category_settings/logic/get_aifactory_sys_env)|get_aifactory_sys_env|无|||
|[save_aifactory_sys_env](module/Base/category_settings/logic/save_aifactory_sys_env)|save_aifactory_sys_env|无|||


## [评论(COMMENT)](module/Base/comment.md) :id=comment

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[删除评论](module/Base/comment/logic/delete)|delete|无||评论数据的删除，将评论内容重置为：该评论已删除|
|[取消置顶](module/Base/comment/logic/no_top)|no_top|无|||
|[评论置顶](module/Base/comment/logic/top)|top|无|||





## [数据资源(DATA_RESOURCE)](module/meta/data_resource.md) :id=data_resource

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[full](module/meta/data_resource/logic/full)|full|无|||


## [部门(DEPARTMENT)](module/Base/department.md) :id=department

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[部门过滤](module/Base/department/logic/dept_filter)|dept_filter|无|||


## [数据字典(DICTIONARY)](module/Base/dictionary_data.md) :id=dictionary_data

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[无操作](module/Base/dictionary_data/logic/nothing)|nothing|无||无操作逻辑，用于替换表单的获取数据行为|


## [动态数据看板(DYNADASHBOARD)](module/Base/dyna_dashboard.md) :id=dyna_dashboard

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[仅获取](module/Base/dyna_dashboard/logic/only_get)|only_get|无|||
|[使用此模板](module/Base/dyna_dashboard/logic/use_cur_template)|use_cur_template|无||使用此模板|
|[更新看板部件模型](module/Base/dyna_dashboard/logic/sync_portlet_model)|sync_portlet_model|无||更新看板部件模型|
|[获取其他仪表盘](module/Base/dyna_dashboard/logic/fill_other_board)|fill_other_board|无||获取其他仪表盘|


## [扩展日志(EXTEND_LOG)](module/Base/extend_log.md) :id=extend_log

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[获取最后一次成功执行时间戳](module/Base/extend_log/logic/last_exec_time)|last_exec_time|无|||



## [扩展计划任务(EXTEND_SCHEDULED_TASK)](module/Base/extend_scheduled_task.md) :id=extend_scheduled_task

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[文档解析记录](module/Base/extend_scheduled_task/logic/doc_parse_record)|doc_parse_record|无|||






## [效能成员(INSIGHT_MEMBER)](module/Insight/insight_member.md) :id=insight_member

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[变更职位](module/Insight/insight_member/logic/change_position)|change_position|无||批量设置角色身份（position_id）|
|[变更角色](module/Insight/insight_member/logic/change_role)|change_role|无||批量设置角色身份（role_id）|
|[无操作](module/Insight/insight_member/logic/nothing)|nothing|无||无操作逻辑，用于替换表单的获取数据行为|


## [效能报表(INSIGHT_REPORT)](module/Insight/insight_report.md) :id=insight_report

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[使用此模板](module/Insight/insight_report/logic/use_cur_template)|use_cur_template|无||使用此模板|
|[删除类别](module/Insight/insight_report/logic/delete_categories)|delete_categories|无||当类别删除时修改发布的类别属性|
|[同步模板模型](module/Insight/insight_report/logic/sync_model)|sync_model|无||同步模板模型|
|[复制报表](module/Insight/insight_report/logic/copy_report)|copy_report|无||复制报表|
|[建立报表扩展模型](module/Insight/insight_report/logic/create_bi_report)|create_bi_report|无||建立报表扩展模型|
|[无操作](module/Insight/insight_report/logic/nothing)|nothing|无||无操作逻辑，用于替换表单的获取数据行为|
|[移除报表扩展模型](module/Insight/insight_report/logic/remove_bi_report)|remove_bi_report|无||移除报表扩展模型|
|[获取视图成员](module/Insight/insight_report/logic/get_view_member)|get_view_member|无||获取视图成员信息，用于判断当前用户权限|
|[计算分组信息](module/Insight/insight_report/logic/calc_group_data)|calc_group_data|属性逻辑||计算分组信息|


## [效能视图(INSIGHT_VIEW)](module/Insight/insight_view.md) :id=insight_view

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[使用此模板](module/Insight/insight_view/logic/use_cur_template)|use_cur_template|无||使用此模板|
|[删除](module/Insight/insight_view/logic/delete)|delete|无||视图的逻辑删除|
|[判断是否需要选择模板](module/Insight/insight_view/logic/recognize_choose_template)|recognize_choose_template|无||判断是否需要选择模板|
|[取消星标](module/Insight/insight_view/logic/un_favorite)|un_favorite|无||取消视图星标|
|[变更管理员角色](module/Insight/insight_view/logic/change_admin_role)|change_admin_role|无||批量变更管理员角色身份（role_id）|
|[填充BI报表默认值](module/Insight/insight_view/logic/fill_bi_form_default)|fill_bi_form_default|无||填充BI报表默认值|
|[恢复](module/Insight/insight_view/logic/recover)|recover|无||恢复|
|[无操作](module/Insight/insight_view/logic/nothing)|nothing|无||无操作逻辑，用于替换表单的获取数据行为|
|[移动视图](module/Insight/insight_view/logic/view_move)|view_move|无||视图更多设置移动视图<br>|
|[自动创建人员](module/Insight/insight_view/logic/auto_create_members)|auto_create_members|无||自动创建人员|
|[获取视图成员](module/Insight/insight_view/logic/get_view_member)|get_view_member|无||获取视图成员信息，用于判断当前用户权限|
|[设置星标](module/Insight/insight_view/logic/favorite)|favorite|无||设置视图为星标|




## [成员(MEMBER)](module/Base/member.md) :id=member

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[变更角色](module/Base/member/logic/change_role)|change_role|无||批量设置角色身份（role_id）|
|[新建成员](module/Base/member/logic/create_member)|create_member|无||批量新建团队成员|
|[无操作](module/Base/member/logic/nothing)|nothing|无||无操作逻辑，用于替换表单的获取数据行为|
|[添加共享页面非空间下成员](module/Base/member/logic/add_shared_page_member)|add_shared_page_member|无||添加共享页面非空间下成员|
|[添加共享页面非空间下成员（移动端）](module/Base/member/logic/mob_add_shared_page_member)|mob_add_shared_page_member|无||添加共享页面非空间下成员（移动端）|
|[添加成员（职位）](module/Base/member/logic/add_member_position)|add_member_position|无|||
|[获取当前项目下资源成员](module/Base/member/logic/cur_project_resource)|cur_project_resource|无||获取当前项目下资源成员|
|[获取当前项目集下资源成员](module/Base/member/logic/cur_portfolio_resource)|cur_portfolio_resource|无||获取当前项目集下资源成员|
|[获取资源成员（全局）](module/Base/member/logic/resource_member)|resource_member|无||获取资源成员（全局）|
|[选择资源成员（全局）](module/Base/member/logic/choose_resource_member)|choose_resource_member|无||选择资源成员（全局）|
|[选择项目资源成员](module/Base/member/logic/choose_project_resource)|choose_project_resource|无||项目资源分配下设置成员：当前项目下成员/部门/团队|
|[选择项目集资源成员](module/Base/member/logic/choose_portfolio_resource)|choose_portfolio_resource|无||项目集资源分配下设置成员：当前项目下成员/部门/团队|
|[非空间下成员](module/Base/member/logic/not_space_mmeber)|not_space_mmeber|无||非空间下成员|



## [通知设置(NOTIFY_SETTING)](module/Base/notify_setting.md) :id=notify_setting

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[保存设置](module/Base/notify_setting/logic/save_setting)|save_setting|无||保存通知设置|
|[无操作](module/Base/notify_setting/logic/nothing)|nothing|无||无操作逻辑，用于替换表单的获取数据行为|
|[获取用户通知设置](module/Base/notify_setting/logic/get_by_user)|get_by_user|无||获取用户通知设置|



## [页面(PAGE)](module/Wiki/article_page.md) :id=article_page

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[AI创建页面](module/Wiki/article_page/logic/ai_create_page)|ai_create_page|无|||
|[保存命名版本](module/Wiki/article_page/logic/set_name_version)|set_name_version|无||设置命名版本：新建命名版本并保存|
|[共享空间下搜索页面](module/Wiki/article_page/logic/space_shared_search)|space_shared_search|无||共享空间下搜索页面时使用|
|[共享空间主页](module/Wiki/article_page/logic/space_shared_home)|space_shared_home|无||共享空间下获取主页|
|[共享空间查询顶层页面](module/Wiki/article_page/logic/space_shared_top)|space_shared_top|无||共享空间下获取顶级页面，查询无parent_id的页面数据|
|[共享设置](module/Wiki/article_page/logic/shared_setting)|shared_setting|无||共享设置|
|[关闭共享](module/Wiki/article_page/logic/closed_shared)|closed_shared|无||页面关闭共享|
|[删除](module/Wiki/article_page/logic/delete)|delete|无||页面数据的逻辑删除，修改页面的是否删除属性值|
|[发布名称](module/Wiki/article_page/logic/publish_name)|publish_name|无||页面树更新发布名称，同步更新名称|
|[发布页面](module/Wiki/article_page/logic/publish_page)|publish_page|无||页面发布，设置发布状态及发布人，发布时间|
|[发布页面（测试）](module/Wiki/article_page/logic/publish_page_test)|publish_page_test|无||（测试）页面发布，设置发布状态及发布人，发布时间|
|[取消星标](module/Wiki/article_page/logic/un_favorite)|un_favorite|无||页面取消收藏|
|[另存为模板](module/Wiki/article_page/logic/save_to_stencil)|save_to_stencil|无||将当前页面存为组织/空间模板|
|[同步发布名称与名称](module/Wiki/article_page/logic/sync_name)|sync_name|无||同步发布名称与名称|
|[基线规划页面数据查询](module/Wiki/article_page/logic/baseline_plan_page)|baseline_plan_page|无||基线规划工作项时，填充页面当前版本名称|
|[复制子页面](module/Wiki/article_page/logic/copy_child_page)|copy_child_page|无||复制页面时调用|
|[复制页面](module/Wiki/article_page/logic/copy_page)|copy_page|无||复制页面，会调用复制子页面处理逻辑|
|[完成关注](module/Wiki/article_page/logic/finish_add_attention)|finish_add_attention|无|||
|[导出页面为pdf](module/Wiki/article_page/logic/export_to_pdf)|export_to_pdf|无||导出页面为pdf|
|[恢复](module/Wiki/article_page/logic/recover)|recover|无||恢复已删除状态页面数据，修改页面的是否删除属性值，并恢复访问记录|
|[恢复历史版本](module/Wiki/article_page/logic/recover_version)|recover_version|无||恢复页面版本至某一指定历史版本|
|[无操作](module/Wiki/article_page/logic/nothing)|nothing|无||无操作逻辑，用于替换表单的获取数据行为|
|[查询空间下的共享页面](module/Wiki/article_page/logic/space_shared_pages)|space_shared_pages|无||查询空间下的共享页面，通过父级标识查询子页面|
|[校验共享访问密码](module/Wiki/article_page/logic/access_password)|access_password|无||校验共享访问密码|
|[检验共享页面](module/Wiki/article_page/logic/check_shared)|check_shared|无||共享页面打开前，判断是否设置密码和有效期|
|[生成最近访问](module/Wiki/article_page/logic/create_recent)|create_recent|无||在用户对页面数据进行了get或update操作时生成相应的访问记录|
|[生成版本](module/Wiki/article_page/logic/commit_version)|commit_version|无||生成页面版本|
|[移动子页面](module/Wiki/article_page/logic/move_child_page)|move_child_page|无||移动子页面至知识空间|
|[移动页面](module/Wiki/article_page/logic/move_page)|move_page|无||移动页面至知识空间|
|[统计页面评论数](module/Wiki/article_page/logic/count_comment)|count_comment|无||统计页面评论数|
|[置空共享访问密码](module/Wiki/article_page/logic/reset_shared_pwd)|reset_shared_pwd|无||默认Get行为Reset共享访问密码|
|[获取共享信息](module/Wiki/article_page/logic/get_shared_info)|get_shared_info|无||页面共享设置表单，获取逻辑|
|[获取共享页面标题](module/Wiki/article_page/logic/get_shared_title)|get_shared_title|无||获取共享页面顶部标题|
|[获取历史版本](module/Wiki/article_page/logic/get_by_version)|get_by_version|无||获取当前页面的历史版本记录|
|[获取模板数据](module/Wiki/article_page/logic/get_form_stencil)|get_form_stencil|无||获取页面的模板数据，并返回|
|[获取知识空间成员](module/Wiki/article_page/logic/get_space_member)|get_space_member|无||获取知识空间成员信息，用于判断当前用户权限|
|[获取草稿页面](module/Wiki/article_page/logic/get_draft_pages)|get_draft_pages|无||查询并返回草稿数据|
|[获取页面共享链接](module/Wiki/article_page/logic/shared_url)|shared_url|无||获取页面共享链接|
|[解锁页面](module/Wiki/article_page/logic/unlock_page)|unlock_page|无||修改页面的is_lock字段|
|[设置星标](module/Wiki/article_page/logic/favorite)|favorite|无||加入到我的收藏页面|
|[访问密码加密](module/Wiki/article_page/logic/encrypt_access_key)|encrypt_access_key|无||访问密码加密|
|[访问密码解密](module/Wiki/article_page/logic/decrypt_access_key)|decrypt_access_key|无||访问密码解密|
|[锁定页面](module/Wiki/article_page/logic/lock_page)|lock_page|无||修改页面的is_lock字段|



## [文件夹(PORTFOLIO)](module/Base/portfolio.md) :id=portfolio

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[从项目集中移除](module/Base/portfolio/logic/remove_from_project_set)|remove_from_project_set|无||从项目集中移除指定的子项目集|
|[删除项目集](module/Base/portfolio/logic/delete_project_set)|delete_project_set|无||项目集数据的逻辑删除，修改项目集的是否删除属性值|
|[取消星标](module/Base/portfolio/logic/un_favorite)|un_favorite|无||项目集取消星标|
|[恢复项目集](module/Base/portfolio/logic/recover_project_set)|recover_project_set|无||恢复已删除状态项目集数据，修改项目集的是否删除属性值|
|[是否删除变更附加逻辑](module/Base/portfolio/logic/is_deleted_onchange)|is_deleted_onchange|属性逻辑||项目集删除或恢复时触发相应的通知消息|
|[设置星标](module/Base/portfolio/logic/favorite)|favorite|无||设置为星标项目集|
|[项目集组件权限计数器](module/Base/portfolio/logic/portfolio_addon_authority)|portfolio_addon_authority|无||获取项目集组件权限|
|[项目集资源成员设置](module/Base/portfolio/logic/resource_member_setting)|resource_member_setting|无||项目集资源成员设置，默认设置容量/工作日|


## [文件夹成员(PORTFOLIO_MEMBER)](module/Base/portfolio_member.md) :id=portfolio_member

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[变更角色](module/Base/portfolio_member/logic/change_role)|change_role|无||批量设置角色身份（role_id）|
|[无操作](module/Base/portfolio_member/logic/nothing)|nothing|无||无操作逻辑，用于替换表单的获取数据行为|
|[移除项目集成员通知](module/Base/portfolio_member/logic/remove_project_set_member_notify)|remove_project_set_member_notify|无||移除项目集成员时向对应用户发送通知消息|






## [核心产品功能(PSCOREPRDFUNC)](module/extension/PSCorePrdFunc.md) :id=PSCorePrdFunc

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[versions](module/extension/PSCorePrdFunc/logic/versions)|versions|无|||


## [实体处理逻辑(PSDELOGIC)](module/extension/PSDELogic.md) :id=PSDELogic

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[WebHook地址](module/extension/PSDELogic/logic/WebHook)|WebHook|属性逻辑||WebHook地址|
|[从模板建立规则](module/extension/PSDELogic/logic/create_by_template)|create_by_template|无||从模板建立规则|
|[切换启用状态](module/extension/PSDELogic/logic/valid)|valid|属性逻辑||切换启用状态|
|[初始化规则](module/extension/PSDELogic/logic/initLogic)|initLogic|无|||
|[失败率计算](module/extension/PSDELogic/logic/failure_per)|failure_per|属性逻辑||失败率计算|
|[获取最后运行状态](module/extension/PSDELogic/logic/get_last_run_info)|get_last_run_info|无||获取最后运行状态|










## [智能报表(PSSYSBIREPORT)](module/extension/PSSysBIReport.md) :id=PSSysBIReport

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[更新报表](module/extension/PSSysBIReport/logic/update_report)|update_report|无||更新报表|



## [最近访问(RECENT)](module/Base/recent.md) :id=recent

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[跳转对应视图](module/Base/recent/logic/jump_corresponding_view)|jump_corresponding_view|无|||



## [分组(SECTION)](module/Base/section.md) :id=section

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[删除分组及其下类别](module/Base/section/logic/delete_section)|delete_section|无||删除分组及其下子类别（测试）|
|[新建分组排序](module/Base/section/logic/sort)|sort|无|||



## [共享空间(SHARED_SPACE)](module/Wiki/shared_space.md) :id=shared_space

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[共享设置](module/Wiki/shared_space/logic/shared_setting)|shared_setting|无||共享设置|
|[关闭共享](module/Wiki/shared_space/logic/closed_shared)|closed_shared|无||关闭共享|
|[校验共享访问密码](module/Wiki/shared_space/logic/access_password)|access_password|无||校验共享访问密码|
|[检验共享页面](module/Wiki/shared_space/logic/check_shared)|check_shared|无||共享页面打开前，判断是否设置密码和有效期|
|[置空共享访问密码](module/Wiki/shared_space/logic/reset_shared_pwd)|reset_shared_pwd|无||默认Get行为Reset共享访问密码|
|[获取共享空间信息](module/Wiki/shared_space/logic/shared_page_info)|shared_page_info|无||获取共享空间信息|
|[获取共享空间标题](module/Wiki/shared_space/logic/get_shared_title)|get_shared_title|无||获取共享空间顶部标题|
|[获取共享链接](module/Wiki/shared_space/logic/shared_url)|shared_url|无||获取共享空间链接|
|[访问密码加密](module/Wiki/shared_space/logic/encrypt_access_key)|encrypt_access_key|无||访问密码加密|
|[访问密码解密](module/Wiki/shared_space/logic/decrypt_access_key)|decrypt_access_key|无||访问密码解密|


## [空间(SPACE)](module/Wiki/space.md) :id=space

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[其他实体关联空间](module/Wiki/space/logic/other_re_space)|other_re_space|无||其他实体关联空间操作，生成正反向关联数据|
|[创建之前](module/Wiki/space/logic/before_create)|before_create|无||创建空间之前，对添加的空间成员进行处理|
|[创建对应的知识库](module/Wiki/space/logic/CreateCorrespondingKB)|CreateCorrespondingKB|无|||
|[删除](module/Wiki/space/logic/delete)|delete|无||空间数据的逻辑删除，修改产品的是否删除属性值|
|[判断当前用户角色](module/Wiki/space/logic/recognize_cur_user_role)|recognize_cur_user_role|无||判断当前用户角色|
|[取消关联](module/Wiki/space/logic/del_relation)|del_relation|无||空间取消关联数据（正反向关联数据同时删除）|
|[取消星标](module/Wiki/space/logic/un_favorite)|un_favorite|无||空间取消星标|
|[变更管理员角色](module/Wiki/space/logic/change_admin_role)|change_admin_role|无||批量变更管理员角色身份（role_id）|
|[开启共享](module/Wiki/space/logic/open_shared)|open_shared|无||空间开启共享|
|[归档](module/Wiki/space/logic/archive)|archive|无||未归档空间数据的归档处理，修改空间的归档状态为已归档|
|[恢复](module/Wiki/space/logic/recover)|recover|无||已删除状态空间数据的恢复，修改空间的是否删除属性值，并恢复访问记录|
|[无操作](module/Wiki/space/logic/nothing)|nothing|无||无操作逻辑，用于替换表单的获取数据行为|
|[是否删除变更附加逻辑](module/Wiki/space/logic/is_deleted_onchange)|is_deleted_onchange|属性逻辑||空间删除或恢复时触发相应的通知消息|
|[是否归档变更附加逻辑](module/Wiki/space/logic/is_archived_onchange)|is_archived_onchange|属性逻辑||空间归档或激活时触发相应的通知消息|
|[标记主空间](module/Wiki/space/logic/mark_main_space)|mark_main_space|无|||
|[激活](module/Wiki/space/logic/activate)|activate|无||激活已归档状态空间，修改空间的归档属性|
|[生成最近访问](module/Wiki/space/logic/create_recent)|create_recent|无||在用户对空间数据进行了get或update操作时生成相应的访问记录|
|[移出分类](module/Wiki/space/logic/move_out_category)|move_out_category|无||将空间移除分类|
|[移动空间](module/Wiki/space/logic/move_space)|move_space|无||更新空间的所属、可见范围|
|[自动创建主页](module/Wiki/space/logic/auto_create_home_page)|auto_create_home_page|无||附加在实体的CREATE行为后，自动生成模板化的主页|
|[自动创建人员](module/Wiki/space/logic/auto_create_members)|auto_create_members|无||当所属选择"团队"时，点击完成后自动添加团队下的所有成员，若选择个人，则添加个人为所属成员。|
|[获取关联的空间](module/Wiki/space/logic/get_re_space)|get_re_space|无|||
|[获取快速新建空间集合](module/Wiki/space/logic/quick_create)|quick_create|无||用于获取可快速新建的空间集合|
|[获取知识空间成员](module/Wiki/space/logic/get_space_member_one)|get_space_member_one|无||获取知识空间成员信息，用于判断当前用户权限|
|[设置星标](module/Wiki/space/logic/favorite)|favorite|无||设置为星标产品|


## [空间成员(SPACE_MEMBER)](module/Wiki/space_member.md) :id=space_member

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[变更职位](module/Wiki/space_member/logic/change_position)|change_position|无||批量设置角色身份（position_id）|
|[变更角色](module/Wiki/space_member/logic/change_role)|change_role|无||批量设置角色身份（role_id）|
|[无操作](module/Wiki/space_member/logic/nothing)|nothing|无||无操作逻辑，用于替换表单的获取数据行为|
|[移除空间成员发送通知](module/Wiki/space_member/logic/remove_space_member_notify)|remove_space_member_notify|无||移除空间成员时向对应用户发送通知消息|


## [页面模板(STENCIL)](module/Wiki/stencil.md) :id=stencil

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[无操作](module/Wiki/stencil/logic/nothing)|nothing|无||无操作逻辑，用于替换表单的获取数据行为|
|[根据模板建立页面草稿](module/Wiki/stencil/logic/new_draft_form_stencil)|new_draft_form_stencil|无||获取页面的模板数据，并返回|









## [企业用户(USER)](module/Base/user.md) :id=user

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[冻结用户](module/Base/user/logic/Freeze)|Freeze|无||冻结用户|
|[取消统计](module/Base/user/logic/cancel_report_flag)|cancel_report_flag|无||取消用户统计状态|
|[激活用户](module/Base/user/logic/Activate)|Activate|无||激活用户|
|[统计过滤](module/Base/user/logic/report_flag_filter)|report_flag_filter|无||排除非统计用户|
|[设置统计](module/Base/user/logic/set_report_flag)|set_report_flag|无||更新用户统计状态|
|[非空间下成员](module/Base/user/logic/not_space_mmeber)|not_space_mmeber|无||非空间下成员|


## [版本(VERSION)](module/Base/version.md) :id=version

| 中文名col200    | 代码名col200    | 子类型col150    | 插件col200    |  备注col500  |
| -------- |---------- |----------- |------------|----------|
|[新建版本时填充默认版本名称](module/Base/version/logic/fill_default_name)|fill_default_name|无||新建版本时，根据已创建的版本记录生成默认版本名称|

