## 默认（全部数据）(View) <!-- {docsify-ignore-all} -->



<p class="panel-title"><b>查看SQL语句</b></p>
<br>

<el-row>
&nbsp;<el-tag @click="POSTGRESQL = true">POSTGRESQL</el-tag>
</el-row>

<br>
<p class="panel-title"><b>是否默认查询</b></p>

* `否`

<p class="panel-title"><b>是否权限使用</b></p>

* `否`

<p class="panel-title"><b>是否自定义SQL</b></p>

* `否`

<p class="panel-title"><b>查询列级别</b></p>

* `全部数据`

> [!ATTENTION|label:存在长文本属性]
>
> `CONVERSATION_SNAPSHOT(会话快照)`
>
> `EXTRACTED_CONTENT(提取内容)`
>
> `RESULT(执行结果)`
>
> `UPDATE_STRATEGY(更新策略)`






<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t11."ai_agent_context_id",
t1."conversation_id",
t1."conversation_snapshot",
t1."create_man",
t1."create_time",
t1."doc_id",
t1."doc_path",
t1."end_at",
t1."executed_at",
t1."extracted_content",
t1."id",
t1."kb_tag",
t1."last_msg_time",
t1."memory_isolation_mode",
t1."name",
t1."result",
t1."scheduled_at",
t11."scope",
t1."status",
t1."trigger_type",
t1."update_man",
t1."update_strategy",
t1."update_time",
t11."user_id"
FROM "ai_agent_memory_task" t1 
LEFT JOIN "ai_agent_conversation" t11 ON t1."conversation_id" = t11."id" 


```

</el-dialog>

<script>
 const { createApp } = Vue
  createApp({
    data() {
      return {
                POSTGRESQL : false
        
      }
    },
    methods: {
    }
  }).use(ElementPlus).mount('#app')
</script>