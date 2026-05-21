# 数据字典  <!-- {docsify-ignore-all} -->

##### AI会话状态 :id=ai_conversation_status



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|active|进行中|active||
|paused|暂停|paused||
|ended|已结束|ended||
|archived|已归档|archived||

##### AI客户端类型 :id=ai_client_type



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|CHAT|交谈|chat||
|WEBHOOK|WebHook|webhook||
|SKILLRUNNER|技能运行沙箱|skillrunner||

##### AI技能加载模式 :id=ai_skill_load_mode



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|all|全部|all|加载全部技能|
|specified|指定|specified|仅加载指定技能|

##### AI消息状态 :id=ai_message_status



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|pending|待处理|pending||
|sent|已发送|sent||
|failed|失败|failed||
|cancelled|用户取消|cancelled||

##### AI消息角色类型 :id=ai_message_role



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|system|系统|system||
|assistant|智能体|assistant||
|user|用户|user||

##### AI生成模式 :id=ai_mode



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|precise|精确模式|precise||
|balanced|平衡模式|balanced||
|creative|创意模式|creative||
|custom|自定义|custom||

##### AI知识库模式 :id=AIKBMode



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|default|支持当前指定或外部传入的知识库|default|支持当前指定或外部传入的知识库|
|include|仅支持指定的知识库|include|仅支持指定的知识库|
|exclude|除指定知识库外的知识库|exclude|支持除指定知识库外的知识库|
|fixed|固定|fixed||

##### BI图表类型 :id=bi_chart_type2



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|NUMBER|数字|number||
|MULTI_SERIES_COL|多系列柱状图|multi_series_col||
|STACK_COL|堆叠柱状图|stack_col||
|ZONE_COL|分区柱状图|zone_col||
|MULTI_SERIES_BAR|多系列条形图|multi_series_bar||
|STACK_BAR|堆积条形图|stack_bar||
|MULTI_SERIES_LINE|多系列折线图|multi_series_line||
|ZONE_LINE|分区折线图|zone_line||
|AREA|面积图|area||
|GRID|表格|grid||
|CROSSTABLE|交叉表|crosstable||
|PIE|饼图|pie||
|RADAR|雷达图|radar||
|GAUGE|仪表盘|gauge||
|SCATTER|散点图|scatter||

##### BI报表_人员类型 :id=bi_form_man_type



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|10|成员|item_10||
|20|部门|item_20||
|30|团队|item_30||

##### HTTP 方法 :id=api_method_codelist



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|GET|GET|get||
|POST|POST|post||
|PUT|PUT|put||
|DELETE|DELETE|delete||

##### Rerank模型 :id=rerank



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|BAAI/bge-reranker-v2-m3|BAAI/bge-reranker-v2-m3|baai_bge_SUB_reranker_SUB_v2_SUB_m3||

##### Tool类型 :id=tool_type_codelist



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|api|HTTP 接口|api||
|mcp|MCP服务|mcp||
|skill|SKILL能力|skill||

##### graphrag方法 :id=graphrag_method



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|general|General|general||
|light|Light|light||

##### layout_recognize :id=layout_recognize



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|OCR|OCR|ocr||
|VL|VL|vl||
|PPT|PPT|ppt||
|MANUAL|MANUAL|manual||

##### 云实体主状态逻辑处理节点类型(设计) :id=DELogicNodeType_MS



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|base|基础|base||

##### 云实体关系属性影射类型 :id=DERDERMapType



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|SUM|合计|sum||
|AVG|平均|avg||
|MAX|最大值|max||
|MIN|最小值|min||
|COUNT|计数|count||
|EXISTS|存在|exists|从实体存在，1表示存在，0表示不存在|
|NOTEXISTS|不存在|notexists|从实体不存在，1表示不存在，0表示存在|
|USER|用户自定义|user||
|USER2|用户自定义2|user2||
|USER3|用户自定义3|user3||
|USER4|用户自定义4|user4||

##### 云平台门户部件类型 :id=PortletType



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|LIST|实体列表|list||
|CHART|实体图表|chart||
|VIEW|系统视图|view||
|REPORT|实体报表|report|嵌入实体报表部件|
|HTML|网页部件|html||
|ACTIONBAR|操作栏|actionbar||
|TOOLBAR|工具栏|toolbar||
|CUSTOM|自定义|custom||

##### 任务状态 :id=TaskStatus



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|PENDING|待处理|pending||
|RUNNING|运行中|running||
|SUCCESS|成功|success||
|FAILED|失败|failed||
|CANCELLED|已取消|cancelled||

