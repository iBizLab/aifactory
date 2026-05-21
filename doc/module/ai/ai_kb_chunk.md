# 知识库文档分块(ai_kb_chunk)  <!-- {docsify-ignore-all} -->


## 属性
|    中文名col150 | 属性名称col200           | 类型col200     | 长度col100    |允许为空col100    |  备注col500  |
| --------   |------------| -----  | -----  | :----: | -------- |
|是否启用|ACTIVE|是否逻辑||否||
|目录|CATEGORIES|外键值附加数据|1000|是||
|分块类型|CHUNK_TYPE|[单项选择(文本值)](index/dictionary_index#chunk_type "文档分块类型")|60|是||
|块内容|CONTENT|长文本，没有长度限制|1048576|是||
|内容全文检索向量|CONTENT_FTS_VECTOR|文本搜索向量||是||
|块内容（预览）|CONTENT_PREVIEW|文本，可指定长度|100|是||
|块内容向量|CONTENT_VECTOR|向量|1024|是||
|建立人|CREATE_MAN|文本，可指定长度|100|否||
|建立时间|CREATE_TIME|日期时间型||否||
|知识库文档标识|DOCUMENT_ID|外键值|100|是||
|知识库文档名称|DOCUMENT_NAME|外键值文本|200|是||
|文档类型|DOCUMENT_SEQUENCE|外键值附加数据||是||
|文档类型|DOCUMENT_TYPE|外键值附加数据|60|是||
|file|DOC_FILE|外键值附加数据|500|是||
|doc_name|DOC_NAME|外键值附加数据|200|是||
|doc_parsed_content|DOC_PARSED_CONTENT|外键值附加数据|1048576|是||
|分块标识<sup class="footnote-symbol"><font color=orange>[PK]</font></sup>|ID|全局唯一标识，文本类型，用户不可见|100|否||
|知识库标识|KB_ID|外键值附加数据|100|是||
|知识库|KB_NAME|外键值附加数据|200|是||
|关键词|KEYWORDS|长文本，长度1000|4000|是||
|关键问题|KEY_QUESTIONS|长文本，长度1000|4000|是||
|关键问题向量|KEY_QUESTIONS_VECTOR|向量|1024|是||
|元数据|META_DATA|长文本，长度1000|4000|是||
|分块名称|NAME|文本，可指定长度|200|是||
|目录信息|PAGE_INDEX_INFO|文本，可指定长度|100|是||
|分块路径|PATH|长文本，长度1000|2000|是||
|父分块标识|PID|外键值|100|是||
|文档位置|POSITIONS|文本，可指定长度|100|是||
|文档索引顺序|SEQUENCE|整型||是||
|源分块计数|SOURCE_COUNT|整型||是||
|源分块索引|SOURCE_INDICES|文本数组（没有长度限制）|1000|是||
|标签|TAGS|多项选择(文本值)|2000|是||
|分块类型|TYPE|[单项选择(文本值)](index/dictionary_index#chunk_type "文档分块类型")|60|是||
|更新人|UPDATE_MAN|文本，可指定长度|100|否||
|更新时间|UPDATE_TIME|日期时间型||否||
|用户标记|USER_TAG|文本，可指定长度|200|是||
|用户标记2|USER_TAG2|文本，可指定长度|200|是||


## 关系

<el-row>
<el-tabs v-model="show_der">
<el-tab-pane label="主关系" name="major">

| 名称col350     |   从实体col200 | 关系类型col200     |   备注col500  |
| -------- |---------- |------------|----- |
|[DER1N_AI_KB_CHUNK_AI_KB_CHUNK_PID](der/DER1N_AI_KB_CHUNK_AI_KB_CHUNK_PID)|[知识库文档分块(AI_KB_CHUNK)](module/ai/ai_kb_chunk)|1:N关系||
|[DER1N_AI_KB_GRAPH_ENTITY_CHUNK_AI_KB_CHUNK_CHUNK_ID](der/DER1N_AI_KB_GRAPH_ENTITY_CHUNK_AI_KB_CHUNK_CHUNK_ID)|[知识库图谱实体文档分块(AI_KB_GRAPH_ENTITY_CHUNK)](module/ai/ai_kb_graph_entity_chunk)|1:N关系||
|[DER1N_AI_KB_GRAPH_RELATION_CHUNK_AI_KB_CHUNK_CHUNK_ID](der/DER1N_AI_KB_GRAPH_RELATION_CHUNK_AI_KB_CHUNK_CHUNK_ID)|[知识库图谱关系文档分块(AI_KB_GRAPH_RELATION_CHUNK)](module/ai/ai_kb_graph_relation_chunk)|1:N关系||


</el-tab-pane>
<el-tab-pane label="从关系" name="minor">

|  名称col350   | 主实体col200   | 关系类型col200   |    备注col500  |
| -------- |---------- |-----------|----- |
|[DER1N_AI_KB_CHUNK_AI_KB_CHUNK_PID](der/DER1N_AI_KB_CHUNK_AI_KB_CHUNK_PID)|[知识库文档分块(AI_KB_CHUNK)](module/ai/ai_kb_chunk)|1:N关系||
|[DER1N_AI_KB_CHUNK_AI_KB_DOCUMENT_DOCUMENT_ID](der/DER1N_AI_KB_CHUNK_AI_KB_DOCUMENT_DOCUMENT_ID)|[知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document)|1:N关系||

</el-tab-pane>
</el-tabs>
</el-row>

## 行为
| 中文名col200    | 代码名col150    | 类型col150    | 事务col100   | 批处理col100   | 附加操作col100  | 插件col150    |  备注col300  |
| -------- |---------- |----------- |:----:|:----:|---------| ----- | ----- |
|CheckKey|CheckKey|内置方法|默认|不支持||||
|Create|Create|内置方法|默认|不支持||||
|Get|Get|内置方法|默认|不支持||||
|GetDraft|GetDraft|内置方法|默认|不支持||||
|Remove|Remove|内置方法|默认|支持||||
|Save|Save|内置方法|默认|不支持||||
|Update|Update|内置方法|默认|不支持||||
|GetFullData|get_full_data|通过键值获取|默认|不支持|[附加操作](index/action_logic_index#ai_kb_chunk_get_full_data)|||

## 处理逻辑
| 中文名col200    | 代码名col150    | 子类型col150    | 插件col200    |  备注col550  |
| -------- |---------- |----------- |------------|----------|
|[检索测试](module/ai/ai_kb_chunk/logic/retrieval_test)|retrieval_test|无|||
|[获取pageIndex信息](module/ai/ai_kb_chunk/logic/get_page_index_info)|get_page_index_info|无|||

## 数据查询
| 中文名col200    | 代码名col150    | 默认查询col100 | 权限使用col100 | 自定义SQLcol100 |  备注col600|
| --------  | --------   | :----:  |:----:  | :----:  |----- |
|[DEFAULT](module/ai/ai_kb_chunk/query/Default)|DEFAULT|是|否 |否 ||
|[默认（全部数据）(VIEW)](module/ai/ai_kb_chunk/query/View)|VIEW|否|否 |否 ||
|[reader](module/ai/ai_kb_chunk/query/reader)|reader|否|否 |否 ||
|[指定知识库(specified_kb)](module/ai/ai_kb_chunk/query/specified_kb)|specified_kb|否|否 |否 ||
|[tree](module/ai/ai_kb_chunk/query/tree)|tree|否|否 |否 ||
|[启用(VALID)](module/ai/ai_kb_chunk/query/valid)|VALID|否|否 |否 ||

## 数据集合
| 中文名col200  | 代码名col150  | 类型col100 | 默认集合col100 |   插件col200|   备注col500|
| --------  | --------   | :----:   | :----:   | ----- |----- |
|[DEFAULT](module/ai/ai_kb_chunk/dataset/Default)|DEFAULT|数据查询|是|||
|[reader](module/ai/ai_kb_chunk/dataset/reader)|reader|数据查询|否|||
|[检索测试(retrieval_test)](module/ai/ai_kb_chunk/dataset/retrieval_test)|retrieval_test|[实体逻辑](module/ai/ai_kb_chunk/logic/retrieval_test)|否|||
|[树表数据集合(tree)](module/ai/ai_kb_chunk/dataset/tree)|tree|数据查询|否|[TreeGridDEDataSetRuntime](index/plugin_index#UsrSFPlugin0407757309)||
|[启用(VALID)](module/ai/ai_kb_chunk/dataset/valid)|VALID|数据查询|否|||

## 数据权限

##### 全部数据（读） :id=ai_kb_chunk-ALL_R

<p class="panel-title"><b>数据范围</b></p>

* `全部数据`

<p class="panel-title"><b>数据能力</b></p>

* `READ`



##### 全部数据（读写） :id=ai_kb_chunk-ALL_RW

<p class="panel-title"><b>数据范围</b></p>

* `全部数据`

<p class="panel-title"><b>数据能力</b></p>

* `DELETE`
* `CREATE`
* `READ`
* `UPDATE`



##### 操作用户(读写) :id=ai_kb_chunk-USER_RW

<p class="panel-title"><b>数据范围</b></p>

* `数据集合` ：[reader](module/ai/ai_kb_chunk#数据集合)

<p class="panel-title"><b>数据能力</b></p>

* `DELETE`
* `READ`
* `UPDATE`
* `CREATE`




## 搜索模式
|   搜索表达式col350   |    属性名col200    |    搜索模式col200        |备注col500  |
| -------- |------------|------------|------|
|N_DOCUMENT_ID_EQ|知识库文档标识|EQ||
|N_DOCUMENT_ID_IN|知识库文档标识|IN||
|N_DOCUMENT_NAME_EQ|知识库文档名称|EQ||
|N_DOCUMENT_NAME_LIKE|知识库文档名称|LIKE||
|N_ID_IN|分块标识|IN||
|N_ID_EQ|分块标识|EQ||
|N_KB_ID_EQ|知识库标识|EQ||
|N_KB_ID_IN|知识库标识|IN||
|N_KB_NAME_LIKE|知识库|LIKE||
|N_KEYWORDS_ISNOTNULL|关键词|ISNOTNULL||
|N_KEY_QUESTIONS_ISNOTNULL|关键问题|ISNOTNULL||
|N_NAME_LIKE|分块名称|LIKE||
|N_PID_EQ|父分块标识|EQ||
|N_PID_ISNOTNULL|父分块标识|ISNOTNULL||
|N_PID_ISNULL|父分块标识|ISNULL||
|N_TYPE_EQ|分块类型|EQ||
|N_TYPE_IN|分块类型|IN||

## 界面行为
|  中文名col200 |  代码名col150 |  标题col100   |     处理目标col100   |    处理类型col200        |  备注col500       |
| --------| --------| -------- |------------|------------|------------|
| null | panel_ad500b587a806bf9660_button_calluilogic_click | 切片 |单项数据|<details><summary>打开视图或向导（模态）</summary>[切片](app/view/ai_kb_chunk_chunk_info_view)</details>||
| null | panel_ada9c64b91f377e6a09_button_calluilogic_click | 切片 |单项数据|<details><summary>打开视图或向导（模态）</summary>[切片](app/view/ai_kb_chunk_chunk_info_view)</details>||
| 检索测试 | retrieval_test | 检索测试 |无数据|用户自定义||
| 切换显示模式 | switch_show_mode | 切换模式 |无数据|用户自定义||

## 界面逻辑
|  中文名col200 | 代码名col150 | 备注col900 |
| --------|--------|--------|
|[切换显示模式](module/ai/ai_kb_chunk/uilogic/switch_show_mode)|switch_show_mode|切换表格的显示模式|
|[打开所属文档](module/ai/ai_kb_chunk/uilogic/open_doc)|open_doc||

<div style="display: block; overflow: hidden; position: fixed; top: 140px; right: 100px;">

##### 导航
<el-anchor >
<el-anchor-link :href="`#/module/ai/ai_kb_chunk?id=属性`">
  属性
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_kb_chunk?id=关系`">
  关系
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_kb_chunk?id=行为`">
  行为
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_kb_chunk?id=处理逻辑`">
  处理逻辑
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_kb_chunk?id=数据查询`">
  数据查询
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_kb_chunk?id=数据集合`">
  数据集合
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_kb_chunk?id=数据权限`">
  数据权限
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_kb_chunk?id=搜索模式`">
  搜索模式
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_kb_chunk?id=界面行为`">
  界面行为
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_kb_chunk?id=界面逻辑`">
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