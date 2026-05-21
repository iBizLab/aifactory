# 智能体记忆任务实例(ai_agent_memory_task) :id=ai_agent_memory_task
## 创建智能体记忆任务实例

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_agent_memory_tasks" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`CREATE`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|名称|
|<el-row justify="space-between"><el-col :span="20">kb_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆库标识|
|<el-row justify="space-between"><el-col :span="20">doc_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆存储文档标识|
|<el-row justify="space-between"><el-col :span="20">conversation_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|会话标识|
|<el-row justify="space-between"><el-col :span="20">trigger_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|触发类型|
|<el-row justify="space-between"><el-col :span="20">scheduled_at</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|计划执行时间|
|<el-row justify="space-between"><el-col :span="20">executed_at</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|执行时间|
|<el-row justify="space-between"><el-col :span="20">end_at</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|结束时间|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|任务状态|
|<el-row justify="space-between"><el-col :span="20">conversation_snapshot</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|会话快照|
|<el-row justify="space-between"><el-col :span="20">extracted_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|提取内容|
|<el-row justify="space-between"><el-col :span="20">update_strategy</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|更新策略|
|<el-row justify="space-between"><el-col :span="20">result</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|执行结果|
|<el-row justify="space-between"><el-col :span="20">memory_isolation_mode</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆隔离模式|
|<el-row justify="space-between"><el-col :span="20">user_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆用户标识|
|<el-row justify="space-between"><el-col :span="20">scope</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆业务范围|
|<el-row justify="space-between"><el-col :span="20">doc_path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆文档路径|
|<el-row justify="space-between"><el-col :span="20">last_msg_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|最后消息时间|
|<el-row justify="space-between"><el-col :span="20">ai_agent_context_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能体业务上下文标识|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "kb_tag" : null,
  "doc_id" : null,
  "conversation_id" : null,
  "trigger_type" : null,
  "scheduled_at" : null,
  "executed_at" : null,
  "end_at" : null,
  "status" : null,
  "conversation_snapshot" : null,
  "extracted_content" : null,
  "update_strategy" : null,
  "result" : null,
  "memory_isolation_mode" : null,
  "user_id" : null,
  "scope" : null,
  "doc_path" : null,
  "last_msg_time" : null,
  "ai_agent_context_id" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
}
```


##### 响应示例： {docsify-ignore}
```json

{
  "id" : null,
  "name" : null,
  "kb_tag" : null,
  "doc_id" : null,
  "conversation_id" : null,
  "trigger_type" : null,
  "scheduled_at" : null,
  "executed_at" : null,
  "end_at" : null,
  "status" : null,
  "conversation_snapshot" : null,
  "extracted_content" : null,
  "update_strategy" : null,
  "result" : null,
  "memory_isolation_mode" : null,
  "user_id" : null,
  "scope" : null,
  "doc_path" : null,
  "last_msg_time" : null,
  "ai_agent_context_id" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
}

```

## 获取智能体记忆任务实例

<el-row>
<div style="width: 80px">
<el-alert center title="GET" type="success" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_agent_memory_tasks/{key}" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|标识|




##### 响应示例： {docsify-ignore}
```json

{
  "id" : null,
  "name" : null,
  "kb_tag" : null,
  "doc_id" : null,
  "conversation_id" : null,
  "trigger_type" : null,
  "scheduled_at" : null,
  "executed_at" : null,
  "end_at" : null,
  "status" : null,
  "conversation_snapshot" : null,
  "extracted_content" : null,
  "update_strategy" : null,
  "result" : null,
  "memory_isolation_mode" : null,
  "user_id" : null,
  "scope" : null,
  "doc_path" : null,
  "last_msg_time" : null,
  "ai_agent_context_id" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
}

