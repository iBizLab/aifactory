## DEFAULT(Default) <!-- {docsify-ignore-all} -->



<p class="panel-title"><b>查看SQL语句</b></p>
<br>

<el-row>
&nbsp;<el-tag @click="MYSQL5 = true">MYSQL5</el-tag>
&nbsp;<el-tag @click="POSTGRESQL = true">POSTGRESQL</el-tag>
</el-row>

<br>
<p class="panel-title"><b>是否默认查询</b></p>

* `是`

<p class="panel-title"><b>是否权限使用</b></p>

* `否`

<p class="panel-title"><b>是否自定义SQL</b></p>

* `否`

<p class="panel-title"><b>查询列级别</b></p>

* `默认（全部查询列）`






<el-dialog v-model="MYSQL5" title="MYSQL5">

```sql
SELECT
t1.`AI_AGENT_CONTEXT_ID`,
t11.`NAME` AS `AI_AGENT_CONTEXT_NAME`,
t11.`AI_AGENT_ID`,
t21.`NAME` AS `AI_AGENT_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`IS_TOP`,
t1.`NAME`,
t1.`SEQUENCE`,
t1.`SESSION_ID`,
t1.`STATUS`,
t1.`TITLE`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_ID`
FROM `AI_AGENT_CONVERSATION` t1 
LEFT JOIN `AI_AGENT_CONTEXT` t11 ON t1.`AI_AGENT_CONTEXT_ID` = t11.`ID` 
LEFT JOIN `AI_AGENT` t21 ON t11.`AI_AGENT_ID` = t21.`ID` 


```

</el-dialog>

<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t11."name" AS "agent_context_name",
t1."ai_agent_context_id",
t1."create_man",
t1."create_time",
t1."id",
t1."is_top",
(SELECT MAX(m.create_time) FROM AI_AGENT_MESSAGE m LEFT JOIN AI_AGENT_CONVERSATION conv ON m.conversation_id = conv.id WHERE conv.id = t1."id") AS "last_active_at",
t1."name",
t1."scope",
t1."sequence",
t1."session_id",
case when t1."title" is null then t11."name" else t1."title" end AS "show_name",
t1."status",
t1."title",
t1."type",
t1."update_man",
t1."update_time",
t1."user_id"
FROM "ai_agent_conversation" t1 
LEFT JOIN "ai_agent_context" t11 ON t1."ai_agent_context_id" = t11."id" 


```

</el-dialog>

<script>
 const { createApp } = Vue
  createApp({
    data() {
      return {
                MYSQL5 : false
                POSTGRESQL : false
        
      }
    },
    methods: {
    }
  }).use(ElementPlus).mount('#app')
</script>