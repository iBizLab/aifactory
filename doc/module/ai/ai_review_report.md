# 智能审查报告(ai_review_report)  <!-- {docsify-ignore-all} -->


## 属性
|    中文名col150 | 属性名称col200           | 类型col200     | 长度col100    |允许为空col100    |  备注col500  |
| --------   |------------| -----  | -----  | :----: | -------- |
|智能体标记|AGENT_TAG|单项选择(文本值)|200|是||
|校验信息|CHECK_INFO|长文本，没有长度限制|1048576|是||
|创建人|CREATE_MAN|文本，可指定长度|100|否||
|创建时间|CREATE_TIME|日期时间型||否||
|知识库文档标识|DOCUMENT_ID|外键值|100|是||
|知识库文档|DOCUMENT_NAME|外键值文本|200|是||
|标识<sup class="footnote-symbol"><font color=orange>[PK]</font></sup>|ID|全局唯一标识，文本类型，用户不可见|100|否||
|知识库标识|KB_ID|外键值|100|是||
|知识库|KB_NAME|外键值文本|200|是||
|审查对象|NAME|文本，可指定长度|200|是||
|记录标识|RECORD_ID|外键值|60|是||
|报告|REVIEW_REPORT|长文本，没有长度限制|1048576|是||
|review_report_html|REVIEW_REPORT_HTML|长文本，没有长度限制|1048576|是||
|审查结果|REVIEW_RESULT|长文本，长度1000|2000|是||
|更新人|UPDATE_MAN|文本，可指定长度|100|否||
|更新时间|UPDATE_TIME|日期时间型||否||


## 关系

<el-row>
<el-tabs v-model="show_der">
<el-tab-pane label="从关系" name="minor">

|  名称col350   | 主实体col200   | 关系类型col200   |    备注col500  |
| -------- |---------- |-----------|----- |
|[DER1N_AI_REVIEW_REPORT_AI_KB_DOCUMENT_DOCUMENT_ID](der/DER1N_AI_REVIEW_REPORT_AI_KB_DOCUMENT_DOCUMENT_ID)|[知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document)|1:N关系||
|[DER1N_AI_REVIEW_REPORT_AI_KNOWLEDGE_BASE_KB_ID](der/DER1N_AI_REVIEW_REPORT_AI_KNOWLEDGE_BASE_KB_ID)|[知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base)|1:N关系||
|[DER1N_AI_REVIEW_REPORT_DATA_RECORD_RECORD_ID](der/DER1N_AI_REVIEW_REPORT_DATA_RECORD_RECORD_ID)|[数据记录(DATA_RECORD)](module/meta/data_record)|1:N关系||

</el-tab-pane>
</el-tabs>
</el-row>

