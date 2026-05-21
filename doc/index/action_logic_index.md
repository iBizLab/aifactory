# 行为附加 <!-- {docsify-ignore-all} -->

## [智能体(AI_AGENT)](module/ai/ai_agent.md)  :id=ai_agent

#### [Create](module/ai/ai_agent#行为) :id=ai_agent_Create




<p class="panel-title"><b>操作之后</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [reload_aiagents](module/ai/ai_agent/logic/reload_aiagents.md)


#### [Remove](module/ai/ai_agent#行为) :id=ai_agent_Remove




<p class="panel-title"><b>操作之后</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [reload_aiagents](module/ai/ai_agent/logic/reload_aiagents.md)


#### [Update](module/ai/ai_agent#行为) :id=ai_agent_Update




<p class="panel-title"><b>操作之后</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [reload_aiagents](module/ai/ai_agent/logic/reload_aiagents.md)



## [智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context.md)  :id=ai_agent_context

#### [Create](module/ai/ai_agent_context#行为) :id=ai_agent_context_Create



<p class="panel-title"><b>操作之前</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [创建之前(beforefile)](module/ai/ai_agent_context/logic/beforefile.md)



<p class="panel-title"><b>操作之后</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [建立默认flow交谈逻辑(create_default_flow_logic)](module/ai/ai_agent_context/logic/create_default_flow_logic.md)

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [reload_aiagents](module/ai/ai_agent_context/logic/reload_aiagents.md)


#### [Remove](module/ai/ai_agent_context#行为) :id=ai_agent_context_Remove



<p class="panel-title"><b>操作之前</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [删除logic扩展模型(delete_extend_model)](module/ai/ai_agent_context/logic/delete_extend_model.md)



<p class="panel-title"><b>操作之后</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [reload_aiagents](module/ai/ai_agent_context/logic/reload_aiagents.md)


#### [Update](module/ai/ai_agent_context#行为) :id=ai_agent_context_Update




<p class="panel-title"><b>操作之后</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [reload_aiagents](module/ai/ai_agent_context/logic/reload_aiagents.md)



## [智能体会话(AI_AGENT_CONVERSATION)](module/ai/ai_agent_conversation.md)  :id=ai_agent_conversation

#### [Create](module/ai/ai_agent_conversation#行为) :id=ai_agent_conversation_Create



<p class="panel-title"><b>操作之前</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [提取session前缀并存储(extract_session_type)](module/ai/ai_agent_conversation/logic/extract_session_type.md)





## [智能体会话(AI_AGENT_SESSION)](module/ai/ai_agent_session.md)  :id=ai_agent_session

#### [Get](module/ai/ai_agent_session#行为) :id=ai_agent_session_Get




<p class="panel-title"><b>操作之后</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [get_info](module/ai/ai_agent_session/logic/get_info.md)



## [AI客户端凭证(AI_CLIENT_CREDENTIAL)](module/ai/ai_client_credential.md)  :id=ai_client_credential

#### [Create](module/ai/ai_client_credential#行为) :id=ai_client_credential_Create




<p class="panel-title"><b>操作之后</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [exrouter](module/ai/ai_client_credential/logic/exrouter.md)


#### [Update](module/ai/ai_client_credential#行为) :id=ai_client_credential_Update




<p class="panel-title"><b>操作之后</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [exrouter](module/ai/ai_client_credential/logic/exrouter.md)



## [知识库文档分块(AI_KB_CHUNK)](module/ai/ai_kb_chunk.md)  :id=ai_kb_chunk

#### [GetFullData(get_full_data)](module/ai/ai_kb_chunk#行为) :id=ai_kb_chunk_get_full_data




<p class="panel-title"><b>操作之后</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [获取pageIndex信息(get_page_index_info)](module/ai/ai_kb_chunk/logic/get_page_index_info.md)



## [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document.md)  :id=ai_kb_document

#### [Create](module/ai/ai_kb_document#行为) :id=ai_kb_document_Create




