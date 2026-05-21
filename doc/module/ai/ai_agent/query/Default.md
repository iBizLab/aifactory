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
t1.`ACTIVE`,
t1.`AI_MODEL_ID`,
t11.`NAME` AS `AI_MODEL_NAME`,
t1.`CODE_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ENABLE_SUGGESTED_QUESTIONS`,
t1.`ENABLE_THINKING`,
t1.`ENABLE_TOOLS`,
t1.`GENERATION_MODE`,
t1.`ID`,
t1.`IS_DEFAULT`,
t1.`MAX_INPUT_TOKENS`,
t1.`MEMORY_MAX_TURNS`,
t1.`MEMORY_MODE`,
t1.`NAME`,
t1.`SEQUENCE`,
t1.`STREAM`,
t1.`TEMPERATURE`,
t1.`TOOL_MAX_CALLS`,
t1.`TOP_P`,
t1.`TRIMMING_STRATEGY`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_AGENT` t1 
LEFT JOIN `AI_MODEL` t11 ON t1.`AI_MODEL_ID` = t11.`ID` 


```

</el-dialog>

<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t1."active",
t1."agent_group_tag",
t1."ai_model_id",
t11."name" AS "ai_model_name",
t1."code_name",
t1."create_man",
t1."create_time",
t1."enable_searching",
t1."enable_suggested_questions",
t1."enable_thinking",
t1."enable_tools",
t1."generation_mode",
t1."id",
t1."is_default",
t1."kb_mode",
t1."max_input_tokens",
t1."memory_doc_tag",
t1."memory_isolation_mode",
t1."memory_kb_tag",
t1."memory_max_turns",
t1."memory_mode",
t1."name",
t1."publish_skill",
t1."rerank",
t1."rerank_model",
t1."rerank_model_id",
t1."sequence",
t1."similarity_threshold",
t1."skill_load_mode",
t1."stream",
t1."temperature",
t1."tool_max_calls",
t1."top_k",
t1."top_p",
t1."trimming_strategy",
t1."update_man",
t1."update_time",
t1."use_kg",
t1."vector_similarity_weight"
FROM "ai_agent" t1 
LEFT JOIN "ai_model" t11 ON t1."ai_model_id" = t11."id" 


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