```

## 删除智能体记忆任务实例

<el-row>
<div style="width: 80px">
<el-alert center title="DELETE" type="error" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_agent_memory_tasks/{key}" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`DELETE`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|标识|





## 更新智能体记忆任务实例

<el-row>
<div style="width: 80px">
<el-alert center title="PUT" type="warning" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_agent_memory_tasks/{key}" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`UPDATE`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|标识|



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|名称|
|<el-row justify="space-between"><el-col :span="20">kb_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆库标识|
|<el-row justify="space-between"><el-col :span="20">doc_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆存储文档标识|
|<el-row justify="space-between"><el-col :span="20">conversation_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|会话标识|
|<el-row justify="space-between"><el-col :span="20">trigger_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|触发类型|
|<el-row justify="space-between"><el-col :span="20">scheduled_at</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|计划执行时间|
|<el-row justify="space-between"><el-col :span="20">executed_at</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|执行时间|
|<el-row justify="space-between"><el-col :span="20">end_at</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|结束时间|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|任务状态|
|<el-row justify="space-between"><el-col :span="20">conversation_snapshot</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|会话快照|
|<el-row justify="space-between"><el-col :span="20">extracted_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|提取内容|
|<el-row justify="space-between"><el-col :span="20">update_strategy</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|更新策略|
|<el-row justify="space-between"><el-col :span="20">result</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|执行结果|
|<el-row justify="space-between"><el-col :span="20">memory_isolation_mode</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆隔离模式|
|<el-row justify="space-between"><el-col :span="20">user_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆用户标识|
|<el-row justify="space-between"><el-col :span="20">scope</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆业务范围|
|<el-row justify="space-between"><el-col :span="20">doc_path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆文档路径|
|<el-row justify="space-between"><el-col :span="20">last_msg_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|最后消息时间|
|<el-row justify="space-between"><el-col :span="20">ai_agent_context_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能体业务上下文标识|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "kb_tag" : null,
  "doc_id" : null,
  "conversation_id" : null,
  "trigger_type" : null,
  "scheduled_at" : null,
  "executed_at" : null,
  "end_at" : null,
  "status" : null,
  "conversation_snapshot" : null,
  "extracted_content" : null,
  "update_strategy" : null,
  "result" : null,
  "memory_isolation_mode" : null,
  "user_id" : null,
  "scope" : null,
  "doc_path" : null,
  "last_msg_time" : null,
  "ai_agent_context_id" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
}
```


##### 响应示例： {docsify-ignore}
```json

{
  "id" : null,
  "name" : null,
  "kb_tag" : null,
  "doc_id" : null,
  "conversation_id" : null,
  "trigger_type" : null,
  "scheduled_at" : null,
  "executed_at" : null,
  "end_at" : null,
  "status" : null,
  "conversation_snapshot" : null,
  "extracted_content" : null,
  "update_strategy" : null,
  "result" : null,
  "memory_isolation_mode" : null,
  "user_id" : null,
  "scope" : null,
  "doc_path" : null,
  "last_msg_time" : null,
  "ai_agent_context_id" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
}

```

