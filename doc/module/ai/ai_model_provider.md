# 模型提供商(ai_model_provider)  <!-- {docsify-ignore-all} -->


## 属性
|    中文名col150 | 属性名称col200           | 类型col200     | 长度col100    |允许为空col100    |  备注col500  |
| --------   |------------| -----  | -----  | :----: | -------- |
|api_base_url|API_BASE_URL|文本，可指定长度|200|是||
|API 地址|BASE_URL|文本，可指定长度|300|是||
|API 密钥|DEFAULT_TOKEN|文本，可指定长度|1000|是||
|默认版本号后缀|DEFAULT_VERSION|文本，可指定长度|100|是||
|是否存在凭证|HAS_CREDENTIAL|文本，可指定长度|200|是||
|标识<sup class="footnote-symbol"><font color=orange>[PK]</font></sup>|ID|全局唯一标识，文本类型，用户不可见|100|否||
|名称|NAME|文本，可指定长度|200|是||
|更新时间|UPDATE_TIME|日期时间型||否||


## 关系

<el-row>
<el-tabs v-model="show_der">
<el-tab-pane label="主关系" name="major">

| 名称col350     |   从实体col200 | 关系类型col200     |   备注col500  |
| -------- |---------- |------------|----- |
|[DER1N_AI_MODEL_AI_MODEL_PROVIDER_PROVIDER](der/DER1N_AI_MODEL_AI_MODEL_PROVIDER_PROVIDER)|[AI大模型(AI_MODEL)](module/ai/ai_model)|1:N关系||


</el-tab-pane>
</el-tabs>
</el-row>

## 行为
| 中文名col200    | 代码名col150    | 类型col150    | 事务col100   | 批处理col100   | 附加操作col100  | 插件col150    |  备注col300  |
| -------- |---------- |----------- |:----:|:----:|---------| ----- | ----- |
|CheckKey|CheckKey|内置方法|默认|不支持||||
|Create|Create|内置方法|默认|不支持|[附加操作](index/action_logic_index#ai_model_provider_Create)|||
|Get|Get|内置方法|默认|不支持|[附加操作](index/action_logic_index#ai_model_provider_Get)|||
|GetDraft|GetDraft|内置方法|默认|不支持||||
|Remove|Remove|内置方法|默认|支持||||
|Save|Save|内置方法|默认|不支持||||
|Update|Update|内置方法|默认|不支持|[附加操作](index/action_logic_index#ai_model_provider_Update)|||

## 处理逻辑
| 中文名col200    | 代码名col150    | 子类型col150    | 插件col200    |  备注col550  |
| -------- |---------- |----------- |------------|----------|
|[生成AI凭证](module/ai/ai_model_provider/logic/create_ai_credential)|create_ai_credential|无|||
|[获取已登记AI凭证](module/ai/ai_model_provider/logic/get_ai_default_credential)|get_ai_default_credential|无|||

## 数据查询
| 中文名col200    | 代码名col150    | 默认查询col100 | 权限使用col100 | 自定义SQLcol100 |  备注col600|
| --------  | --------   | :----:  |:----:  | :----:  |----- |
|[DEFAULT](module/ai/ai_model_provider/query/Default)|DEFAULT|是|否 |否 ||
|[默认（全部数据）(VIEW)](module/ai/ai_model_provider/query/View)|VIEW|否|否 |否 ||
|[存在凭证(has_credential)](module/ai/ai_model_provider/query/has_credential)|has_credential|否|否 |否 ||
|[不存在凭证(no_has_credential)](module/ai/ai_model_provider/query/no_has_credential)|no_has_credential|否|否 |否 ||

## 数据集合
| 中文名col200  | 代码名col150  | 类型col100 | 默认集合col100 |   插件col200|   备注col500|
| --------  | --------   | :----:   | :----:   | ----- |----- |
|[DEFAULT](module/ai/ai_model_provider/dataset/Default)|DEFAULT|数据查询|是|||
|[凭证配置(credential_state)](module/ai/ai_model_provider/dataset/credential_state)|credential_state|数据查询|否|||

## 数据权限

##### 全部数据（读） :id=ai_model_provider-ALL_R

<p class="panel-title"><b>数据范围</b></p>

* `全部数据`

<p class="panel-title"><b>数据能力</b></p>

* `READ`



##### 全部数据（读写） :id=ai_model_provider-ALL_RW

<p class="panel-title"><b>数据范围</b></p>

* `全部数据`

<p class="panel-title"><b>数据能力</b></p>

* `DELETE`
* `READ`
* `CREATE`
* `UPDATE`




## 搜索模式
|   搜索表达式col350   |    属性名col200    |    搜索模式col200        |备注col500  |
| -------- |------------|------------|------|
|N_ID_EQ|标识|EQ||
|N_NAME_LIKE|名称|LIKE||

## 界面行为
|  中文名col200 |  代码名col150 |  标题col100   |     处理目标col100   |    处理类型col200        |  备注col500       |
| --------| --------| -------- |------------|------------|------------|
| 打开模型提供商新建视图 | open_provider_quick_create_view | 模型提供商新建 |无数据|<details><summary>打开视图或向导（模态）</summary>[添加提供商](app/view/ai_model_provider_quick_create_view)</details>||

<div style="display: block; overflow: hidden; position: fixed; top: 140px; right: 100px;">

##### 导航
<el-anchor >
<el-anchor-link :href="`#/module/ai/ai_model_provider?id=属性`">
  属性
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_model_provider?id=关系`">
  关系
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_model_provider?id=行为`">
  行为
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_model_provider?id=处理逻辑`">
  处理逻辑
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_model_provider?id=数据查询`">
  数据查询
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_model_provider?id=数据集合`">
  数据集合
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_model_provider?id=数据权限`">
  数据权限
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_model_provider?id=搜索模式`">
  搜索模式
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_model_provider?id=界面行为`">
  界面行为
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