##### 会话类型 :id=conversation_type



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|topic|话题|topic||
|temp|临时|temp||
|inline|行内补全|inline||

##### 关注类型 :id=attention_type



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|10|不关注|item_10||
|20|订阅|item_20||
|30|重要通知|item_30||
|40|关注|item_40||

##### 凭证类型 :id=credential_type



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|api_key|API Key|api_key||
|bearer_token|Bearer Token|bearer_token||
|access_key_secret|Access Key/Secret|access_key_secret||
|oauth2_client|OAuth2 Client|oauth2_client||
|custom|Custom|custom||

##### 切片策略 :id=chunkingstrategy



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|NAIVE|按段落|NAIVE||
|QA|Q&A|QA||
|MANUAL|手册|MANUAL||
|LAWS|法律|LAWS||
|ONE|单个|ONE||
|PICTURE|图片|PICTURE||
|PRESENTATION|演示文稿|PRESENTATION||
|TABLE|表格|TABLE||
|CHUNKS|预切片段|CHUNKS||
|RAW_CHUNKS|预切直接片段|RAW_CHUNKS||

##### 历史版本 :id=history_version_list



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|all|全部版本|all||
|named_list|命名版本|named_list||

##### 参考类型 :id=reference_type



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|image|图片|image||
|url|链接|url||

##### 反馈类型 :id=feedback_type



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|like|点赞|like||
|dislike|点踩|dislike||

##### 可供选择的属性变更 :id=enable_field_change



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|ai.ai_knowledge_base.status|变更知识库状态|ai_ai_knowledge_base_status||
|ai.ai_document.status|变更文档状态|ai_ai_document_status||

##### 可供选择的触发器 :id=enable_action



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|knowledge|知识库|knowledge||
|meta|资源数据|meta||
|wiki|空间|wiki||

##### 启停状态 :id=user_report_flag



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|1|开启|item_1||
|0|停止|item_0||

##### 启用标记 :id=enable_tag_codelist



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|1|启用|item_1||
|0|不启用|item_0||
|-1|不涉及|_SUB_1||

##### 团队角色类型 :id=user_group_role_type



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|admin|团队管理员|admin||
|user|团队成员|user||

##### 图实体引用类型 :id=graph_entity_reference_type



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|generic|泛指|generic|表示该实体是泛指的，代表一类事物或通用概念，无唯一指代|
|specific|特指|specific|表示该实体是特指的，有明确、唯一的现实世界指代（如具体人物、组织、地点等）|

##### 多维分析指标类别 :id=BIMeasureType



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|COMMON|常规|common||
|CALCULATED|动态计算|calculated||

##### 多维分析维度类别 :id=BIDimensionType



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|COMMON|常规|common||
|CALCULATED|动态计算|calculated||

##### 字典项类型 :id=dictionary_type



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|pending|未开始|pending||
|in_progress|进行中|in_progress||
|completed|已完成|completed||
|closed|已关闭|closed||

##### 实体通知目标类型 :id=DENotifyTargetType



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|EVENTDATAFIELD|属性|eventdatafield||
|DSTUSER|成员|dstuser||
|DSTDEPARTMENT|部门|dstdepartment||

##### 实体逻辑处理节点类型(设计) :id=DELogicNodeType



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|BaseEvent|基础事件|baseevent||
|ParamAction|参数操作|paramaction||
|GeneralProcess|常规处理|generalprocess||
|DBProcess|数据库操作|dbprocess||
|WFProcess|工作流处理|wfprocess||
|Advanced|高级|advanced||

##### 实体逻辑处理节点类型(设计)3 :id=DELogicNodeType3



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|BaseEvent|基础事件|baseevent||
|ParamAction|参数操作|paramaction||
|GeneralProcess|常规处理|generalprocess||
|DBProcess|数据库操作|dbprocess||
|WFProcess|工作流处理|wfprocess||
|Advanced|高级|advanced||

##### 实体逻辑系统AI聊天代理类型 :id=DELogicSysAIChatAgentType



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|DEFAULT|默认|default|同步调用聊天请求|
|CHATCATEGORY|交谈问题分类|chatcategory||
|CHATOUTPUT|交谈输出|chatoutput||
|CHATAGGREGATION|交谈聚合|chataggregation||
|CHATAGGREGATIONOUTPUT|交谈聚合（等待输入）|chataggregationoutput||

