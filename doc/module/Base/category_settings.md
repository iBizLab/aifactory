# 类别设置(category_settings)  <!-- {docsify-ignore-all} -->


## 属性
|    中文名col150 | 属性名称col200           | 类型col200     | 长度col100    |允许为空col100    |  备注col500  |
| --------   |------------| -----  | -----  | :----: | -------- |
|自动创建资源知识库|AUTO_GEN_KB|[单项选择(文本值)](index/dictionary_index#resource_kb_sync_type "资源库同步类型")|200|是||
|交谈模型|CHAT_MODEL|外键值文本|100|是||
|交谈模型标识|CHAT_MODEL_ID|外键值|100|是||
|切片方法|CHUNK_METHOD|[单项选择(文本值)](index/dictionary_index#chunkingstrategy "切片策略")|100|是||
|configs|CONFIGS|长文本，没有长度限制|1048576|是||
|创建人|CREATE_MAN|文本，可指定长度|100|否||
|创建时间|CREATE_TIME|日期时间型||否||
|embedding模型|EMBEDDING_MODEL|外键值文本|100|是||
|嵌入模型标识|EMBEDDING_MODEL_ID|外键值|100|是||
|逻辑有效标识|ENABLE|是否逻辑||是||
|快速交谈模型|FLASH_MODEL|外键值文本|100|是||
|快速交谈模型标识|FLASH_MODEL_ID|外键值|100|是||
|引导提示词智能体标识|GUIDED_PROMPT_AGENT_ID|文本，可指定长度|100|是||
|标识<sup class="footnote-symbol"><font color=orange>[PK]</font></sup>|ID|全局唯一标识，文本类型，用户不可见|100|否||
|快速交谈模型|INTENT_MODEL|外键值文本|100|是||
|模型标识|INTENT_MODEL_ID|外键值|100|是||
|名称|NAME|文本，可指定长度|200|是||
|解析配置|PARSER_CONFIG|一对一关系数据对象|1048576|是||
|召回重排|RERANK|是否逻辑||是||
|召回重排模型|RERANK_MODEL|外键值文本|100|是||
|召回重排模型标识|RERANK_MODEL_ID|外键值|100|是||
|数据资源|RESOURCE|外键值文本|200|是||
|数据资源|RESOURCE_CODE|外键值附加数据|100|是||
|标识|RESOURCE_ID|外键值|100|是||
|召回相似度阈值|SIMILARITY_THRESHOLD|数值||是||
|知识库源标识|SOURCE_ID|外键值|100|是||
|知识库源名称|SOURCE_NAME|外键值文本|200|是||
|最大召回数量|TOP_K|整型||是||
|更新人|UPDATE_MAN|文本，可指定长度|100|否||
|更新时间|UPDATE_TIME|日期时间型||否||
|使用知识图谱|USE_KG|是否逻辑||是||
|向量相似度权重|VECTOR_SIMILARITY_WEIGHT|数值||是||
|可见范围|VISIBILITY|单项选择(文本值)|60|是||
|多模态模型|VL_MODEL|外键值文本|100|是||
|多模态模型标识|VL_MODEL_ID|外键值|100|是||


## 关系

<el-row>
<el-tabs v-model="show_der">
<el-tab-pane label="主关系" name="major">

| 名称col350     |   从实体col200 | 关系类型col200     |   备注col500  |
| -------- |---------- |------------|----- |
|[DERCUSTOM_AI_KB_CHUNKING_STRATEGY_CATEGORY_SETTING](der/DERCUSTOM_AI_KB_CHUNKING_STRATEGY_CATEGORY_SETTING)|[知识库文档切片策略(AI_KB_CHUNKING_STRATEGY)](module/ai/ai_kb_chunking_strategy)|自定义关系||


</el-tab-pane>
<el-tab-pane label="从关系" name="minor">

|  名称col350   | 主实体col200   | 关系类型col200   |    备注col500  |
| -------- |---------- |-----------|----- |
|[DER1N_CATEGORY_SETTINGS_AI_KNOWLEDGE_SOURCE_SOURCE_ID](der/DER1N_CATEGORY_SETTINGS_AI_KNOWLEDGE_SOURCE_SOURCE_ID)|[知识库源(AI_KNOWLEDGE_SOURCE)](module/ai/ai_knowledge_source)|1:N关系||
|[DER1N_CATEGORY_SETTINGS_AI_MODEL_CHAT_MODEL_ID](der/DER1N_CATEGORY_SETTINGS_AI_MODEL_CHAT_MODEL_ID)|[AI大模型(AI_MODEL)](module/ai/ai_model)|1:N关系||
|[DER1N_CATEGORY_SETTINGS_AI_MODEL_EMBEDDING_MODEL_ID](der/DER1N_CATEGORY_SETTINGS_AI_MODEL_EMBEDDING_MODEL_ID)|[AI大模型(AI_MODEL)](module/ai/ai_model)|1:N关系||
|[DER1N_CATEGORY_SETTINGS_AI_MODEL_FLASH_MODEL_ID](der/DER1N_CATEGORY_SETTINGS_AI_MODEL_FLASH_MODEL_ID)|[AI大模型(AI_MODEL)](module/ai/ai_model)|1:N关系||
|[DER1N_CATEGORY_SETTINGS_AI_MODEL_INTENT_MODEL_ID](der/DER1N_CATEGORY_SETTINGS_AI_MODEL_INTENT_MODEL_ID)|[AI大模型(AI_MODEL)](module/ai/ai_model)|1:N关系||
|[DER1N_CATEGORY_SETTINGS_AI_MODEL_RERANK_MODEL_ID](der/DER1N_CATEGORY_SETTINGS_AI_MODEL_RERANK_MODEL_ID)|[AI大模型(AI_MODEL)](module/ai/ai_model)|1:N关系||
|[DER1N_CATEGORY_SETTINGS_AI_MODEL_VL_MODEL_ID](der/DER1N_CATEGORY_SETTINGS_AI_MODEL_VL_MODEL_ID)|[AI大模型(AI_MODEL)](module/ai/ai_model)|1:N关系||
|[DER1N_CATEGORY_SETTINGS_DATA_RESOURCE_RESOURCE_ID](der/DER1N_CATEGORY_SETTINGS_DATA_RESOURCE_RESOURCE_ID)|[数据资源(DATA_RESOURCE)](module/meta/data_resource)|1:N关系||
|[DERCUSTOM_CATEGORY_SETTINGS_CATEGORY](der/DERCUSTOM_CATEGORY_SETTINGS_CATEGORY)|[类别(CATEGORY)](module/Base/category)|自定义关系||

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
|find_aifactory_sys_env|find_aifactory_sys_env|[实体处理逻辑](module/Base/category_settings/logic/get_aifactory_sys_env "get_aifactory_sys_env")|默认|不支持||||
|save_aifactory_sys_env|save_aifactory_sys_env|[实体处理逻辑](module/Base/category_settings/logic/save_aifactory_sys_env "save_aifactory_sys_env")|默认|不支持||||

## 处理逻辑
| 中文名col200    | 代码名col150    | 子类型col150    | 插件col200    |  备注col550  |
| -------- |---------- |----------- |------------|----------|
|[get_aifactory_sys_env](module/Base/category_settings/logic/get_aifactory_sys_env)|get_aifactory_sys_env|无|||
|[save_aifactory_sys_env](module/Base/category_settings/logic/save_aifactory_sys_env)|save_aifactory_sys_env|无|||

## 数据查询
| 中文名col200    | 代码名col150    | 默认查询col100 | 权限使用col100 | 自定义SQLcol100 |  备注col600|
| --------  | --------   | :----:  |:----:  | :----:  |----- |
|[DEFAULT](module/Base/category_settings/query/Default)|DEFAULT|是|否 |否 ||
|[默认（全部数据）(VIEW)](module/Base/category_settings/query/View)|VIEW|否|否 |否 ||

## 数据集合
| 中文名col200  | 代码名col150  | 类型col100 | 默认集合col100 |   插件col200|   备注col500|
| --------  | --------   | :----:   | :----:   | ----- |----- |
|[DEFAULT](module/Base/category_settings/dataset/Default)|DEFAULT|数据查询|是|||

## 数据权限

##### 全部数据（读写） :id=category_settings-ALL_RW

<p class="panel-title"><b>数据范围</b></p>

* `全部数据`

<p class="panel-title"><b>数据能力</b></p>

* `CREATE`
* `DELETE`
* `READ`
* `UPDATE`
* `ENV`



##### 操作用户(读写) :id=category_settings-USER_RW

<p class="panel-title"><b>数据范围</b></p>

* `无`

<p class="panel-title"><b>数据能力</b></p>

* `UPDATE`
* `READ`
* `DELETE`
* `CREATE`




## 搜索模式
|   搜索表达式col350   |    属性名col200    |    搜索模式col200        |备注col500  |
| -------- |------------|------------|------|
|N_CHAT_MODEL_ID_EQ|交谈模型标识|EQ||
|N_EMBEDDING_MODEL_ID_EQ|嵌入模型标识|EQ||
|N_FLASH_MODEL_ID_EQ|快速交谈模型标识|EQ||
|N_ID_EQ|标识|EQ||
|N_INTENT_MODEL_ID_EQ|模型标识|EQ||
|N_NAME_LIKE|名称|LIKE||
|N_RERANK_MODEL_ID_EQ|召回重排模型标识|EQ||
|N_RESOURCE_ID_EQ|标识|EQ||
|N_SOURCE_ID_EQ|知识库源标识|EQ||
|N_VL_MODEL_ID_EQ|多模态模型标识|EQ||

<div style="display: block; overflow: hidden; position: fixed; top: 140px; right: 100px;">

##### 导航
<el-anchor >
<el-anchor-link :href="`#/module/Base/category_settings?id=属性`">
  属性
</el-anchor-link>
<el-anchor-link :href="`#/module/Base/category_settings?id=关系`">
  关系
</el-anchor-link>
<el-anchor-link :href="`#/module/Base/category_settings?id=行为`">
  行为
</el-anchor-link>
<el-anchor-link :href="`#/module/Base/category_settings?id=处理逻辑`">
  处理逻辑
</el-anchor-link>
<el-anchor-link :href="`#/module/Base/category_settings?id=数据查询`">
  数据查询
</el-anchor-link>
<el-anchor-link :href="`#/module/Base/category_settings?id=数据集合`">
  数据集合
</el-anchor-link>
<el-anchor-link :href="`#/module/Base/category_settings?id=数据权限`">
  数据权限
</el-anchor-link>
<el-anchor-link :href="`#/module/Base/category_settings?id=搜索模式`">
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