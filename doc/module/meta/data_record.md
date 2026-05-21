# 数据记录(data_record)  <!-- {docsify-ignore-all} -->


## 属性
|    中文名col150 | 属性名称col200           | 类型col200     | 长度col100    |允许为空col100    |  备注col500  |
| --------   |------------| -----  | -----  | :----: | -------- |
|创建时间|_CREATE_TIME|日期时间型||否||
|创建人|_CREATOR|文本，可指定长度|100|否||
|逻辑有效标记|_ENABLED|是否逻辑||是||
|标识<sup class="footnote-symbol"><font color=orange>[PK]</font></sup>|_ID|全局唯一标识，文本类型，用户不可见|60|是||
|编号|_KEY|文本，可指定长度|100|是||
|NER标记|_NER_FLAG|是否逻辑||是||
|区域标识|_REGION|文本，可指定长度|100|是||
|资源代码|_RESOURCE_CODE|外键值附加数据|100|是||
|资源标识|_RESOURCE_ID|外键值|100|是||
|资源名称|_RESOURCE_NAME|外键值文本|200|是||
|摘要|_SUMMARY|长文本，没有长度限制|1048576|是||
|标题|_TITLE|文本，可指定长度|1000|是||
|最后更新人|_UPDATER|文本，可指定长度|100|否||
|最后更新时间|_UPDATE_TIME|日期时间型||否||


## 关系

<el-row>
<el-tabs v-model="show_der">
<el-tab-pane label="主关系" name="major">

| 名称col350     |   从实体col200 | 关系类型col200     |   备注col500  |
| -------- |---------- |------------|----- |
|[DER1N_AI_KNOWLEDGE_BASE_DATA_RECORD_RECORD_ID](der/DER1N_AI_KNOWLEDGE_BASE_DATA_RECORD_RECORD_ID)|[知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base)|1:N关系||
|[DER1N_AI_REVIEW_REPORT_DATA_RECORD_RECORD_ID](der/DER1N_AI_REVIEW_REPORT_DATA_RECORD_RECORD_ID)|[智能审查报告(AI_REVIEW_REPORT)](module/ai/ai_review_report)|1:N关系||


</el-tab-pane>
<el-tab-pane label="从关系" name="minor">

|  名称col350   | 主实体col200   | 关系类型col200   |    备注col500  |
| -------- |---------- |-----------|----- |
|[DER1N_DATA_RECORD_DATA_RESOURCE__RESOURCE_ID](der/DER1N_DATA_RECORD_DATA_RESOURCE__RESOURCE_ID)|[数据资源(DATA_RESOURCE)](module/meta/data_resource)|1:N关系||

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
|获取关联知识库标识|find_kb_id|用户自定义|默认|不支持||||
|保存数据|upsert|用户自定义|默认|不支持||||
|批量保存数据|upsert_batch|用户自定义|默认|仅支持批操作||||

## 数据查询
| 中文名col200    | 代码名col150    | 默认查询col100 | 权限使用col100 | 自定义SQLcol100 |  备注col600|
| --------  | --------   | :----:  |:----:  | :----:  |----- |
|[DEFAULT](module/meta/data_record/query/Default)|DEFAULT|是|否 |否 ||
|[默认（全部数据）(VIEW)](module/meta/data_record/query/View)|VIEW|否|否 |否 ||

## 数据集合
| 中文名col200  | 代码名col150  | 类型col100 | 默认集合col100 |   插件col200|   备注col500|
| --------  | --------   | :----:   | :----:   | ----- |----- |
|[DEFAULT](module/meta/data_record/dataset/Default)|DEFAULT|数据查询|是|||

## 搜索模式
|   搜索表达式col350   |    属性名col200    |    搜索模式col200        |备注col500  |
| -------- |------------|------------|------|
|N__ID_EQ|标识|EQ||
|N__RESOURCE_ID_EQ|资源标识|EQ||
|N__RESOURCE_NAME_EQ|资源名称|EQ||
|N__RESOURCE_NAME_LIKE|资源名称|LIKE||
|N__TITLE_LIKE|标题|LIKE||

<div style="display: block; overflow: hidden; position: fixed; top: 140px; right: 100px;">

##### 导航
<el-anchor >
<el-anchor-link :href="`#/module/meta/data_record?id=属性`">
  属性
</el-anchor-link>
<el-anchor-link :href="`#/module/meta/data_record?id=关系`">
  关系
</el-anchor-link>
<el-anchor-link :href="`#/module/meta/data_record?id=行为`">
  行为
</el-anchor-link>
<el-anchor-link :href="`#/module/meta/data_record?id=数据查询`">
  数据查询
</el-anchor-link>
<el-anchor-link :href="`#/module/meta/data_record?id=数据集合`">
  数据集合
</el-anchor-link>
<el-anchor-link :href="`#/module/meta/data_record?id=搜索模式`">
  搜索模式
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