##### 导入方式 :id=import_method



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|space_manual|手动从空间导入|space_manual||
|space_auto_sync|自动从空间同步|space_auto_sync||
|local_upload|上传本地文件|local_upload||

##### 应用模型类型 :id=pscoreprdfunc_type



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|BASE|基础|base||
|EXTENSION|扩展|extension||
|MERGENCE|合并|mergence||
|COMPONENT|组件|component||

##### 待办状态 :id=CodeListTodoState



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|ACTIVE|待处理|active||
|COMPLETED|已处理|completed||
|PAUSED|挂起|paused||
|CANCELED|已取消|canceled||

##### 截断策略 :id=trimming_strategy



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|oldest|丢弃最早消息|oldest||
|least_important|基于内容重要性|least_important||
|summarize_oldest|摘要保留早期|summarize_oldest||

##### 所属类型（包含个人） :id=user_scope_type



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|organization|组织|organization||
|user_group|团队|user_group||
|user|个人|user||

##### 所属类型（包含个人） :id=user_scope_type



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|organization|组织|organization||
|user_group|团队|user_group||
|user|个人|user||

##### 执行器子类型 :id=executor_subtype



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|PSDELOGIC|处理逻辑|psdelogic||
|PSDEACTION|实体行为|psdeaction||
|SYSUTIL|系统功能|sysutil||

##### 执行器类型 :id=executor_type



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|INTERNAL|内置逻辑|internal||
|GROOVY|GROOVY|groovy||
|PYTHON|PYTHON|python||

##### 扩展状态 :id=extension_status



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|0|未应用|item_0||
|1|已应用|item_1||

##### 报表_数据集BI :id=report_group_bi



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|BIScheme.insight_report|报表|bischeme_insight_report||

##### 文件类型 :id=file_type



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|txt|TXT​|txt||
|md|MD|md||
|doc|DOC|doc||
|docx|DOCX|docx||
|pdf|PDF|pdf||
|ppt|PPT|ppt||
|pptx|PPTX|pptx||

##### 文档分块类型 :id=chunk_type



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|original|默认|original||
|cluster|聚合簇|cluster|clusters生成得摘要节点|
|manual|手动|manual||
|index|页面索引|index||
|page|页面|page||

##### 文档切片状态 :id=slice_status



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|0|未解析|unparsed||
|1|就绪|ready||
|3|待切片|chunk_pending||
|2|解析中|parsing||
|4|切片中|chunking||
|99|失败|failed||

##### 日志状态 :id=log_state



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|SUCCESS|成功|success||
|FAILURE|失败|failure||

##### 智能体业务范围 :id=ai_agent_context_scopes



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|idea|需求|idea||
|ticket|工单|ticket||
|test_case|用例|test_case||
|work_item|工作项|work_item||
|page|页面|page||
|post|讨论|post||
|other|其他|other||

##### 智能体业务范围 :id=ai_agent_context_scopes



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|ai_knowledge_base|空间|ai_knowledge_base||
|ai_kb_document|文档|ai_kb_document||
|ai_agent_context|智能体|ai_agent_context||
|page|页面|page||
|deep_research|深度研究|deep_research||
|qa|问答|qa||
|other|其他|other||

##### 智能体工作流模式 :id=flow_mode



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|DEFAULT|默认|default||
|DE|逻辑模式|de||
|SKILL|技能|skill||
|HUB|总线|hub||
|SCRIPT|脚本代码|script||

##### 智能体状态 :id=agent_status



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|1|使用中|item_1||
|0|停用|item_0||

##### 智能报表报表指标引用类型 :id=BIReportItemMSRefType



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|NONE|无|none||
|YEARERLIER|同比|yearerlier||
|PERIODEARLIER|环比|periodearlier||
|RATIO|占比|ratio||

##### 智能报表报表项放置位置 :id=BIReportItemPlacement



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|NONE|无|none||
|ROWHEADER|行头|rowheader||
|COLHEADER|列头|colheader||

##### 智能报表报表项放置类型 :id=BIReportItemPlaceType



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|VISIBLE|默认显示|visible||
|INVISIBLE|默认隐藏|invisible||
|FROZEN|固定|frozen||

##### 智能报表报表项类型 :id=BIReportItemType



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|MEASURE|指标|measure||
|DIMENSION|维度|dimension||
|USER|用户自定义|user||

##### 最近使用 :id=recent_use



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|space|space|space||

##### 最近访问 :id=recent_visite



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|page|页面|page||

##### 最近访问对象 :id=recent_type



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|space|知识管理|space||