<p class="panel-title"><b>操作之后</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [统计文档类型并更新知识库(cal_source_type)](module/ai/ai_kb_document/logic/cal_source_type.md)


#### [Get](module/ai/ai_kb_document#行为) :id=ai_kb_document_Get




<p class="panel-title"><b>操作之后</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [参考引用(references)](module/ai/ai_kb_document/logic/references.md)

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [获取关联信息(retrieve_ref_info)](module/ai/ai_kb_document/logic/retrieve_ref_info.md)


#### [Remove](module/ai/ai_kb_document#行为) :id=ai_kb_document_Remove




<p class="panel-title"><b>操作之后</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [统计文档类型并更新知识库(cal_source_type)](module/ai/ai_kb_document/logic/cal_source_type.md)


#### [GetFullData(get_full_data)](module/ai/ai_kb_document#行为) :id=ai_kb_document_get_full_data




<p class="panel-title"><b>操作之后</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [获取关联信息(retrieve_ref_info)](module/ai/ai_kb_document/logic/retrieve_ref_info.md)

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [获取fullText信息(get_full_text_info)](module/ai/ai_kb_document/logic/get_full_text_info.md)



## [知识库文档同步(AI_KB_DOCUMENT_SYNC)](module/ai/ai_kb_document_sync.md)  :id=ai_kb_document_sync

#### [Create](module/ai/ai_kb_document_sync#行为) :id=ai_kb_document_sync_Create


<p class="panel-title"><b>数据准备</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [准备建立(prepare_create)](module/ai/ai_kb_document_sync/logic/prepare_create.md)




<p class="panel-title"><b>操作之后</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [同步创建知识库文档(sync_create_doc)](module/ai/ai_kb_document_sync/logic/sync_create_doc.md)


#### [Remove](module/ai/ai_kb_document_sync#行为) :id=ai_kb_document_sync_Remove



<p class="panel-title"><b>操作之前</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [同步删除文档和分块(sync_remove_doc_chunk)](module/ai/ai_kb_document_sync/logic/sync_remove_doc_chunk.md)





## [知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base.md)  :id=ai_knowledge_base

#### [Create](module/ai/ai_knowledge_base#行为) :id=ai_knowledge_base_Create



<p class="panel-title"><b>操作之前</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [填充分类配置(fill_category_config)](module/ai/ai_knowledge_base/logic/fill_category_config.md)



<p class="panel-title"><b>操作之后</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [创建默认成员(create_member)](module/ai/ai_knowledge_base/logic/create_member.md)


#### [更新状态(UPDATE_STATUS)](module/ai/ai_knowledge_base#行为) :id=ai_knowledge_base_UPDATE_STATUS




<p class="panel-title"><b>操作之后</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [计算解析数完成知识库状态处理(calc_parsed_cnt)](module/ai/ai_knowledge_base/logic/calc_parsed_cnt.md)


#### [GetFullData(get_full_data)](module/ai/ai_knowledge_base#行为) :id=ai_knowledge_base_get_full_data




<p class="panel-title"><b>操作之后</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [获取summary信息(get_summary)](module/ai/ai_knowledge_base/logic/get_summary.md)



## [模型提供商(AI_MODEL_PROVIDER)](module/ai/ai_model_provider.md)  :id=ai_model_provider

#### [Create](module/ai/ai_model_provider#行为) :id=ai_model_provider_Create




<p class="panel-title"><b>操作之后</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [生成AI凭证(create_ai_credential)](module/ai/ai_model_provider/logic/create_ai_credential.md)


#### [Get](module/ai/ai_model_provider#行为) :id=ai_model_provider_Get




<p class="panel-title"><b>操作之后</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [获取已登记AI凭证(get_ai_default_credential)](module/ai/ai_model_provider/logic/get_ai_default_credential.md)


#### [Update](module/ai/ai_model_provider#行为) :id=ai_model_provider_Update