## 行为
| 中文名col200    | 代码名col150    | 类型col150    | 事务col100   | 批处理col100   | 附加操作col100  | 插件col150    |  备注col300  |
| -------- |---------- |----------- |:----:|:----:|---------| ----- | ----- |
|CheckKey|CheckKey|内置方法|默认|不支持||||
|Create|Create|内置方法|默认|不支持||||
|Get|Get|内置方法|默认|不支持|[附加操作](index/action_logic_index#ai_review_report_Get)|||
|GetDraft|GetDraft|内置方法|默认|不支持||||
|Remove|Remove|内置方法|默认|支持||||
|Save|Save|内置方法|默认|不支持||||
|Update|Update|内置方法|默认|不支持||||
|upsert|upsert|[实体处理逻辑](module/ai/ai_review_report/logic/upsert "upsert")|默认|不支持||||

## 处理逻辑
| 中文名col200    | 代码名col150    | 子类型col150    | 插件col200    |  备注col550  |
| -------- |---------- |----------- |------------|----------|
|[upsert](module/ai/ai_review_report/logic/upsert)|upsert|无|||
|[获取转换html](module/ai/ai_review_report/logic/ConvertedHTML)|ConvertedHTML|无|||

## 数据查询
| 中文名col200    | 代码名col150    | 默认查询col100 | 权限使用col100 | 自定义SQLcol100 |  备注col600|
| --------  | --------   | :----:  |:----:  | :----:  |----- |
|[Bykb_id_agent](module/ai/ai_review_report/query/Bykb_id_agent)|Bykb_id_agent|否|否 |否 ||
|[DEFAULT](module/ai/ai_review_report/query/Default)|DEFAULT|是|否 |否 ||
|[默认（全部数据）(VIEW)](module/ai/ai_review_report/query/View)|VIEW|否|否 |否 ||
|[reader](module/ai/ai_review_report/query/reader)|reader|否|否 |否 ||

## 数据集合
| 中文名col200  | 代码名col150  | 类型col100 | 默认集合col100 |   插件col200|   备注col500|
| --------  | --------   | :----:   | :----:   | ----- |----- |
|[DEFAULT](module/ai/ai_review_report/dataset/Default)|DEFAULT|数据查询|是|||
|[reader](module/ai/ai_review_report/dataset/reader)|reader|数据查询|否|||

## 数据权限

##### 操作角色 :id=ai_review_report-ALL_R

<p class="panel-title"><b>数据范围</b></p>

* `全部数据`

<p class="panel-title"><b>数据能力</b></p>

* `READ`



##### 操作用户(读) :id=ai_review_report-USER_R

<p class="panel-title"><b>数据范围</b></p>

* `数据集合` ：[reader](module/ai/ai_review_report#数据集合)

<p class="panel-title"><b>数据能力</b></p>

* `READ(知识库(READ))`



##### 操作用户(读写) :id=ai_review_report-USER_RW

<p class="panel-title"><b>数据范围</b></p>

* `数据集合` ：[reader](module/ai/ai_review_report#数据集合)

<p class="panel-title"><b>数据能力</b></p>

* `READ(知识库(READ))`
* `DELETE(知识库(SUBDATA))`
* `UPDATE(知识库(SUBDATA))`
* `CREATE(知识库(SUBDATA))`




## 搜索模式
|   搜索表达式col350   |    属性名col200    |    搜索模式col200        |备注col500  |
| -------- |------------|------------|------|
|N_AGENT_TAG_EQ|智能体标记|EQ||
|N_AGENT_TAG_IN|智能体标记|IN||
|N_AGENT_TAG_LIKE|智能体标记|LIKE||
|N_DOCUMENT_ID_EQ|知识库文档标识|EQ||
|N_DOCUMENT_NAME_EQ|知识库文档|EQ||
|N_DOCUMENT_NAME_LIKE|知识库文档|LIKE||
|N_ID_EQ|标识|EQ||
|N_KB_ID_EQ|知识库标识|EQ||
|N_KB_NAME_EQ|知识库|EQ||
|N_KB_NAME_LIKE|知识库|LIKE||
|N_NAME_LIKE|审查对象|LIKE||
|N_RECORD_ID_EQ|记录标识|EQ||
|N_REVIEW_REPORT_LIKE|报告|LIKE||
|N_REVIEW_RESULT_EQ|审查结果|EQ||
|N_UPDATE_TIME_GTANDEQ|更新时间|GTANDEQ||
|N_UPDATE_TIME_LTANDEQ|更新时间|LTANDEQ||

## 界面行为
|  中文名col200 |  代码名col150 |  标题col100   |     处理目标col100   |    处理类型col200        |  备注col500       |
| --------| --------| -------- |------------|------------|------------|
| AI添加审查报告 | ai_add | AI添加审查报告 |单项数据|用户自定义||
| 打印 | export_pdf | 打印 |单项数据|用户自定义||

## 界面逻辑
|  中文名col200 | 代码名col150 | 备注col900 |
| --------|--------|--------|
|[AI添加审查报告](module/ai/ai_review_report/uilogic/ai_add)|ai_add||

<div style="display: block; overflow: hidden; position: fixed; top: 140px; right: 100px;">

##### 导航
<el-anchor >
<el-anchor-link :href="`#/module/ai/ai_review_report?id=属性`">
  属性
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_review_report?id=关系`">
  关系
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_review_report?id=行为`">
  行为
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_review_report?id=处理逻辑`">
  处理逻辑
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_review_report?id=数据查询`">
  数据查询
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_review_report?id=数据集合`">
  数据集合
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_review_report?id=数据权限`">
  数据权限
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_review_report?id=搜索模式`">
  搜索模式
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_review_report?id=界面行为`">
  界面行为
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_review_report?id=界面逻辑`">
  界面逻辑
</el-anchor-link>
</el-anchor>
</div>

<script>
 const { createApp } = Vue
  createApp({
    data() {
      return {
show_der:'minor',


      }
    },
    methods: {
    }
  }).use(ElementPlus).mount('#app')
</script>