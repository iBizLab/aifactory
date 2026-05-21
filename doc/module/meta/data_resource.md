# 数据资源(data_resource)  <!-- {docsify-ignore-all} -->


## 属性
|    中文名col150 | 属性名称col200           | 类型col200     | 长度col100    |允许为空col100    |  备注col500  |
| --------   |------------| -----  | -----  | :----: | -------- |
|创建时间|CREATE_TIME|日期时间型||否||
|definition|DEFINITION|一对一动态对象|1048576|是||
|逻辑有效标记|ENABLED|是否逻辑||否||
|标识<sup class="footnote-symbol"><font color=orange>[PK]</font></sup>|ID|全局唯一标识，文本类型，用户不可见|100|否||
|名称|NAME|文本，可指定长度|200|否||
|资源代码|RESOURCE_CODE|文本，可指定长度|100|是||
|格式定义|SCHEMA|一对一动态对象|1048576|是||
|排序|SORT|大整型||是||
|最后更新时间|UPDATE_TIME|日期时间型||否||


## 关系

<el-row>
<el-tabs v-model="show_der">
<el-tab-pane label="主关系" name="major">

| 名称col350     |   从实体col200 | 关系类型col200     |   备注col500  |
| -------- |---------- |------------|----- |
|[DER1N_AI_KNOWLEDGE_BASE_DATA_RESOURCE_RESOURCE_ID](der/DER1N_AI_KNOWLEDGE_BASE_DATA_RESOURCE_RESOURCE_ID)|[知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base)|1:N关系||
|[DER1N_CATEGORY_SETTINGS_DATA_RESOURCE_RESOURCE_ID](der/DER1N_CATEGORY_SETTINGS_DATA_RESOURCE_RESOURCE_ID)|[类别设置(CATEGORY_SETTINGS)](module/Base/category_settings)|1:N关系||
|[DER1N_DATA_RECORD_DATA_RESOURCE__RESOURCE_ID](der/DER1N_DATA_RECORD_DATA_RESOURCE__RESOURCE_ID)|[数据记录(DATA_RECORD)](module/meta/data_record)|1:N关系||


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
|反馈资源状态feedback|feedback|用户自定义|默认|不支持|||反馈资源状态|
|full|full|[实体处理逻辑](module/meta/data_resource/logic/full "full")|默认|不支持||||

## 处理逻辑
| 中文名col200    | 代码名col150    | 子类型col150    | 插件col200    |  备注col550  |
| -------- |---------- |----------- |------------|----------|
|[full](module/meta/data_resource/logic/full)|full|无|||

## 数据查询
| 中文名col200    | 代码名col150    | 默认查询col100 | 权限使用col100 | 自定义SQLcol100 |  备注col600|
| --------  | --------   | :----:  |:----:  | :----:  |----- |
|[DEFAULT](module/meta/data_resource/query/Default)|DEFAULT|是|否 |否 ||
|[默认（全部数据）(VIEW)](module/meta/data_resource/query/View)|VIEW|否|否 |否 ||

## 数据集合
| 中文名col200  | 代码名col150  | 类型col100 | 默认集合col100 |   插件col200|   备注col500|
| --------  | --------   | :----:   | :----:   | ----- |----- |
|[DEFAULT](module/meta/data_resource/dataset/Default)|DEFAULT|数据查询|是|||

## 数据权限

##### 全部数据（读） :id=data_resource-ALL_R

<p class="panel-title"><b>数据范围</b></p>

* `全部数据`

<p class="panel-title"><b>数据能力</b></p>

* `READ`



##### 全部数据（读写） :id=data_resource-ALL_RW

<p class="panel-title"><b>数据范围</b></p>

* `全部数据`

<p class="panel-title"><b>数据能力</b></p>

* `UPDATE`
* `DELETE`
* `READ`
* `CREATE`




## 搜索模式
|   搜索表达式col350   |    属性名col200    |    搜索模式col200        |备注col500  |
| -------- |------------|------------|------|
|N_ID_EQ|标识|EQ||
|N_NAME_LIKE|名称|LIKE||

<div style="display: block; overflow: hidden; position: fixed; top: 140px; right: 100px;">

##### 导航
<el-anchor >
<el-anchor-link :href="`#/module/meta/data_resource?id=属性`">
  属性
</el-anchor-link>
<el-anchor-link :href="`#/module/meta/data_resource?id=关系`">
  关系
</el-anchor-link>
<el-anchor-link :href="`#/module/meta/data_resource?id=行为`">
  行为
</el-anchor-link>
<el-anchor-link :href="`#/module/meta/data_resource?id=处理逻辑`">
  处理逻辑
</el-anchor-link>
<el-anchor-link :href="`#/module/meta/data_resource?id=数据查询`">
  数据查询
</el-anchor-link>
<el-anchor-link :href="`#/module/meta/data_resource?id=数据集合`">
  数据集合
</el-anchor-link>
<el-anchor-link :href="`#/module/meta/data_resource?id=数据权限`">
  数据权限
</el-anchor-link>
<el-anchor-link :href="`#/module/meta/data_resource?id=搜索模式`">
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