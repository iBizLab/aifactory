## 默认（全部数据）(View) <!-- {docsify-ignore-all} -->



<p class="panel-title"><b>查看SQL语句</b></p>
<br>

<el-row>
&nbsp;<el-tag @click="MYSQL5 = true">MYSQL5</el-tag>
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






<el-dialog v-model="MYSQL5" title="MYSQL5">

```sql
SELECT
t11.`CODE_NAME` AS `CONTEXT_CODE_NAME`,
t1.`CONTEXT_ID`,
t11.`NAME` AS `CONTEXT_NAME`,
t11.`SYSTEM_FLAG` AS `CONTEXT_SYSTEM_FLAG`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
case when t11.`SCOPES` like '%deep_research%'  and t11.`SYNTHESIZER` is not null then 1  else 0 end AS `DEEP_RESEARCH`,
t11.`DESCRIPTION`,
t1.`ID`,
t1.`NAME`,
t11.`PAGE_INDEX`,
t11.`SCOPES`,
t11.`SPEC_KB_ID`,
t1.`SYSTEM_FLAG`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USE_TAG`
FROM `AI_AGENT_ASSIGNMENT` t1 
LEFT JOIN `AI_AGENT_CONTEXT` t11 ON t1.`CONTEXT_ID` = t11.`ID` 


```

</el-dialog>

<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t11."code_name" AS "context_code_name",
t1."context_id",
t11."name" AS "context_name",
t11."system_flag" AS "context_system_flag",
t1."create_man",
t1."create_time",
case when t11."scopes" like '%deep_research%'  and t11."synthesizer" is not null then 1  else 0 end AS "deep_research",
t11."description",
t1."id",
t1."name",
t11."page_index",
t11."scopes",
t11."spec_kb_id",
t1."system_flag",
t1."update_man",
t1."update_time",
t11."use_fulltext",
t1."use_tag"
FROM "ai_agent_assignment" t1 
LEFT JOIN "ai_agent_context" t11 ON t1."context_id" = t11."id" 


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