## 检查智能体记忆任务实例主键

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_agent_memory_tasks/check_key" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`CREATE`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|名称|
|<el-row justify="space-between"><el-col :span="20">kb_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆库标识|
|<el-row justify="space-between"><el-col :span="20">doc_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆存储文档标识|
|<el-row justify="space-between"><el-col :span="20">conversation_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|会话标识|
|<el-row justify="space-between"><el-col :span="20">trigger_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|触发类型|
|<el-row justify="space-between"><el-col :span="20">scheduled_at</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|计划执行时间|
|<el-row justify="space-between"><el-col :span="20">executed_at</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|执行时间|
|<el-row justify="space-between"><el-col :span="20">end_at</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|结束时间|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|任务状态|
|<el-row justify="space-between"><el-col :span="20">conversation_snapshot</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|会话快照|
|<el-row justify="space-between"><el-col :span="20">extracted_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|提取内容|
|<el-row justify="space-between"><el-col :span="20">update_strategy</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|更新策略|
|<el-row justify="space-between"><el-col :span="20">result</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|执行结果|
|<el-row justify="space-between"><el-col :span="20">memory_isolation_mode</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆隔离模式|
|<el-row justify="space-between"><el-col :span="20">user_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆用户标识|
|<el-row justify="space-between"><el-col :span="20">scope</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆业务范围|
|<el-row justify="space-between"><el-col :span="20">doc_path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆文档路径|
|<el-row justify="space-between"><el-col :span="20">last_msg_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|最后消息时间|
|<el-row justify="space-between"><el-col :span="20">ai_agent_context_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能体业务上下文标识|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "kb_tag" : null,
  "doc_id" : null,
  "conversation_id" : null,
  "trigger_type" : null,
  "scheduled_at" : null,
  "executed_at" : null,
  "end_at" : null,
  "status" : null,
  "conversation_snapshot" : null,
  "extracted_content" : null,
  "update_strategy" : null,
  "result" : null,
  "memory_isolation_mode" : null,
  "user_id" : null,
  "scope" : null,
  "doc_path" : null,
  "last_msg_time" : null,
  "ai_agent_context_id" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
}
```


##### 响应示例： {docsify-ignore}
```json
Integer
```

## 提取记忆内容

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_agent_memory_tasks/{key}/extract" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`UPDATE`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|标识|



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|名称|
|<el-row justify="space-between"><el-col :span="20">kb_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆库标识|
|<el-row justify="space-between"><el-col :span="20">doc_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆存储文档标识|
|<el-row justify="space-between"><el-col :span="20">conversation_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|会话标识|
|<el-row justify="space-between"><el-col :span="20">trigger_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|触发类型|
|<el-row justify="space-between"><el-col :span="20">scheduled_at</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|计划执行时间|
|<el-row justify="space-between"><el-col :span="20">executed_at</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|执行时间|
|<el-row justify="space-between"><el-col :span="20">end_at</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|结束时间|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|任务状态|
|<el-row justify="space-between"><el-col :span="20">conversation_snapshot</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|会话快照|
|<el-row justify="space-between"><el-col :span="20">extracted_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|提取内容|
|<el-row justify="space-between"><el-col :span="20">update_strategy</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|更新策略|
|<el-row justify="space-between"><el-col :span="20">result</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|执行结果|
|<el-row justify="space-between"><el-col :span="20">memory_isolation_mode</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆隔离模式|
|<el-row justify="space-between"><el-col :span="20">user_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆用户标识|
|<el-row justify="space-between"><el-col :span="20">scope</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆业务范围|
|<el-row justify="space-between"><el-col :span="20">doc_path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆文档路径|
|<el-row justify="space-between"><el-col :span="20">last_msg_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|最后消息时间|
|<el-row justify="space-between"><el-col :span="20">ai_agent_context_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能体业务上下文标识|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "kb_tag" : null,
  "doc_id" : null,
  "conversation_id" : null,
  "trigger_type" : null,
  "scheduled_at" : null,
  "executed_at" : null,
  "end_at" : null,
  "status" : null,
  "conversation_snapshot" : null,
  "extracted_content" : null,
  "update_strategy" : null,
  "result" : null,
  "memory_isolation_mode" : null,
  "user_id" : null,
  "scope" : null,
  "doc_path" : null,
  "last_msg_time" : null,
  "ai_agent_context_id" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
}
```