<p class="panel-title"><b>操作之后</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [生成AI凭证(create_ai_credential)](module/ai/ai_model_provider/logic/create_ai_credential.md)



## [智能审查报告(AI_REVIEW_REPORT)](module/ai/ai_review_report.md)  :id=ai_review_report

#### [Get](module/ai/ai_review_report#行为) :id=ai_review_report_Get




<p class="panel-title"><b>操作之后</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [获取转换html(ConvertedHTML)](module/ai/ai_review_report/logic/ConvertedHTML.md)



## [类别(CATEGORY)](module/Base/category.md)  :id=category

#### [Create](module/Base/category#行为) :id=category_Create



<p class="panel-title"><b>操作之前</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [新建类别排序(sort)](module/Base/category/logic/sort.md)




#### [Get](module/Base/category#行为) :id=category_Get




<p class="panel-title"><b>操作之后</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [默认设定(default_setting)](module/Base/category/logic/default_setting.md)



## [效能报表(INSIGHT_REPORT)](module/Insight/insight_report.md)  :id=insight_report

#### [Create](module/Insight/insight_report#行为) :id=insight_report_Create



<p class="panel-title"><b>操作之前</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [建立报表扩展模型(create_bi_report)](module/Insight/insight_report/logic/create_bi_report.md)




#### [Remove](module/Insight/insight_report#行为) :id=insight_report_Remove



<p class="panel-title"><b>操作之前</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [移除报表扩展模型(remove_bi_report)](module/Insight/insight_report/logic/remove_bi_report.md)





## [页面(PAGE)](module/Wiki/article_page.md)  :id=article_page

#### [Create](module/Wiki/article_page#行为) :id=article_page_Create



<p class="panel-title"><b>操作之前</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [同步发布名称与名称(sync_name)](module/Wiki/article_page/logic/sync_name.md)



<p class="panel-title"><b>操作之后</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [生成最近访问(create_recent)](module/Wiki/article_page/logic/create_recent.md)


#### [Get](module/Wiki/article_page#行为) :id=article_page_Get




<p class="panel-title"><b>操作之后</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [生成最近访问(create_recent)](module/Wiki/article_page/logic/create_recent.md)

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [获取知识空间成员(get_space_member)](module/Wiki/article_page/logic/get_space_member.md)

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [置空共享访问密码(reset_shared_pwd)](module/Wiki/article_page/logic/reset_shared_pwd.md)


#### [Update](module/Wiki/article_page#行为) :id=article_page_Update



<p class="panel-title"><b>操作之前</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [同步发布名称与名称(sync_name)](module/Wiki/article_page/logic/sync_name.md)


