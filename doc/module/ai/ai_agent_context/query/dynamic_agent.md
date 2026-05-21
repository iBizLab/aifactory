## dynamic_agent(dynamic_agent) <!-- {docsify-ignore-all} -->



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



### 查询条件

(`DEEP_RESEARCH(deep_research)` NOTEQ `'1'` AND `SPEC_KB_ID(规格库标识)` ISNULL AND (`USE_FULLTEXT(使用全文推理)` NOTEQ `'1'` OR `USE_FULLTEXT(使用全文推理)` ISNULL))





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

WHERE ( case when t1."scopes" like '%deep_research%'  and t1."synthesizer" is not null then 1  else 0 end <> 1  AND  t1."spec_kb_id" IS NULL  AND  ( t1."use_fulltext" <> 1  OR  t1."use_fulltext" IS NULL ) )
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