##### 核心产品功能状态 :id=product_func_state



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|0|未安装|not_install||
|1|已安装|Installed||
|2|已禁用|disabled||
|3|已安装（需重新加载）|installedneedreload||
|4|已禁用（需重新加载）|disabledneedreload||

##### 检索召回结果模式 :id=retrieval_mode



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|single|单一召回|single||
|cluster|合并召回|cluster||

##### 模型类别 :id=model_category



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|chat|对话|chat||
|embedding|向量|embedding||
|text_ranking|重排序|text_ranking||
|vision|多模态|vision||
|stt|语音识别|stt||
|tts|语音合成|tts||
|txt2img|文生图|txt2img||
|t2v|视频生成|t2v||

##### 模型能力 :id=model_capability



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|reasoning|推理|reasoning||
|coding|编码|coding||
|function_calling|工具调用|function_calling||
|streaming|流式输出|streaming||
|long_context|长上下文|long_context||

##### 模板分组 :id=stenci_type



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|space_stencil|空间|space_stencil||
|org_stencil|组织|org_stencil||

##### 模板可见范围 :id=stencil_scope



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|space_stencil|空间模板|space_stencil||
|org_stencil|组织模板|org_stencil||

##### 消息发送方类型 :id=msg_sender_type



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|user|用户|user||
|agent|AI智能体|agent||
|system|系统通知|system||

##### 特定版本类型 :id=pscoreprdfunc_spec_version_type



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|history|历史版本|history||
|custom|定制版本|custom||

##### 监听通知事件 :id=notify_event



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|ProjMgmt.work_item.create:AFTER|创建工作项|projmgmt_work_item_create_after||
|ProjMgmt.work_item.delete:AFTER|删除工作项|projmgmt_work_item_delete_after||
|ProjMgmt.work_item.archive:AFTER|归档工作项|projmgmt_work_item_archive_after||

##### 知识库同步频率 :id=KBSyncFrequency



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|daily|每天|daily||
|weekly|每周|weekly||
|monthly|每月|monthly||

##### 知识库文档类型2 :id=ai_kb_document_type2



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|case_card|案卡|case_card||
|case_file|卷宗|case_file||
|legal_document|文书|legal_document||

##### 知识库检索记录来源 :id=ai_search_source



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|common|常规|common||
|ai_agent|智能体|ai_agent||
|test|检索测试|test||

##### 知识库源类型 :id=knowledge_source



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|ragflow|RAGFlow|ragflow|对接 RAGFlow 开源 RAG 平台|
|dify_kb|Dify 知识库|dify_kb|对接 Dify 的知识库 API|
|langchain|LangChain|langchain|对接 LangChain|
|elasticsearch|Elasticsearch|elasticsearch|使用 ES 的 dense_vector 或 knn 功能|
|yuque|语雀|yuque|通过语雀开放 API 同步知识库|
|custom_api|自定义 API|custom_api|通用 HTTP 接口，通过 query_template 配置请求格式|
|nas_sync|网络存储同步|nas_sync||
|nas_virtual|网络存储（虚拟）|nas_virtual||
|local|本地模式|local||

##### 空间共享状态 :id=space_shared_status



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|0|未共享|item_0||
|1|全部页面共享|item_1||
|2|部分页面共享|item_2||

##### 空间共享页面范围 :id=space_shared_scope



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|1|全部页面|item_1||
|2|自定义页面|item_2||

##### 背景样式 :id=background_style



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|blue-span|蓝色|blue_SUB_span||
|green-span|绿色|green_SUB_span||
|orange-span|橙色|orange_SUB_span||
|grey-span|灰色|grey_SUB_span||
|purple-span|紫色|purple_SUB_span||
|red-span|红色|red_SUB_span||

##### 自动化规则类型 :id=auto_flow_type



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|TIMERTASK|定时作业|timertask||
|EVENTHOOK|事件处理|eventhook||
|FIELDCHANGEHOOK|属性变化处理|fieldchangehook||
|WEBHOOK|收到WebHook|webhook||
|MCPTOOL|提供MCP工具|mcptool||

##### 自定义切片 :id=custom_chunk



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|0|使用知识库默认|item_0||
|1|是|item_1||

##### 角色类型 :id=role_type



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|admin|管理员|admin|业务对象的管理员，可维护该业务对象全部数据|
|user|普通成员|user|业务对象的普通成员，可维护该业务对象的子数据|
|reader|只读成员|reader|业务对象的只读用户，只能查看该业务对象基本信息及其子数据|