> [!NOTE|label:外部行为]
> 执行处理逻辑 [生成版本(commit_version)](module/Wiki/article_page/logic/commit_version.md)
> 执行实体 [页面(PAGE)](module/Wiki/article_page.md) 的 [生成版本(commit_version)](module/Wiki/article_page#行为) 行为




#### [共享设置(shared_setting)](module/Wiki/article_page#行为) :id=article_page_shared_setting



<p class="panel-title"><b>操作之前</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [访问密码加密(encrypt_access_key)](module/Wiki/article_page/logic/encrypt_access_key.md)





## [文件夹成员(PORTFOLIO_MEMBER)](module/Base/portfolio_member.md)  :id=portfolio_member

#### [Remove](module/Base/portfolio_member#行为) :id=portfolio_member_Remove



<p class="panel-title"><b>操作之前</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [移除项目集成员通知(remove_project_set_member_notify)](module/Base/portfolio_member/logic/remove_project_set_member_notify.md)





## [实体处理逻辑(PSDELOGIC)](module/extension/PSDELogic.md)  :id=PSDELogic

#### [Create](module/extension/PSDELogic#行为) :id=PSDELogic_Create



<p class="panel-title"><b>操作之前</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [初始化规则(initLogic)](module/extension/PSDELogic/logic/initLogic.md)




#### [Get](module/extension/PSDELogic#行为) :id=PSDELogic_Get




<p class="panel-title"><b>操作之后</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [获取最后运行状态(get_last_run_info)](module/extension/PSDELogic/logic/get_last_run_info.md)



## [实体通知(PSDENOTIFY)](module/extension/PSDENotify.md)  :id=PSDENotify

#### [Create](module/extension/PSDENotify#行为) :id=PSDENotify_Create




<p class="panel-title"><b>操作之后</b></p>
<br>

> [!NOTE|label:外部行为]
> 执行实体 [实体通知(PSDENOTIFY)](module/extension/PSDENotify.md) 的 [应用(APPLY)](module/extension/PSDENotify#行为) 行为


#### [Update](module/extension/PSDENotify#行为) :id=PSDENotify_Update




<p class="panel-title"><b>操作之后</b></p>
<br>

> [!NOTE|label:外部行为]
> 执行实体 [实体通知(PSDENOTIFY)](module/extension/PSDENotify.md) 的 [应用(APPLY)](module/extension/PSDENotify#行为) 行为



## [智能报表(PSSYSBIREPORT)](module/extension/PSSysBIReport.md)  :id=PSSysBIReport

#### [Update](module/extension/PSSysBIReport#行为) :id=PSSysBIReport_Update




<p class="panel-title"><b>操作之后</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [更新报表(update_report)](module/extension/PSSysBIReport/logic/update_report.md)



## [分组(SECTION)](module/Base/section.md)  :id=section

#### [Create](module/Base/section#行为) :id=section_Create



<p class="panel-title"><b>操作之前</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [新建分组排序(sort)](module/Base/section/logic/sort.md)





## [共享空间(SHARED_SPACE)](module/Wiki/shared_space.md)  :id=shared_space

#### [Get](module/Wiki/shared_space#行为) :id=shared_space_Get




<p class="panel-title"><b>操作之后</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [获取共享链接(shared_url)](module/Wiki/shared_space/logic/shared_url.md)

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [置空共享访问密码(reset_shared_pwd)](module/Wiki/shared_space/logic/reset_shared_pwd.md)


#### [共享设置(shared_setting)](module/Wiki/shared_space#行为) :id=shared_space_shared_setting



<p class="panel-title"><b>操作之前</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [访问密码加密(encrypt_access_key)](module/Wiki/shared_space/logic/encrypt_access_key.md)





## [空间(SPACE)](module/Wiki/space.md)  :id=space

#### [Create](module/Wiki/space#行为) :id=space_Create



<p class="panel-title"><b>操作之前</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [创建之前(before_create)](module/Wiki/space/logic/before_create.md)



<p class="panel-title"><b>操作之后</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [生成最近访问(create_recent)](module/Wiki/space/logic/create_recent.md)

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [自动创建主页(auto_create_home_page)](module/Wiki/space/logic/auto_create_home_page.md)

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [自动创建人员(auto_create_members)](module/Wiki/space/logic/auto_create_members.md)


#### [Get](module/Wiki/space#行为) :id=space_Get




<p class="panel-title"><b>操作之后</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [获取知识空间成员(get_space_member_one)](module/Wiki/space/logic/get_space_member_one.md)

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [生成最近访问(create_recent)](module/Wiki/space/logic/create_recent.md)



## [空间成员(SPACE_MEMBER)](module/Wiki/space_member.md)  :id=space_member

#### [Remove](module/Wiki/space_member#行为) :id=space_member_Remove



<p class="panel-title"><b>操作之前</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [移除空间成员发送通知(remove_space_member_notify)](module/Wiki/space_member/logic/remove_space_member_notify.md)





## [版本(VERSION)](module/Base/version.md)  :id=version

#### [GetDraft](module/Base/version#行为) :id=version_GetDraft



<p class="panel-title"><b>操作之前</b></p>
<br>

> [!NOTE|label:内部逻辑]
> 执行处理逻辑 [新建版本时填充默认版本名称(fill_default_name)](module/Base/version/logic/fill_default_name.md)











