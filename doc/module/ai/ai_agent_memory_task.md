# 智能体记忆任务实例(ai_agent_memory_task)  <!-- {docsify-ignore-all} -->


## 属性
|    中文名col150 | 属性名称col200           | 类型col200     | 长度col100    |允许为空col100    |  备注col500  |
| --------   |------------| -----  | -----  | :----: | -------- |
|智能体业务上下文标识|AI_AGENT_CONTEXT_ID|外键值附加数据|100|是||
|会话标识|CONVERSATION_ID|外键值|100|是||
|会话快照|CONVERSATION_SNAPSHOT|长文本，没有长度限制|16777215|是||
|创建人|CREATE_MAN|文本，可指定长度|100|否||
|创建时间|CREATE_TIME|日期时间型||否||
|记忆存储文档标识|DOC_ID|文本，可指定长度|100|是||
|记忆文档路径|DOC_PATH|长文本，长度1000|2000|是||
|结束时间|END_AT|日期时间型||是||
|执行时间|EXECUTED_AT|日期时间型||是||
|提取内容|EXTRACTED_CONTENT|长文本，没有长度限制|16777215|是||
|标识<sup class="footnote-symbol"><font color=orange>[PK]</font></sup>|ID|全局唯一标识，文本类型，用户不可见|100|否||
|记忆库标识|KB_TAG|文本，可指定长度|100|是||
|最后消息时间|LAST_MSG_TIME|日期时间型||是||
|记忆隔离模式|MEMORY_ISOLATION_MODE|[单项选择(文本值)](index/dictionary_index#memory_isolation_mode "记忆隔离模式")|60|是||
|名称|NAME|文本，可指定长度|200|是||
|执行结果|RESULT|长文本，没有长度限制|16777215|是||
|计划执行时间|SCHEDULED_AT|日期时间型||是||
|记忆业务范围|SCOPE|外键值附加数据|200|是||
|任务状态|STATUS|[单项选择(文本值)](index/dictionary_index#TaskStatus "任务状态")|60|是||
|触发类型|TRIGGER_TYPE|[单项选择(文本值)](index/dictionary_index#trigger_type "触发类型")|60|是||
|更新人|UPDATE_MAN|文本，可指定长度|100|否||
|更新策略|UPDATE_STRATEGY|长文本，没有长度限制|16777215|是||
|更新时间|UPDATE_TIME|日期时间型||否||
|记忆用户标识|USER_ID|外键值附加数据|100|是||


## 关系

<el-row>
<el-tabs v-model="show_der">
<el-tab-pane label="从关系" name="minor">

|  名称col350   | 主实体col200   | 关系类型col200   |    备注col500  |
| -------- |---------- |-----------|----- |
|[DER1N_AI_AGENT_MEMORY_TASK_AI_AGENT_CONVERSATION_CONVERSATION_ID](der/DER1N_AI_AGENT_MEMORY_TASK_AI_AGENT_CONVERSATION_CONVERSATION_ID)|[智能体会话(AI_AGENT_CONVERSATION)](module/ai/ai_agent_conversation)|1:N关系||

</el-tab-pane>
</el-tabs>
</el-row>

## 行为
| 中文名col200    | 代码名col150    | 类型col150    | 事务col100   | 批处理col100   | 附加操作col100  | 插件col150    |  备注col300  |
| -------- |---------- |----------- |:----:|:----:|---------| ----- | ----- |
|CheckKey|CheckKey|内置方法|默认|不支持||||
|Create|Create|内置方法|默认|不支持||||
|提取记忆内容|extract|脚本代码|默认|不支持||||
|Get|Get|内置方法|默认|不支持||||
|GetDraft|GetDraft|内置方法|默认|不支持||||
|Remove|Remove|内置方法|默认|支持||||
|Save|Save|内置方法|默认|不支持||||
|更新状态|update_status|用户扩展更新|默认|不支持||||
|Update|Update|内置方法|默认|不支持||||
|记忆提取并存储|extract_and_store|用户自定义|默认|不支持||[ExtractAndStoreDEActionRuntime](index/plugin_index#ExtractAndStoreDEActionRuntime)||

## 处理逻辑
| 中文名col200    | 代码名col150    | 子类型col150    | 插件col200    |  备注col550  |
| -------- |---------- |----------- |------------|----------|
|[保存记忆分块](module/ai/ai_agent_memory_task/logic/save_chunk)|save_chunk|无|||
|[填充默认文档标识](module/ai/ai_agent_memory_task/logic/fill_default_doc_id)|fill_default_doc_id|无|||
|[更新每日记忆文档](module/ai/ai_agent_memory_task/logic/update_daily_log)|update_daily_log|无|||
|[获取记忆分块](module/ai/ai_agent_memory_task/logic/get_chunk)|get_chunk|无|||
|[获取记忆文档](module/ai/ai_agent_memory_task/logic/get_document)|get_document|无|||
|[记忆提取并存储](module/ai/ai_agent_memory_task/logic/extract_and_store)|extract_and_store|无|||

## 数据查询
| 中文名col200    | 代码名col150    | 默认查询col100 | 权限使用col100 | 自定义SQLcol100 |  备注col600|
| --------  | --------   | :----:  |:----:  | :----:  |----- |
|[DEFAULT](module/ai/ai_agent_memory_task/query/Default)|DEFAULT|是|否 |否 ||
|[默认（全部数据）(VIEW)](module/ai/ai_agent_memory_task/query/View)|VIEW|否|否 |否 ||
|[待执行计划任务(PENDING_SCHEDULED)](module/ai/ai_agent_memory_task/query/pending_scheduled)|PENDING_SCHEDULED|否|否 |否 ||

## 数据集合
| 中文名col200  | 代码名col150  | 类型col100 | 默认集合col100 |   插件col200|   备注col500|
| --------  | --------   | :----:   | :----:   | ----- |----- |
|[DEFAULT](module/ai/ai_agent_memory_task/dataset/Default)|DEFAULT|数据查询|是|||
|[待执行计划任务(PENDING_SCHEDULED)](module/ai/ai_agent_memory_task/dataset/pending_scheduled)|PENDING_SCHEDULED|数据查询|否|||

## 搜索模式
|   搜索表达式col350   |    属性名col200    |    搜索模式col200        |备注col500  |
| -------- |------------|------------|------|
|N_CONVERSATION_ID_EQ|会话标识|EQ||
|N_ID_EQ|标识|EQ||
|N_MEMORY_ISOLATION_MODE_EQ|记忆隔离模式|EQ||
|N_NAME_LIKE|名称|LIKE||
|N_STATUS_EQ|任务状态|EQ||
|N_TRIGGER_TYPE_EQ|触发类型|EQ||

## 界面行为
|  中文名col200 |  代码名col150 |  标题col100   |     处理目标col100   |    处理类型col200        |  备注col500       |
| --------| --------| -------- |------------|------------|------------|
| 记忆提取并存储 | extract_and_store | 记忆提取并存储 |单项数据（主键）|<details><summary>后台调用</summary>[extract](#行为)||

<div style="display: block; overflow: hidden; position: fixed; top: 140px; right: 100px;">

##### 导航
<el-anchor >
<el-anchor-link :href="`#/module/ai/ai_agent_memory_task?id=属性`">
  属性
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_agent_memory_task?id=关系`">
  关系
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_agent_memory_task?id=行为`">
  行为
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_agent_memory_task?id=处理逻辑`">
  处理逻辑
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_agent_memory_task?id=数据查询`">
  数据查询
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_agent_memory_task?id=数据集合`">
  数据集合
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_agent_memory_task?id=搜索模式`">
  搜索模式
</el-anchor-link>
<el-anchor-link :href="`#/module/ai/ai_agent_memory_task?id=界面行为`">
  界面行为
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