# 知识库文档(ai_kb_document)  <!-- {docsify-ignore-all} -->


## 属性
|    中文名col150 | 属性名称col200           | 类型col200     | 长度col100    |允许为空col100    |  备注col500  |
| --------   |------------| -----  | -----  | :----: | -------- |
|是否启用|ACTIVE|是否逻辑||否||
|目录|CATEGORIES|文本，可指定长度|1000|是||
|切片方法|CHUNK_METHOD|[单项选择(文本值)](index/dictionary_index#chunkingstrategy "切片策略")|100|是||
|切片数量|CHUNK_NUM|数值||是||
|内容|CONTENT|长文本，没有长度限制|1048576|是||
|建立人|CREATE_MAN|文本，可指定长度|100|否||
|建立时间|CREATE_TIME|日期时间型||否||
|自定义切片|CUSTOM_CHUNK|[单项选择(数值)](index/dictionary_index#custom_chunk "自定义切片")||是||
|摘要代码|DIGEST_CODE|文本，可指定长度|64|是||
|文档创建时间|DOC_CREATE_TIME|文本，可指定长度|200|是||
|上传文件|FILE|文件|500|是||
|文件类型|FILE_TYPE|文本，可指定长度|100|是||
|知识库文档标识<sup class="footnote-symbol"><font color=orange>[PK]</font></sup>|ID|全局唯一标识，文本类型，用户不可见|100|否||
|智能分析|INTELLIGENT_ANALYSIS|文本，可指定长度|100|是||
|知识库标识|KB_ID|外键值|100|是||
|知识库|KB_NAME|外键值文本|200|是||
|业务主键|KEY|文本，可指定长度|100|是||
|关键字|KEYWORDS|文本，可指定长度|100|是||
|关键问题|KEY_QUESTIONS|文本，可指定长度|100|是||
|关键问题列表|KEY_QUESTION_LIST|一对多关系数据集合|1048576|是||
|文档元数据|META_DATA|长文本，没有长度限制|1048576|是||
|文档名称|NAME|文本，可指定长度|200|是||
|目录信息|PAGE_INDEX_INFO|文本，可指定长度|100|是||
|解析内容|PARSED_CONTENT|长文本，没有长度限制|1048576|是||
|解析配置|PARSER_CONFIG|一对一关系数据对象|1048576|是||
|解析信息|PARSE_ERROR|长文本，没有长度限制|1048576|是||
|路径|PATH|文本，可指定长度|200|是||
|最近创建日期|RECENT_CREATE_DAYS|整型||是||
|参考引用|REFERENCES|一对多动态对象|1048576|是||
|资源|RESOURCE|文本，可指定长度|200|是||
|resource_count|RESOURCE_COUNT|整型||是||
|resource_id|RESOURCE_ID|文本，可指定长度|100|是||
|序号<sup class="footnote-symbol">[[序列]](index/sequence_index#seq_doc_id)</sup>|SEQUENCE|数值||是||
|内容大小|SIZE|数值||是||
|源标识|SOURCE_ID|文本，可指定长度|200|是||
|源类型|SOURCE_TYPE|文本，可指定长度|60|是||
|状态|STATUS|[单项选择(文本值)](index/dictionary_index#slice_status "文档切片状态")|60|是||
|摘要|SUMMARY|文本，可指定长度|100|是||
|同步频率|SYNC_FREQUENCY|[单项选择(文本值)](index/dictionary_index#KBSyncFrequency "知识库同步频率")|60|是||
|文档同步标识|SYNC_ID|外键值|100|是||
|标签集|TAG_SETS|外键值附加数据|2000|是||
|文档类型|TYPE|单项选择(文本值)|60|是||
|更新人|UPDATE_MAN|文本，可指定长度|100|否||
|更新时间|UPDATE_TIME|日期时间型||否||
|用户标记|USER_TAG|文本，可指定长度|200|是||
|用户标记2|USER_TAG2|文本，可指定长度|200|是||


###### 属性组

<el-row>
<el-tabs v-model="show_field_group">

<el-tab-pane label="AI文档内容属性组" name="field_group_ai_doc_content">

|    中文名col150 | 属性名称col200           | 类型col200     | 长度col100    |允许为空col100    |  备注col500  |
| --------   |------------| -----  | -----  | :----: | -------- |
|智能分析|INTELLIGENT_ANALYSIS|文本，可指定长度|100|是||
|知识库文档标识<sup class="footnote-symbol"><font color=orange>[PK]</font></sup>|ID|全局唯一标识，文本类型，用户不可见|100|否||
|文档名称|NAME|文本，可指定长度|200|是||
|解析内容|PARSED_CONTENT|长文本，没有长度限制|1048576|是||
|关键字|KEYWORDS|文本，可指定长度|100|是||
|内容|CONTENT|长文本，没有长度限制|1048576|是||

</el-tab-pane>
<el-tab-pane label="AI文档清单属性组" name="field_group_ai_doc_list">

|    中文名col150 | 属性名称col200           | 类型col200     | 长度col100    |允许为空col100    |  备注col500  |
| --------   |------------| -----  | -----  | :----: | -------- |
|知识库文档标识<sup class="footnote-symbol"><font color=orange>[PK]</font></sup>|ID|全局唯一标识，文本类型，用户不可见|100|否||
|文档名称|NAME|文本，可指定长度|200|是||
|状态|STATUS|[单项选择(文本值)](index/dictionary_index#slice_status "文档切片状态")|60|是||
|智能分析|INTELLIGENT_ANALYSIS|文本，可指定长度|100|是||
|目录|CATEGORIES|文本，可指定长度|1000|是||
|资源|RESOURCE|文本，可指定长度|200|是||

</el-tab-pane>
<el-tab-pane label="ls" name="field_group_ls">

|    中文名col150 | 属性名称col200           | 类型col200     | 长度col100    |允许为空col100    |  备注col500  |
| --------   |------------| -----  | -----  | :----: | -------- |
|知识库文档标识<sup class="footnote-symbol"><font color=orange>[PK]</font></sup>|ID|全局唯一标识，文本类型，用户不可见|100|否||
|内容大小|SIZE|数值||是||
|路径|PATH|文本，可指定长度|200|是||

</el-tab-pane>
<el-tab-pane label="基础数据" name="field_group_simple">

|    中文名col150 | 属性名称col200           | 类型col200     | 长度col100    |允许为空col100    |  备注col500  |
| --------   |------------| -----  | -----  | :----: | -------- |
|文档名称|NAME|文本，可指定长度|200|是||
|更新时间|UPDATE_TIME|日期时间型||否||
|文档同步标识|SYNC_ID|外键值|100|是||
|切片方法|CHUNK_METHOD|[单项选择(文本值)](index/dictionary_index#chunkingstrategy "切片策略")|100|是||
|文档类型|TYPE|单项选择(文本值)|60|是||
|状态|STATUS|[单项选择(文本值)](index/dictionary_index#slice_status "文档切片状态")|60|是||
|自定义切片|CUSTOM_CHUNK|[单项选择(数值)](index/dictionary_index#custom_chunk "自定义切片")||是||
|路径|PATH|文本，可指定长度|200|是||
|序号<sup class="footnote-symbol">[[序列]](index/sequence_index#seq_doc_id)</sup>|SEQUENCE|数值||是||

</el-tab-pane>

</el-tabs>
</el-row>

## 关系

<el-row>
<el-tabs v-model="show_der">
<el-tab-pane label="主关系" name="major">

| 名称col350     |   从实体col200 | 关系类型col200     |   备注col500  |
| -------- |---------- |------------|----- |
|[DER1N_AI_KB_CHUNK_AI_KB_DOCUMENT_DOCUMENT_ID](der/DER1N_AI_KB_CHUNK_AI_KB_DOCUMENT_DOCUMENT_ID)|[知识库文档分块(AI_KB_CHUNK)](module/ai/ai_kb_chunk)|1:N关系||
|[DER1N_AI_KB_GRAPH_ENTITY_AI_KB_DOCUMENT_DOCUMENT_ID](der/DER1N_AI_KB_GRAPH_ENTITY_AI_KB_DOCUMENT_DOCUMENT_ID)|[知识库图谱实体(AI_KB_GRAPH_ENTITY)](module/ai/ai_kb_graph_entity)|1:N关系||
|[DER1N_AI_REVIEW_REPORT_AI_KB_DOCUMENT_DOCUMENT_ID](der/DER1N_AI_REVIEW_REPORT_AI_KB_DOCUMENT_DOCUMENT_ID)|[智能审查报告(AI_REVIEW_REPORT)](module/ai/ai_review_report)|1:N关系||
|[DERCUSTOM_AI_KB_CHUNKING_STRATEGY_AI_KB_DOCUMENT](der/DERCUSTOM_AI_KB_CHUNKING_STRATEGY_AI_KB_DOCUMENT)|[知识库文档切片策略(AI_KB_CHUNKING_STRATEGY)](module/ai/ai_kb_chunking_strategy)|自定义关系||
|[DERCUSTOM_AI_KB_LIST_AI_KB_DOCUMENT](der/DERCUSTOM_AI_KB_LIST_AI_KB_DOCUMENT)|[ai_kb_list(AI_KB_LIST)](module/ai/ai_kb_list)|自定义关系||
|[DERCUSTOM_COMMENT_AI_KB_DOCUMENT](der/DERCUSTOM_COMMENT_AI_KB_DOCUMENT)|[评论(COMMENT)](module/Base/comment)|自定义关系||


</el-tab-pane>
<el-tab-pane label="从关系" name="minor">

|  名称col350   | 主实体col200   | 关系类型col200   |    备注col500  |
| -------- |---------- |-----------|----- |
|[DER1N_AI_KB_DOCUMENT_AI_KB_DOCUMENT_SYNC_SYNC_ID](der/DER1N_AI_KB_DOCUMENT_AI_KB_DOCUMENT_SYNC_SYNC_ID)|[知识库文档同步(AI_KB_DOCUMENT_SYNC)](module/ai/ai_kb_document_sync)|1:N关系||
|[DER1N_AI_KB_DOCUMENT_AI_KNOWLEDGE_BASE_KB_ID](der/DER1N_AI_KB_DOCUMENT_AI_KNOWLEDGE_BASE_KB_ID)|[知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base)|1:N关系||
|[DERCUSTOM_AI_KB_DOCUMENT_PAGE](der/DERCUSTOM_AI_KB_DOCUMENT_PAGE)|[页面(PAGE)](module/Wiki/article_page)|自定义关系||

</el-tab-pane>
</el-tabs>
</el-row>

## 行为
| 中文名col200    | 代码名col150    | 类型col150    | 事务col100   | 批处理col100   | 附加操作col100  | 插件col150    |  备注col300  |
| -------- |---------- |----------- |:----:|:----:|---------| ----- | ----- |
|异步重新索引|Async_reindex|用户自定义|默认|不支持||||
|异步重新切片|Async_build_chunk|用户自定义|默认|不支持||||
|异步文档解析|Async_reparse|用户自定义|默认|不支持||||
|切片|chunk|用户自定义|默认|不支持||||
|CheckKey|CheckKey|内置方法|默认|不支持||||
|Create|Create|内置方法|默认|不支持|[附加操作](index/action_logic_index#ai_kb_document_Create)|||
|获取完整文本|get_full_text|用户自定义|默认|不支持||||
|获取页面目录|get_page_index|用户自定义|默认|不支持||||
|Get|Get|内置方法|默认|不支持|[附加操作](index/action_logic_index#ai_kb_document_Get)|||
|GetDraft|GetDraft|内置方法|默认|不支持||||
|重新切片|rechunk|用户自定义|默认|不支持||||
|重新索引|reindex|用户自定义|默认|不支持||||
|Remove|Remove|内置方法|默认|支持|[附加操作](index/action_logic_index#ai_kb_document_Remove)|||
|Save|Save|内置方法|默认|不支持||||
|更新状态|update_status|用户扩展更新|默认|不支持||||
|Update|Update|内置方法|默认|不支持||||
|ai_kb_document_type_counters|ai_kb_document_type_counters|[实体处理逻辑](module/ai/ai_kb_document/logic/ai_kb_document_type_counters "ai_kb_document_type_counters")|默认|不支持||||
|批量解析|batch_parse|[实体处理逻辑](module/ai/ai_kb_document/logic/parse "文档解析处理")|默认|不支持||||
|立即切片|build_chunk|[实体处理逻辑](module/ai/ai_kb_document/logic/build_chunk "构建切片")|无事务|不支持||||
|立即索引|build_index|[实体处理逻辑](module/ai/ai_kb_document/logic/build_index "构建索引")|无事务（存在则挂起）|不支持||||
|统计评论数|comment_counters|[实体处理逻辑](module/ai/ai_kb_document/logic/comment_counters "统计评论数")|默认|不支持||||
|提取元数据|extract_meta_data|用户自定义|默认|不支持||[ExtractMetaDataDEActionRuntime](index/plugin_index#ExtractMetaDataDEActionRuntime)||
|GetFullData|get_full_data|通过键值获取|默认|不支持|[附加操作](index/action_logic_index#ai_kb_document_get_full_data)|||
|文档解析处理|parse|[实体处理逻辑](module/ai/ai_kb_document/logic/parse "文档解析处理")|默认|不支持||||
|推理|reason|[实体处理逻辑](module/ai/ai_kb_document/logic/reason "全文推理")|默认|不支持|||针对document的原始内容的审查|
|文档重新解析|reparse|[实体处理逻辑](module/ai/ai_kb_document/logic/reparse "文档重新解析")|默认|不支持||||

## 处理逻辑
| 中文名col200    | 代码名col150    | 子类型col150    | 插件col200    |  备注col550  |
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

## 数据查询
| 中文名col200    | 代码名col150    | 默认查询col100 | 权限使用col100 | 自定义SQLcol100 |  备注col600|
| --------  | --------   | :----:  |:----:  | :----:  |----- |
|[DEFAULT](module/ai/ai_kb_document/query/Default)|DEFAULT|是|否 |否 ||
|[默认（全部数据）(VIEW)](module/ai/ai_kb_document/query/View)|VIEW|否|否 |否 ||
|[AI文档内容(ai_doc_content)](module/ai/ai_kb_document/query/ai_doc_content)|ai_doc_content|否|否 |否 ||
|[AI文档清单(ai_doc_list)](module/ai/ai_kb_document/query/ai_doc_list)|ai_doc_list|否|否 |否 ||
|[当前知识库(cur_kb)](module/ai/ai_kb_document/query/cur_kb)|cur_kb|否|否 |否 ||
|[exp_list](module/ai/ai_kb_document/query/exp_list)|exp_list|否|否 |是 ||
|[数据查询(ls)](module/ai/ai_kb_document/query/ls)|ls|否|否 |否 ||
|[过滤器查询(my_filter)](module/ai/ai_kb_document/query/my_filter)|my_filter|否|否 |否 ||
|[reader](module/ai/ai_kb_document/query/reader)|reader|否|否 |否 ||
|[最近文档(recent)](module/ai/ai_kb_document/query/recent)|recent|否|否 |否 ||
|[资源分类(resource_classification)](module/ai/ai_kb_document/query/resource_classification)|resource_classification|否|否 |否 ||
|[选中的数据(selected_data)](module/ai/ai_kb_document/query/selected_data)|selected_data|否|否 |否 ||
|[简单查询(simple)](module/ai/ai_kb_document/query/simple)|simple|否|否 |否 ||
|[未解析文档(UNPARSED)](module/ai/ai_kb_document/query/unparsed)|UNPARSED|否|否 |否 ||

## 数据集合
| 中文名col200  | 代码名col150  | 类型col100 | 默认集合col100 |   插件col200|   备注col500|
| --------  | --------   | :----:   | :----:   | ----- |----- |
|[DEFAULT](module/ai/ai_kb_document/dataset/Default)|DEFAULT|数据查询|是|||
|[AI知识库文档查询(ai_doc_query)](module/ai/ai_kb_document/dataset/ai_doc_query)|ai_doc_query|数据查询|否|[AI知识库文档查询](index/plugin_index#AIDocQueryListDataSetRuntime)||
|[导航列表数据(exp_list)](module/ai/ai_kb_document/dataset/exp_list)|exp_list|数据查询|否|||
|[过滤器查询(my_filter)](module/ai/ai_kb_document/dataset/my_filter)|my_filter|数据查询|否|||
|[reader](module/ai/ai_kb_document/dataset/reader)|reader|数据查询|否|||
|[最近文档(recent)](module/ai/ai_kb_document/dataset/recent)|recent|数据查询|否|||
|[资源分类(resource_classification)](module/ai/ai_kb_document/dataset/resource_classification)|resource_classification|数据查询|否|||
|[简单查询(simple)](module/ai/ai_kb_document/dataset/simple)|simple|数据查询|否|||
|[未解析文档(UNPARSED)](module/ai/ai_kb_document/dataset/unparsed)|UNPARSED|数据查询|否|||

## 数据权限

##### 全部数据（读） :id=ai_kb_document-ALL_R

<p class="panel-title"><b>数据范围</b></p>

* `全部数据`

<p class="panel-title"><b>数据能力</b></p>

* `READ`



##### 全部数据（读写） :id=ai_kb_document-ALL_RW

<p class="panel-title"><b>数据范围</b></p>

* `全部数据`

<p class="panel-title"><b>数据能力</b></p>

* `UPDATE`
* `DELETE`
* `READ`
* `CREATE`



##### 操作用户(读) :id=ai_kb_document-USER_R

<p class="panel-title"><b>数据范围</b></p>

* `数据集合` ：[reader](module/ai/ai_kb_document#数据集合)

<p class="panel-title"><b>数据能力</b></p>

* `READ(知识库(READ))`



##### 操作用户(读写) :id=ai_kb_document-USER_W

<p class="panel-title"><b>数据范围</b></p>

* `数据集合` ：[reader](module/ai/ai_kb_document#数据集合)

<p class="panel-title"><b>数据能力</b></p>

* `READ(知识库(READ))`
* `UPDATE(知识库(SUBDATA))`
* `DELETE(知识库(SUBDATA))`
* `CREATE(知识库(SUBDATA))`




## 搜索模式
|   搜索表达式col350   |    属性名col200    |    搜索模式col200        |备注col500  |
| -------- |------------|------------|------|
|N_FILE_TYPE_EQ|文件类型|EQ||
|N_ID_EQ|知识库文档标识|EQ||
|N_KB_ID_EQ|知识库标识|EQ||
|N_KB_NAME_EQ|知识库|EQ||
|N_KB_NAME_LIKE|知识库|LIKE||
|N_NAME_LIKE|文档名称|LIKE||
|N_RECENT_CREATE_DAYS_LTANDEQ|最近创建日期|LTANDEQ||
|N_RESOURCE_EQ|资源|EQ||
|N_SOURCE_ID_EQ|源标识|EQ||
|N_STATUS_EQ|状态|EQ||
|N_SYNC_FREQUENCY_EQ|同步频率|EQ||
|N_SYNC_ID_EQ|文档同步标识|EQ||
|N_TYPE_EQ|文档类型|EQ||

## 界面行为
|  中文名col200 |  代码名col150 |  标题col100   |     处理目标col100   |    处理类型col200        |  备注col500       |
| --------| --------| -------- |------------|------------|------------|
| 打开知识库文档编辑视图 | open_edit_view | 编辑 |单项数据（主键）|<details><summary>打开视图或向导（模态）</summary>[知识库文档](app/view/ai_kb_document_edit_view)</details>||
| 重新索引 | reindex | 重新索引 |单项数据|<details><summary>后台调用</summary>[build_index](#行为)||
| 打印交谈资料_文档 | chat_resource_print | 打印 |单项数据|<details><summary>打开打印视图</summary>[chat_resource]()</details>||
| 关闭评论，打开基础信息 | toolbar_main_show_view_toolbar_deuiaction1_click | 关闭评论，打开基础信息 |单项数据|用户自定义||
| 打开切片树表格 | open_chunk_tree | 打开切片树表格 |无数据|<details><summary>打开视图或向导（模态）</summary>[知识库文档分块](app/view/ai_kb_chunk_tree_grid_view)</details>||
| 打开知识库文档信息视图 | open_base_info_view | 文档信息 |单项数据（主键）|<details><summary>打开视图或向导（模态）</summary>[文档信息](app/view/ai_kb_document_base_info_view)</details>||
| 文档解析 | parsing | 文档解析 |单项数据（主键）|<details><summary>后台调用</summary>[parse](#行为)||
| 打开知识库文档切片视图 | open_chunk_view | 文档切片 |单项数据（主键）|<details><summary>打开视图或向导（模态）</summary>[文档切片设置](app/view/ai_kb_document_chunk_view)</details>||
| 打开评论 | toolbar_main_show_view_toolbar_deuiaction2_click | 打开评论 |单项数据|用户自定义||
| 打开知识库文档同步表格视图 | open_doc_sync_grid_view | 同步设置 |无数据|<details><summary>打开视图或向导（模态）</summary>[同步设置](app/view/ai_kb_document_sync_grid_view)</details>||
| 打开文档概览导航 | open_main_info_view | 打开文档概览导航 |单项数据|<details><summary>打开视图或向导（模态）</summary>[文档概览导航](app/view/ai_kb_document_main_list_exp_view)</details>||
| 文档重新解析 | reparse | 文档解析 |多项数据（主键）|<details><summary>后台调用</summary>[Async_reparse](#行为)||
| 设置元数据 | set_meta_data | 设置元数据 |单项数据|<details><summary>打开视图或向导（模态）</summary>[文档元数据](app/view/ai_kb_document_meta_data_view)</details>||
| 重新切片 | rechunk | 重新切片 |单项数据|<details><summary>后台调用</summary>[build_chunk](#行为)||
| 批量解析 | batch_parse | 批量解析 |多项数据（主键）|<details><summary>后台调用</summary>[batch_parse](#行为)||
| 关闭 | toolbar_main_show_view_toolbar_deuiaction4_click | 关闭 |单项数据|用户自定义||

## 界面逻辑
|  中文名col200 | 代码名col150 | 备注col900 |
| --------|--------|--------|
|[显示基本信息](module/ai/ai_kb_document/uilogic/show_info)|show_info||
|[显示评论信息](module/ai/ai_kb_document/uilogic/show_comment)|show_comment||

<div style="display: block; overflow: hidden; position: fixed; top: 140px; right: 100px;">

##### 导航
<el-anchor >
<el-anchor-link :href="`#/module/ai/ai_kb_document?id=属性`">
  属性
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_kb_document?id=关系`">
  关系
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_kb_document?id=行为`">
  行为
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_kb_document?id=处理逻辑`">
  处理逻辑
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_kb_document?id=数据查询`">
  数据查询
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_kb_document?id=数据集合`">
  数据集合
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_kb_document?id=数据权限`">
  数据权限
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_kb_document?id=搜索模式`">
  搜索模式
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_kb_document?id=界面行为`">
  界面行为
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_kb_document?id=界面逻辑`">
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
show_field_group:'field_group_ai_doc_content',

      }
    },
    methods: {
    }
  }).use(ElementPlus).mount('#app')
</script>