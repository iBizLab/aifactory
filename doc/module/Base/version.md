# 版本(version)  <!-- {docsify-ignore-all} -->


用于管理和记录软件的版本历史和变更。


## 属性
|    中文名col150 | 属性名称col200           | 类型col200     | 长度col100    |允许为空col100    |  备注col500  |
| --------   |------------| -----  | -----  | :----: | -------- |
|建立人|CREATE_MAN|文本，可指定长度|100|否||
|建立时间|CREATE_TIME|日期时间型||否||
|数据|DATA|长文本，没有长度限制|1048576|是||
|描述|DESCRIPTION|长文本，长度1000|2000|是||
|标识<sup class="footnote-symbol"><font color=orange>[PK]</font></sup>|ID|全局唯一标识，文本类型，用户不可见|100|否||
|版本|IDENTIFIER|数值||是||
|是否命名|IS_NAMED|是否逻辑||是||
|手动提交|MANUAL|是否逻辑||是||
|名称|NAME|文本，可指定长度|200|是||
|所属数据标识|OWNER_ID|文本，可指定长度|100|是||
|所属数据对象|OWNER_TYPE|文本，可指定长度|100|是||
|支持恢复|RESTORABLE|文本，可指定长度|100|是||
|更新人|UPDATE_MAN|文本，可指定长度|100|否||
|更新时间|UPDATE_TIME|日期时间型||否||


###### 索引

<el-row>
<el-tabs v-model="show_index">

<el-tab-pane label="VERSION" name="index_VERSION">

|    中文名col150 | 属性名称col200           | 包含属性col100 | 排序方向col100 | 索引长度col100 | 备注col600 |
| --------   |------------| -----  | -----  | :----: | -------- |
|所属数据标识|OWNER_ID|false|升序|-1||

</el-tab-pane>

</el-tabs>
</el-row>

## 关系

<el-row>
<el-tabs v-model="show_der">
<el-tab-pane label="从关系" name="minor">

|  名称col350   | 主实体col200   | 关系类型col200   |    备注col500  |
| -------- |---------- |-----------|----- |
|[DERCUSTOM_VERSION_PAGE](der/DERCUSTOM_VERSION_PAGE)|[页面(PAGE)](module/Wiki/article_page)|自定义关系||

</el-tab-pane>
</el-tabs>
</el-row>

## 行为
| 中文名col200    | 代码名col150    | 类型col150    | 事务col100   | 批处理col100   | 附加操作col100  | 插件col150    |  备注col300  |
| -------- |---------- |----------- |:----:|:----:|---------| ----- | ----- |
|提交版本|Commit|用户自定义|默认|不支持||[CommitVersionDEActionRuntime](index/plugin_index#UsrSFPlugin0324806543)||
|CheckKey|CheckKey|内置方法|默认|不支持||||
|Create|Create|内置方法|默认|不支持||||
|修复版本|fix_commit|用户自定义|默认|不支持||[FixCommitVersionDEActionRuntime](index/plugin_index#UsrSFPlugin0424197954)||
|Get|Get|内置方法|默认|不支持||||
|GetDraft|GetDraft|内置方法|默认|不支持|[附加操作](index/action_logic_index#version_GetDraft)|||
|恢复指定版本|Restore|用户自定义|默认|不支持||[RestoreVersionDEActionRuntime](index/plugin_index#UsrSFPlugin0324899435)||
|Remove|Remove|内置方法|默认|支持||||
|Save|Save|内置方法|默认|不支持||||
|Update|Update|内置方法|默认|不支持||||

## 处理逻辑
| 中文名col200    | 代码名col150    | 子类型col150    | 插件col200    |  备注col550  |
| -------- |---------- |----------- |------------|----------|
|[新建版本时填充默认版本名称](module/Base/version/logic/fill_default_name)|fill_default_name|无||新建版本时，根据已创建的版本记录生成默认版本名称|

## 数据查询
| 中文名col200    | 代码名col150    | 默认查询col100 | 权限使用col100 | 自定义SQLcol100 |  备注col600|
| --------  | --------   | :----:  |:----:  | :----:  |----- |
|[数据查询(DEFAULT)](module/Base/version/query/Default)|DEFAULT|是|否 |否 ||
|[默认（全部数据）(VIEW)](module/Base/version/query/View)|VIEW|否|否 |否 ||
|[命名版本(name_version)](module/Base/version/query/name_version)|name_version|否|否 |否 ||
|[所属对象版本(owner)](module/Base/version/query/owner)|owner|否|否 |否 ||

## 数据集合
| 中文名col200  | 代码名col150  | 类型col100 | 默认集合col100 |   插件col200|   备注col500|
| --------  | --------   | :----:   | :----:   | ----- |----- |
|[数据集(DEFAULT)](module/Base/version/dataset/Default)|DEFAULT|数据查询|是|||
|[命名版本(name_version)](module/Base/version/dataset/name_version)|name_version|数据查询|否|||
|[所属对象版本(owner)](module/Base/version/dataset/owner)|owner|数据查询|否|||

## 数据权限

##### 全部数据（读） :id=version-ALL_R

<p class="panel-title"><b>数据范围</b></p>

* `全部数据`

<p class="panel-title"><b>数据能力</b></p>

* `READ`



##### 全部数据（读写） :id=version-ALL_RW

<p class="panel-title"><b>数据范围</b></p>

* `全部数据`

<p class="panel-title"><b>数据能力</b></p>

* `CREATE`
* `UPDATE`
* `READ`
* `DELETE`




## 搜索模式
|   搜索表达式col350   |    属性名col200    |    搜索模式col200        |备注col500  |
| -------- |------------|------------|------|
|N_ID_IN|标识|IN||
|N_ID_EQ|标识|EQ||
|N_IS_NAMED_EQ|是否命名|EQ||
|N_NAME_LIKE|名称|LIKE||
|N_OWNER_ID_EQ|所属数据标识|EQ||
|N_OWNER_ID_IN|所属数据标识|IN||
|N_OWNER_TYPE_EQ|所属数据对象|EQ||

<div style="display: block; overflow: hidden; position: fixed; top: 140px; right: 100px;">

##### 导航
<el-anchor >
<el-anchor-link :href="`#/module/Base/version?id=属性`">
  属性
</el-anchor-link>
<el-anchor-link :href="`#/module/Base/version?id=关系`">
  关系
</el-anchor-link>
<el-anchor-link :href="`#/module/Base/version?id=行为`">
  行为
</el-anchor-link>
<el-anchor-link :href="`#/module/Base/version?id=处理逻辑`">
  处理逻辑
</el-anchor-link>
<el-anchor-link :href="`#/module/Base/version?id=数据查询`">
  数据查询
</el-anchor-link>
<el-anchor-link :href="`#/module/Base/version?id=数据集合`">
  数据集合
</el-anchor-link>
<el-anchor-link :href="`#/module/Base/version?id=数据权限`">
  数据权限
</el-anchor-link>
<el-anchor-link :href="`#/module/Base/version?id=搜索模式`">
  搜索模式
</el-anchor-link>
</el-anchor>
</div>

<script>
 const { createApp } = Vue
  createApp({
    data() {
      return {
show_der:'minor',

show_index:'index_VERSION',
      }
    },
    methods: {
    }
  }).use(ElementPlus).mount('#app')
</script>