## 记忆提取并存储

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_agent_memory_tasks/{key}/extract_and_store" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`UPDATE`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|标识|



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|名称|
|<el-row justify="space-between"><el-col :span="20">kb_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆库标识|
|<el-row justify="space-between"><el-col :span="20">doc_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆存储文档标识|
|<el-row justify="space-between"><el-col :span="20">conversation_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|会话标识|
|<el-row justify="space-between"><el-col :span="20">trigger_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|触发类型|
|<el-row justify="space-between"><el-col :span="20">scheduled_at</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|计划执行时间|
|<el-row justify="space-between"><el-col :span="20">executed_at</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|执行时间|
|<el-row justify="space-between"><el-col :span="20">end_at</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|结束时间|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|任务状态|
|<el-row justify="space-between"><el-col :span="20">conversation_snapshot</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|会话快照|
|<el-row justify="space-between"><el-col :span="20">extracted_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|提取内容|
|<el-row justify="space-between"><el-col :span="20">update_strategy</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|更新策略|
|<el-row justify="space-between"><el-col :span="20">result</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|执行结果|
|<el-row justify="space-between"><el-col :span="20">memory_isolation_mode</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆隔离模式|
|<el-row justify="space-between"><el-col :span="20">user_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆用户标识|
|<el-row justify="space-between"><el-col :span="20">scope</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆业务范围|
|<el-row justify="space-between"><el-col :span="20">doc_path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆文档路径|
|<el-row justify="space-between"><el-col :span="20">last_msg_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|最后消息时间|
|<el-row justify="space-between"><el-col :span="20">ai_agent_context_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能体业务上下文标识|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "kb_tag" : null,
  "doc_id" : null,
  "conversation_id" : null,
  "trigger_type" : null,
  "scheduled_at" : null,
  "executed_at" : null,
  "end_at" : null,
  "status" : null,
  "conversation_snapshot" : null,
  "extracted_content" : null,
  "update_strategy" : null,
  "result" : null,
  "memory_isolation_mode" : null,
  "user_id" : null,
  "scope" : null,
  "doc_path" : null,
  "last_msg_time" : null,
  "ai_agent_context_id" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
}
```



## 获取智能体记忆任务实例草稿

<el-row>
<div style="width: 80px">
<el-alert center title="GET" type="success" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_agent_memory_tasks/get_draft" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`CREATE`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|名称|
|<el-row justify="space-between"><el-col :span="20">kb_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆库标识|
|<el-row justify="space-between"><el-col :span="20">doc_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆存储文档标识|
|<el-row justify="space-between"><el-col :span="20">conversation_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|会话标识|
|<el-row justify="space-between"><el-col :span="20">trigger_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|触发类型|
|<el-row justify="space-between"><el-col :span="20">scheduled_at</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|计划执行时间|
|<el-row justify="space-between"><el-col :span="20">executed_at</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|执行时间|
|<el-row justify="space-between"><el-col :span="20">end_at</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|结束时间|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|任务状态|
|<el-row justify="space-between"><el-col :span="20">conversation_snapshot</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|会话快照|
|<el-row justify="space-between"><el-col :span="20">extracted_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|提取内容|
|<el-row justify="space-between"><el-col :span="20">update_strategy</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|更新策略|
|<el-row justify="space-between"><el-col :span="20">result</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|执行结果|
|<el-row justify="space-between"><el-col :span="20">memory_isolation_mode</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆隔离模式|
|<el-row justify="space-between"><el-col :span="20">user_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆用户标识|
|<el-row justify="space-between"><el-col :span="20">scope</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆业务范围|
|<el-row justify="space-between"><el-col :span="20">doc_path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆文档路径|
|<el-row justify="space-between"><el-col :span="20">last_msg_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|最后消息时间|
|<el-row justify="space-between"><el-col :span="20">ai_agent_context_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能体业务上下文标识|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "kb_tag" : null,
  "doc_id" : null,
  "conversation_id" : null,
  "trigger_type" : null,
  "scheduled_at" : null,
  "executed_at" : null,
  "end_at" : null,
  "status" : null,
  "conversation_snapshot" : null,
  "extracted_content" : null,
  "update_strategy" : null,
  "result" : null,
  "memory_isolation_mode" : null,
  "user_id" : null,
  "scope" : null,
  "doc_path" : null,
  "last_msg_time" : null,
  "ai_agent_context_id" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
}
```


##### 响应示例： {docsify-ignore}
```json

{
  "id" : null,
  "name" : null,
  "kb_tag" : null,
  "doc_id" : null,
  "conversation_id" : null,
  "trigger_type" : null,
  "scheduled_at" : null,
  "executed_at" : null,
  "end_at" : null,
  "status" : null,
  "conversation_snapshot" : null,
  "extracted_content" : null,
  "update_strategy" : null,
  "result" : null,
  "memory_isolation_mode" : null,
  "user_id" : null,
  "scope" : null,
  "doc_path" : null,
  "last_msg_time" : null,
  "ai_agent_context_id" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
}

```

