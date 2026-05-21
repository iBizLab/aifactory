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

> [!ATTENTION|label:存在长文本属性]
>
> `CONTEXT_DEBUG_DATA(调试数据)`
>
> `CUSTOM_CODE(自定义代码)`
>
> `CUSTOM_SUGGESTION_PROMPT(自定义建议提示词)`
>
> `DEFAULT_SYSTEM_PROMPT(默认系统提示词)`
>
> `SKILL_PROMPT(技能提示词)`
>
> `SKILL_README(技能说明)`
>
> `SKILL_TAGS(激活技能标记)`
>
> `TOOL_EXCEED_MESSAGE(工具调用超限提示语)`
>
> `VLM_PROMPT(视觉识别提示词)`
>
> `WELCOME_MESSAGE(欢迎消息模板)`






<el-dialog v-model="MYSQL5" title="MYSQL5">

```sql
SELECT
t1.`ACTIVE`,
t1.`AI_AGENT_ID`,
t21.`NAME` AS `AI_AGENT_NAME`,
t1.`AI_MODEL_ID`,
t11.`NAME` AS `AI_MODEL_NAME`,
t1.`CODE_NAME`,
t1.`CONTEXT_DEBUG_DATA`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`CUSTOM_SUGGESTION_PROMPT`,
t1.`DEFAULT_SYSTEM_PROMPT`,
t1.`DESCRIPTION`,
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
t1.`SCOPES`,
t1.`SEQUENCE`,
t1.`STREAM`,
t1.`SUGGESTED_QUESTIONS`,
t1.`SYSTEM_FLAG`,
t1.`TEMPERATURE`,
t1.`TOOL_EXCEED_MESSAGE`,
t1.`TOOL_MAX_CALLS`,
t1.`TOP_P`,
t1.`TRIMMING_STRATEGY`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`WELCOME_MESSAGE`
FROM `AI_AGENT_CONTEXT` t1 
LEFT JOIN `AI_MODEL` t11 ON t1.`AI_MODEL_ID` = t11.`ID` 
LEFT JOIN `AI_AGENT` t21 ON t1.`AI_AGENT_ID` = t21.`ID` 


```

</el-dialog>

<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t1."active",
t1."agent_group_tag",
t1."ai_agent_id",
t1."ai_agent_knowledge_rels",
t31."name" AS "ai_agent_name",
t1."ai_model_id",
t21."name" AS "ai_model_name",
t1."allow_any_knowledge_base",
t1."code_name",
t1."context_debug_data",
t1."create_man",
t1."create_time",
t1."custom_code",
t1."custom_suggestion_prompt",
case when t1."scopes" like '%deep_research%'  and t1."synthesizer" is not null then 1  else 0 end AS "deep_research",
t1."default_system_prompt",
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
t1."skill_prompt",
t1."skill_readme",
t1."skill_tags",
t1."spec_kb_id",
t11."name" AS "spec_kb_name",
t1."stream",
t1."suggested_questions",
t1."synthesizer",
t1."system_flag",
t1."temperature",
t1."tools",
t1."tool_exceed_message",
t1."tool_max_calls",
t1."top_k",
t1."top_p",
t1."trimming_strategy",
t1."update_man",
t1."update_time",
t1."use_fulltext",
t1."use_kg",
t1."vector_similarity_weight",
t1."vlm_prompt",
t1."welcome_message"
FROM "ai_agent_context" t1 
LEFT JOIN "ai_knowledge_base" t11 ON t1."spec_kb_id" = t11."id" 
LEFT JOIN "ai_model" t21 ON t1."ai_model_id" = t21."id" 
LEFT JOIN "ai_agent" t31 ON t1."ai_agent_id" = t31."id" 


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