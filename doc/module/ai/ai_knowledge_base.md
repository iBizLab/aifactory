# 知识库(ai_knowledge_base)  <!-- {docsify-ignore-all} -->


## 属性
|    中文名col150 | 属性名称col200           | 类型col200     | 长度col100    |允许为空col100    |  备注col500  |
| --------   |------------| -----  | -----  | :----: | -------- |
|目录标识|CATEGORY_ID|外键值|100|是||
|目录|CATEGORY_NAME|外键值文本|200|是||
|交谈模型|CHAT_MODEL|外键值文本|100|是||
|交谈模型标识|CHAT_MODEL_ID|外键值|100|是||
|切片方法|CHUNK_METHOD|[单项选择(文本值)](index/dictionary_index#chunkingstrategy "切片策略")|100|是||
|代码标识|CODE_NAME|文本，可指定长度|200|是||
|建立人|CREATE_MAN|文本，可指定长度|100|否||
|建立时间|CREATE_TIME|日期时间型||否||
|描述|DESCRIPTION|长文本，长度1000|2000|是||
|描述向量|DESCRIPTION_VECTOR|向量|1024|是||
|文档数|DOCUMENT_CNT|整型||是||
|embedding模型|EMBEDDING_MODEL|外键值文本|100|是||
|嵌入模型标识|EMBEDDING_MODEL_ID|外键值|100|是||
|引导提示词|GUIDANCE_PROMPT|长文本，长度1000|2000|是||
|引导词向量|GUIDANCE_PROMPT_VECTOR|向量|1024|是||
|知识库标识<sup class="footnote-symbol"><font color=orange>[PK]</font></sup>|ID|全局唯一标识，文本类型，用户不可见|100|否||
|是否已归档|IS_ARCHIVED|是否逻辑||是||
|是否已删除|IS_DELETED|是否逻辑||是||
|是否星标|IS_FAVORITE|文本，可指定长度|200|是||
|业务键值|KEY|文本，可指定长度|100|是||
|命中文档|MATCHED_DOCUMENTS|一对多动态对象|1048576|是||
|文档元数据|META_DATA|长文本，没有长度限制|1048576|是||
|知识库名称|NAME|文本，可指定长度|200|是||
|智能目录索引|PAGEINDEX|是否逻辑||是||
|目录信息|PAGE_INDEX_INFO|文本，可指定长度|100|是||
|解析文档数|PARSED_CNT|整型||是||
|解析配置|PARSER_CONFIG|一对一关系数据对象|1048576|是||
|数据记录标识|RECORD_ID|外键值|60|是||
|标题|RECORD_TITLE|外键值文本|1000|是||
|召回重排|RERANK|单项选择(数值)||是||
|召回重排模型|RERANK_MODEL|外键值文本|100|是||
|召回重排模型标识|RERANK_MODEL_ID|外键值|100|是||
|数据资源|RESOURCE|外键值文本|200|是||
|数据资源|RESOURCE_CODE|外键值附加数据|100|是||
|资源标识|RESOURCE_ID|外键值|100|是||
|所属对象|SCOPE_ID|文本，可指定长度|100|是||
|所属|SCOPE_TYPE|[单项选择(文本值)](index/dictionary_index#user_scope_type "所属类型（包含个人）")|60|是||
|召回相似度阈值|SIMILARITY_THRESHOLD|数值||是||
|知识库源标识|SOURCE_ID|外键值|100|是||
|知识库源名称|SOURCE_NAME|外键值文本|200|是||
|资源类型|SOURCE_TYPE|多项选择(文本值)|2000|是||
|状态|STATUS|[单项选择(文本值)](index/dictionary_index#slice_status "文档切片状态")|60|是||
|摘要|SUMMARY|文本，可指定长度|100|是||
|标签集|TAG_SETS|多项选择(文本值)|2000|是||
|最大召回数量|TOP_K|整型||是||
|更新人|UPDATE_MAN|文本，可指定长度|100|否||
|更新时间|UPDATE_TIME|日期时间型||否||
|使用知识图谱|USE_KG|是否逻辑||是||
|向量相似度权重|VECTOR_SIMILARITY_WEIGHT|数值||是||
|可见范围|VISIBILITY|单项选择(文本值)|60|否||


###### 属性组

<el-row>
<el-tabs v-model="show_field_group">

<el-tab-pane label="ai_kb_query" name="field_group_ai_kb_query">

|    中文名col150 | 属性名称col200           | 类型col200     | 长度col100    |允许为空col100    |  备注col500  |
| --------   |------------| -----  | -----  | :----: | -------- |
|知识库标识<sup class="footnote-symbol"><font color=orange>[PK]</font></sup>|ID|全局唯一标识，文本类型，用户不可见|100|否||
|知识库名称|NAME|文本，可指定长度|200|是||
|更新时间|UPDATE_TIME|日期时间型||否||
|引导提示词|GUIDANCE_PROMPT|长文本，长度1000|2000|是||
|数据资源|RESOURCE|外键值文本|200|是||
|命中文档|MATCHED_DOCUMENTS|一对多动态对象|1048576|是||
|目录|CATEGORY_NAME|外键值文本|200|是||
|描述|DESCRIPTION|长文本，长度1000|2000|是||
|知识库源名称|SOURCE_NAME|外键值文本|200|是||

</el-tab-pane>

</el-tabs>
</el-row>

## 关系

<el-row>
<el-tabs v-model="show_der">
<el-tab-pane label="主关系" name="major">

| 名称col350     |   从实体col200 | 关系类型col200     |   备注col500  |
| -------- |---------- |------------|----- |
|[DER1N_AI_AGENT_CONTEXT_AI_KNOWLEDGE_BASE_SPEC_KB_ID](der/DER1N_AI_AGENT_CONTEXT_AI_KNOWLEDGE_BASE_SPEC_KB_ID)|[智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context)|1:N关系||
|[DER1N_AI_AGENT_KNOWLEDGE_REL_AI_KNOWLEDGE_BASE_AI_KNOWLEDGE_BASE_ID](der/DER1N_AI_AGENT_KNOWLEDGE_REL_AI_KNOWLEDGE_BASE_AI_KNOWLEDGE_BASE_ID)|[智能体知识库引用(AI_AGENT_KNOWLEDGE_REL)](module/ai/ai_agent_knowledge_rel)|1:N关系||
|[DER1N_AI_KB_DOCUMENT_AI_KNOWLEDGE_BASE_KB_ID](der/DER1N_AI_KB_DOCUMENT_AI_KNOWLEDGE_BASE_KB_ID)|[知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document)|1:N关系||
|[DER1N_AI_KB_DOCUMENT_SYNC_AI_KNOWLEDGE_BASE_AI_KNOWLEDGE_BASE_ID](der/DER1N_AI_KB_DOCUMENT_SYNC_AI_KNOWLEDGE_BASE_AI_KNOWLEDGE_BASE_ID)|[知识库文档同步(AI_KB_DOCUMENT_SYNC)](module/ai/ai_kb_document_sync)|1:N关系||
|[DER1N_AI_KB_GRAPH_ENTITY_AI_KNOWLEDGE_BASE_KB_ID](der/DER1N_AI_KB_GRAPH_ENTITY_AI_KNOWLEDGE_BASE_KB_ID)|[知识库图谱实体(AI_KB_GRAPH_ENTITY)](module/ai/ai_kb_graph_entity)|1:N关系||
|[DER1N_AI_KB_GRAPH_RELATION_AI_KNOWLEDGE_BASE_KB_ID](der/DER1N_AI_KB_GRAPH_RELATION_AI_KNOWLEDGE_BASE_KB_ID)|[知识库图谱关系(AI_KB_GRAPH_RELATION)](module/ai/ai_kb_graph_relation)|1:N关系||
|[DER1N_AI_KB_MEMBER_AI_KNOWLEDGE_BASE_KB_ID](der/DER1N_AI_KB_MEMBER_AI_KNOWLEDGE_BASE_KB_ID)|[知识库成员(AI_KB_MEMBER)](module/ai/ai_kb_member)|1:N关系||
|[DER1N_AI_REVIEW_REPORT_AI_KNOWLEDGE_BASE_KB_ID](der/DER1N_AI_REVIEW_REPORT_AI_KNOWLEDGE_BASE_KB_ID)|[智能审查报告(AI_REVIEW_REPORT)](module/ai/ai_review_report)|1:N关系||
|[DERCUSTOM_AI_KB_CHUNKING_STRATEGY_AI_KNOWLEDGE_BASE](der/DERCUSTOM_AI_KB_CHUNKING_STRATEGY_AI_KNOWLEDGE_BASE)|[知识库文档切片策略(AI_KB_CHUNKING_STRATEGY)](module/ai/ai_kb_chunking_strategy)|自定义关系||


</el-tab-pane>
<el-tab-pane label="从关系" name="minor">

|  名称col350   | 主实体col200   | 关系类型col200   |    备注col500  |
| -------- |---------- |-----------|----- |
|[DER1N_AI_KNOWLEDGE_BASE_AI_KNOWLEDGE_SOURCE_SOURCE_ID](der/DER1N_AI_KNOWLEDGE_BASE_AI_KNOWLEDGE_SOURCE_SOURCE_ID)|[知识库源(AI_KNOWLEDGE_SOURCE)](module/ai/ai_knowledge_source)|1:N关系||
|[DER1N_AI_KNOWLEDGE_BASE_AI_MODEL_CHAT_MODEL_ID](der/DER1N_AI_KNOWLEDGE_BASE_AI_MODEL_CHAT_MODEL_ID)|[AI大模型(AI_MODEL)](module/ai/ai_model)|1:N关系||
|[DER1N_AI_KNOWLEDGE_BASE_AI_MODEL_EMBEDDING_MODEL_ID](der/DER1N_AI_KNOWLEDGE_BASE_AI_MODEL_EMBEDDING_MODEL_ID)|[AI大模型(AI_MODEL)](module/ai/ai_model)|1:N关系||
|[DER1N_AI_KNOWLEDGE_BASE_AI_MODEL_RERANK_MODEL_ID](der/DER1N_AI_KNOWLEDGE_BASE_AI_MODEL_RERANK_MODEL_ID)|[AI大模型(AI_MODEL)](module/ai/ai_model)|1:N关系||
|[DER1N_AI_KNOWLEDGE_BASE_CATEGORY_CATEGORY_ID](der/DER1N_AI_KNOWLEDGE_BASE_CATEGORY_CATEGORY_ID)|[类别(CATEGORY)](module/Base/category)|1:N关系||
|[DER1N_AI_KNOWLEDGE_BASE_DATA_RECORD_RECORD_ID](der/DER1N_AI_KNOWLEDGE_BASE_DATA_RECORD_RECORD_ID)|[数据记录(DATA_RECORD)](module/meta/data_record)|1:N关系||
|[DER1N_AI_KNOWLEDGE_BASE_DATA_RESOURCE_RESOURCE_ID](der/DER1N_AI_KNOWLEDGE_BASE_DATA_RESOURCE_RESOURCE_ID)|[数据资源(DATA_RESOURCE)](module/meta/data_resource)|1:N关系||

</el-tab-pane>
</el-tabs>
</el-row>

## 行为
| 中文名col200    | 代码名col150    | 类型col150    | 事务col100   | 批处理col100   | 附加操作col100  | 插件col150    |  备注col300  |
| -------- |---------- |----------- |:----:|:----:|---------| ----- | ----- |
|CheckKey|CheckKey|内置方法|默认|不支持||||
|Create|Create|内置方法|默认|不支持|[附加操作](index/action_logic_index#ai_knowledge_base_Create)|||
|CreateTemp|CreateTemp|内置方法|默认|不支持||||
|CreateTempMajor|CreateTempMajor|内置方法|默认|不支持||||
|Get|Get|内置方法|默认|不支持||||
|GetDraft|GetDraft|内置方法|默认|不支持||||
|GetDraftTemp|GetDraftTemp|内置方法|默认|不支持||||
|GetDraftTempMajor|GetDraftTempMajor|内置方法|默认|不支持||||
|GetTemp|GetTemp|内置方法|默认|不支持||||
|GetTempMajor|GetTempMajor|内置方法|默认|不支持||||
|Remove|Remove|内置方法|默认|支持||||
|RemoveTemp|RemoveTemp|内置方法|默认|支持||||
|RemoveTempMajor|RemoveTempMajor|内置方法|默认|支持||||
|Save|Save|内置方法|默认|不支持||||
|更新状态|update_status|用户扩展更新|默认|不支持|[附加操作](index/action_logic_index#ai_knowledge_base_UPDATE_STATUS)|||
|Update|Update|内置方法|默认|不支持||||
|UpdateTemp|UpdateTemp|内置方法|默认|不支持||||
|UpdateTempMajor|UpdateTempMajor|内置方法|默认|不支持||||
|知识库全盘推理|all_doc_reason|[实体处理逻辑](module/ai/ai_knowledge_base/logic/all_doc_reason "all_doc_reason")|默认|不支持||||
|变更管理员角色|change_admin_role|[实体处理逻辑](module/ai/ai_knowledge_base/logic/change_admin_role "变更管理员角色")|默认|不支持||||
|深度研究|deep_research|[实体处理逻辑](module/ai/ai_knowledge_base/logic/deep_research "深度研究")|默认|不支持||||
|删除|delete|[实体处理逻辑](module/ai/ai_knowledge_base/logic/delete "删除")|默认|不支持||||
|设置星标|favorite|[实体处理逻辑](module/ai/ai_knowledge_base/logic/favorite "设置星标")|默认|不支持||||
|填充分类配置|fill_category_config|[实体处理逻辑](module/ai/ai_knowledge_base/logic/fill_category_config "填充分类配置")|默认|不支持||||
|find_by_code|find_by_code|[实体处理逻辑](module/ai/ai_knowledge_base/logic/get_by_code "get_by_code")|默认|不支持||||
|查找知识库首页模版|find_template|[实体处理逻辑](module/ai/ai_knowledge_base/logic/find_template "查找知识库首页模版")|默认|不支持||||
|全文内容推理|fulltext_reason|[实体处理逻辑](module/ai/ai_knowledge_base/logic/fulltext_reason "全文内容推理")|默认|不支持|||查询知识库下文档，将多文档内容合并后以字数为分割进行逐一推理，最后再总结为整个知识库的报告|
|生成引导提示词|generate_guided_prompts|[实体处理逻辑](module/ai/ai_knowledge_base/logic/generate_guided_prompts "生成引导提示词")|默认|不支持||||
|GetFullData|get_full_data|通过键值获取|默认|不支持|[附加操作](index/action_logic_index#ai_knowledge_base_get_full_data)|||
|ls|get_ls|[实体处理逻辑](module/ai/ai_knowledge_base/logic/ls "ls")|默认|不支持||||
|获取参考资料|query_references|[实体处理逻辑](module/ai/ai_knowledge_base/logic/query_references "获取参考资料")|默认|不支持||||
|推理|reason|[实体处理逻辑](module/ai/ai_knowledge_base/logic/reason "推理")|默认|不支持||||
|恢复|recover|[实体处理逻辑](module/ai/ai_knowledge_base/logic/recover "恢复")|默认|不支持||||
|取消星标|un_favorite|[实体处理逻辑](module/ai/ai_knowledge_base/logic/un_favorite "取消星标")|默认|不支持||||

## 处理逻辑
| 中文名col200    | 代码名col150    | 子类型col150    | 插件col200    |  备注col550  |
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

## 数据查询
| 中文名col200    | 代码名col150    | 默认查询col100 | 权限使用col100 | 自定义SQLcol100 |  备注col600|
| --------  | --------   | :----:  |:----:  | :----:  |----- |
|[CurSelected](module/ai/ai_knowledge_base/query/CurSelected)|CurSelected|否|否 |否 ||
|[DEFAULT](module/ai/ai_knowledge_base/query/Default)|DEFAULT|是|否 |否 ||
|[默认（全部数据）(VIEW)](module/ai/ai_knowledge_base/query/View)|VIEW|否|否 |否 ||
|[管理员(admin)](module/ai/ai_knowledge_base/query/admin)|admin|否|否 |否 ||
|[目录下的知识库(category_ai_kb)](module/ai/ai_knowledge_base/query/category_ai_kb)|category_ai_kb|否|否 |否 ||
|[已删除(deleted)](module/ai/ai_knowledge_base/query/deleted)|deleted|否|否 |否 ||
|[查询星标(favorite)](module/ai/ai_knowledge_base/query/favorite)|favorite|否|否 |否 ||
|[组管理员(group_admin)](module/ai/ai_knowledge_base/query/group_admin)|group_admin|否|否 |否 ||
|[组管理员(group_user)](module/ai/ai_knowledge_base/query/group_user)|group_user|否|否 |否 ||
|[组织私有库(org)](module/ai/ai_knowledge_base/query/org)|org|否|否 |否 ||
|[公开(public)](module/ai/ai_knowledge_base/query/public)|public|否|否 |否 ||
|[只读用户(reader)](module/ai/ai_knowledge_base/query/reader)|reader|否|否 |否 ||
|[search](module/ai/ai_knowledge_base/query/search)|search|否|否 |是 ||
|[非星标知识库(unfavorite)](module/ai/ai_knowledge_base/query/unfavorite)|unfavorite|否|否 |否 ||
|[操作用户(user)](module/ai/ai_knowledge_base/query/user)|user|否|否 |否 ||
|[启用知识库(VALID)](module/ai/ai_knowledge_base/query/valid)|VALID|否|否 |否 ||

## 数据集合
| 中文名col200  | 代码名col150  | 类型col100 | 默认集合col100 |   插件col200|   备注col500|
| --------  | --------   | :----:   | :----:   | ----- |----- |
|[DEFAULT](module/ai/ai_knowledge_base/dataset/Default)|DEFAULT|数据查询|是|||
|[数据集(Switch)](module/ai/ai_knowledge_base/dataset/Switch)|Switch|[实体逻辑](module/ai/ai_knowledge_base/logic/switch_set)|否|||
|[管理员(admin)](module/ai/ai_knowledge_base/dataset/admin)|admin|数据查询|否|||
|[AI知识库目录查询(ai_docs_by_kb)](module/ai/ai_knowledge_base/dataset/ai_docs_by_kb)|ai_docs_by_kb|数据查询|否|[AI知识库目录查询](index/plugin_index#AIDocListByKBDataSetRuntime)||
|[AI知识库清单查询(ai_kb_query)](module/ai/ai_knowledge_base/dataset/ai_kb_query)|ai_kb_query|数据查询|否|[AI知识库清单查询](index/plugin_index#AIKBQueryListDataSetRuntime)||
|[目录下的知识库(category_ai_kb)](module/ai/ai_knowledge_base/dataset/category_ai_kb)|category_ai_kb|数据查询|否|||
|[已删除(deleted)](module/ai/ai_knowledge_base/dataset/deleted)|deleted|数据查询|否|||
|[查询星标(favorite)](module/ai/ai_knowledge_base/dataset/favorite)|favorite|数据查询|否|||
|[全文检索(full_text)](module/ai/ai_knowledge_base/dataset/full_text)|full_text|数据查询|否||根据keyword参数搜索，keyword可以是一组词以空格分割，命中多着靠前|
|[主表格查询(main)](module/ai/ai_knowledge_base/dataset/main)|main|数据查询|否|||
|[只读用户(reader)](module/ai/ai_knowledge_base/dataset/reader)|reader|数据查询|否|||
|[操作用户(user)](module/ai/ai_knowledge_base/dataset/user)|user|数据查询|否|||
|[启用数据集(VALID)](module/ai/ai_knowledge_base/dataset/valid)|VALID|数据查询|否|||
|[with_record](module/ai/ai_knowledge_base/dataset/with_record)|with_record|数据查询|否|[AI知识库查询(record)](index/plugin_index#AIKBWithRecordDataSetRuntime)||

## 数据权限

##### 成员中设置的管理员（读写） :id=ai_knowledge_base-ADMIN_RW

<p class="panel-title"><b>数据范围</b></p>

* `数据集合` ：[管理员(admin)](module/ai/ai_knowledge_base#数据集合)

<p class="panel-title"><b>数据能力</b></p>

* `DELETE`
* `READ`
* `UPDATE`
* `CREATE`
* `SUBDATA`



##### 全部数据（读） :id=ai_knowledge_base-ALL_R

<p class="panel-title"><b>数据范围</b></p>

* `全部数据`

<p class="panel-title"><b>数据能力</b></p>

* `READ`



##### 全部数据（读写） :id=ai_knowledge_base-ALL_RW

<p class="panel-title"><b>数据范围</b></p>

* `全部数据`

<p class="panel-title"><b>数据能力</b></p>

* `CREATE`
* `UPDATE`
* `DELETE`
* `READ`



##### 只读用户（读） :id=ai_knowledge_base-USER_R

<p class="panel-title"><b>数据范围</b></p>

* `数据集合` ：[只读用户(reader)](module/ai/ai_knowledge_base#数据集合)

<p class="panel-title"><b>数据能力</b></p>

* `READ`



##### 成员中设置的普通用户（读写） :id=ai_knowledge_base-USER_RW

<p class="panel-title"><b>数据范围</b></p>

* `数据集合` ：[操作用户(user)](module/ai/ai_knowledge_base#数据集合)

<p class="panel-title"><b>数据能力</b></p>

* `UPDATE`
* `READ`
* `CREATE`
* `SUBDATA`




## 搜索模式
|   搜索表达式col350   |    属性名col200    |    搜索模式col200        |备注col500  |
| -------- |------------|------------|------|
|N_CATEGORY_ID_EQ|目录标识|EQ||
|N_CATEGORY_NAME_EQ|目录|EQ||
|N_CATEGORY_NAME_LIKE|目录|LIKE||
|N_CHAT_MODEL_ID_EQ|交谈模型标识|EQ||
|N_EMBEDDING_MODEL_ID_EQ|嵌入模型标识|EQ||
|N_ID_NOTEQ|知识库标识|NOTEQ||
|N_ID_EQ|知识库标识|EQ||
|N_NAME_LIKE|知识库名称|LIKE||
|N_RECORD_ID_EQ|数据记录标识|EQ||
|N_RECORD_TITLE_EQ|标题|EQ||
|N_RECORD_TITLE_LIKE|标题|LIKE||
|N_RERANK_MODEL_ID_EQ|召回重排模型标识|EQ||
|N_RESOURCE_EQ|数据资源|EQ||
|N_RESOURCE_LIKE|数据资源|LIKE||
|N_RESOURCE_ID_EQ|资源标识|EQ||
|N_SCOPE_TYPE_EQ|所属|EQ||
|N_SOURCE_ID_EQ|知识库源标识|EQ||
|N_SOURCE_NAME_EQ|知识库源名称|EQ||
|N_SOURCE_NAME_LIKE|知识库源名称|LIKE||

## 界面行为
|  中文名col200 |  代码名col150 |  标题col100   |     处理目标col100   |    处理类型col200        |  备注col500       |
| --------| --------| -------- |------------|------------|------------|
| 新建目录 | create_category | 新建目录 |无数据|用户自定义||
| 取消星标 | cancel_favorite | 取消星标 |单项数据（主键）|<details><summary>后台调用</summary>[un_favorite](#行为)||
| 编辑基本信息 | edit_base_info | 编辑基本信息 |单项数据（主键）|用户自定义||
| 设置星标 | add_favorite | 设置星标 |单项数据（主键）|<details><summary>后台调用</summary>[favorite](#行为)||
| 提示词反馈 | prompt_feedback | 提示词反馈 |单项数据|用户自定义||
| 生成引导提示词 | generate_guided_prompts | 生成引导提示词 |单项数据（主键）|<details><summary>后台调用</summary>[generate_guided_prompts](#行为)||
| 删除知识库 | remove | 删除 |单项数据（主键）|<details><summary>后台调用</summary>[Remove](#行为)||
| 新建知识库 | create_kb | 新建知识库 |无数据|<details><summary>打开视图或向导（模态）</summary>[新建知识库](app/view/ai_knowledge_base_create_wizard_view)</details>||
| 打开知识库主页面 | open_kb_index | 打开知识库主页面 |单项数据（主键）|<details><summary>打开视图或向导（模态）</summary>[知识库](app/view/ai_knowledge_base_index_view)</details>||
| 查看知识库成员 | open_kb_member | 知识库成员 |单项数据（主键）|用户自定义||
| 打开知识库导航页 | open_ai_knowledge_base_tree_exp_view | 打开知识库导航页 |无数据|<details><summary>打开顶级视图</summary>[知识库](app/view/ai_knowledge_base_tree_exp_view)</details>||
| 打开知识库信息视图 | open_kb_doc_info_view | 知识库信息 |单项数据（主键）|<details><summary>打开视图或向导（模态）</summary>[知识库信息](app/view/ai_knowledge_base_base_info_view)</details>||
| 打开新建知识库 | open_new_kb | 打开新建知识库 |单项数据|<details><summary>打开视图或向导（模态）</summary>[知识库](app/view/ai_knowledge_base_index_view)</details>||
| 打开配置中心 | open_setting_center | 更多设置 |单项数据（主键）|用户自定义||

## 界面逻辑
|  中文名col200 | 代码名col150 | 备注col900 |
| --------|--------|--------|
|[刷新当前表格](module/ai/ai_knowledge_base/uilogic/refresh_current_grid)|refresh_current_grid|刷新当前表格|
|[提示词填充](module/ai/ai_knowledge_base/uilogic/prompt_feedback)|prompt_feedback||
|[新建目录](module/ai/ai_knowledge_base/uilogic/create_category)|create_category|新建空间目录|
|[查找知识库首页模版](module/ai/ai_knowledge_base/uilogic/find_template)|find_template||
|[计算表格列行为状态(ai_knowledge_base)](module/ai/ai_knowledge_base/uilogic/calc_column_action_state)|calc_column_action_state|用于动态控制收藏和取消收藏的禁用状态|

<div style="display: block; overflow: hidden; position: fixed; top: 140px; right: 100px;">

##### 导航
<el-anchor >
<el-anchor-link :href="`#/module/ai/ai_knowledge_base?id=属性`">
  属性
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_knowledge_base?id=关系`">
  关系
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_knowledge_base?id=行为`">
  行为
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_knowledge_base?id=处理逻辑`">
  处理逻辑
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_knowledge_base?id=数据查询`">
  数据查询
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_knowledge_base?id=数据集合`">
  数据集合
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_knowledge_base?id=数据权限`">
  数据权限
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_knowledge_base?id=搜索模式`">
  搜索模式
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_knowledge_base?id=界面行为`">
  界面行为
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_knowledge_base?id=界面逻辑`">
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
show_field_group:'field_group_ai_kb_query',

      }
    },
    methods: {
    }
  }).use(ElementPlus).mount('#app')
</script>