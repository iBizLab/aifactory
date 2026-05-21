# 智能体业务上下文(ai_agent_context)  <!-- {docsify-ignore-all} -->


## 属性
|    中文名col150 | 属性名称col200           | 类型col200     | 长度col100    |允许为空col100    |  备注col500  |
| --------   |------------| -----  | -----  | :----: | -------- |
|有效|ACTIVE|是否逻辑||是||
|分组标记|AGENT_GROUP_TAG|文本，可指定长度|200|是||
|智能体标识|AI_AGENT_ID|外键值|100|是||
|引用知识库集合|AI_AGENT_KNOWLEDGE_RELS|一对多动态对象|1048576|是||
|智能体名称|AI_AGENT_NAME|外键值文本|200|是||
|引用工具集合|AI_AGENT_TOOL_RELS|一对多动态对象|1048576|是||
|模型标识|AI_MODEL_ID|外键值|100|是||
|模型名称|AI_MODEL_NAME|外键值文本|200|是||
|允许任意知识库|ALLOW_ANY_KNOWLEDGE_BASE|是否逻辑||是||
|代码标识|CODE_NAME|文本，可指定长度|100|否||
|调试数据|CONTEXT_DEBUG_DATA|长文本，没有长度限制|1048576|是||
|建立人|CREATE_MAN|文本，可指定长度|100|否||
|建立时间|CREATE_TIME|日期时间型||否||
|自定义代码|CUSTOM_CODE|长文本，没有长度限制|16777215|是||
|自定义建议提示词|CUSTOM_SUGGESTION_PROMPT|长文本，没有长度限制|1048576|是||
|deep_research|DEEP_RESEARCH|整型||是||
|默认系统提示词|DEFAULT_SYSTEM_PROMPT|长文本，没有长度限制|1048576|是||
|描述|DESCRIPTION|长文本，长度1000|2000|是||
|支持联网搜索|ENABLE_SEARCHING|是否逻辑||是||
|启用问题建议|ENABLE_SUGGESTED_QUESTIONS|是否逻辑||是||
|启用思考链|ENABLE_THINKING|是否逻辑||是||
|调用工具|ENABLE_TOOLS|是否逻辑||是||
|智能体模式|FLOW_MODE|[单项选择(文本值)](index/dictionary_index#flow_mode "智能体工作流模式")|60|是||
|生成模式|GENERATION_MODE|[单项选择(文本值)](index/dictionary_index#ai_mode "AI生成模式")|60|是||
|智能体业务上下文标识<sup class="footnote-symbol"><font color=orange>[PK]</font></sup>|ID|全局唯一标识，文本类型，用户不可见|100|否||
|是否默认Agent|IS_DEFAULT|是否逻辑||否||
|引用知识库|KBS|长文本，长度1000|4000|是||
|知识库模式|KB_MODE|[单项选择(文本值)](index/dictionary_index#AIKBMode "AI知识库模式")|60|是||
|知识库标识集合|KB_TAGS|文本，可指定长度|100|是||
|最大输入token数|MAX_INPUT_TOKENS|整型||是||
|mcp服务标识集合|MCP_SERVER_TAGS|文本，可指定长度|100|是||
|记忆存储文档标记|MEMORY_DOC_TAG|文本，可指定长度|200|是||
|记忆隔离模式|MEMORY_ISOLATION_MODE|[单项选择(文本值)](index/dictionary_index#memory_isolation_mode "记忆隔离模式")|60|是||
|记忆存储知识库标记|MEMORY_KB_TAG|文本，可指定长度|200|是||
|记忆对话轮数|MEMORY_MAX_TURNS|整型||是||
|记忆模式|MEMORY_MODE|[单项选择(文本值)](index/dictionary_index#memory_mode "记忆模式")|60|是||
|名称|NAME|文本，可指定长度|200|是||
|输出格式|OUTPUT_FORMAT_TYPE|[单项选择(文本值)](index/dictionary_index#output_format_type "输出格式")|200|是||
|启用增强目录召回|PAGE_INDEX|是否逻辑||是||
|发布技能到cloud|PUBLISH_SKILL|是否逻辑||是||
|召回重排|RERANK|是否逻辑||是||
|召回重排模型|RERANK_MODEL|外键值文本|100|是||
|模型标识|RERANK_MODEL_ID|外键值|100|是||
|业务范围|SCOPES|[多项选择(文本值)](index/dictionary_index#ai_agent_context_scopes "智能体业务范围")|500|是||
|排序|SEQUENCE|整型||是||
|召回相似度阈值|SIMILARITY_THRESHOLD|数值||是||
|技能加载模式|SKILL_LOAD_MODE|[单项选择(文本值)](index/dictionary_index#ai_skill_load_mode "AI技能加载模式")|60|是||
|技能提示词|SKILL_PROMPT|长文本，没有长度限制|1048576|是||
|技能说明|SKILL_README|长文本，没有长度限制|1048576|是||
|激活技能标记|SKILL_TAGS|长文本，没有长度限制|1048576|是||
|规格库标识|SPEC_KB_ID|外键值|100|是||
|规格库|SPEC_KB_NAME|外键值文本|200|是||
|流式输出|STREAM|是否逻辑||是||
|预置建议问题|SUGGESTED_QUESTIONS|文本数组（没有长度限制）|1000|是||
|总结智能体|SYNTHESIZER|文本，可指定长度|100|是||
|系统标记|SYSTEM_FLAG|是否逻辑||是||
|模型随机性参数|TEMPERATURE|数值||是||
|引用工具|TOOLS|长文本，长度1000|4000|是||
|工具调用超限提示语|TOOL_EXCEED_MESSAGE|长文本，没有长度限制|1048576|是||
|最大工具调用次数|TOOL_MAX_CALLS|整型||是||
|最大召回数量|TOP_K|整型||是||
|概率核采样|TOP_P|数值||是||
|截断策略|TRIMMING_STRATEGY|[单项选择(文本值)](index/dictionary_index#trimming_strategy "截断策略")|60|是||
|更新人|UPDATE_MAN|文本，可指定长度|100|否||
|更新时间|UPDATE_TIME|日期时间型||否||
|使用全文推理|USE_FULLTEXT|是否逻辑||是||
|使用知识图谱|USE_KG|是否逻辑||是||
|向量相似度权重|VECTOR_SIMILARITY_WEIGHT|数值||是||
|视觉识别提示词|VLM_PROMPT|长文本，没有长度限制|1048576|是||
|欢迎消息模板|WELCOME_MESSAGE|长文本，没有长度限制|1048576|是||


## 关系

<el-row>
<el-tabs v-model="show_der">
<el-tab-pane label="主关系" name="major">

| 名称col350     |   从实体col200 | 关系类型col200     |   备注col500  |
| -------- |---------- |------------|----- |
|[DER1N_AI_AGENT_ASSIGNMENT_AI_AGENT_CONTEXT_CONTEXT_ID](der/DER1N_AI_AGENT_ASSIGNMENT_AI_AGENT_CONTEXT_CONTEXT_ID)|[智能体分配(AI_AGENT_ASSIGNMENT)](module/ai/ai_agent_assignment)|1:N关系||
|[DER1N_AI_AGENT_CONVERSATION_AI_AGENT_CONTEXT_AI_AGENT_CONTEXT_ID](der/DER1N_AI_AGENT_CONVERSATION_AI_AGENT_CONTEXT_AI_AGENT_CONTEXT_ID)|[智能体会话(AI_AGENT_CONVERSATION)](module/ai/ai_agent_conversation)|1:N关系||
|[DER1N_AI_AGENT_SESSION_AI_AGENT_CONTEXT_CONTEXT_ID](der/DER1N_AI_AGENT_SESSION_AI_AGENT_CONTEXT_CONTEXT_ID)|[智能体会话(AI_AGENT_SESSION)](module/ai/ai_agent_session)|1:N关系||


</el-tab-pane>
<el-tab-pane label="从关系" name="minor">

|  名称col350   | 主实体col200   | 关系类型col200   |    备注col500  |
| -------- |---------- |-----------|----- |
|[DER1N_AI_AGENT_CONTEXT_AI_AGENT_AI_AGENT_ID](der/DER1N_AI_AGENT_CONTEXT_AI_AGENT_AI_AGENT_ID)|[智能体(AI_AGENT)](module/ai/ai_agent)|1:N关系||
|[DER1N_AI_AGENT_CONTEXT_AI_KNOWLEDGE_BASE_SPEC_KB_ID](der/DER1N_AI_AGENT_CONTEXT_AI_KNOWLEDGE_BASE_SPEC_KB_ID)|[知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base)|1:N关系||
|[DER1N_AI_AGENT_CONTEXT_AI_MODEL_AI_MODEL_ID](der/DER1N_AI_AGENT_CONTEXT_AI_MODEL_AI_MODEL_ID)|[AI大模型(AI_MODEL)](module/ai/ai_model)|1:N关系||
|[DER1N_AI_AGENT_CONTEXT_AI_MODEL_RERANK_MODEL_ID](der/DER1N_AI_AGENT_CONTEXT_AI_MODEL_RERANK_MODEL_ID)|[AI大模型(AI_MODEL)](module/ai/ai_model)|1:N关系||

</el-tab-pane>
</el-tabs>
</el-row>

## 行为
| 中文名col200    | 代码名col150    | 类型col150    | 事务col100   | 批处理col100   | 附加操作col100  | 插件col150    |  备注col300  |
| -------- |---------- |----------- |:----:|:----:|---------| ----- | ----- |
|异步_批量执行|Async_batch_execution|用户自定义|默认|不支持||||
|CheckKey|CheckKey|内置方法|默认|不支持||||
|Create|Create|内置方法|默认|不支持|[附加操作](index/action_logic_index#ai_agent_context_Create)|||
|Get|Get|内置方法|默认|不支持||||
|GetDraft|GetDraft|内置方法|默认|不支持||||
|Remove|Remove|内置方法|默认|支持|[附加操作](index/action_logic_index#ai_agent_context_Remove)|||
|Save|Save|内置方法|默认|不支持||||
|Update|Update|内置方法|默认|不支持|[附加操作](index/action_logic_index#ai_agent_context_Update)|||
|flow智能体克隆|agent_flow_clone|[实体处理逻辑](module/ai/ai_agent_context/logic/agent_flow_clone "agent_flow_clone")|默认|不支持||||
|批量执行|batch_execution|[实体处理逻辑](module/ai/ai_agent_context/logic/batch_execution "批量执行")|默认|不支持||||
|绑定智能体|bind|[实体处理逻辑](module/ai/ai_agent_context/logic/bind "绑定智能体")|默认|不支持||||
|填充智能体参数|fill_with_agent|[实体处理逻辑](module/ai/ai_agent_context/logic/fill_with_agent "fill_with_agent")|默认|不支持||||
|find_by_code|find_by_code|[实体处理逻辑](module/ai/ai_agent_context/logic/get_by_code "get_by_code")|默认|不支持||||

## 处理逻辑
| 中文名col200    | 代码名col150    | 子类型col150    | 插件col200    |  备注col550  |
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

## 数据查询
| 中文名col200    | 代码名col150    | 默认查询col100 | 权限使用col100 | 自定义SQLcol100 |  备注col600|
| --------  | --------   | :----:  |:----:  | :----:  |----- |
|[DEFAULT](module/ai/ai_agent_context/query/Default)|DEFAULT|是|否 |否 ||
|[默认（全部数据）(VIEW)](module/ai/ai_agent_context/query/View)|VIEW|否|否 |否 ||
|[待绑定(bind)](module/ai/ai_agent_context/query/bind)|bind|否|否 |否 ||
|[deep_research_agent](module/ai/ai_agent_context/query/deep_research_agent)|deep_research_agent|否|否 |否 ||
|[dynamic_agent](module/ai/ai_agent_context/query/dynamic_agent)|dynamic_agent|否|否 |否 ||
|[业务过滤(filter)](module/ai/ai_agent_context/query/filter)|filter|否|否 |否 ||
|[flow智能体(flow_agents)](module/ai/ai_agent_context/query/flow_agents)|flow_agents|否|否 |否 ||
|[full_text_agent](module/ai/ai_agent_context/query/full_text_agent)|full_text_agent|否|否 |否 ||
|[hub智能体(hub_agents)](module/ai/ai_agent_context/query/hub_agents)|hub_agents|否|否 |否 ||
|[lookup_agent](module/ai/ai_agent_context/query/lookup_agent)|lookup_agent|否|否 |否 ||
|[skill智能体(skill_agents)](module/ai/ai_agent_context/query/skill_agents)|skill_agents|否|否 |否 ||
|[系统的(system)](module/ai/ai_agent_context/query/system)|system|否|否 |否 ||

## 数据集合
| 中文名col200  | 代码名col150  | 类型col100 | 默认集合col100 |   插件col200|   备注col500|
| --------  | --------   | :----:   | :----:   | ----- |----- |
|[DEFAULT](module/ai/ai_agent_context/dataset/Default)|DEFAULT|数据查询|是|||
|[待绑定(bind)](module/ai/ai_agent_context/dataset/bind)|bind|数据查询|否|||
|[deep_research_agent](module/ai/ai_agent_context/dataset/deep_research_agent)|deep_research_agent|数据查询|否|||
|[dynamic_agent](module/ai/ai_agent_context/dataset/dynamic_agent)|dynamic_agent|[实体逻辑](module/ai/ai_agent_context/logic/dynamic_agent_dataset)|否|||
|[业务过滤(filter)](module/ai/ai_agent_context/dataset/filter)|filter|数据查询|否|||
|[flow智能体(flow_agents)](module/ai/ai_agent_context/dataset/flow_agents)|flow_agents|数据查询|否|||
|[全部数据(full_info)](module/ai/ai_agent_context/dataset/full_info)|full_info|数据查询|否|||
|[full_text_agent](module/ai/ai_agent_context/dataset/full_text_agent)|full_text_agent|数据查询|否|||
|[hub智能体(hub_agents)](module/ai/ai_agent_context/dataset/hub_agents)|hub_agents|数据查询|否|||
|[lookup_agent](module/ai/ai_agent_context/dataset/lookup_agent)|lookup_agent|数据查询|否|||
|[skill智能体(skill_agents)](module/ai/ai_agent_context/dataset/skill_agents)|skill_agents|数据查询|否|||
|[系统的(system)](module/ai/ai_agent_context/dataset/system)|system|数据查询|否|||

## 数据权限

##### 全部数据（读） :id=ai_agent_context-ALL_R

<p class="panel-title"><b>数据范围</b></p>

* `全部数据`

<p class="panel-title"><b>数据能力</b></p>

* `READ`



##### 全部数据（读写） :id=ai_agent_context-ALL_RW

<p class="panel-title"><b>数据范围</b></p>

* `全部数据`

<p class="panel-title"><b>数据能力</b></p>

* `UPDATE`
* `CREATE`
* `DELETE`
* `READ`



##### 全部数据（写） :id=ai_agent_context-ALL_W

<p class="panel-title"><b>数据范围</b></p>

* `全部数据`

<p class="panel-title"><b>数据能力</b></p>

* `CREATE`



##### 系统的（读） :id=ai_agent_context-SYSTEM_R

<p class="panel-title"><b>数据范围</b></p>

* `数据集合` ：[系统的(system)](module/ai/ai_agent_context#数据集合)

<p class="panel-title"><b>数据能力</b></p>

* `READ`



##### 我的智能体上下文（读写） :id=ai_agent_context-USER_RW

<p class="panel-title"><b>数据范围</b></p>

* `自定义条件` ：`[('CREATE_MAN','=',#{srf.sessioncontext.srfpersonid})]`

<p class="panel-title"><b>数据能力</b></p>

* `READ`
* `UPDATE`
* `DELETE`
* `CREATE`




## 搜索模式
|   搜索表达式col350   |    属性名col200    |    搜索模式col200        |备注col500  |
| -------- |------------|------------|------|
|N_AI_AGENT_ID_EQ|智能体标识|EQ||
|N_AI_MODEL_ID_EQ|模型标识|EQ||
|N_CREATE_MAN_EQ|建立人|EQ||
|N_DEEP_RESEARCH_EQ|deep_research|EQ||
|N_ID_EQ|智能体业务上下文标识|EQ||
|N_KB_MODE_EQ|知识库模式|EQ||
|N_NAME_LIKE|名称|LIKE||
|N_OUTPUT_FORMAT_TYPE_EQ|输出格式|EQ||
|N_RERANK_MODEL_ID_EQ|模型标识|EQ||
|N_SKILL_LOAD_MODE_EQ|技能加载模式|EQ||
|N_SPEC_KB_ID_EQ|规格库标识|EQ||
|N_SPEC_KB_NAME_EQ|规格库|EQ||
|N_SPEC_KB_NAME_LIKE|规格库|LIKE||
|N_SYSTEM_FLAG_EQ|系统标记|EQ||

## 界面行为
|  中文名col200 |  代码名col150 |  标题col100   |     处理目标col100   |    处理类型col200        |  备注col500       |
| --------| --------| -------- |------------|------------|------------|
| 打开完整信息视图 | open_info_view | 查看完整配置 |单项数据（主键）|<details><summary>打开视图或向导（模态）</summary>[智能体](app/view/ai_agent_context_info_view)</details>||
| 打开建立的智能体 | open_edit_view | 打开建立的智能体 |单项数据|<details><summary>打开视图或向导（模态）</summary>[智能体](app/view/ai_agent_context_edit_view)</details>||
| 克隆Flow智能体 | agent_flow_clone | 克隆Flow智能体 |无数据|<details><summary>打开视图或向导（模态）</summary>[克隆flow智能体](app/view/ai_agent_context_flow_agent_clone_view)</details>||
| 编辑 | edit | 编辑 |单项数据（主键）|<details><summary>打开视图或向导（模态）</summary>[智能体](app/view/ai_agent_context_edit_view)</details>||
| 打开批量执行操作视图 | open_batch_execution_view | 后台批量执行 |单项数据（主键）|<details><summary>打开视图或向导（模态）</summary>[后台批量执行](app/view/ai_agent_context_batch_execution_option_view)</details>||
| 提示词反馈 | prompt_feedback | 提示词反馈 |单项数据|用户自定义||
| 打开调试页面 | open_debug_view | 打开调试页面 |无数据|<details><summary>打开视图或向导（模态）</summary>[调试](app/view/ai_agent_session_debug_view)</details>||
| 打开审查报告页面 | open_report_grid_view | 打开审查报告页面 |无数据|<details><summary>打开视图或向导（模态）</summary>[智能审查报告](app/view/ai_review_report_grid_view)</details>||
| 查看 | check | 查看 |单项数据（主键）|<details><summary>打开视图或向导（模态）</summary>[智能体](app/view/ai_agent_context_info_view)</details>||
| 引用资料 | header_extra_link | 引用资料 |无数据|<details><summary>打开视图或向导（模态）</summary>[选择资资料](app/view/search_hub_advance_pick_up_view)</details>||
| 智能创建 | ai_create | 智能创建 |无数据|<details><summary>打开视图或向导（模态）</summary>[创建智能体](app/view/ai_agent_context_ai_create_view)</details>||
| 删除 | delete | 删除 |多项数据（主键）|<details><summary>后台调用</summary>[Remove](#行为)||
| 上下文模版反馈 | template_feedback | 上下文模版反馈 |单项数据|用户自定义||
| 确认单一执行 | confirm_execute | 确认 |单项数据|用户自定义||
| 绑定智能体 | bind | 绑定 |单项数据（主键）|<details><summary>后台调用</summary>[bind](#行为)||
| 确认创建 | confirm_creation | 确认 |单项数据|用户自定义||
| 打开单一执行操作视图 | open_execute_view | 执行 |单项数据（主键）|<details><summary>打开视图或向导（模态）</summary>[执行](app/view/ai_agent_context_execute_option_view)</details>||
| 创建智能体 | create_ai_agent_context | 创建智能体 |单项数据|<details><summary>打开聊天界面</summary></details>||
| 新建Flow智能体 | create_flow_agent | 新建Flow智能体 |无数据|<details><summary>打开视图或向导（模态）</summary>[Flow智能体新建](app/view/ai_agent_context_flow_agent_create_view)</details>||
| 编辑智能体上下文 | edit_agent | 编辑 |单项数据（主键）|<details><summary>打开视图或向导（模态）</summary>[智能体](app/view/ai_agent_context_edit_view)</details>||
| 文档问题沟通 | doc_issue_communication | 文档问题沟通 |单项数据|<details><summary>打开聊天界面</summary></details>||
| 批量执行智能体 | batch_execution_agent | 批量执行智能体 |单项数据|<details><summary>后台调用</summary>[Async_batch_execution](#行为)||
| 智能体工作流设计 | open_design_view | 设计 |单项数据（主键）|<details><summary>打开视图或向导（模态）</summary>[flow智能体设计](app/view/ai_agent_context_flow_design_exp_view)</details>||
| 提示词填充 | prompt | 提示词智能生成 |单项数据|<details><summary>打开聊天界面</summary></details>||

## 界面逻辑
|  中文名col200 | 代码名col150 | 备注col900 |
| --------|--------|--------|
|[prompt_feedback](module/ai/ai_agent_context/uilogic/prompt_feedback)|prompt_feedback||
|[run智能体逻辑](module/ai/ai_agent_context/uilogic/run)|run||
|[template_feedback](module/ai/ai_agent_context/uilogic/template_feedback)|template_feedback||
|[提示并打开审查报告](module/ai/ai_agent_context/uilogic/open_report)|open_report|打开提示弹窗并按照用户选择打开审查报告页面|

<div style="display: block; overflow: hidden; position: fixed; top: 140px; right: 100px;">

##### 导航
<el-anchor >
<el-anchor-link :href="`#/module/ai/ai_agent_context?id=属性`">
  属性
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_agent_context?id=关系`">
  关系
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_agent_context?id=行为`">
  行为
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_agent_context?id=处理逻辑`">
  处理逻辑
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_agent_context?id=数据查询`">
  数据查询
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_agent_context?id=数据集合`">
  数据集合
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_agent_context?id=数据权限`">
  数据权限
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_agent_context?id=搜索模式`">
  搜索模式
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_agent_context?id=界面行为`">
  界面行为
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_agent_context?id=界面逻辑`">
  界面逻辑
</el-anchor-link>
</el-anchor>
</div>

<script>
 const { createApp } = Vue
  createApp({
    data() {
      return {
show_der:'major',


      }
    },
    methods: {
    }
  }).use(ElementPlus).mount('#app')
</script>