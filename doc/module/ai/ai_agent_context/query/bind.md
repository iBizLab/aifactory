## 待绑定(bind) <!-- {docsify-ignore-all} -->



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

* `默认（全部查询列）`




### 查询连接
* **AI_AGENT_ASSIGNMENT不存在1:N（NOT EXISTS (SELECT)）DER1N_AI_AGENT_ASSIGNMENT_AI_AGENT_CONTEXT_CONTEXT_ID**<br>
连接关系：[DER1N_AI_AGENT_ASSIGNMENT_AI_AGENT_CONTEXT_CONTEXT_ID](der/DER1N_AI_AGENT_ASSIGNMENT_AI_AGENT_CONTEXT_CONTEXT_ID)<br>
连接实体：[智能体业务上下文](module/ai/ai_agent_context)<br>
连接条件：(`USE_TAG(引用标记)` EQ `网页请求上下文.use_tag`)<br>




<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t1."active",
t1."agent_group_tag",
t1."ai_agent_id",
t31."name" AS "ai_agent_name",
t1."ai_model_id",
t21."name" AS "ai_model_name",
t1."allow_any_knowledge_base",
t1."code_name",
t1."create_man",
t1."create_time",
case when t1."scopes" like '%deep_research%'  and t1."synthesizer" is not null then 1  else 0 end AS "deep_research",
t1."description",
t1."enable_searching",
t1."enable_suggested_questions",
t1."enable_thinking",
t1."enable_tools",
t1."flow_mode",
t1."generation_mode",
t1."id",
t1."is_default",
t1."kbs",
t1."kb_mode",
t1."max_input_tokens",
t1."memory_doc_tag",
t1."memory_isolation_mode",
t1."memory_kb_tag",
t1."memory_max_turns",
t1."memory_mode",
t1."name",
t1."page_index",
t1."publish_skill",
t1."rerank",
t1."rerank_model",
t1."rerank_model_id",
t1."scopes",
t1."sequence",
t1."similarity_threshold",
t1."skill_load_mode",
t1."spec_kb_id",
t11."name" AS "spec_kb_name",
t1."stream",
t1."synthesizer",
t1."system_flag",
t1."temperature",
t1."tools",
t1."tool_max_calls",
t1."top_k",
t1."top_p",
t1."trimming_strategy",
t1."update_man",
t1."update_time",
t1."use_fulltext",
t1."use_kg",
t1."vector_similarity_weight"
FROM "ai_agent_context" t1 
LEFT JOIN "ai_knowledge_base" t11 ON t1."spec_kb_id" = t11."id" 
LEFT JOIN "ai_model" t21 ON t1."ai_model_id" = t21."id" 
LEFT JOIN "ai_agent" t31 ON t1."ai_agent_id" = t31."id" 

WHERE NOT(EXISTS(SELECT * FROM "ai_agent_assignment" t41 
 WHERE 
 t1."id" = t41."context_id"  AND  ( t41."use_tag" = #{ctx.webcontext.use_tag} ) ))
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