## 保存智能体记忆任务实例

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_agent_memory_tasks/save" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`CREATE`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|名称|
|<el-row justify="space-between"><el-col :span="20">kb_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆库标识|
|<el-row justify="space-between"><el-col :span="20">doc_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆存储文档标识|
|<el-row justify="space-between"><el-col :span="20">conversation_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|会话标识|
|<el-row justify="space-between"><el-col :span="20">trigger_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|触发类型|
|<el-row justify="space-between"><el-col :span="20">scheduled_at</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|计划执行时间|
|<el-row justify="space-between"><el-col :span="20">executed_at</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|执行时间|
|<el-row justify="space-between"><el-col :span="20">end_at</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|结束时间|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|任务状态|
|<el-row justify="space-between"><el-col :span="20">conversation_snapshot</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|会话快照|
|<el-row justify="space-between"><el-col :span="20">extracted_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|提取内容|
|<el-row justify="space-between"><el-col :span="20">update_strategy</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|更新策略|
|<el-row justify="space-between"><el-col :span="20">result</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|执行结果|
|<el-row justify="space-between"><el-col :span="20">memory_isolation_mode</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆隔离模式|
|<el-row justify="space-between"><el-col :span="20">user_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆用户标识|
|<el-row justify="space-between"><el-col :span="20">scope</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆业务范围|
|<el-row justify="space-between"><el-col :span="20">doc_path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆文档路径|
|<el-row justify="space-between"><el-col :span="20">last_msg_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|最后消息时间|
|<el-row justify="space-between"><el-col :span="20">ai_agent_context_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能体业务上下文标识|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "kb_tag" : null,
  "doc_id" : null,
  "conversation_id" : null,
  "trigger_type" : null,
  "scheduled_at" : null,
  "executed_at" : null,
  "end_at" : null,
  "status" : null,
  "conversation_snapshot" : null,
  "extracted_content" : null,
  "update_strategy" : null,
  "result" : null,
  "memory_isolation_mode" : null,
  "user_id" : null,
  "scope" : null,
  "doc_path" : null,
  "last_msg_time" : null,
  "ai_agent_context_id" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
}
```


##### 响应示例： {docsify-ignore}
```json

{
  "id" : null,
  "name" : null,
  "kb_tag" : null,
  "doc_id" : null,
  "conversation_id" : null,
  "trigger_type" : null,
  "scheduled_at" : null,
  "executed_at" : null,
  "end_at" : null,
  "status" : null,
  "conversation_snapshot" : null,
  "extracted_content" : null,
  "update_strategy" : null,
  "result" : null,
  "memory_isolation_mode" : null,
  "user_id" : null,
  "scope" : null,
  "doc_path" : null,
  "last_msg_time" : null,
  "ai_agent_context_id" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
}