##### 触发类型 :id=trigger_type



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|MANUAL|手动触发|manual||
|SCHEDULED|定时触发|scheduled||

##### 认证方式 :id=api_auth_type_codelist



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|none|无认证|none||
|api_key|API Key|api_key||
|bearer_token|Bearer Token|bearer_token||
|oauth2|OAuth2|oauth2||
|access_key_secret|Access Key/Secret|access_key_secret||

##### 记忆模式 :id=memory_mode



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|none|无记忆|none||
|short_term|短期记忆|short_term||
|long_term|长期记忆|long_term||
|hybrid|混合模式|hybrid||

##### 记忆隔离模式 :id=memory_isolation_mode



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|NONE|无|none||
|BUSINESS_SCOPE|业务范围|business_scope||
|USER_SCOPE|用户范围|user_scope||
|BUSINESS_USER_SCOPE|业务用户范围|business_user_scope||

##### 访问策略 :id=access_strategy



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|INCLUSION|包含|inclusion||
|EXCLUSION|排除|exclusion||

##### 评论主体类型 :id=principal_type



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|work_item|工作项|work_item||
|idea|需求|idea||
|test_case|用例|test_case||

##### 调度类型 :id=schedule_type



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|CRON|Cron表达式|cron||

##### 资源库同步类型 :id=resource_kb_sync_type



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|none|不同步创建知识库|none||
|resource|按资源类型创建一个知识库|resource||
|record|每条资源数据创建一个知识库|record||

##### 输出格式 :id=output_format_type



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|JSON|JSON|json||
|Markdown|文档|markdown||

##### 通用文本清洗配置 :id=text_clean_config



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|remove_extra_whitespace|合并多个空格/换行为单个|remove_extra_whitespace||
|remove_html_tags|剥离 HTML 标签（保留文本）|remove_html_tags||
|remove_js_css|移除 <script> <style> 内容|remove_js_css||
|remove_emails_url|移除电子邮箱及Url|remove_emails_url||
|remove_img_url|移除Md格式中的图片与链接|remove_img_url||
|normalize_punctuation|统一中英文标点（如 “” → "")|normalize_punctuation||
|remove_header_footer|尝试移除页眉页脚（PDF 场景）|remove_header_footer||
|remove_watermark|启用 OCR 后处理识别水印并过滤|remove_watermark||

##### 通知分组 :id=group



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|product|产品管理|product||
|wiki|知识管理|wiki||

##### 通知子类 :id=DENotifySubType



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|NONE|无|none||
|EVENTHOOK|事件通知|eventhook||
|FIELDCHANGEHOOK|属性变更通知|fieldchangehook||

##### 通知消息类型 :id=WFInfomMsgType



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|1|系统消息|INTERNAL||
|2|电子邮件|EMAIL||
|4|手机短信|SMS||
|32|微信|WT||
|64|钉钉|DT||
|128|企业微信|ENTWT||

##### 逻辑子类 :id=DELogicSubType



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|NONE|无|none||
|DEFIELD|属性逻辑|defield|面向属性的处理逻辑子类型，|
|ATTACHTODEACTION|附加到行为|attachtodeaction|附加到指定行为|
|ATTACHTODEDATASET|附加到数据集|attachtodedataset|附加到指定数据集|
|WEBHOOK|收到WebHook|webhook|WEB钩子|
|MCPTOOL|提供MCP工具|mcptool||
|EVENTHOOK|事件处理|eventhook||
|TIMERTASK|定时作业|timertask|后台定时作业|
|FIELDCHANGEHOOK|属性变化处理|fieldchangehook||
|USER|用户自定义|user||
|USER2|用户自定义2|user2||
|USER3|用户自定义3|user3||
|USER4|用户自定义4|user4||

##### 非空间成员查看共享页面类型 :id=shared_page_check_type



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|reader|仅查看|reader||
|user|可编辑|user||

##### 页面共享类型 :id=shared_page_type



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|0|未共享|item_0||
|1|仅自身页面共享|item_1||
|2|同时共享子页面|item_2||

##### 页面类型 :id=page_type



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|1|文档|item_1||
|2|分组|item_2||
|3|画板|item_3||

##### 页面高级搜索属性 :id=page_advanced_search_field



| 值col150        |    文本col150    |   代码名col150    |  备注col800     |
| --------   |------------|------------|------------|
|n_name_like|主题|n_name_like||
|n_content_like|页面内容|n_content_like||

