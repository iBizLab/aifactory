# 模型预警 <!-- {docsify-ignore-all} -->


### 行为使用脚本<sup class="footnote-symbol"> <font color=orange>[1]</font></sup>
| 实体col200   | 行为col300  |
| --------   |------------|
|[智能体记忆任务实例(AI_AGENT_MEMORY_TASK)](module/ai/ai_agent_memory_task)|[提取记忆内容(EXTRACT)](module/ai/ai_agent_memory_task#行为)|

### 处理逻辑中使用脚本<sup class="footnote-symbol"> <font color=orange>[86]</font></sup>
| 实体col200   | 处理逻辑col300  | 脚本模式col100  |
| --------   |------------|----------|
|[智能体(AI_AGENT)](module/ai/ai_agent#处理逻辑)|[reload_aiagents](module/ai/ai_agent/logic/reload_aiagents.md)|否|
|[智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context#处理逻辑)|[agent_flow_clone](module/ai/ai_agent_context/logic/agent_flow_clone.md)|否|
|[智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context#处理逻辑)|[agent_flow_templ](module/ai/ai_agent_context/logic/agent_flow_templ.md)|否|
|[智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context#处理逻辑)|[get_by_code](module/ai/ai_agent_context/logic/get_by_code.md)|否|
|[智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context#处理逻辑)|[reload_aiagents](module/ai/ai_agent_context/logic/reload_aiagents.md)|否|
|[智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context#处理逻辑)|[交谈全文内容推理(chat_fulltext_reason)](module/ai/ai_agent_context/logic/chat_fulltext_reason.md)|否|
|[智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context#处理逻辑)|[删除logic扩展模型(delete_extend_model)](module/ai/ai_agent_context/logic/delete_extend_model.md)|否|
|[智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context#处理逻辑)|[建立默认flow交谈逻辑(create_default_flow_logic)](module/ai/ai_agent_context/logic/create_default_flow_logic.md)|否|
|[智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context#处理逻辑)|[批量执行(batch_execution)](module/ai/ai_agent_context/logic/batch_execution.md)|否|
|[智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context#处理逻辑)|[查表审查(lookup)](module/ai/ai_agent_context/logic/lookup.md)|否|
|[智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context#处理逻辑)|[深度研究(deep_research)](module/ai/ai_agent_context/logic/deep_research.md)|否|
|[智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context#处理逻辑)|[辅助生成引导提示词（停用）(guided_prompt)](module/ai/ai_agent_context/logic/guided_prompt.md)|否|
|[智能体会话(AI_AGENT_CONVERSATION)](module/ai/ai_agent_conversation#处理逻辑)|[提取session前缀并存储(extract_session_type)](module/ai/ai_agent_conversation/logic/extract_session_type.md)|否|
|[智能体记忆任务实例(AI_AGENT_MEMORY_TASK)](module/ai/ai_agent_memory_task#处理逻辑)|[保存记忆分块(save_chunk)](module/ai/ai_agent_memory_task/logic/save_chunk.md)|否|
|[智能体记忆任务实例(AI_AGENT_MEMORY_TASK)](module/ai/ai_agent_memory_task#处理逻辑)|[填充默认文档标识(fill_default_doc_id)](module/ai/ai_agent_memory_task/logic/fill_default_doc_id.md)|否|
|[智能体记忆任务实例(AI_AGENT_MEMORY_TASK)](module/ai/ai_agent_memory_task#处理逻辑)|[更新每日记忆文档(update_daily_log)](module/ai/ai_agent_memory_task/logic/update_daily_log.md)|否|
|[智能体记忆任务实例(AI_AGENT_MEMORY_TASK)](module/ai/ai_agent_memory_task#处理逻辑)|[获取记忆分块(get_chunk)](module/ai/ai_agent_memory_task/logic/get_chunk.md)|否|
|[智能体记忆任务实例(AI_AGENT_MEMORY_TASK)](module/ai/ai_agent_memory_task#处理逻辑)|[获取记忆文档(get_document)](module/ai/ai_agent_memory_task/logic/get_document.md)|否|
|[智能体记忆任务实例(AI_AGENT_MEMORY_TASK)](module/ai/ai_agent_memory_task#处理逻辑)|[记忆提取并存储(extract_and_store)](module/ai/ai_agent_memory_task/logic/extract_and_store.md)|否|
|[AI客户端凭证(AI_CLIENT_CREDENTIAL)](module/ai/ai_client_credential#处理逻辑)|[exrouter](module/ai/ai_client_credential/logic/exrouter.md)|否|
|[知识库文档分块(AI_KB_CHUNK)](module/ai/ai_kb_chunk#处理逻辑)|[检索测试(retrieval_test)](module/ai/ai_kb_chunk/logic/retrieval_test.md)|否|
|[知识库文档分块(AI_KB_CHUNK)](module/ai/ai_kb_chunk#处理逻辑)|[获取pageIndex信息(get_page_index_info)](module/ai/ai_kb_chunk/logic/get_page_index_info.md)|否|
|[知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document#处理逻辑)|[全文推理(reason)](module/ai/ai_kb_document/logic/reason.md)|否|
|[知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document#处理逻辑)|[参考引用(references)](module/ai/ai_kb_document/logic/references.md)|否|
|[知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document#处理逻辑)|[文档解析处理(parse)](module/ai/ai_kb_document/logic/parse.md)|否|
|[知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document#处理逻辑)|[获取fullText信息(get_full_text_info)](module/ai/ai_kb_document/logic/get_full_text_info.md)|否|
|[知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document#处理逻辑)|[获取pageIndex信息(get_page_index_info)](module/ai/ai_kb_document/logic/get_page_index_info.md)|否|
|[知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document#处理逻辑)|[获取关联信息(retrieve_ref_info)](module/ai/ai_kb_document/logic/retrieve_ref_info.md)|否|
|[知识库文档同步(AI_KB_DOCUMENT_SYNC)](module/ai/ai_kb_document_sync#处理逻辑)|[空间文档解析处理(space_parsing)](module/ai/ai_kb_document_sync/logic/space_parsing.md)|否|
|[知识库文档向导(AI_KB_DOCUMENT_WIZARD)](module/ai/ai_kb_document_wizard#处理逻辑)|[创建知识库文档(create_ai_kb_doc)](module/ai/ai_kb_document_wizard/logic/create_ai_kb_doc.md)|否|
|[知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base#处理逻辑)|[all_doc_reason](module/ai/ai_knowledge_base/logic/all_doc_reason.md)|否|
|[知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base#处理逻辑)|[get_by_code](module/ai/ai_knowledge_base/logic/get_by_code.md)|否|
|[知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base#处理逻辑)|[keywords计算(keywords)](module/ai/ai_knowledge_base/logic/keywords.md)|否|
|[知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base#处理逻辑)|[全文内容推理(fulltext_reason)](module/ai/ai_knowledge_base/logic/fulltext_reason.md)|否|
|[知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base#处理逻辑)|[推理(reason)](module/ai/ai_knowledge_base/logic/reason.md)|否|
|[知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base#处理逻辑)|[深度研究(deep_research)](module/ai/ai_knowledge_base/logic/deep_research.md)|否|
|[知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base#处理逻辑)|[生成引导提示词(generate_guided_prompts)](module/ai/ai_knowledge_base/logic/generate_guided_prompts.md)|否|
|[知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base#处理逻辑)|[知识库切换（对话窗口）(switch_set)](module/ai/ai_knowledge_base/logic/switch_set.md)|否|
|[知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base#处理逻辑)|[获取summary信息(get_summary)](module/ai/ai_knowledge_base/logic/get_summary.md)|否|
|[AI大模型(AI_MODEL)](module/ai/ai_model#处理逻辑)|[获取Cloud配置(get_cloud_config)](module/ai/ai_model/logic/get_cloud_config.md)|否|
|[AI大模型(AI_MODEL)](module/ai/ai_model#处理逻辑)|[获取模型提供商版本(provider_model_version)](module/ai/ai_model/logic/provider_model_version.md)|否|
|[智能审查报告(AI_REVIEW_REPORT)](module/ai/ai_review_report#处理逻辑)|[upsert](module/ai/ai_review_report/logic/upsert.md)|否|
|[智能审查报告(AI_REVIEW_REPORT)](module/ai/ai_review_report#处理逻辑)|[获取转换html(ConvertedHTML)](module/ai/ai_review_report/logic/ConvertedHTML.md)|否|
|[类别(CATEGORY)](module/Base/category#处理逻辑)|[新建类别排序(sort)](module/Base/category/logic/sort.md)|否|
|[类别设置(CATEGORY_SETTINGS)](module/Base/category_settings#处理逻辑)|[get_aifactory_sys_env](module/Base/category_settings/logic/get_aifactory_sys_env.md)|否|
|[类别设置(CATEGORY_SETTINGS)](module/Base/category_settings#处理逻辑)|[save_aifactory_sys_env](module/Base/category_settings/logic/save_aifactory_sys_env.md)|否|
|[动态数据看板(DYNADASHBOARD)](module/Base/dyna_dashboard#处理逻辑)|[使用此模板(use_cur_template)](module/Base/dyna_dashboard/logic/use_cur_template.md)|否|
|[动态数据看板(DYNADASHBOARD)](module/Base/dyna_dashboard#处理逻辑)|[更新看板部件模型(sync_portlet_model)](module/Base/dyna_dashboard/logic/sync_portlet_model.md)|否|
|[扩展计划任务(EXTEND_SCHEDULED_TASK)](module/Base/extend_scheduled_task#处理逻辑)|[文档解析记录(doc_parse_record)](module/Base/extend_scheduled_task/logic/doc_parse_record.md)|否|
|[效能报表(INSIGHT_REPORT)](module/Insight/insight_report#处理逻辑)|[使用此模板(use_cur_template)](module/Insight/insight_report/logic/use_cur_template.md)|否|
|[效能报表(INSIGHT_REPORT)](module/Insight/insight_report#处理逻辑)|[同步模板模型(sync_model)](module/Insight/insight_report/logic/sync_model.md)|否|
|[效能报表(INSIGHT_REPORT)](module/Insight/insight_report#处理逻辑)|[复制报表(copy_report)](module/Insight/insight_report/logic/copy_report.md)|否|
|[效能报表(INSIGHT_REPORT)](module/Insight/insight_report#处理逻辑)|[建立报表扩展模型(create_bi_report)](module/Insight/insight_report/logic/create_bi_report.md)|否|
|[效能报表(INSIGHT_REPORT)](module/Insight/insight_report#处理逻辑)|[获取视图成员(get_view_member)](module/Insight/insight_report/logic/get_view_member.md)|否|
|[效能报表(INSIGHT_REPORT)](module/Insight/insight_report#处理逻辑)|[计算分组信息(calc_group_data)](module/Insight/insight_report/logic/calc_group_data.md)|否|
|[效能视图(INSIGHT_VIEW)](module/Insight/insight_view#处理逻辑)|[使用此模板(use_cur_template)](module/Insight/insight_view/logic/use_cur_template.md)|否|
|[效能视图(INSIGHT_VIEW)](module/Insight/insight_view#处理逻辑)|[填充BI报表默认值(fill_bi_form_default)](module/Insight/insight_view/logic/fill_bi_form_default.md)|是|
|[效能视图(INSIGHT_VIEW)](module/Insight/insight_view#处理逻辑)|[获取视图成员(get_view_member)](module/Insight/insight_view/logic/get_view_member.md)|否|
|[成员(MEMBER)](module/Base/member#处理逻辑)|[添加共享页面非空间下成员(add_shared_page_member)](module/Base/member/logic/add_shared_page_member.md)|否|
|[成员(MEMBER)](module/Base/member#处理逻辑)|[添加共享页面非空间下成员（移动端）(mob_add_shared_page_member)](module/Base/member/logic/mob_add_shared_page_member.md)|否|
|[成员(MEMBER)](module/Base/member#处理逻辑)|[选择资源成员（全局）(choose_resource_member)](module/Base/member/logic/choose_resource_member.md)|否|
|[成员(MEMBER)](module/Base/member#处理逻辑)|[非空间下成员(not_space_mmeber)](module/Base/member/logic/not_space_mmeber.md)|否|
|[页面(PAGE)](module/Wiki/article_page#处理逻辑)|[共享设置(shared_setting)](module/Wiki/article_page/logic/shared_setting.md)|否|
|[页面(PAGE)](module/Wiki/article_page#处理逻辑)|[发布页面(publish_page)](module/Wiki/article_page/logic/publish_page.md)|否|
|[页面(PAGE)](module/Wiki/article_page#处理逻辑)|[发布页面（测试）(publish_page_test)](module/Wiki/article_page/logic/publish_page_test.md)|否|
|[页面(PAGE)](module/Wiki/article_page#处理逻辑)|[校验共享访问密码(access_password)](module/Wiki/article_page/logic/access_password.md)|否|
|[页面(PAGE)](module/Wiki/article_page#处理逻辑)|[检验共享页面(check_shared)](module/Wiki/article_page/logic/check_shared.md)|否|
|[页面(PAGE)](module/Wiki/article_page#处理逻辑)|[获取历史版本(get_by_version)](module/Wiki/article_page/logic/get_by_version.md)|否|
|[页面(PAGE)](module/Wiki/article_page#处理逻辑)|[获取知识空间成员(get_space_member)](module/Wiki/article_page/logic/get_space_member.md)|否|
|[页面(PAGE)](module/Wiki/article_page#处理逻辑)|[获取页面共享链接(shared_url)](module/Wiki/article_page/logic/shared_url.md)|否|
|[核心产品功能(PSCOREPRDFUNC)](module/extension/PSCorePrdFunc#处理逻辑)|[versions](module/extension/PSCorePrdFunc/logic/versions.md)|否|
|[实体处理逻辑(PSDELOGIC)](module/extension/PSDELogic#处理逻辑)|[WebHook地址(WebHook)](module/extension/PSDELogic/logic/WebHook.md)|是|
|[实体处理逻辑(PSDELOGIC)](module/extension/PSDELogic#处理逻辑)|[失败率计算(failure_per)](module/extension/PSDELogic/logic/failure_per.md)|是|
|[实体处理逻辑(PSDELOGIC)](module/extension/PSDELogic#处理逻辑)|[获取最后运行状态(get_last_run_info)](module/extension/PSDELogic/logic/get_last_run_info.md)|否|
|[智能报表(PSSYSBIREPORT)](module/extension/PSSysBIReport#处理逻辑)|[更新报表(update_report)](module/extension/PSSysBIReport/logic/update_report.md)|否|
|[分组(SECTION)](module/Base/section#处理逻辑)|[新建分组排序(sort)](module/Base/section/logic/sort.md)|否|
|[共享空间(SHARED_SPACE)](module/Wiki/shared_space#处理逻辑)|[校验共享访问密码(access_password)](module/Wiki/shared_space/logic/access_password.md)|否|
|[共享空间(SHARED_SPACE)](module/Wiki/shared_space#处理逻辑)|[检验共享页面(check_shared)](module/Wiki/shared_space/logic/check_shared.md)|否|
|[共享空间(SHARED_SPACE)](module/Wiki/shared_space#处理逻辑)|[获取共享链接(shared_url)](module/Wiki/shared_space/logic/shared_url.md)|否|
|[空间(SPACE)](module/Wiki/space#处理逻辑)|[开启共享(open_shared)](module/Wiki/space/logic/open_shared.md)|否|
|[空间(SPACE)](module/Wiki/space#处理逻辑)|[自动创建主页(auto_create_home_page)](module/Wiki/space/logic/auto_create_home_page.md)|否|
|[空间(SPACE)](module/Wiki/space#处理逻辑)|[获取关联的空间(get_re_space)](module/Wiki/space/logic/get_re_space.md)|否|
|[空间(SPACE)](module/Wiki/space#处理逻辑)|[获取快速新建空间集合(quick_create)](module/Wiki/space/logic/quick_create.md)|否|
|[空间(SPACE)](module/Wiki/space#处理逻辑)|[获取知识空间成员(get_space_member_one)](module/Wiki/space/logic/get_space_member_one.md)|否|
|[企业用户(USER)](module/Base/user#处理逻辑)|[非空间下成员(not_space_mmeber)](module/Base/user/logic/not_space_mmeber.md)|否|
|[版本(VERSION)](module/Base/version#处理逻辑)|[新建版本时填充默认版本名称(fill_default_name)](module/Base/version/logic/fill_default_name.md)|否|

### 处理逻辑中使用SQL调用<sup class="footnote-symbol"> <font color=orange>[40]</font></sup>
| 实体col200   | 处理逻辑col300  |
| --------   |------------|
|[智能体业务上下文(AI_AGENT_CONTEXT)#处理逻辑](module/ai/ai_agent_context)|[get_by_code](module/ai/ai_agent_context/logic/get_by_code.md)|
|[智能体业务上下文(AI_AGENT_CONTEXT)#处理逻辑](module/ai/ai_agent_context)|[创建之前(beforefile)](module/ai/ai_agent_context/logic/beforefile.md)|
|[智能体会话(AI_AGENT_CONVERSATION)#处理逻辑](module/ai/ai_agent_conversation)|[清空消息(clear_message)](module/ai/ai_agent_conversation/logic/clear_message.md)|
|[智能体会话(AI_AGENT_CONVERSATION)#处理逻辑](module/ai/ai_agent_conversation)|[除指定外清空会话(clear_all_except)](module/ai/ai_agent_conversation/logic/clear_all_except.md)|
|[知识库文档(AI_KB_DOCUMENT)#处理逻辑](module/ai/ai_kb_document)|[ai_kb_document_type_counters](module/ai/ai_kb_document/logic/ai_kb_document_type_counters.md)|
|[知识库文档(AI_KB_DOCUMENT)#处理逻辑](module/ai/ai_kb_document)|[构建切片(build_chunk)](module/ai/ai_kb_document/logic/build_chunk.md)|
|[知识库文档(AI_KB_DOCUMENT)#处理逻辑](module/ai/ai_kb_document)|[构建索引(build_index)](module/ai/ai_kb_document/logic/build_index.md)|
|[知识库文档(AI_KB_DOCUMENT)#处理逻辑](module/ai/ai_kb_document)|[统计文档类型并更新知识库(cal_source_type)](module/ai/ai_kb_document/logic/cal_source_type.md)|
|[知识库文档(AI_KB_DOCUMENT)#处理逻辑](module/ai/ai_kb_document)|[统计评论数(comment_counters)](module/ai/ai_kb_document/logic/comment_counters.md)|
|[知识库文档(AI_KB_DOCUMENT)#处理逻辑](module/ai/ai_kb_document)|[获取关联信息(retrieve_ref_info)](module/ai/ai_kb_document/logic/retrieve_ref_info.md)|
|[知识库文档同步(AI_KB_DOCUMENT_SYNC)#处理逻辑](module/ai/ai_kb_document_sync)|[同步删除文档和分块(sync_remove_doc_chunk)](module/ai/ai_kb_document_sync/logic/sync_remove_doc_chunk.md)|
|[知识库(AI_KNOWLEDGE_BASE)#处理逻辑](module/ai/ai_knowledge_base)|[取消星标(un_favorite)](module/ai/ai_knowledge_base/logic/un_favorite.md)|
|[知识库(AI_KNOWLEDGE_BASE)#处理逻辑](module/ai/ai_knowledge_base)|[生成引导提示词(generate_guided_prompts)](module/ai/ai_knowledge_base/logic/generate_guided_prompts.md)|
|[知识库(AI_KNOWLEDGE_BASE)#处理逻辑](module/ai/ai_knowledge_base)|[计算解析数完成知识库状态处理(calc_parsed_cnt)](module/ai/ai_knowledge_base/logic/calc_parsed_cnt.md)|
|[知识库(AI_KNOWLEDGE_BASE)#处理逻辑](module/ai/ai_knowledge_base)|[重置分片索引数据(reset_all_chunk)](module/ai/ai_knowledge_base/logic/reset_all_chunk.md)|
|[类别(CATEGORY)#处理逻辑](module/Base/category)|[删除类别及子类别(delete_child_category)](module/Base/category/logic/delete_child_category.md)|
|[类别(CATEGORY)#处理逻辑](module/Base/category)|[设置默认分组(set_section)](module/Base/category/logic/set_section.md)|
|[动态数据看板(DYNADASHBOARD)#处理逻辑](module/Base/dyna_dashboard)|[仅获取(only_get)](module/Base/dyna_dashboard/logic/only_get.md)|
|[效能报表(INSIGHT_REPORT)#处理逻辑](module/Insight/insight_report)|[删除类别(delete_categories)](module/Insight/insight_report/logic/delete_categories.md)|
|[效能视图(INSIGHT_VIEW)#处理逻辑](module/Insight/insight_view)|[取消星标(un_favorite)](module/Insight/insight_view/logic/un_favorite.md)|
|[页面(PAGE)#处理逻辑](module/Wiki/article_page)|[关闭共享(closed_shared)](module/Wiki/article_page/logic/closed_shared.md)|
|[页面(PAGE)#处理逻辑](module/Wiki/article_page)|[删除(delete)](module/Wiki/article_page/logic/delete.md)|
|[页面(PAGE)#处理逻辑](module/Wiki/article_page)|[发布页面（测试）(publish_page_test)](module/Wiki/article_page/logic/publish_page_test.md)|
|[页面(PAGE)#处理逻辑](module/Wiki/article_page)|[取消星标(un_favorite)](module/Wiki/article_page/logic/un_favorite.md)|
|[页面(PAGE)#处理逻辑](module/Wiki/article_page)|[恢复(recover)](module/Wiki/article_page/logic/recover.md)|
|[页面(PAGE)#处理逻辑](module/Wiki/article_page)|[统计页面评论数(count_comment)](module/Wiki/article_page/logic/count_comment.md)|
|[页面(PAGE)#处理逻辑](module/Wiki/article_page)|[获取共享信息(get_shared_info)](module/Wiki/article_page/logic/get_shared_info.md)|
|[页面(PAGE)#处理逻辑](module/Wiki/article_page)|[获取草稿页面(get_draft_pages)](module/Wiki/article_page/logic/get_draft_pages.md)|
|[文件夹(PORTFOLIO)#处理逻辑](module/Base/portfolio)|[从项目集中移除(remove_from_project_set)](module/Base/portfolio/logic/remove_from_project_set.md)|
|[文件夹(PORTFOLIO)#处理逻辑](module/Base/portfolio)|[取消星标(un_favorite)](module/Base/portfolio/logic/un_favorite.md)|
|[分组(SECTION)#处理逻辑](module/Base/section)|[删除分组及其下类别(delete_section)](module/Base/section/logic/delete_section.md)|
|[共享空间(SHARED_SPACE)#处理逻辑](module/Wiki/shared_space)|[校验共享访问密码(access_password)](module/Wiki/shared_space/logic/access_password.md)|
|[共享空间(SHARED_SPACE)#处理逻辑](module/Wiki/shared_space)|[检验共享页面(check_shared)](module/Wiki/shared_space/logic/check_shared.md)|
|[共享空间(SHARED_SPACE)#处理逻辑](module/Wiki/shared_space)|[获取共享空间信息(shared_page_info)](module/Wiki/shared_space/logic/shared_page_info.md)|
|[空间(SPACE)#处理逻辑](module/Wiki/space)|[删除(delete)](module/Wiki/space/logic/delete.md)|
|[空间(SPACE)#处理逻辑](module/Wiki/space)|[取消星标(un_favorite)](module/Wiki/space/logic/un_favorite.md)|
|[空间(SPACE)#处理逻辑](module/Wiki/space)|[恢复(recover)](module/Wiki/space/logic/recover.md)|
|[空间(SPACE)#处理逻辑](module/Wiki/space)|[标记主空间(mark_main_space)](module/Wiki/space/logic/mark_main_space.md)|
|[空间(SPACE)#处理逻辑](module/Wiki/space)|[获取关联的空间(get_re_space)](module/Wiki/space/logic/get_re_space.md)|
|[版本(VERSION)#处理逻辑](module/Base/version)|[新建版本时填充默认版本名称(fill_default_name)](module/Base/version/logic/fill_default_name.md)|

### 界面逻辑中使用脚本<sup class="footnote-symbol"> <font color=orange>[72]</font></sup>
| 实体col200   | 界面逻辑col300  |
| --------   |------------|
|[智能体分配(AI_AGENT_ASSIGNMENT)](module/ai/ai_agent_assignment#界面逻辑)|[run分配智能体逻辑](module/ai/ai_agent_assignment/uilogic/run)|
|[智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context#界面逻辑)|[prompt_feedback](module/ai/ai_agent_context/uilogic/prompt_feedback)|
|[智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context#界面逻辑)|[run智能体逻辑](module/ai/ai_agent_context/uilogic/run)|
|[智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context#界面逻辑)|[template_feedback](module/ai/ai_agent_context/uilogic/template_feedback)|
|[智能体会话(AI_AGENT_SESSION)](module/ai/ai_agent_session#界面逻辑)|[jenkins_build](module/ai/ai_agent_session/uilogic/jenkins_build)|
|[智能体会话(AI_AGENT_SESSION)](module/ai/ai_agent_session#界面逻辑)|[remark_feedback](module/ai/ai_agent_session/uilogic/remark_feedback)|
|[智能体会话(AI_AGENT_SESSION)](module/ai/ai_agent_session#界面逻辑)|[debug_context](module/ai/ai_agent_session/uilogic/debug_context)|
|[智能体会话(AI_AGENT_SESSION)](module/ai/ai_agent_session#界面逻辑)|[accept_feedback](module/ai/ai_agent_session/uilogic/accept_feedback)|
|[智能体会话(AI_AGENT_SESSION)](module/ai/ai_agent_session#界面逻辑)|[dyna_context](module/ai/ai_agent_session/uilogic/dyna_context)|
|[AI客户端凭证(AI_CLIENT_CREDENTIAL)](module/ai/ai_client_credential#界面逻辑)|[复制密钥](module/ai/ai_client_credential/uilogic/copy_access_key)|
|[知识库文档分块(AI_KB_CHUNK)](module/ai/ai_kb_chunk#界面逻辑)|[打开所属文档](module/ai/ai_kb_chunk/uilogic/open_doc)|
|[知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document#界面逻辑)|[显示基本信息](module/ai/ai_kb_document/uilogic/show_info)|
|[知识库文档同步(AI_KB_DOCUMENT_SYNC)](module/ai/ai_kb_document_sync#界面逻辑)|[刷新文档同步表格](module/ai/ai_kb_document_sync/uilogic/refresh_doc_sync_grid)|
|[知识库文档向导(AI_KB_DOCUMENT_WIZARD)](module/ai/ai_kb_document_wizard#界面逻辑)|[通知刷新](module/ai/ai_kb_document_wizard/uilogic/notify_refresh)|
|[知识库成员(AI_KB_MEMBER)](module/ai/ai_kb_member#界面逻辑)|[新建知识库默认临时成员](module/ai/ai_kb_member/uilogic/create_default_temp_members)|
|[知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base#界面逻辑)|[计算表格列行为状态(ai_knowledge_base)](module/ai/ai_knowledge_base/uilogic/calc_column_action_state)|
|[知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base#界面逻辑)|[查找知识库首页模版](module/ai/ai_knowledge_base/uilogic/find_template)|
|[知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base#界面逻辑)|[提示词填充](module/ai/ai_knowledge_base/uilogic/prompt_feedback)|
|[知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base#界面逻辑)|[刷新当前表格](module/ai/ai_knowledge_base/uilogic/refresh_current_grid)|
|[智能审查报告(AI_REVIEW_REPORT)](module/ai/ai_review_report#界面逻辑)|[AI添加审查报告](module/ai/ai_review_report/uilogic/ai_add)|
|[附件(ATTACHMENT)](module/Base/attachment#界面逻辑)|[附件删除](module/Base/attachment/uilogic/remove_attachment)|
|[附件(ATTACHMENT)](module/Base/attachment#界面逻辑)|[附件预览](module/Base/attachment/uilogic/attachment_preview)|
|[附件(ATTACHMENT)](module/Base/attachment#界面逻辑)|[计算附件是否隐藏逻辑](module/Base/attachment/uilogic/calc_attachment_hidden)|
|[评论(COMMENT)](module/Base/comment#界面逻辑)|[控制评论按钮显示（知识库）](module/Base/comment/uilogic/comment_icon_show_wiki)|
|[评论(COMMENT)](module/Base/comment#界面逻辑)|[ai添加评论](module/Base/comment/uilogic/ai_comment)|
|[评论(COMMENT)](module/Base/comment#界面逻辑)|[发送评论(知识库)](module/Base/comment/uilogic/send_comment_wiki)|
|[评论(COMMENT)](module/Base/comment#界面逻辑)|[清空评论（知识库）](module/Base/comment/uilogic/clear_comment_wiki)|
|[评论(COMMENT)](module/Base/comment#界面逻辑)|[控制评论按钮隐藏（知识库）](module/Base/comment/uilogic/comment_icon_hidden_wiki)|
|[评论(COMMENT)](module/Base/comment#界面逻辑)|[回复评论（知识库）](module/Base/comment/uilogic/reply_comment_wiki)|
|[评论(COMMENT)](module/Base/comment#界面逻辑)|[编辑评论（知识库）](module/Base/comment/uilogic/edit_comment_wiki)|
|[动态数据看板(DYNADASHBOARD)](module/Base/dyna_dashboard#界面逻辑)|[仪表盘操作列](module/Base/dyna_dashboard/uilogic/control_del)|
|[动态数据看板(DYNADASHBOARD)](module/Base/dyna_dashboard#界面逻辑)|[通知刷新](module/Base/dyna_dashboard/uilogic/notify_refresh)|
|[动态数据看板(DYNADASHBOARD)](module/Base/dyna_dashboard#界面逻辑)|[使用此模板(禁止关闭)](module/Base/dyna_dashboard/uilogic/use_cur_template_no_closed)|
|[动态数据看板(DYNADASHBOARD)](module/Base/dyna_dashboard#界面逻辑)|[列表加载完成](module/Base/dyna_dashboard/uilogic/list_load_success)|
|[动态数据看板(DYNADASHBOARD)](module/Base/dyna_dashboard#界面逻辑)|[获取选中模板名称](module/Base/dyna_dashboard/uilogic/fill_choosed_board_name)|
|[效能成员(INSIGHT_MEMBER)](module/Insight/insight_member#界面逻辑)|[新建视图默认临时成员](module/Insight/insight_member/uilogic/create_default_temp_members)|
|[效能报表(INSIGHT_REPORT)](module/Insight/insight_report#界面逻辑)|[导出表格](module/Insight/insight_report/uilogic/export_excel)|
|[效能报表(INSIGHT_REPORT)](module/Insight/insight_report#界面逻辑)|[使用此模板](module/Insight/insight_report/uilogic/use_cur_template)|
|[效能报表(INSIGHT_REPORT)](module/Insight/insight_report#界面逻辑)|[导出为pdf](module/Insight/insight_report/uilogic/export_pdf)|
|[效能视图(INSIGHT_VIEW)](module/Insight/insight_view#界面逻辑)|[计算表格列行为状态(insight)](module/Insight/insight_view/uilogic/calc_column_action_state)|
|[效能视图(INSIGHT_VIEW)](module/Insight/insight_view#界面逻辑)|[通知刷新](module/Insight/insight_view/uilogic/notify_refresh)|
|[效能视图(INSIGHT_VIEW)](module/Insight/insight_view#界面逻辑)|[批量删除视图成员临时数据](module/Insight/insight_view/uilogic/remove_batch_temp)|
|[成员(MEMBER)](module/Base/member#界面逻辑)|[添加页面共享成员](module/Base/member/uilogic/add_shared_member)|
|[通知事件(NOTIFY_EVENT)](module/extension/notify_event#界面逻辑)|[保存列表多数据部件](module/extension/notify_event/uilogic/save_list_mdctrl)|
|[页面(PAGE)](module/Wiki/article_page#界面逻辑)|[关闭评论区](module/Wiki/article_page/uilogic/close_comment)|
|[页面(PAGE)](module/Wiki/article_page#界面逻辑)|[ai添加page](module/Wiki/article_page/uilogic/ai_add_page)|
|[页面(PAGE)](module/Wiki/article_page#界面逻辑)|[恢复历史版本并通知刷新](module/Wiki/article_page/uilogic/page_refresh)|
|[页面(PAGE)](module/Wiki/article_page#界面逻辑)|[复制共享链接](module/Wiki/article_page/uilogic/copy_shared_url)|
|[页面(PAGE)](module/Wiki/article_page#界面逻辑)|[后续刷新](module/Wiki/article_page/uilogic/refresh)|
|[页面(PAGE)](module/Wiki/article_page#界面逻辑)|[添加附件数据](module/Wiki/article_page/uilogic/add_attachment)|
|[页面(PAGE)](module/Wiki/article_page#界面逻辑)|[新建发布并通知刷新](module/Wiki/article_page/uilogic/save_notify_refresh)|
|[页面(PAGE)](module/Wiki/article_page#界面逻辑)|[共享设置表单加载数据](module/Wiki/article_page/uilogic/shared_form_data)|
|[页面(PAGE)](module/Wiki/article_page#界面逻辑)|[显示评论区](module/Wiki/article_page/uilogic/show_commnet)|
|[核心产品功能(PSCOREPRDFUNC)](module/extension/PSCorePrdFunc#界面逻辑)|[跳转设置页面](module/extension/PSCorePrdFunc/uilogic/skip_setting)|
|[核心产品功能(PSCOREPRDFUNC)](module/extension/PSCorePrdFunc#界面逻辑)|[clone此应用](module/extension/PSCorePrdFunc/uilogic/clone_git)|
|[核心产品功能(PSCOREPRDFUNC)](module/extension/PSCorePrdFunc#界面逻辑)|[自定义版本安装](module/extension/PSCorePrdFunc/uilogic/custom_version_info)|
|[核心产品功能(PSCOREPRDFUNC)](module/extension/PSCorePrdFunc#界面逻辑)|[准备版本数据](module/extension/PSCorePrdFunc/uilogic/prepare_version_info)|
|[核心产品功能(PSCOREPRDFUNC)](module/extension/PSCorePrdFunc#界面逻辑)|[初始化插件信息](module/extension/PSCorePrdFunc/uilogic/init_plugin_info)|
|[核心产品功能(PSCOREPRDFUNC)](module/extension/PSCorePrdFunc#界面逻辑)|[跳转gitlab](module/extension/PSCorePrdFunc/uilogic/skip_gitlab)|
|[核心产品功能(PSCOREPRDFUNC)](module/extension/PSCorePrdFunc#界面逻辑)|[更新插件设置](module/extension/PSCorePrdFunc/uilogic/update_plugin_setting)|
|[实体处理逻辑(PSDELOGIC)](module/extension/PSDELogic#界面逻辑)|[webhook调试](module/extension/PSDELogic/uilogic/debug_webhook)|
|[最近访问(RECENT)](module/Base/recent#界面逻辑)|[最近访问跳转其他视图](module/Base/recent/uilogic/recent_jump_other_view)|
|[共享空间(SHARED_SPACE)](module/Wiki/shared_space#界面逻辑)|[复制共享链接](module/Wiki/shared_space/uilogic/copy_shared_url)|
|[共享空间(SHARED_SPACE)](module/Wiki/shared_space#界面逻辑)|[后续刷新](module/Wiki/shared_space/uilogic/refresh)|
|[空间(SPACE)](module/Wiki/space#界面逻辑)|[计算表格列行为状态(space)](module/Wiki/space/uilogic/calc_column_action_state)|
|[空间(SPACE)](module/Wiki/space#界面逻辑)|[批量删除空间成员临时数据](module/Wiki/space/uilogic/remove_batch_temp)|
|[空间(SPACE)](module/Wiki/space#界面逻辑)|[刷新当前表格](module/Wiki/space/uilogic/refresh_current_grid)|
|[空间成员(SPACE_MEMBER)](module/Wiki/space_member#界面逻辑)|[新建空间默认临时成员](module/Wiki/space_member/uilogic/create_default_temp_members)|
|[页面模板(STENCIL)](module/Wiki/stencil#界面逻辑)|[发布](module/Wiki/stencil/uilogic/release)|
|[页面模板(STENCIL)](module/Wiki/stencil#界面逻辑)|[打开新建页面并关闭模板中心](module/Wiki/stencil/uilogic/open_new_page)|
|[企业用户(USER)](module/Base/user#界面逻辑)|[修改密码（表单）](module/Base/user/uilogic/change_pas)|
|[企业用户(USER)](module/Base/user#界面逻辑)|[删除部门](module/Base/user/uilogic/trash_dept)|

### 包含长文本的查询<sup class="footnote-symbol"> <font color=orange>[24]</font></sup>
| 实体col200   | 数据查询col300  |
| --------   |------------|
|[智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context)|[deep_research_agent](module/ai/ai_agent_context/query/deep_research_agent)|
|[智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context)|[dynamic_agent](module/ai/ai_agent_context/query/dynamic_agent)|
|[智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context)|[full_text_agent](module/ai/ai_agent_context/query/full_text_agent)|
|[智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context)|[lookup_agent](module/ai/ai_agent_context/query/lookup_agent)|
|[知识库文档分块(AI_KB_CHUNK)](module/ai/ai_kb_chunk)|[DEFAULT](module/ai/ai_kb_chunk/query/Default)|
|[知识库文档分块(AI_KB_CHUNK)](module/ai/ai_kb_chunk)|[reader](module/ai/ai_kb_chunk/query/reader)|
|[知识库文档分块(AI_KB_CHUNK)](module/ai/ai_kb_chunk)|[指定知识库(specified_kb)](module/ai/ai_kb_chunk/query/specified_kb)|
|[知识库文档分块(AI_KB_CHUNK)](module/ai/ai_kb_chunk)|[tree](module/ai/ai_kb_chunk/query/tree)|
|[知识库文档分块(AI_KB_CHUNK)](module/ai/ai_kb_chunk)|[启用(VALID)](module/ai/ai_kb_chunk/query/valid)|
|[知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document)|[AI文档内容(ai_doc_content)](module/ai/ai_kb_document/query/ai_doc_content)|
|[知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document)|[未解析文档(UNPARSED)](module/ai/ai_kb_document/query/unparsed)|
|[知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base)|[启用知识库(VALID)](module/ai/ai_knowledge_base/query/valid)|
|[AI调用工具(AI_TOOL)](module/ai/ai_tool)|[启用的技能数据(SKILL_VALID)](module/ai/ai_tool/query/skill_valid)|
|[评论(COMMENT)](module/Base/comment)|[数据查询(DEFAULT)](module/Base/comment/query/Default)|
|[数据字典(DICTIONARY)](module/Base/dictionary_data)|[数据查询(DEFAULT)](module/Base/dictionary_data/query/Default)|
|[数据字典(DICTIONARY)](module/Base/dictionary_data)|[知识库文档导入方式(ai_kb_doc_import_method)](module/Base/dictionary_data/query/ai_kb_doc_import_method)|
|[动态数据看板(DYNADASHBOARD)](module/Base/dyna_dashboard)|[数据查询(DEFAULT)](module/Base/dyna_dashboard/query/Default)|
|[动态数据看板(DYNADASHBOARD)](module/Base/dyna_dashboard)|[示例图(example_chart)](module/Base/dyna_dashboard/query/example_chart)|
|[动态数据看板(DYNADASHBOARD)](module/Base/dyna_dashboard)|[系统仪表盘(is_system)](module/Base/dyna_dashboard/query/is_system)|
|[动态数据看板(DYNADASHBOARD)](module/Base/dyna_dashboard)|[我的看板(my_dashboard)](module/Base/dyna_dashboard/query/my_dashboard)|
|[动态数据看板(DYNADASHBOARD)](module/Base/dyna_dashboard)|[正常数据(normal)](module/Base/dyna_dashboard/query/normal)|
|[扩展执行计划(EXTEND_SCHEDULE)](module/Base/extend_schedule)|[启用(VALID)](module/Base/extend_schedule/query/Valid)|
|[效能报表(INSIGHT_REPORT)](module/Insight/insight_report)|[模板报表(is_system)](module/Insight/insight_report/query/is_system)|
|[页面版本(PAGE_VERSION)](module/Wiki/page_version)|[数据查询(DEFAULT)](module/Wiki/page_version/query/Default)|

### 使用自定义SQL的查询<sup class="footnote-symbol"> <font color=orange>[3]</font></sup>
| 实体col200   | 数据查询col300  |
| --------   |------------|
|[知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document)|[exp_list](module/ai/ai_kb_document/query/exp_list)|
|[知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base)|[search](module/ai/ai_knowledge_base/query/search)|
|[空间(SPACE)](module/Wiki/space)|[移动端非星标空间(mob_unfavorite)](module/Wiki/space/query/mob_unfavorite)|


### 未配置查询的数据集合<sup class="footnote-symbol"> <font color=orange>[5]</font></sup>
| 实体col200   | 数据集合col300  |
| --------   |------------|
|[知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document)|[AI知识库文档查询(ai_doc_query)](module/ai/ai_kb_document/dataset/ai_doc_query)|
|[知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base)|[AI知识库目录查询(ai_docs_by_kb)](module/ai/ai_knowledge_base/dataset/ai_docs_by_kb)|
|[知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base)|[AI知识库清单查询(ai_kb_query)](module/ai/ai_knowledge_base/dataset/ai_kb_query)|
|[知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base)|[with_record](module/ai/ai_knowledge_base/dataset/with_record)|
|[空间(SPACE)](module/Wiki/space)|[未关联的空间(no_re_space)](module/Wiki/space/dataset/no_re_space)|

### 未配置权限请求接口<sup class="footnote-symbol"> <font color=orange>[6]</font></sup>
| 实体col200| 请求路径col500| 请求方式col100   |    行为/集合col300    |
| -------- |-------- | --------|-------- |
|[知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base.md)|/ai_knowledge_bases/{key}/delete|POST|[删除(delete)](module/ai/ai_knowledge_base#行为)|
|[知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base.md)|/ai_knowledge_bases/{key}/recover|POST|[恢复(recover)](module/ai/ai_knowledge_base#行为)|
|[动态数据看板(DYNADASHBOARD)](module/Base/dyna_dashboard.md)|/dyna_dashboards/{key}/move_order|POST|[移动排序(move_order)](module/Base/dyna_dashboard#行为)|
|[效能报表(INSIGHT_REPORT)](module/Insight/insight_report.md)|/insight_reports/{key}/use_cur_template|POST|[使用此模板(use_cur_template)](module/Insight/insight_report#行为)|
|[文件夹(PORTFOLIO)](module/Base/portfolio.md)|/portfolios/{key}/favorite|POST|[设置星标(favorite)](module/Base/portfolio#行为)|
|[文件夹(PORTFOLIO)](module/Base/portfolio.md)|/portfolios/{key}/un_favorite|POST|[取消星标(un_favorite)](module/Base/portfolio#行为)|

### NONE权限请求接口<sup class="footnote-symbol"> <font color=orange>[15]</font></sup>
| 实体col200| 请求路径col500| 请求方式col100   |    行为/集合col300    |
| -------- |-------- | --------|-------- |
|[类别(CATEGORY)](module/Base/category.md)|/categories/fetch_space_category|POST|[空间目录(space_category)](module/Base/category#数据集合)|
|[类别(CATEGORY)](module/Base/category.md)|/categories/fetch_space_category_top|POST|[空间目录（顶级）(space_category_top)](module/Base/category#数据集合)|
|[成员(MEMBER)](module/Base/member.md)|/members/fetch_choose_portfolio_resource|POST|[选择项目集资源成员(choose_portfolio_resource)](module/Base/member#数据集合)|
|[成员(MEMBER)](module/Base/member.md)|/members/fetch_choose_project_resource|POST|[选择项目资源成员(choose_project_resource)](module/Base/member#数据集合)|
|[成员(MEMBER)](module/Base/member.md)|/members/fetch_choose_resource_member|POST|[选择资源成员（全局）(choose_resource_member)](module/Base/member#数据集合)|
|[成员(MEMBER)](module/Base/member.md)|/members/fetch_cur_portfolio_resource|POST|[获取当前项目集下资源成员(cur_portfolio_resource)](module/Base/member#数据集合)|
|[成员(MEMBER)](module/Base/member.md)|/members/fetch_cur_project_resource|POST|[获取当前项目下资源成员(cur_project_resource)](module/Base/member#数据集合)|
|[成员(MEMBER)](module/Base/member.md)|/members/fetch_resource_member|POST|[获取资源成员（全局）(resource_member)](module/Base/member#数据集合)|
|[页面(PAGE)](module/Wiki/article_page.md)|/article_pages/fetch_advanced_search|POST|[高级搜索(advanced_search)](module/Wiki/article_page#数据集合)|
|[页面(PAGE)](module/Wiki/article_page.md)|/article_pages/fetch_shared_with_me|POST|[与我共享(shared_with_me)](module/Wiki/article_page#数据集合)|
|[智能报表(PSSYSBIREPORT)](module/extension/PSSysBIReport.md)|/pssysbireports/{key}/compileappbireport|POST|[编译报表模型(COMPILEAPPBIREPORT)](module/extension/PSSysBIReport#行为)|
|[最近访问(RECENT)](module/Base/recent.md)|/recents/fetch_recent_page|POST|[最近访问页面(recent_page)](module/Base/recent#数据集合)|
|[空间(SPACE)](module/Wiki/space.md)|/spaces/fetch_other_re_space|POST|[关联的空间(other_re_space)](module/Wiki/space#数据集合)|
|[页面模板(STENCIL)](module/Wiki/stencil.md)|/stencils/fetch_no_space_stencil|POST|[非空间下模板(no_space_stencil)](module/Wiki/stencil#数据集合)|
|[页面模板(STENCIL)](module/Wiki/stencil.md)|/stencils/fetch_space_stencil|POST|[空间下页面模板(space_stencil)](module/Wiki/stencil#数据集合)|

### 操作标识未配置映射<sup class="footnote-symbol"> <font color=orange>[3]</font></sup>
| 实体col200   | 操作标识col300  |
| --------   |------------|
|[页面版本(PAGE_VERSION)](module/Wiki/page_version.md)|CREATE<br>READ<br>DELETE<br>UPDATE|
|[评论(COMMENT)](module/Base/comment.md)|DELETE<br>UPDATE|
|[关注(ATTENTION)](module/Base/attention.md)|CREATE<br>READ<br>DELETE<br>UPDATE|

### 除主键、主信息、预置属性外，不包含其他配置的表格<sup class="footnote-symbol"> <font color=orange>[5]</font></sup>
| 实体col200   |   视图col400 | 表格col400  |
| --------   |------------|------------|
|[AI大模型(AI_MODEL)](module/ai/ai_model)|选择提供商模型版本表格(choose_provider_version_grid)|[AI大模型(ai_model_pickup_grid_view2)](app/view/ai_model_pickup_grid_view2)|
|[部门(DEPARTMENT)](module/Base/department)|主表格(main)|[部门(department_pick_up_grid_view)](app/view/department_pick_up_grid_view)|
|[页面(PAGE)](module/Wiki/article_page)|嵌入知识库文档向导_表格(nested_doc_wizard_grid)|[知识库文档(article_page_nested_doc_grid_view)](app/view/article_page_nested_doc_grid_view)|
|[分组(SECTION)](module/Base/section)|主表格(main)|[分组(section_pick_up_grid_view)](app/view/section_pick_up_grid_view)|
|[企业用户(USER)](module/Base/user)|主表格(main)|[企业用户(user_pick_up_grid_view)](app/view/user_pick_up_grid_view)|

### 无搜索项的搜索表单<sup class="footnote-symbol"> <font color=orange>[29]</font></sup>
| 实体col200   |   视图col400 | 搜索表单col400  |
| --------   |------------|-----------|
|[智能体(AI_AGENT)](module/ai/ai_agent)|默认搜索表单(default)|[智能体模板(ai_agent_grid_view)](app/view/ai_agent_grid_view)|
|[智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context)|默认搜索表单(default)|[绑定智能体(ai_agent_context_bind_view)](app/view/ai_agent_context_bind_view)|
|[智能体会话(AI_AGENT_CONVERSATION)](module/ai/ai_agent_conversation)|默认搜索表单(default)|[智能体会话(ai_agent_conversation_grid_view)](app/view/ai_agent_conversation_grid_view)|
|[智能体知识库引用(AI_AGENT_KNOWLEDGE_REL)](module/ai/ai_agent_knowledge_rel)|默认搜索表单(default)|[智能体知识库引用(ai_agent_knowledge_rel_grid_view)](app/view/ai_agent_knowledge_rel_grid_view)|
|[智能体记忆任务实例(AI_AGENT_MEMORY_TASK)](module/ai/ai_agent_memory_task)|默认搜索表单(default)|[智能体记忆任务实例(ai_agent_memory_task_grid_view)](app/view/ai_agent_memory_task_grid_view)|
|[智能体会话消息(AI_AGENT_MESSAGE)](module/ai/ai_agent_message)|默认搜索表单(default)|[会话消息(ai_agent_message_grid_view)](app/view/ai_agent_message_grid_view)|
|[智能体工具引用(AI_AGENT_TOOL_REL)](module/ai/ai_agent_tool_rel)|默认搜索表单(default)|[智能体工具引用(ai_agent_tool_rel_grid_view)](app/view/ai_agent_tool_rel_grid_view)|
|[AI客户端凭证(AI_CLIENT_CREDENTIAL)](module/ai/ai_client_credential)|我的AI客户端凭证实体表格视图_搜索表单(main3)|[AI客户端凭证(ai_client_credential_grid_view)](app/view/ai_client_credential_grid_view)|
|[AI凭证(AI_CREDENTIAL)](module/ai/ai_credential)|默认搜索表单(default)|[AI凭证(ai_credential_grid_view)](app/view/ai_credential_grid_view)|
|[知识库文档分块(AI_KB_CHUNK)](module/ai/ai_kb_chunk)|默认搜索表单(default)|[文档切片(ai_kb_chunk_list_view9)](app/view/ai_kb_chunk_list_view9)|
|[知识库图谱实体类型(AI_KB_GRAPH_ENTITY_TYPE)](module/ai/ai_kb_graph_entity_type)|知识库图谱实体类型配置中心表格视图_搜索表单(main2)|[知识库图谱实体类型(ai_kb_graph_entity_type_config_grid_view)](app/view/ai_kb_graph_entity_type_config_grid_view)|
|[知识库成员(AI_KB_MEMBER)](module/ai/ai_kb_member)|知识库成员配置表格_搜索表单(main2)|[知识库成员(ai_kb_member_config_grid_view)](app/view/ai_kb_member_config_grid_view)|
|[知识库标签(AI_KB_TAG)](module/ai/ai_kb_tag)|默认搜索表单(default)|[标签(ai_kb_tag_nested_grid_view)](app/view/ai_kb_tag_nested_grid_view)|
|[知识库标签集(AI_KB_TAG_SET)](module/ai/ai_kb_tag_set)|默认搜索表单(default)|[标签集(ai_kb_tag_set_grid_view)](app/view/ai_kb_tag_set_grid_view)|
|[知识库源(AI_KNOWLEDGE_SOURCE)](module/ai/ai_knowledge_source)|默认搜索表单(default)|[知识库源(ai_knowledge_source_grid_view)](app/view/ai_knowledge_source_grid_view)|
|[AI大模型(AI_MODEL)](module/ai/ai_model)|默认搜索表单(default)|[模型(ai_model_embedding_provider_grid_view)](app/view/ai_model_embedding_provider_grid_view)|
|[智能审查报告(AI_REVIEW_REPORT)](module/ai/ai_review_report)|审查记录_搜索表单(main4)|[智能审查记录(ai_review_report_review_grid)](app/view/ai_review_report_review_grid)|
|[数据资源(DATA_RESOURCE)](module/meta/data_resource)|默认搜索表单(default)|[资源(data_resource_grid_view)](app/view/data_resource_grid_view)|
|[部门(DEPARTMENT)](module/Base/department)|默认搜索表单(default)|[部门(department_pick_up_grid_view)](app/view/department_pick_up_grid_view)|
|[扩展计划任务(EXTEND_SCHEDULED_TASK)](module/Base/extend_scheduled_task)|默认搜索表单(default)|[扩展计划任务(extend_scheduled_task_grid_view)](app/view/extend_scheduled_task_grid_view)|
|[扩展任务类型(EXTEND_TASK_TYPE)](module/Base/extend_task_type)|默认搜索表单(default)|[扩展任务类型(extend_task_type_grid_view)](app/view/extend_task_type_grid_view)|
|[效能成员(INSIGHT_MEMBER)](module/Insight/insight_member)|效能成员绑定_搜索表单(assigned_grid_view_search_form)|[视图成员(insight_member_assigned_grid_view)](app/view/insight_member_assigned_grid_view)|
|[效能报表(INSIGHT_REPORT)](module/Insight/insight_report)|全部报表表格视图_搜索表单(usr05200683_search_form)|[全部报表(insight_report_all_report_grid_view)](app/view/insight_report_all_report_grid_view)|
|[效能视图(INSIGHT_VIEW)](module/Insight/insight_view)|默认搜索表单(default)|[全部视图(insight_view_all_grid_view)](app/view/insight_view_all_grid_view)|
|[成员(MEMBER)](module/Base/member)|默认搜索表单(default)|[成员(member_grid_view)](app/view/member_grid_view)|
|[页面(PAGE)](module/Wiki/article_page)|默认搜索表单(default)|[知识库文档(article_page_nested_doc_grid_view)](app/view/article_page_nested_doc_grid_view)|
|[实体处理逻辑(PSDELOGIC)](module/extension/PSDELogic)|自动化规则逻辑表格视图_搜索表单(flow_grid_view_search_form)|[全部规则(psde_logic_global_flow_grid_view)](app/view/psde_logic_global_flow_grid_view)|
|[分组(SECTION)](module/Base/section)|默认搜索表单(default)|[分组(section_pick_up_grid_view)](app/view/section_pick_up_grid_view)|
|[企业用户(USER)](module/Base/user)|企业用户管理表格视图_搜索表单(grid_view_search_form)|[企业用户(user_pick_up_grid_view)](app/view/user_pick_up_grid_view)|

### 除主键、主信息、预置属性外，不包含其他配置的表单<sup class="footnote-symbol"> <font color=orange>[12]</font></sup>
| 实体col200   |   视图col400 |表单col400  |
| --------   |------------|------------|
|[智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context)|发现_表单(main5)|[发现(ai_agent_context_discovery)](app/view/ai_agent_context_discovery)|
|[智能体知识库引用(AI_AGENT_KNOWLEDGE_REL)](module/ai/ai_agent_knowledge_rel)|主编辑表单(main)|[智能体知识库引用(ai_agent_knowledge_rel_edit_view)](app/view/ai_agent_knowledge_rel_edit_view)|
|[智能体工具引用(AI_AGENT_TOOL_REL)](module/ai/ai_agent_tool_rel)|主编辑表单(main)|[智能体工具引用(ai_agent_tool_rel_edit_view)](app/view/ai_agent_tool_rel_edit_view)|
|[知识库文档同步(AI_KB_DOCUMENT_SYNC)](module/ai/ai_kb_document_sync)|主编辑表单(main)|[知识库文档同步(ai_kb_document_sync_edit_view)](app/view/ai_kb_document_sync_edit_view)|
|[知识库图谱实体类型(AI_KB_GRAPH_ENTITY_TYPE)](module/ai/ai_kb_graph_entity_type)|主编辑表单(main)|[知识库图谱实体类型(ai_kb_graph_entity_type_edit_view)](app/view/ai_kb_graph_entity_type_edit_view)|
|[知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base)|知识库高级设置_表单(main2)|[高级设置(ai_knowledge_base_advanced_setting_view)](app/view/ai_knowledge_base_advanced_setting_view)|
|[类别(CATEGORY)](module/Base/category)|知识库分类设置(kb_setting)|[知识库分类设置(category_kb_setting)](app/view/category_kb_setting)|
|[效能成员(INSIGHT_MEMBER)](module/Insight/insight_member)|主编辑表单(main)|[效能成员(insight_member_edit_view)](app/view/insight_member_edit_view)|
|[效能视图(INSIGHT_VIEW)](module/Insight/insight_view)|视图配置视图_表单(setting_view_form)|[视图配置(insight_view_setting_view)](app/view/insight_view_setting_view)|
|[成员(MEMBER)](module/Base/member)|主编辑表单(main)|[成员(member_edit_view)](app/view/member_edit_view)|
|[页面(PAGE)](module/Wiki/article_page)|主编辑表单(main)|[页面(article_page_edit_view)](app/view/article_page_edit_view)|
|[企业用户(USER)](module/Base/user)|主编辑表单(main)|[帐号设置(user_account_view)](app/view/user_account_view)|