```

## DEFAULT

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_agent_memory_tasks/fetch_default" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_conversation_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|会话标识|
|<el-row justify="space-between"><el-col :span="20">n_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标识|
|<el-row justify="space-between"><el-col :span="20">n_memory_isolation_mode_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆隔离模式|
|<el-row justify="space-between"><el-col :span="20">n_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|名称|
|<el-row justify="space-between"><el-col :span="20">n_status_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|任务状态|
|<el-row justify="space-between"><el-col :span="20">n_trigger_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|触发类型|



##### 请求示例： {docsify-ignore}
```json
{
  "page" : 0,
  "size" : 20,
  "sort" : null,
  "n_conversation_id_eq" : null,
  "n_id_eq" : null,
  "n_memory_isolation_mode_eq" : null,
  "n_name_like" : null,
  "n_status_eq" : null,
  "n_trigger_type_eq" : null,
}
```


##### 响应示例： {docsify-ignore}
```json
[
  {
    "id" : null,
    "name" : null,
    "kb_tag" : null,
    "doc_id" : null,
    "conversation_id" : null,
    "trigger_type" : null,
    "scheduled_at" : null,
    "executed_at" : null,
    "end_at" : null,
    "status" : null,
    "conversation_snapshot" : null,
    "extracted_content" : null,
    "update_strategy" : null,
    "result" : null,
    "memory_isolation_mode" : null,
    "user_id" : null,
    "scope" : null,
    "doc_path" : null,
    "last_msg_time" : null,
    "ai_agent_context_id" : null,
    "create_man" : null,
    "create_time" : null,
    "update_man" : null,
    "update_time" : null,
  }
]
```

## 待执行计划任务

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_agent_memory_tasks/fetch_pending_scheduled" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_conversation_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|会话标识|
|<el-row justify="space-between"><el-col :span="20">n_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标识|
|<el-row justify="space-between"><el-col :span="20">n_memory_isolation_mode_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|记忆隔离模式|
|<el-row justify="space-between"><el-col :span="20">n_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|名称|
|<el-row justify="space-between"><el-col :span="20">n_status_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|任务状态|
|<el-row justify="space-between"><el-col :span="20">n_trigger_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|触发类型|



##### 请求示例： {docsify-ignore}
```json
{
  "page" : 0,
  "size" : 20,
  "sort" : null,
  "n_conversation_id_eq" : null,
  "n_id_eq" : null,
  "n_memory_isolation_mode_eq" : null,
  "n_name_like" : null,
  "n_status_eq" : null,
  "n_trigger_type_eq" : null,
}
```


##### 响应示例： {docsify-ignore}
```json
[
  {
    "id" : null,
    "name" : null,
    "kb_tag" : null,
    "doc_id" : null,
    "conversation_id" : null,
    "trigger_type" : null,
    "scheduled_at" : null,
    "executed_at" : null,
    "end_at" : null,
    "status" : null,
    "conversation_snapshot" : null,
    "extracted_content" : null,
    "update_strategy" : null,
    "result" : null,
    "memory_isolation_mode" : null,
    "user_id" : null,
    "scope" : null,
    "doc_path" : null,
    "last_msg_time" : null,
    "ai_agent_context_id" : null,
    "create_man" : null,
    "create_time" : null,
    "update_man" : null,
    "update_time" : null,
  }
]
```



## 下载导入模板
<el-row>
<div style="width: 80px">
<el-alert center title="GET" type="success" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_agent_memory_tasks/importtemplate" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 查询参数 {docsify-ignore}

|字段col300|类型col150|备注col400|
|---|---|----|
| srfimporttag | String | 导入标识 |



## 数据导出

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_agent_memory_tasks/exportdata/{param},/ai_agent_memory_tasks/exportdata/{param}/{key}" type="info" :closable="false" ></el-alert>
</div>
</el-row>

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|param|String|导出集合方法名称|
|key|String|数据主键|

##### 查询参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|srfexporttag|String|导出模板标识|

##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|page|Integer|page|
|size|Integer|分页大小|
|n_xxx_eq|String|过滤参数|


## 数据导入

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_agent_memory_tasks/importdata" type="info" :closable="false" ></el-alert>
</div>
</el-row>

##### 查询参数 {docsify-ignore}

|字段col300|类型col150|备注col400|
|---|---|----|
| srfimporttag | String | 导入标识 |

##### 请求参数 {docsify-ignore}

|字段col300|类型col150|备注col400|
|---|---|----|
| file | file | 导入数据文具 |

## 数据导入（返回错误excel）

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_agent_memory_tasks/importdata2" type="info" :closable="false" ></el-alert>
</div>
</el-row>

##### 查询参数 {docsify-ignore}

|字段col300|类型col150|备注col400|
|---|---|----|
| srfimporttag | String | 导入标识 |

##### 请求参数 {docsify-ignore}

|字段col300|类型col150|备注col400|
|---|---|----|
| file | file | 导入数据文具 |

## 自定义表头导入（异步）
<el-row>
<div style="width: 80px">
<el-alert center title="GET" type="success" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_agent_memory_tasks/asyncimportdata2" type="info" :closable="false" ></el-alert>
</div>
</el-row>

##### 查询参数 {docsify-ignore}

|字段col300|类型col150|备注col400|
|---|---|----|
| srfimporttag | String | 导入标识 |
| srfossfileid | String | 导入文件 |
| srfimportschemaid | String | 表头定义 |


## 数据打印
<el-row>
<div style="width: 80px">
<el-alert center title="GET" type="success" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_agent_memory_tasks/printdata/{key}" type="info" :closable="false" ></el-alert>
</div>
</el-row>

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|数据主键|

##### 查询参数 {docsify-ignore}

|字段col300|类型col150|备注col400|
|---|---|----|
| srfprinttag | String | 打印标识 |
| srfcontenttype | String | 打印类型 |



## 报表打印

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_agent_memory_tasks/report" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 查询参数 {docsify-ignore}

|字段col300|类型col150|备注col400|
|---|---|----|
| srfreporttag | String | 报表标识 |
| srfcontenttype | String | 报表类型 |




<script>
 const { createApp } = Vue
  createApp({
    data() {
      return {

      }
    },
    methods: {

    }
  }).use(ElementPlus).mount('#app')
</script>