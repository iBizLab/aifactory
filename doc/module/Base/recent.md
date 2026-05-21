# 最近访问(recent)  <!-- {docsify-ignore-all} -->


记录用户最近访问过的实体记录，便于快速回溯和提高工作效率。


## 属性
|    中文名col150 | 属性名称col200           | 类型col200     | 长度col100    |允许为空col100    |  备注col500  |
| --------   |------------| -----  | -----  | :----: | -------- |
|建立人|CREATE_MAN|文本，可指定长度|100|否||
|建立时间|CREATE_TIME|日期时间型||否||
|标识<sup class="footnote-symbol"><font color=orange>[PK]</font></sup>|ID|全局唯一标识，文本类型，用户不可见|100|否||
|编号|IDENTIFIER|文本，可指定长度|100|是||
|是否已删除|IS_DELETED|是否逻辑||是||
|名称|NAME|文本，可指定长度|500|是||
|所属数据标识|OWNER_ID|文本，可指定长度|100|是||
|所属对象子类型|OWNER_SUBTYPE|[文本，可指定长度](index/dictionary_index#recent_visite "最近访问")|100|是||
|所属数据对象|OWNER_TYPE|[单项选择(文本值)](index/dictionary_index#recent_type "最近访问对象")|100|是||
|访问父类|RECENT_PARENT|文本，可指定长度|100|是||
|访问父类编号|RECENT_PARENT_IDENTIFIER|文本，可指定长度|100|是||
|访问父类名称|RECENT_PARENT_NAME|文本，可指定长度|100|是||
|编号|SHOW_IDENTIFIER|文本，可指定长度|200|是||
|访问类型|TYPE|文本，可指定长度|100|是||
|更新人|UPDATE_MAN|文本，可指定长度|100|否||
|更新时间|UPDATE_TIME|日期时间型||否||

<p class="panel-title"><b>联合主键</b></p>

  * `建立人(CREATE_MAN)`
  * `所属对象子类型(OWNER_SUBTYPE)`
  * `所属数据标识(OWNER_ID)`

###### 索引

<el-row>
<el-tabs v-model="show_index">

<el-tab-pane label="RECENT" name="index_RECENT">

|    中文名col150 | 属性名称col200           | 包含属性col100 | 排序方向col100 | 索引长度col100 | 备注col600 |
| --------   |------------| -----  | -----  | :----: | -------- |
|建立人|CREATE_MAN|false|升序|-1||
|所属对象子类型|OWNER_SUBTYPE|false|升序|-1||
|访问类型|TYPE|false|升序|-1||

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
|跳转对应视图|jump_corresponding_view|[实体处理逻辑](module/Base/recent/logic/jump_corresponding_view "跳转对应视图")|默认|不支持||||

## 处理逻辑
| 中文名col200    | 代码名col150    | 子类型col150    | 插件col200    |  备注col550  |
| -------- |---------- |----------- |------------|----------|
|[跳转对应视图](module/Base/recent/logic/jump_corresponding_view)|jump_corresponding_view|无|||

## 数据查询
| 中文名col200    | 代码名col150    | 默认查询col100 | 权限使用col100 | 自定义SQLcol100 |  备注col600|
| --------  | --------   | :----:  |:----:  | :----:  |----- |
|[数据查询(DEFAULT)](module/Base/recent/query/Default)|DEFAULT|是|否 |否 ||
|[默认（全部数据）(VIEW)](module/Base/recent/query/View)|VIEW|否|否 |否 ||
|[最近访问页面(recent_page)](module/Base/recent/query/recent_page)|recent_page|否|否 |否 ||
|[最近使用(recent_use)](module/Base/recent/query/recent_use)|recent_use|否|否 |否 ||
|[本人最新访问(user)](module/Base/recent/query/user)|user|否|否 |否 ||

## 数据集合
| 中文名col200  | 代码名col150  | 类型col100 | 默认集合col100 |   插件col200|   备注col500|
| --------  | --------   | :----:   | :----:   | ----- |----- |
|[数据集(DEFAULT)](module/Base/recent/dataset/Default)|DEFAULT|数据查询|是|||
|[最近访问页面(recent_page)](module/Base/recent/dataset/recent_page)|recent_page|数据查询|否|||
|[最近使用(recent_use)](module/Base/recent/dataset/recent_use)|recent_use|数据查询|否|||
|[本人最新访问(user)](module/Base/recent/dataset/user)|user|数据查询|否|||

## 数据权限

##### 全部数据（读写） :id=recent-ALL_RW

<p class="panel-title"><b>数据范围</b></p>

* `全部数据`

<p class="panel-title"><b>数据能力</b></p>

* `CREATE`
* `READ`
* `DELETE`
* `UPDATE`



##### 普通用户（读写） :id=recent-USER_RW

<p class="panel-title"><b>数据范围</b></p>

* `数据集合` ：[本人最新访问(user)](module/Base/recent#数据集合)

<p class="panel-title"><b>数据能力</b></p>

* `UPDATE`
* `DELETE`
* `CREATE`
* `READ`




## 搜索模式
|   搜索表达式col350   |    属性名col200    |    搜索模式col200        |备注col500  |
| -------- |------------|------------|------|
|N_CREATE_MAN_EQ|建立人|EQ||
|N_ID_EQ|标识|EQ||
|N_NAME_LIKE|名称|LIKE||
|N_OWNER_ID_EQ|所属数据标识|EQ||
|N_OWNER_SUBTYPE_EQ|所属对象子类型|EQ||
|N_OWNER_TYPE_EQ|所属数据对象|EQ||
|N_RECENT_PARENT_EQ|访问父类|EQ||
|N_SHOW_IDENTIFIER_LIKE|编号|LIKE||

## 界面行为
|  中文名col200 |  代码名col150 |  标题col100   |     处理目标col100   |    处理类型col200        |  备注col500       |
| --------| --------| -------- |------------|------------|------------|
| 通过重定向视图跳转 | jump | 通过重定向视图跳转 |单项数据|<details><summary>打开视图或向导（模态）</summary></details>||

## 界面逻辑
|  中文名col200 | 代码名col150 | 备注col900 |
| --------|--------|--------|
|[最近访问跳转其他视图](module/Base/recent/uilogic/recent_jump_other_view)|recent_jump_other_view|首页最近访问点击后跳转其他视图|

<div style="display: block; overflow: hidden; position: fixed; top: 140px; right: 100px;">

##### 导航
<el-anchor >
<el-anchor-link :href="`#/module/Base/recent?id=属性`">
  属性
</el-anchor-link>
<el-anchor-link :href="`#/module/Base/recent?id=行为`">
  行为
</el-anchor-link>
<el-anchor-link :href="`#/module/Base/recent?id=处理逻辑`">
  处理逻辑
</el-anchor-link>
<el-anchor-link :href="`#/module/Base/recent?id=数据查询`">
  数据查询
</el-anchor-link>
<el-anchor-link :href="`#/module/Base/recent?id=数据集合`">
  数据集合
</el-anchor-link>
<el-anchor-link :href="`#/module/Base/recent?id=数据权限`">
  数据权限
</el-anchor-link>
<el-anchor-link :href="`#/module/Base/recent?id=搜索模式`">
  搜索模式
</el-anchor-link>
<el-anchor-link :href="`#/module/Base/recent?id=界面行为`">
  界面行为
</el-anchor-link>
<el-anchor-link :href="`#/module/Base/recent?id=界面逻辑`">
  界面逻辑
</el-anchor-link>
</el-anchor>
</div>

<script>
 const { createApp } = Vue
  createApp({
    data() {
      return {


show_index:'index_RECENT',
      }
    },
    methods: {
    }
  }).use(ElementPlus).mount('#app')
</script>