# POSTGRESQL <!-- {docsify-ignore-all} -->

## [活动(ACTIVITY)](module/Base/activity.md) :id=activity

#### 数据查询(DEFAULT) :id=activity-Default
```sql
SELECT
t1."audittype",
t1."create_man",
t1."create_time",
t1."id",
t1."ipaddress",
t1."name",
t1."objectid",
t1."objecttype",
t1."oppersonid",
t1."oppersonname",
t1."update_man",
t1."update_time"
FROM "activity" t1 

```

#### 默认（全部数据）(VIEW) :id=activity-View
```sql
SELECT
t1."auditinfo",
t1."audittype",
t1."create_man",
t1."create_time",
t1."id",
t1."ipaddress",
t1."name",
t1."objectid",
t1."objecttype",
t1."oppersonid",
t1."oppersonname",
t1."update_man",
t1."update_time"
FROM "activity" t1 

```


## [智能体(AI_AGENT)](module/ai/ai_agent.md) :id=ai_agent

#### DEFAULT :id=ai_agent-Default
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

#### 默认（全部数据）(VIEW) :id=ai_agent-View
```sql
SELECT
t1."active",
t1."agent_group_tag",
t1."ai_model_id",
t11."name" AS "ai_model_name",
t1."code_name",
t1."create_man",
t1."create_time",
t1."custom_suggestion_prompt",
t1."default_system_prompt",
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
t1."skill_prompt",
t1."skill_tags",
t1."stream",
t1."suggested_questions",
t1."temperature",
t1."tool_exceed_message",
t1."tool_max_calls",
t1."top_k",
t1."top_p",
t1."trimming_strategy",
t1."update_man",
t1."update_time",
t1."use_kg",
t1."vector_similarity_weight",
t1."vlm_prompt",
t1."welcome_message"
FROM "ai_agent" t1 
LEFT JOIN "ai_model" t11 ON t1."ai_model_id" = t11."id" 

```


## [智能体分配(AI_AGENT_ASSIGNMENT)](module/ai/ai_agent_assignment.md) :id=ai_agent_assignment

#### DEFAULT :id=ai_agent_assignment-Default
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

#### 系统的(System) :id=ai_agent_assignment-System
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

WHERE ( ( t1."system_flag" = 1  OR  t11."system_flag" = 1 ) )
```

#### 默认（全部数据）(VIEW) :id=ai_agent_assignment-View
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

#### bind :id=ai_agent_assignment-bind
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


## [智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context.md) :id=ai_agent_context

#### DEFAULT :id=ai_agent_context-Default
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

```

#### 默认（全部数据）(VIEW) :id=ai_agent_context-View
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

#### 待绑定(bind) :id=ai_agent_context-bind
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

#### deep_research_agent :id=ai_agent_context-deep_research_agent
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

WHERE ( case when t1."scopes" like '%deep_research%'  and t1."synthesizer" is not null then 1  else 0 end = 1 )
```

#### dynamic_agent :id=ai_agent_context-dynamic_agent
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

#### 业务过滤(filter) :id=ai_agent_context-filter
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

WHERE ( ( t1."scopes" IS NULL ) )
```

#### flow智能体(flow_agents) :id=ai_agent_context-flow_agents
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

WHERE ( t1."flow_mode" = 'DE' )
```

#### full_text_agent :id=ai_agent_context-full_text_agent
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

WHERE ( t1."use_fulltext" = 1 )
```

#### hub智能体(hub_agents) :id=ai_agent_context-hub_agents
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

WHERE ( t1."flow_mode" = 'HUB' )
```

#### lookup_agent :id=ai_agent_context-lookup_agent
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

WHERE ( t1."spec_kb_id" IS NOT NULL )
```

#### skill智能体(skill_agents) :id=ai_agent_context-skill_agents
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

WHERE ( ( t1."publish_skill" = 1 ) )
```

#### 系统的(system) :id=ai_agent_context-system
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

WHERE ( t1."system_flag" = 1 )
```


## [智能体会话(AI_AGENT_CONVERSATION)](module/ai/ai_agent_conversation.md) :id=ai_agent_conversation

#### DEFAULT :id=ai_agent_conversation-Default
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

#### 默认（全部数据）(VIEW) :id=ai_agent_conversation-View
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

#### 有效会话(active) :id=ai_agent_conversation-active
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

WHERE ( ( t1."status" = 'active'  OR  t1."status" = 'paused' ) )
```

#### 当前用户会话(cur_user_active) :id=ai_agent_conversation-cur_user_active
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

WHERE ( ( t1."status" = 'active'  OR  t1."status" = 'paused' )  AND  t1."user_id" = #{ctx.sessioncontext.srfpersonid}  AND  t1."type" = 'topic' )
```


## [智能体回复反馈(AI_AGENT_FEEDBACK)](module/ai/ai_agent_feedback.md) :id=ai_agent_feedback

#### DEFAULT :id=ai_agent_feedback-Default
```sql
SELECT
t1."conversation_id",
t1."create_man",
t1."create_time",
t1."feedback_content",
t1."feedback_type",
t1."id",
t1."message_id",
t1."name",
t1."update_man",
t1."update_time",
t1."user_id"
FROM "ai_agent_feedback" t1 

```

#### 默认（全部数据）(VIEW) :id=ai_agent_feedback-View
```sql
SELECT
t1."conversation_id",
t1."create_man",
t1."create_time",
t1."feedback_content",
t1."feedback_type",
t1."id",
t1."message_id",
t1."name",
t1."update_man",
t1."update_time",
t1."user_id"
FROM "ai_agent_feedback" t1 

```


## [智能体知识库引用(AI_AGENT_KNOWLEDGE_REL)](module/ai/ai_agent_knowledge_rel.md) :id=ai_agent_knowledge_rel

#### DEFAULT :id=ai_agent_knowledge_rel-Default
```sql
SELECT
t1."ai_agent_id",
t21."name" AS "ai_agent_name",
t1."ai_knowledge_base_id",
t11."name" AS "ai_knowledge_base_name",
t1."create_man",
t1."create_time",
t1."id",
t1."name",
t1."update_man",
t1."update_time"
FROM "ai_agent_knowledge_rel" t1 
LEFT JOIN "ai_knowledge_base" t11 ON t1."ai_knowledge_base_id" = t11."id" 
LEFT JOIN "ai_agent" t21 ON t1."ai_agent_id" = t21."id" 

```

#### 默认（全部数据）(VIEW) :id=ai_agent_knowledge_rel-View
```sql
SELECT
t1."ai_agent_id",
t21."name" AS "ai_agent_name",
t1."ai_knowledge_base_id",
t11."name" AS "ai_knowledge_base_name",
t1."create_man",
t1."create_time",
t1."id",
t1."name",
t1."update_man",
t1."update_time"
FROM "ai_agent_knowledge_rel" t1 
LEFT JOIN "ai_knowledge_base" t11 ON t1."ai_knowledge_base_id" = t11."id" 
LEFT JOIN "ai_agent" t21 ON t1."ai_agent_id" = t21."id" 

```


## [智能体记忆任务实例(AI_AGENT_MEMORY_TASK)](module/ai/ai_agent_memory_task.md) :id=ai_agent_memory_task

#### DEFAULT :id=ai_agent_memory_task-Default
```sql
SELECT
t11."ai_agent_context_id",
t1."conversation_id",
t1."create_man",
t1."create_time",
t1."doc_id",
t1."doc_path",
t1."end_at",
t1."executed_at",
t1."id",
t1."kb_tag",
t1."last_msg_time",
t1."memory_isolation_mode",
t1."name",
t1."scheduled_at",
t11."scope",
t1."status",
t1."trigger_type",
t1."update_man",
t1."update_time",
t11."user_id"
FROM "ai_agent_memory_task" t1 
LEFT JOIN "ai_agent_conversation" t11 ON t1."conversation_id" = t11."id" 

```

#### 默认（全部数据）(VIEW) :id=ai_agent_memory_task-View
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

#### 待执行计划任务(PENDING_SCHEDULED) :id=ai_agent_memory_task-pending_scheduled
```sql
SELECT
t11."ai_agent_context_id",
t1."conversation_id",
t1."create_man",
t1."create_time",
t1."doc_id",
t1."doc_path",
t1."end_at",
t1."executed_at",
t1."id",
t1."kb_tag",
t1."last_msg_time",
t1."memory_isolation_mode",
t1."name",
t1."scheduled_at",
t11."scope",
t1."status",
t1."trigger_type",
t1."update_man",
t1."update_time",
t11."user_id"
FROM "ai_agent_memory_task" t1 
LEFT JOIN "ai_agent_conversation" t11 ON t1."conversation_id" = t11."id" 

WHERE ( t1."trigger_type" = 'SCHEDULED'  AND  t1."status" = 'PENDING' )
```


## [智能体会话消息(AI_AGENT_MESSAGE)](module/ai/ai_agent_message.md) :id=ai_agent_message

#### DEFAULT :id=ai_agent_message-Default
```sql
SELECT
t1."content_type",
t1."conversation_id",
t11."name" AS "conversation_name",
t11."title" AS "conversation_title",
t1."create_man",
t1."create_time",
t1."id",
(select count(1) from ai_agent_feedback t where t.user_id=#{ctx.sessioncontext.srfuserid} and t.message_id=t1."id" and t.feedback_type='dislike') AS "is_dislike",
(select count(1) from ai_agent_feedback t where t.user_id=#{ctx.sessioncontext.srfuserid} and t.message_id=t1."id" and t.feedback_type='like') AS "is_like",
t1."name",
t1."sender_type",
t1."sequence",
t11."session_id",
t1."status",
t1."update_man",
t1."update_time",
t11."user_id"
FROM "ai_agent_message" t1 
LEFT JOIN "ai_agent_conversation" t11 ON t1."conversation_id" = t11."id" 

```

#### 默认（全部数据）(VIEW) :id=ai_agent_message-View
```sql
SELECT
t1."content",
t1."content_type",
t1."conversation_id",
t11."name" AS "conversation_name",
t11."title" AS "conversation_title",
t1."create_man",
t1."create_time",
t1."id",
(select count(1) from ai_agent_feedback t where t.user_id=#{ctx.sessioncontext.srfuserid} and t.message_id=t1."id" and t.feedback_type='dislike') AS "is_dislike",
(select count(1) from ai_agent_feedback t where t.user_id=#{ctx.sessioncontext.srfuserid} and t.message_id=t1."id" and t.feedback_type='like') AS "is_like",
t1."metadata",
t1."name",
t1."sender_type",
t1."sequence",
t11."session_id",
t1."status",
t1."update_man",
t1."update_time",
t11."user_id"
FROM "ai_agent_message" t1 
LEFT JOIN "ai_agent_conversation" t11 ON t1."conversation_id" = t11."id" 

```


## [智能体工具引用(AI_AGENT_TOOL_REL)](module/ai/ai_agent_tool_rel.md) :id=ai_agent_tool_rel

#### DEFAULT :id=ai_agent_tool_rel-Default
```sql
SELECT
t1."ai_agent_id",
t21."name" AS "ai_agent_name",
t1."ai_tool_id",
t11."name" AS "ai_tool_name",
t1."create_man",
t1."create_time",
t1."id",
t1."name",
t11."tool_tag",
t11."tool_type",
t1."update_man",
t1."update_time"
FROM "ai_agent_tool_rel" t1 
LEFT JOIN "ai_tool" t11 ON t1."ai_tool_id" = t11."id" 
LEFT JOIN "ai_agent" t21 ON t1."ai_agent_id" = t21."id" 

```

#### 默认（全部数据）(VIEW) :id=ai_agent_tool_rel-View
```sql
SELECT
t1."ai_agent_id",
t21."name" AS "ai_agent_name",
t1."ai_tool_id",
t11."name" AS "ai_tool_name",
t1."create_man",
t1."create_time",
t1."id",
t1."name",
t11."tool_tag",
t11."tool_type",
t1."update_man",
t1."update_time"
FROM "ai_agent_tool_rel" t1 
LEFT JOIN "ai_tool" t11 ON t1."ai_tool_id" = t11."id" 
LEFT JOIN "ai_agent" t21 ON t1."ai_agent_id" = t21."id" 

```


## [AI客户端凭证(AI_CLIENT_CREDENTIAL)](module/ai/ai_client_credential.md) :id=ai_client_credential

#### DEFAULT :id=ai_client_credential-Default
```sql
SELECT
t1."access_strategy",
t1."access_types",
t1."active",
t1."create_man",
t1."create_time",
t1."description",
t1."expiration_date",
t1."id",
t1."name",
t1."update_man",
t1."update_time",
t1."user_id"
FROM "ai_client_credential" t1 

```

#### 默认（全部数据）(VIEW) :id=ai_client_credential-View
```sql
SELECT
t1."access_key",
t1."access_strategy",
t1."access_types",
t1."active",
t1."create_man",
t1."create_time",
t1."description",
t1."expiration_date",
t1."id",
t1."name",
t1."update_man",
t1."update_time",
t1."user_id"
FROM "ai_client_credential" t1 

```

#### my :id=ai_client_credential-my
```sql
SELECT
t1."access_strategy",
t1."access_types",
t1."active",
t1."create_man",
t1."create_time",
t1."description",
t1."expiration_date",
t1."id",
t1."name",
t1."update_man",
t1."update_time",
t1."user_id"
FROM "ai_client_credential" t1 

WHERE ( t1."user_id" = #{ctx.sessioncontext.srfpersonid} )
```


## [AI凭证(AI_CREDENTIAL)](module/ai/ai_credential.md) :id=ai_credential

#### DEFAULT :id=ai_credential-Default
```sql
SELECT
t1."active",
t1."api_key",
t1."client_id",
t1."code_name",
t1."create_man",
t1."create_time",
t1."credential_type",
t1."description",
t1."id",
t1."name",
t1."provider",
t1."region",
t1."scope",
t1."token_url",
t1."update_man",
t1."update_time"
FROM "ai_credential" t1 

```

#### 默认（全部数据）(VIEW) :id=ai_credential-View
```sql
SELECT
t1."access_key",
t1."active",
t1."api_key",
t1."bearer_token",
t1."client_id",
t1."client_secret",
t1."code_name",
t1."create_man",
t1."create_time",
t1."credential_type",
t1."description",
t1."id",
t1."name",
t1."provider",
t1."region",
t1."scope",
t1."secret_key",
t1."token_url",
t1."update_man",
t1."update_time"
FROM "ai_credential" t1 

```


## [知识库文档分块(AI_KB_CHUNK)](module/ai/ai_kb_chunk.md) :id=ai_kb_chunk

#### DEFAULT :id=ai_kb_chunk-Default
```sql
SELECT
t1."active",
t11."categories",
t1."chunk_type",
t1."content",
t1."content_preview",
t1."create_man",
t1."create_time",
t1."document_id",
t11."name" AS "document_name",
t11."sequence" AS "document_sequence",
t11."type" AS "document_type",
t11."file" AS "doc_file",
t11."name" AS "doc_name",
t11."parsed_content" AS "doc_parsed_content",
t1."id",
t11."kb_id",
t21."name" AS "kb_name",
t1."keywords",
t1."key_questions",
t1."meta_data",
t1."name",
t1."path",
t1."pid",
t1."positions",
t1."sequence",
t1."source_count",
t1."source_indices",
t1."tags",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "ai_kb_chunk" t1 
LEFT JOIN "ai_kb_document" t11 ON t1."document_id" = t11."id" 
LEFT JOIN "ai_knowledge_base" t21 ON t11."kb_id" = t21."id" 

```

#### 默认（全部数据）(VIEW) :id=ai_kb_chunk-View
```sql
SELECT
t1."active",
t11."categories",
t1."chunk_type",
t1."content",
t1."content_preview",
t1."create_man",
t1."create_time",
t1."document_id",
t11."name" AS "document_name",
t11."sequence" AS "document_sequence",
t11."type" AS "document_type",
t11."file" AS "doc_file",
t11."name" AS "doc_name",
t11."parsed_content" AS "doc_parsed_content",
t1."id",
t11."kb_id",
t21."name" AS "kb_name",
t1."keywords",
t1."key_questions",
t1."meta_data",
t1."name",
t1."path",
t1."pid",
t1."positions",
t1."sequence",
t1."source_count",
t1."source_indices",
t1."tags",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "ai_kb_chunk" t1 
LEFT JOIN "ai_kb_document" t11 ON t1."document_id" = t11."id" 
LEFT JOIN "ai_knowledge_base" t21 ON t11."kb_id" = t21."id" 

```

#### reader :id=ai_kb_chunk-reader
```sql
SELECT
t1."active",
t11."categories",
t1."chunk_type",
t1."content",
t1."content_preview",
t1."create_man",
t1."create_time",
t1."document_id",
t11."name" AS "document_name",
t11."sequence" AS "document_sequence",
t11."type" AS "document_type",
t11."file" AS "doc_file",
t11."name" AS "doc_name",
t1."id",
t11."kb_id",
t21."name" AS "kb_name",
t1."keywords",
t1."key_questions",
t1."meta_data",
t1."name",
t1."path",
t1."pid",
t1."positions",
t1."sequence",
t1."source_count",
t1."tags",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "ai_kb_chunk" t1 
LEFT JOIN "ai_kb_document" t11 ON t1."document_id" = t11."id" 
LEFT JOIN "ai_knowledge_base" t21 ON t11."kb_id" = t21."id" 

WHERE ( ( t21."visibility" = 'public'  OR  ( t21."scope_type" = 'organization'  AND  t21."scope_id" = #{ctx.sessioncontext.srforgid} )  OR  EXISTS(SELECT 1 FROM AI_KB_MEMBER m 
 WHERE 
 t21.ID = m.KB_ID  AND  ( m.USER_ID = #{ctx.sessioncontext.srfpersonid} ) ) ) )
```

#### 指定知识库(specified_kb) :id=ai_kb_chunk-specified_kb
```sql
SELECT
t1."active",
t11."categories",
t1."chunk_type",
t1."content",
t1."content_preview",
t1."create_man",
t1."create_time",
t1."document_id",
t11."name" AS "document_name",
t11."sequence" AS "document_sequence",
t11."type" AS "document_type",
t11."file" AS "doc_file",
t11."name" AS "doc_name",
t1."id",
t11."kb_id",
t21."name" AS "kb_name",
t1."keywords",
t1."key_questions",
t1."meta_data",
t1."name",
t1."path",
t1."pid",
t1."positions",
t1."sequence",
t1."source_count",
t1."tags",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "ai_kb_chunk" t1 
LEFT JOIN "ai_kb_document" t11 ON t1."document_id" = t11."id" 
LEFT JOIN "ai_knowledge_base" t21 ON t11."kb_id" = t21."id" 

WHERE ( t21."id" = #{ctx.datacontext.kb_id} ) AND ( t1."pid" IS NULL )
```

#### tree :id=ai_kb_chunk-tree
```sql
SELECT
t1."active",
t11."categories",
t1."chunk_type",
t1."content",
t1."content_preview",
t1."create_man",
t1."create_time",
t1."document_id",
t11."name" AS "document_name",
t11."sequence" AS "document_sequence",
t11."type" AS "document_type",
t11."file" AS "doc_file",
t11."name" AS "doc_name",
t11."parsed_content" AS "doc_parsed_content",
t1."id",
t11."kb_id",
t21."name" AS "kb_name",
t1."keywords",
t1."key_questions",
t1."meta_data",
t1."name",
t1."path",
t1."pid",
t1."positions",
t1."sequence",
t1."source_count",
t1."source_indices",
t1."tags",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "ai_kb_chunk" t1 
LEFT JOIN "ai_kb_document" t11 ON t1."document_id" = t11."id" 
LEFT JOIN "ai_knowledge_base" t21 ON t11."kb_id" = t21."id" 

WHERE ( <choose><when test="ctx.datacontext.ai_kb_document !=null ">  t1."document_id" = #{ctx.datacontext.ai_kb_document}  </when><otherwise>1=1</otherwise></choose> )
```

#### 启用(VALID) :id=ai_kb_chunk-valid
```sql
SELECT
t1."active",
t11."categories",
t1."chunk_type",
t1."content",
t1."content_preview",
t1."create_man",
t1."create_time",
t1."document_id",
t11."name" AS "document_name",
t11."sequence" AS "document_sequence",
t11."type" AS "document_type",
t11."file" AS "doc_file",
t11."name" AS "doc_name",
t11."parsed_content" AS "doc_parsed_content",
t1."id",
t11."kb_id",
t21."name" AS "kb_name",
t1."keywords",
t1."key_questions",
t1."meta_data",
t1."name",
t1."path",
t1."pid",
t1."positions",
t1."sequence",
t1."source_count",
t1."source_indices",
t1."tags",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "ai_kb_chunk" t1 
LEFT JOIN "ai_kb_document" t11 ON t1."document_id" = t11."id" 
LEFT JOIN "ai_knowledge_base" t21 ON t11."kb_id" = t21."id" 

WHERE ( t1."active" = 1 )
```


## [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document.md) :id=ai_kb_document

#### DEFAULT :id=ai_kb_document-Default
```sql
SELECT
t1."active",
t1."categories",
t1."chunk_method",
t1."chunk_num",
t1."create_man",
t1."create_time",
t1."custom_chunk",
t1."digest_code",
TO_CHAR(t1."create_time", 'YYYY-MM-DD') AS "doc_create_time",
t1."file",
t1."file_type",
t1."id",
t1."kb_id",
t11."name" AS "kb_name",
t1."key",
t1."name",
concat_ws('/',nullif(btrim(t1."categories", '/'),''),t1."name"||'.'||COALESCE(t1."file_type",'md')) AS "path",
CURRENT_DATE - t1."create_time"::date AS "recent_create_days",
t1."resource",
t1."sequence",
t1."size",
t1."source_id",
t1."source_type",
t1."status",
t1."sync_frequency",
t1."sync_id",
t11."tag_sets",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "ai_kb_document" t1 
LEFT JOIN "ai_knowledge_base" t11 ON t1."kb_id" = t11."id" 

```

#### 默认（全部数据）(VIEW) :id=ai_kb_document-View
```sql
SELECT
t1."active",
t1."categories",
t1."chunk_method",
t1."chunk_num",
t1."content",
t1."create_man",
t1."create_time",
t1."custom_chunk",
t1."digest_code",
TO_CHAR(t1."create_time", 'YYYY-MM-DD') AS "doc_create_time",
t1."file",
t1."file_type",
t1."id",
t1."kb_id",
t11."name" AS "kb_name",
t1."key",
t1."meta_data",
t1."name",
t1."parsed_content",
t1."parser_config",
t1."parse_error",
concat_ws('/',nullif(btrim(t1."categories", '/'),''),t1."name"||'.'||COALESCE(t1."file_type",'md')) AS "path",
CURRENT_DATE - t1."create_time"::date AS "recent_create_days",
t1."resource",
t1."sequence",
t1."size",
t1."source_id",
t1."source_type",
t1."status",
t1."sync_frequency",
t1."sync_id",
t11."tag_sets",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "ai_kb_document" t1 
LEFT JOIN "ai_knowledge_base" t11 ON t1."kb_id" = t11."id" 

```

#### AI文档内容(ai_doc_content) :id=ai_kb_document-ai_doc_content
```sql
SELECT
t1."content",
t1."id",
t1."name",
t1."parsed_content"
FROM "ai_kb_document" t1 

```

#### AI文档清单(ai_doc_list) :id=ai_kb_document-ai_doc_list
```sql
SELECT
t1."categories",
t1."id",
t1."name",
t1."resource",
t1."status"
FROM "ai_kb_document" t1 

```

#### 当前知识库(cur_kb) :id=ai_kb_document-cur_kb
```sql
SELECT
t1."active",
t1."categories",
t1."chunk_method",
t1."chunk_num",
t1."create_man",
t1."create_time",
t1."custom_chunk",
t1."digest_code",
TO_CHAR(t1."create_time", 'YYYY-MM-DD') AS "doc_create_time",
t1."file",
t1."file_type",
t1."id",
t1."kb_id",
t11."name" AS "kb_name",
t1."key",
t1."name",
concat_ws('/',nullif(btrim(t1."categories", '/'),''),t1."name"||'.'||COALESCE(t1."file_type",'md')) AS "path",
CURRENT_DATE - t1."create_time"::date AS "recent_create_days",
t1."resource",
t1."sequence",
t1."size",
t1."source_id",
t1."source_type",
t1."status",
t1."sync_frequency",
t1."sync_id",
t11."tag_sets",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "ai_kb_document" t1 
LEFT JOIN "ai_knowledge_base" t11 ON t1."kb_id" = t11."id" 

WHERE ( t1."kb_id" = #{ctx.datacontext.kb_id} )
```

#### exp_list :id=ai_kb_document-exp_list
```sql
SELECT * FROM (
SELECT 
    t1.ACTIVE, t1.CATEGORIES, t1.CHUNK_METHOD, t1.CHUNK_NUM, 
    t1.CREATE_MAN, t1.CREATE_TIME, t1.CUSTOM_CHUNK, t1.FILE, 
    t1.FILE_TYPE, t1.ID, t1.KB_ID, t1.KEY, t1.NAME, t1.RESOURCE, 
    t1.SIZE, t1.SOURCE_ID, t1.SOURCE_TYPE, t1.STATUS, 
    t1.SYNC_FREQUENCY, t1.SYNC_ID, t11.TAG_SETS, t1.TYPE, 
    t1.UPDATE_MAN, t1.UPDATE_TIME ,CASE WHEN t1.ID = #{ctx.datacontext.selected_data} THEN 0 ELSE t1.SEQUENCE END AS SEQUENCE
FROM AI_KB_DOCUMENT t1 
LEFT JOIN AI_KNOWLEDGE_BASE t11 ON t1.KB_ID = t11.ID 
WHERE t1.KB_ID = #{ctx.datacontext.ai_knowledge_base}
ORDER BY 
    CASE WHEN t1.ID = #{ctx.datacontext.selected_data} THEN 0 ELSE 1 END
) t1

```

#### 数据查询(ls) :id=ai_kb_document-ls
```sql
SELECT
t1."id",
concat_ws('/',nullif(btrim(t1."categories", '/'),''),t1."name"||'.'||COALESCE(t1."file_type",'md')) AS "path",
t1."size"
FROM "ai_kb_document" t1 

```

#### 过滤器查询(my_filter) :id=ai_kb_document-my_filter
```sql
SELECT
t1."active",
t1."categories",
t1."chunk_method",
t1."chunk_num",
t1."create_man",
t1."create_time",
t1."custom_chunk",
t1."digest_code",
TO_CHAR(t1."create_time", 'YYYY-MM-DD') AS "doc_create_time",
t1."file",
t1."file_type",
t1."id",
t1."kb_id",
t11."name" AS "kb_name",
t1."key",
t1."name",
concat_ws('/',nullif(btrim(t1."categories", '/'),''),t1."name"||'.'||COALESCE(t1."file_type",'md')) AS "path",
CURRENT_DATE - t1."create_time"::date AS "recent_create_days",
t1."resource",
t1."sequence",
t1."size",
t1."source_id",
t1."source_type",
t1."status",
t1."sync_frequency",
t1."sync_id",
t11."tag_sets",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "ai_kb_document" t1 
LEFT JOIN "ai_knowledge_base" t11 ON t1."kb_id" = t11."id" 

```

#### reader :id=ai_kb_document-reader
```sql
SELECT
t1."active",
t1."categories",
t1."chunk_method",
t1."chunk_num",
t1."create_man",
t1."create_time",
t1."custom_chunk",
t1."digest_code",
TO_CHAR(t1."create_time", 'YYYY-MM-DD') AS "doc_create_time",
t1."file",
t1."file_type",
t1."id",
t1."kb_id",
t11."name" AS "kb_name",
t1."key",
t1."name",
concat_ws('/',nullif(btrim(t1."categories", '/'),''),t1."name"||'.'||COALESCE(t1."file_type",'md')) AS "path",
CURRENT_DATE - t1."create_time"::date AS "recent_create_days",
t1."resource",
t1."sequence",
t1."size",
t1."source_id",
t1."source_type",
t1."status",
t1."sync_frequency",
t1."sync_id",
t11."tag_sets",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "ai_kb_document" t1 
LEFT JOIN "ai_knowledge_base" t11 ON t1."kb_id" = t11."id" 

WHERE ( ( t11."visibility" = 'public'  OR  ( t11."scope_id" = #{ctx.sessioncontext.srforgid}  AND  t11."scope_type" = 'organization' )  OR  EXISTS(SELECT 1 FROM AI_KB_MEMBER m 
 WHERE 
 t11.ID = m.KB_ID  AND  ( m.USER_ID = #{ctx.sessioncontext.srfpersonid} ) )  OR  ( t11."scope_type" = 'user_group'  AND  t11."scope_id" = #{ctx.sessioncontext.srfgroup_user} ) ) )
```

#### 最近文档(recent) :id=ai_kb_document-recent
```sql
SELECT
t1."active",
t1."categories",
t1."chunk_method",
t1."chunk_num",
t1."create_man",
t1."create_time",
t1."custom_chunk",
t1."digest_code",
TO_CHAR(t1."create_time", 'YYYY-MM-DD') AS "doc_create_time",
t1."file",
t1."file_type",
t1."id",
t1."kb_id",
t11."name" AS "kb_name",
t1."key",
t1."name",
concat_ws('/',nullif(btrim(t1."categories", '/'),''),t1."name"||'.'||COALESCE(t1."file_type",'md')) AS "path",
CURRENT_DATE - t1."create_time"::date AS "recent_create_days",
t1."resource",
t1."sequence",
t1."size",
t1."source_id",
t1."source_type",
t1."status",
t1."sync_frequency",
t1."sync_id",
t11."tag_sets",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "ai_kb_document" t1 
LEFT JOIN "ai_knowledge_base" t11 ON t1."kb_id" = t11."id" 

```

#### 资源分类(resource_classification) :id=ai_kb_document-resource_classification
```sql
SELECT
t1."active",
t1."categories",
t1."chunk_method",
t1."chunk_num",
t1."create_man",
t1."create_time",
t1."custom_chunk",
t1."digest_code",
TO_CHAR(t1."create_time", 'YYYY-MM-DD') AS "doc_create_time",
t1."file",
t1."file_type",
t1."id",
t1."kb_id",
t11."name" AS "kb_name",
t1."key",
t1."name",
concat_ws('/',nullif(btrim(t1."categories", '/'),''),t1."name"||'.'||COALESCE(t1."file_type",'md')) AS "path",
CURRENT_DATE - t1."create_time"::date AS "recent_create_days",
t1."resource",
t1."sequence",
t1."size",
t1."source_id",
t1."source_type",
t1."status",
t1."sync_frequency",
t1."sync_id",
t11."tag_sets",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "ai_kb_document" t1 
LEFT JOIN "ai_knowledge_base" t11 ON t1."kb_id" = t11."id" 

WHERE ( t1."resource" IS NOT NULL )
```

#### 选中的数据(selected_data) :id=ai_kb_document-selected_data
```sql
SELECT
t1."active",
t1."categories",
t1."chunk_method",
t1."chunk_num",
t1."create_man",
t1."create_time",
t1."custom_chunk",
t1."digest_code",
TO_CHAR(t1."create_time", 'YYYY-MM-DD') AS "doc_create_time",
t1."file",
t1."file_type",
t1."id",
t1."kb_id",
t11."name" AS "kb_name",
t1."key",
t1."name",
concat_ws('/',nullif(btrim(t1."categories", '/'),''),t1."name"||'.'||COALESCE(t1."file_type",'md')) AS "path",
CURRENT_DATE - t1."create_time"::date AS "recent_create_days",
t1."resource",
t1."sequence",
t1."size",
t1."source_id",
t1."source_type",
t1."status",
t1."sync_frequency",
t1."sync_id",
t11."tag_sets",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "ai_kb_document" t1 
LEFT JOIN "ai_knowledge_base" t11 ON t1."kb_id" = t11."id" 

WHERE ( t1."id" = #{ctx.datacontext.selected_data} )
```

#### 简单查询(simple) :id=ai_kb_document-simple
```sql
SELECT
t1."chunk_method",
t1."custom_chunk",
t1."id",
t1."name",
concat_ws('/',nullif(btrim(t1."categories", '/'),''),t1."name"||'.'||COALESCE(t1."file_type",'md')) AS "path",
t1."sequence",
t1."status",
t1."sync_id",
t1."type",
t1."update_time"
FROM "ai_kb_document" t1 

```

#### 未解析文档(UNPARSED) :id=ai_kb_document-unparsed
```sql
SELECT
t1."active",
t1."categories",
t1."chunk_method",
t1."chunk_num",
t1."content",
t1."create_man",
t1."create_time",
t1."custom_chunk",
t1."digest_code",
TO_CHAR(t1."create_time", 'YYYY-MM-DD') AS "doc_create_time",
t1."file",
t1."file_type",
t1."id",
t1."kb_id",
t11."name" AS "kb_name",
t1."key",
t1."meta_data",
t1."name",
t1."parsed_content",
t1."parser_config",
t1."parse_error",
concat_ws('/',nullif(btrim(t1."categories", '/'),''),t1."name"||'.'||COALESCE(t1."file_type",'md')) AS "path",
CURRENT_DATE - t1."create_time"::date AS "recent_create_days",
t1."resource",
t1."sequence",
t1."size",
t1."source_id",
t1."source_type",
t1."status",
t1."sync_frequency",
t1."sync_id",
t11."tag_sets",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "ai_kb_document" t1 
LEFT JOIN "ai_knowledge_base" t11 ON t1."kb_id" = t11."id" 

WHERE ( t1."active" = 1  AND  t1."status" = '3'  AND  ( t1."parsed_content" IS NOT NULL  OR  t1."file" IS NOT NULL ) )
```


## [知识库文档同步(AI_KB_DOCUMENT_SYNC)](module/ai/ai_kb_document_sync.md) :id=ai_kb_document_sync

#### DEFAULT :id=ai_kb_document_sync-Default
```sql
SELECT
t1."ai_knowledge_base_id",
t1."create_man",
t1."create_time",
t1."id",
t1."name",
t1."source_id",
t1."source_type",
t1."sync_frequency",
t1."update_man",
t1."update_time"
FROM "ai_kb_document_sync" t1 

```

#### 默认（全部数据）(VIEW) :id=ai_kb_document_sync-View
```sql
SELECT
t1."ai_knowledge_base_id",
t1."create_man",
t1."create_time",
t1."id",
t1."name",
t1."source_id",
t1."source_type",
t1."sync_frequency",
t1."update_man",
t1."update_time"
FROM "ai_kb_document_sync" t1 

```


## [知识库图谱实体(AI_KB_GRAPH_ENTITY)](module/ai/ai_kb_graph_entity.md) :id=ai_kb_graph_entity

#### DEFAULT :id=ai_kb_graph_entity-Default
```sql
SELECT
t1."confidence",
t1."context",
t1."create_man",
t1."create_time",
t1."description",
t1."document_id",
t21."name" AS "document_name",
t1."id",
t1."kb_id",
t11."name" AS "kb_name",
t1."keywords",
t1."name",
t1."normalized_name",
t1."reference_type",
t1."type",
t1."update_man",
t1."update_time"
FROM "ai_kb_graph_entity" t1 
LEFT JOIN "ai_knowledge_base" t11 ON t1."kb_id" = t11."id" 
LEFT JOIN "ai_kb_document" t21 ON t1."document_id" = t21."id" 

```

#### 默认（全部数据）(VIEW) :id=ai_kb_graph_entity-View
```sql
SELECT
t1."confidence",
t1."context",
t1."create_man",
t1."create_time",
t1."description",
t1."document_id",
t21."name" AS "document_name",
t1."id",
t1."kb_id",
t11."name" AS "kb_name",
t1."keywords",
t1."name",
t1."normalized_name",
t1."reference_type",
t1."type",
t1."update_man",
t1."update_time"
FROM "ai_kb_graph_entity" t1 
LEFT JOIN "ai_knowledge_base" t11 ON t1."kb_id" = t11."id" 
LEFT JOIN "ai_kb_document" t21 ON t1."document_id" = t21."id" 

```

#### 实体类型(cur_entity_type) :id=ai_kb_graph_entity-cur_entity_type
```sql
SELECT
t1."confidence",
t1."context",
t1."create_man",
t1."create_time",
t1."description",
t1."document_id",
t21."name" AS "document_name",
t1."id",
t1."kb_id",
t11."name" AS "kb_name",
t1."keywords",
t1."name",
t1."normalized_name",
t1."reference_type",
t1."type",
t1."update_man",
t1."update_time"
FROM "ai_kb_graph_entity" t1 
LEFT JOIN "ai_knowledge_base" t11 ON t1."kb_id" = t11."id" 
LEFT JOIN "ai_kb_document" t21 ON t1."document_id" = t21."id" 

WHERE ( <choose><when test="ctx.datacontext.ai_knowledge_base !=null ">  t1."kb_id" = #{ctx.datacontext.ai_knowledge_base}  </when><otherwise>1=1</otherwise></choose> )
```

#### 当前数据库实体(cur_kb) :id=ai_kb_graph_entity-cur_kb
```sql
SELECT
t1."confidence",
t1."context",
t1."create_man",
t1."create_time",
t1."description",
t1."document_id",
t21."name" AS "document_name",
t1."id",
t1."kb_id",
t11."name" AS "kb_name",
t1."keywords",
t1."name",
t1."normalized_name",
t1."reference_type",
t1."type",
t1."update_man",
t1."update_time"
FROM "ai_kb_graph_entity" t1 
LEFT JOIN "ai_knowledge_base" t11 ON t1."kb_id" = t11."id" 
LEFT JOIN "ai_kb_document" t21 ON t1."document_id" = t21."id" 

WHERE ( t1."kb_id" = #{ctx.datacontext.ai_knowledge_base} )
```


## [知识库图谱实体文档分块(AI_KB_GRAPH_ENTITY_CHUNK)](module/ai/ai_kb_graph_entity_chunk.md) :id=ai_kb_graph_entity_chunk

#### DEFAULT :id=ai_kb_graph_entity_chunk-Default
```sql
SELECT
t1."chunk_id",
t1."create_man",
t1."create_time",
t1."entity_id",
t1."id",
t1."name",
t1."update_man",
t1."update_time"
FROM "ai_kb_graph_entity_chunk" t1 

```

#### 默认（全部数据）(VIEW) :id=ai_kb_graph_entity_chunk-View
```sql
SELECT
t1."chunk_id",
t1."create_man",
t1."create_time",
t1."entity_id",
t1."id",
t1."name",
t1."update_man",
t1."update_time"
FROM "ai_kb_graph_entity_chunk" t1 

```


## [知识库图谱实体类型(AI_KB_GRAPH_ENTITY_TYPE)](module/ai/ai_kb_graph_entity_type.md) :id=ai_kb_graph_entity_type

#### DEFAULT :id=ai_kb_graph_entity_type-Default
```sql
SELECT
t1."create_man",
t1."create_time",
t1."description",
t1."icon",
t1."id",
t1."name",
t1."update_man",
t1."update_time",
t1."value"
FROM "ai_kb_graph_entity_type" t1 

```

#### 默认（全部数据）(VIEW) :id=ai_kb_graph_entity_type-View
```sql
SELECT
t1."create_man",
t1."create_time",
t1."description",
t1."icon",
t1."id",
t1."name",
t1."update_man",
t1."update_time",
t1."value"
FROM "ai_kb_graph_entity_type" t1 

```

#### 数据查询(VALID) :id=ai_kb_graph_entity_type-valid
```sql
SELECT
t1."create_man",
t1."create_time",
t1."description",
t1."icon",
t1."id",
t1."name",
t1."update_man",
t1."update_time",
t1."value"
FROM "ai_kb_graph_entity_type" t1 

```


## [知识库图谱关系(AI_KB_GRAPH_RELATION)](module/ai/ai_kb_graph_relation.md) :id=ai_kb_graph_relation

#### DEFAULT :id=ai_kb_graph_relation-Default
```sql
SELECT
t1."active",
t1."confidence",
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."kb_id",
t31."name" AS "kb_name",
t1."name",
t1."object_id",
t21."name" AS "object_name",
t1."predicate",
t1."subject_id",
t11."name" AS "subject_name",
t1."update_man",
t1."update_time"
FROM "ai_kb_graph_relation" t1 
LEFT JOIN "ai_kb_graph_entity" t11 ON t1."subject_id" = t11."id" 
LEFT JOIN "ai_kb_graph_entity" t21 ON t1."object_id" = t21."id" 
LEFT JOIN "ai_knowledge_base" t31 ON t1."kb_id" = t31."id" 

```

#### 默认（全部数据）(VIEW) :id=ai_kb_graph_relation-View
```sql
SELECT
t1."active",
t1."confidence",
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."kb_id",
t31."name" AS "kb_name",
t1."name",
t1."object_id",
t21."name" AS "object_name",
t1."predicate",
t1."subject_id",
t11."name" AS "subject_name",
t1."update_man",
t1."update_time"
FROM "ai_kb_graph_relation" t1 
LEFT JOIN "ai_kb_graph_entity" t11 ON t1."subject_id" = t11."id" 
LEFT JOIN "ai_kb_graph_entity" t21 ON t1."object_id" = t21."id" 
LEFT JOIN "ai_knowledge_base" t31 ON t1."kb_id" = t31."id" 

```

#### 当前数据库(cur_kb) :id=ai_kb_graph_relation-cur_kb
```sql
SELECT
t1."active",
t1."confidence",
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."kb_id",
t31."name" AS "kb_name",
t1."name",
t1."object_id",
t21."name" AS "object_name",
t1."predicate",
t1."subject_id",
t11."name" AS "subject_name",
t1."update_man",
t1."update_time"
FROM "ai_kb_graph_relation" t1 
LEFT JOIN "ai_kb_graph_entity" t11 ON t1."subject_id" = t11."id" 
LEFT JOIN "ai_kb_graph_entity" t21 ON t1."object_id" = t21."id" 
LEFT JOIN "ai_knowledge_base" t31 ON t1."kb_id" = t31."id" 

WHERE ( <choose><when test="ctx.datacontext.ai_knowledge_base !=null ">  t1."kb_id" = #{ctx.datacontext.ai_knowledge_base}  </when><otherwise>1=1</otherwise></choose> )
```


## [知识库图谱关系文档分块(AI_KB_GRAPH_RELATION_CHUNK)](module/ai/ai_kb_graph_relation_chunk.md) :id=ai_kb_graph_relation_chunk

#### DEFAULT :id=ai_kb_graph_relation_chunk-Default
```sql
SELECT
t1."chunk_id",
t1."create_man",
t1."create_time",
t1."id",
t1."name",
t1."relation_id",
t1."update_man",
t1."update_time"
FROM "ai_kb_graph_relation_chunk" t1 

```

#### 默认（全部数据）(VIEW) :id=ai_kb_graph_relation_chunk-View
```sql
SELECT
t1."chunk_id",
t1."create_man",
t1."create_time",
t1."id",
t1."name",
t1."relation_id",
t1."update_man",
t1."update_time"
FROM "ai_kb_graph_relation_chunk" t1 

```


## [知识库成员(AI_KB_MEMBER)](module/ai/ai_kb_member.md) :id=ai_kb_member

#### DEFAULT :id=ai_kb_member-Default
```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."kb_id",
t11."name" AS "kb_name",
t1."name",
t1."role_id",
t1."update_man",
t1."update_time",
t1."user_id"
FROM "ai_kb_member" t1 
LEFT JOIN "ai_knowledge_base" t11 ON t1."kb_id" = t11."id" 

```

#### 默认（全部数据）(VIEW) :id=ai_kb_member-View
```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."kb_id",
t11."name" AS "kb_name",
t1."name",
t1."role_id",
t1."update_man",
t1."update_time",
t1."user_id"
FROM "ai_kb_member" t1 
LEFT JOIN "ai_knowledge_base" t11 ON t1."kb_id" = t11."id" 

```

#### 启用(VALID) :id=ai_kb_member-valid
```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."kb_id",
t11."name" AS "kb_name",
t1."name",
t1."role_id",
t1."update_man",
t1."update_time",
t1."user_id"
FROM "ai_kb_member" t1 
LEFT JOIN "ai_knowledge_base" t11 ON t1."kb_id" = t11."id" 

```


## [知识库检索记录(AI_KB_SEARCH_QUERY)](module/ai/ai_kb_search_query.md) :id=ai_kb_search_query

#### DEFAULT :id=ai_kb_search_query-Default
```sql
SELECT
t1."create_man",
t1."create_time",
t1."feedback",
t1."id",
t1."is_answered",
t1."is_knowledge_gap",
t1."name",
t1."normalized_query",
t1."source",
t1."tags",
t1."total_duration",
t1."update_man",
t1."update_time",
t1."user_id",
t1."user_satisfaction"
FROM "ai_kb_search_query" t1 

```

#### 默认（全部数据）(VIEW) :id=ai_kb_search_query-View
```sql
SELECT
t1."create_man",
t1."create_time",
t1."feedback",
t1."id",
t1."is_answered",
t1."is_knowledge_gap",
t1."name",
t1."normalized_query",
t1."raw_query",
t1."retrieval_config",
t1."source",
t1."source_metadata",
t1."tags",
t1."total_duration",
t1."update_man",
t1."update_time",
t1."user_id",
t1."user_satisfaction"
FROM "ai_kb_search_query" t1 

```


## [知识库检索结果(AI_KB_SEARCH_RESULT)](module/ai/ai_kb_search_result.md) :id=ai_kb_search_result

#### DEFAULT :id=ai_kb_search_result-Default
```sql
SELECT
t1."create_man",
t1."create_time",
t1."document_id",
t1."id",
t1."kb_id",
t1."name",
t1."query_id",
t1."rank",
t1."retrieval_mode",
t1."similarity",
t1."update_man",
t1."update_time"
FROM "ai_kb_search_result" t1 

```

#### 默认（全部数据）(VIEW) :id=ai_kb_search_result-View
```sql
SELECT
t1."chunk_snapshots",
t1."create_man",
t1."create_time",
t1."document_id",
t1."hit_content",
t1."id",
t1."kb_id",
t1."merged_content",
t1."name",
t1."query_id",
t1."rank",
t1."retrieval_mode",
t1."similarity",
t1."update_man",
t1."update_time"
FROM "ai_kb_search_result" t1 

```


## [知识库标签(AI_KB_TAG)](module/ai/ai_kb_tag.md) :id=ai_kb_tag

#### DEFAULT :id=ai_kb_tag-Default
```sql
SELECT
t1."create_man",
t1."create_time",
t1."description",
t1."enable",
t1."id",
t1."name",
t1."set_id",
t1."update_man",
t1."update_time",
t1."value"
FROM "ai_kb_tag" t1 

```

#### 默认（全部数据）(VIEW) :id=ai_kb_tag-View
```sql
SELECT
t1."create_man",
t1."create_time",
t1."description",
t1."enable",
t1."id",
t1."name",
t1."set_id",
t1."update_man",
t1."update_time",
t1."value"
FROM "ai_kb_tag" t1 

```

#### 启用(VALID) :id=ai_kb_tag-valid
```sql
SELECT
t1."create_man",
t1."create_time",
t1."description",
t1."enable",
t1."id",
t1."name",
t1."set_id",
t1."update_man",
t1."update_time",
t1."value"
FROM "ai_kb_tag" t1 

```


## [知识库标签集(AI_KB_TAG_SET)](module/ai/ai_kb_tag_set.md) :id=ai_kb_tag_set

#### DEFAULT :id=ai_kb_tag_set-Default
```sql
SELECT
t1."create_man",
t1."create_time",
t1."description",
t1."enable",
t1."id",
t1."name",
t1."owner_id",
t1."scope",
t1."source_id",
t1."update_man",
t1."update_time"
FROM "ai_kb_tag_set" t1 

```

#### 默认（全部数据）(VIEW) :id=ai_kb_tag_set-View
```sql
SELECT
t1."create_man",
t1."create_time",
t1."description",
t1."enable",
t1."id",
t1."name",
t1."owner_id",
t1."scope",
t1."source_id",
t1."update_man",
t1."update_time"
FROM "ai_kb_tag_set" t1 

```


## [知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base.md) :id=ai_knowledge_base

#### CurSelected :id=ai_knowledge_base-CurSelected
```sql
SELECT
t1."category_id",
t1."category_name",
t1."chat_model",
t1."chat_model_id",
t1."chunk_method",
t1."code_name",
t1."create_man",
t1."create_time",
t1."description",
t1."embedding_model",
t1."embedding_model_id",
t1."guidance_prompt",
t1."id",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."key",
t1."name",
t1."pageindex",
t1."record_id",
t11."_title" AS "record_title",
t1."rerank",
t1."rerank_model",
t1."rerank_model_id",
t1."resource",
t1."resource_code",
t1."resource_id",
t1."scope_id",
t1."scope_type",
t1."similarity_threshold",
t1."source_id",
t1."source_name",
t1."source_type",
t1."status",
t1."tag_sets",
t1."top_k",
t1."update_man",
t1."update_time",
t1."use_kg",
t1."vector_similarity_weight",
t1."visibility"
FROM "ai_knowledge_base" t1 
LEFT JOIN "data_record" t11 ON t1."record_id" = t11."_id" 

WHERE ( t1."id" = #{ctx.datacontext.knowledgebases} )
```

#### DEFAULT :id=ai_knowledge_base-Default
```sql
SELECT
t1."category_id",
t1."category_name",
t1."chat_model",
t1."chat_model_id",
t1."chunk_method",
t1."code_name",
t1."create_man",
t1."create_time",
t1."description",
t1."embedding_model",
t1."embedding_model_id",
t1."guidance_prompt",
t1."id",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."key",
t1."name",
t1."pageindex",
t1."record_id",
t11."_title" AS "record_title",
t1."rerank",
t1."rerank_model",
t1."rerank_model_id",
t1."resource",
t1."resource_code",
t1."resource_id",
t1."scope_id",
t1."scope_type",
t1."similarity_threshold",
t1."source_id",
t1."source_name",
t1."source_type",
t1."status",
t1."tag_sets",
t1."top_k",
t1."update_man",
t1."update_time",
t1."use_kg",
t1."vector_similarity_weight",
t1."visibility"
FROM "ai_knowledge_base" t1 
LEFT JOIN "data_record" t11 ON t1."record_id" = t11."_id" 

```

#### 默认（全部数据）(VIEW) :id=ai_knowledge_base-View
```sql
SELECT
t1."category_id",
t1."category_name",
t1."chat_model",
t1."chat_model_id",
t1."chunk_method",
t1."code_name",
t1."create_man",
t1."create_time",
t1."description",
t1."embedding_model",
t1."embedding_model_id",
t1."guidance_prompt",
t1."id",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."key",
t1."meta_data",
t1."name",
t1."pageindex",
t1."parser_config",
t1."record_id",
t11."_title" AS "record_title",
t1."rerank",
t1."rerank_model",
t1."rerank_model_id",
t1."resource",
t1."resource_code",
t1."resource_id",
t1."scope_id",
t1."scope_type",
t1."similarity_threshold",
t1."source_id",
t1."source_name",
t1."source_type",
t1."status",
t1."tag_sets",
t1."top_k",
t1."update_man",
t1."update_time",
t1."use_kg",
t1."vector_similarity_weight",
t1."visibility"
FROM "ai_knowledge_base" t1 
LEFT JOIN "data_record" t11 ON t1."record_id" = t11."_id" 

```

#### 管理员(admin) :id=ai_knowledge_base-admin
```sql
SELECT
t1."category_id",
t1."category_name",
t1."chat_model",
t1."chat_model_id",
t1."chunk_method",
t1."code_name",
t1."create_man",
t1."create_time",
t1."description",
t1."embedding_model",
t1."embedding_model_id",
t1."guidance_prompt",
t1."id",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."key",
t1."name",
t1."pageindex",
t1."record_id",
t11."_title" AS "record_title",
t1."rerank",
t1."rerank_model",
t1."rerank_model_id",
t1."resource",
t1."resource_code",
t1."resource_id",
t1."scope_id",
t1."scope_type",
t1."similarity_threshold",
t1."source_id",
t1."source_name",
t1."source_type",
t1."status",
t1."tag_sets",
t1."top_k",
t1."update_man",
t1."update_time",
t1."use_kg",
t1."vector_similarity_weight",
t1."visibility"
FROM "ai_knowledge_base" t1 
LEFT JOIN "data_record" t11 ON t1."record_id" = t11."_id" 

WHERE EXISTS(SELECT * FROM "ai_kb_member" t21 
 WHERE 
 t1."id" = t21."kb_id"  AND  ( t21."user_id" = #{ctx.sessioncontext.srfpersonid}  AND  t21."role_id" = 'admin' ) )
```

#### 目录下的知识库(category_ai_kb) :id=ai_knowledge_base-category_ai_kb
```sql
SELECT
t1."category_id",
t1."category_name",
t1."chat_model",
t1."chat_model_id",
t1."chunk_method",
t1."code_name",
t1."create_man",
t1."create_time",
t1."description",
t1."embedding_model",
t1."embedding_model_id",
t1."guidance_prompt",
t1."id",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."key",
t1."name",
t1."pageindex",
t1."record_id",
t11."_title" AS "record_title",
t1."rerank",
t1."rerank_model",
t1."rerank_model_id",
t1."resource",
t1."resource_code",
t1."resource_id",
t1."scope_id",
t1."scope_type",
t1."similarity_threshold",
t1."source_id",
t1."source_name",
t1."source_type",
t1."status",
t1."tag_sets",
t1."top_k",
t1."update_man",
t1."update_time",
t1."use_kg",
t1."vector_similarity_weight",
t1."visibility"
FROM "ai_knowledge_base" t1 
LEFT JOIN "data_record" t11 ON t1."record_id" = t11."_id" 

WHERE ( t1."is_deleted" = 0  AND  ( t1."category_id" = #{ctx.webcontext.category_id} ) )
```

#### 已删除(deleted) :id=ai_knowledge_base-deleted
```sql
SELECT
t1."category_id",
t1."category_name",
t1."chat_model",
t1."chat_model_id",
t1."chunk_method",
t1."code_name",
t1."create_man",
t1."create_time",
t1."description",
t1."embedding_model",
t1."embedding_model_id",
t1."guidance_prompt",
t1."id",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."key",
t1."name",
t1."pageindex",
t1."record_id",
t11."_title" AS "record_title",
t1."rerank",
t1."rerank_model",
t1."rerank_model_id",
t1."resource",
t1."resource_code",
t1."resource_id",
t1."scope_id",
t1."scope_type",
t1."similarity_threshold",
t1."source_id",
t1."source_name",
t1."source_type",
t1."status",
t1."tag_sets",
t1."top_k",
t1."update_man",
t1."update_time",
t1."use_kg",
t1."vector_similarity_weight",
t1."visibility"
FROM "ai_knowledge_base" t1 
LEFT JOIN "data_record" t11 ON t1."record_id" = t11."_id" 

WHERE ( t1."is_deleted" = 1 )
```

#### 查询星标(favorite) :id=ai_knowledge_base-favorite
```sql
SELECT
t1."category_id",
t1."category_name",
t1."chat_model",
t1."chat_model_id",
t1."chunk_method",
t1."code_name",
t1."create_man",
t1."create_time",
t1."description",
t1."embedding_model",
t1."embedding_model_id",
t1."guidance_prompt",
t1."id",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."key",
t1."name",
t1."pageindex",
t1."record_id",
t11."_title" AS "record_title",
t1."rerank",
t1."rerank_model",
t1."rerank_model_id",
t1."resource",
t1."resource_code",
t1."resource_id",
t1."scope_id",
t1."scope_type",
t1."similarity_threshold",
t1."source_id",
t1."source_name",
t1."source_type",
t1."status",
t1."tag_sets",
t1."top_k",
t1."update_man",
t1."update_time",
t1."use_kg",
t1."vector_similarity_weight",
t1."visibility"
FROM "ai_knowledge_base" t1 
LEFT JOIN "data_record" t11 ON t1."record_id" = t11."_id" 

WHERE ( t1."is_archived" = 0  AND  t1."is_deleted" = 0  AND  (select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) = '1' )
```

#### 组管理员(group_admin) :id=ai_knowledge_base-group_admin
```sql
SELECT
t1."category_id",
t1."category_name",
t1."chat_model",
t1."chat_model_id",
t1."chunk_method",
t1."code_name",
t1."create_man",
t1."create_time",
t1."description",
t1."embedding_model",
t1."embedding_model_id",
t1."guidance_prompt",
t1."id",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."key",
t1."name",
t1."pageindex",
t1."record_id",
t11."_title" AS "record_title",
t1."rerank",
t1."rerank_model",
t1."rerank_model_id",
t1."resource",
t1."resource_code",
t1."resource_id",
t1."scope_id",
t1."scope_type",
t1."similarity_threshold",
t1."source_id",
t1."source_name",
t1."source_type",
t1."status",
t1."tag_sets",
t1."top_k",
t1."update_man",
t1."update_time",
t1."use_kg",
t1."vector_similarity_weight",
t1."visibility"
FROM "ai_knowledge_base" t1 
LEFT JOIN "data_record" t11 ON t1."record_id" = t11."_id" 

WHERE ( t1."scope_type" = 'user_group'  AND  t1."scope_id" IN (#{ctx.sessioncontext.srfgroup_admin}) )
```

#### 组管理员(group_user) :id=ai_knowledge_base-group_user
```sql
SELECT
t1."category_id",
t1."category_name",
t1."chat_model",
t1."chat_model_id",
t1."chunk_method",
t1."code_name",
t1."create_man",
t1."create_time",
t1."description",
t1."embedding_model",
t1."embedding_model_id",
t1."guidance_prompt",
t1."id",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."key",
t1."name",
t1."pageindex",
t1."record_id",
t11."_title" AS "record_title",
t1."rerank",
t1."rerank_model",
t1."rerank_model_id",
t1."resource",
t1."resource_code",
t1."resource_id",
t1."scope_id",
t1."scope_type",
t1."similarity_threshold",
t1."source_id",
t1."source_name",
t1."source_type",
t1."status",
t1."tag_sets",
t1."top_k",
t1."update_man",
t1."update_time",
t1."use_kg",
t1."vector_similarity_weight",
t1."visibility"
FROM "ai_knowledge_base" t1 
LEFT JOIN "data_record" t11 ON t1."record_id" = t11."_id" 

WHERE ( t1."scope_type" = 'user_group'  AND  t1."scope_id" IN (#{ctx.sessioncontext.srfgroup_user}) )
```

#### 组织私有库(org) :id=ai_knowledge_base-org
```sql
SELECT
t1."category_id",
t1."category_name",
t1."chat_model",
t1."chat_model_id",
t1."chunk_method",
t1."code_name",
t1."create_man",
t1."create_time",
t1."description",
t1."embedding_model",
t1."embedding_model_id",
t1."guidance_prompt",
t1."id",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."key",
t1."name",
t1."pageindex",
t1."record_id",
t11."_title" AS "record_title",
t1."rerank",
t1."rerank_model",
t1."rerank_model_id",
t1."resource",
t1."resource_code",
t1."resource_id",
t1."scope_id",
t1."scope_type",
t1."similarity_threshold",
t1."source_id",
t1."source_name",
t1."source_type",
t1."status",
t1."tag_sets",
t1."top_k",
t1."update_man",
t1."update_time",
t1."use_kg",
t1."vector_similarity_weight",
t1."visibility"
FROM "ai_knowledge_base" t1 
LEFT JOIN "data_record" t11 ON t1."record_id" = t11."_id" 

WHERE ( t1."scope_type" = 'organization'  AND  t1."scope_id" = #{ctx.sessioncontext.srforgid}  AND  t1."visibility" = 'private' )
```

#### 公开(public) :id=ai_knowledge_base-public
```sql
SELECT
t1."category_id",
t1."category_name",
t1."chat_model",
t1."chat_model_id",
t1."chunk_method",
t1."code_name",
t1."create_man",
t1."create_time",
t1."description",
t1."embedding_model",
t1."embedding_model_id",
t1."guidance_prompt",
t1."id",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."key",
t1."name",
t1."pageindex",
t1."record_id",
t11."_title" AS "record_title",
t1."rerank",
t1."rerank_model",
t1."rerank_model_id",
t1."resource",
t1."resource_code",
t1."resource_id",
t1."scope_id",
t1."scope_type",
t1."similarity_threshold",
t1."source_id",
t1."source_name",
t1."source_type",
t1."status",
t1."tag_sets",
t1."top_k",
t1."update_man",
t1."update_time",
t1."use_kg",
t1."vector_similarity_weight",
t1."visibility"
FROM "ai_knowledge_base" t1 
LEFT JOIN "data_record" t11 ON t1."record_id" = t11."_id" 

WHERE ( t1."visibility" = 'public' )
```

#### 只读用户(reader) :id=ai_knowledge_base-reader
```sql
SELECT
t1."category_id",
t1."category_name",
t1."chat_model",
t1."chat_model_id",
t1."chunk_method",
t1."code_name",
t1."create_man",
t1."create_time",
t1."description",
t1."embedding_model",
t1."embedding_model_id",
t1."guidance_prompt",
t1."id",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."key",
t1."name",
t1."pageindex",
t1."record_id",
t11."_title" AS "record_title",
t1."rerank",
t1."rerank_model",
t1."rerank_model_id",
t1."resource",
t1."resource_code",
t1."resource_id",
t1."scope_id",
t1."scope_type",
t1."similarity_threshold",
t1."source_id",
t1."source_name",
t1."source_type",
t1."status",
t1."tag_sets",
t1."top_k",
t1."update_man",
t1."update_time",
t1."use_kg",
t1."vector_similarity_weight",
t1."visibility"
FROM "ai_knowledge_base" t1 
LEFT JOIN "data_record" t11 ON t1."record_id" = t11."_id" 

WHERE EXISTS(SELECT * FROM "ai_kb_member" t21 
 WHERE 
 t1."id" = t21."kb_id"  AND  ( t21."user_id" = #{ctx.sessioncontext.srfpersonid}  AND  t21."role_id" = 'reader' ) )
```

#### search :id=ai_knowledge_base-search
```sql
SELECT
    t1."category_id",
    t1."category_name",
    t1."create_man",
    t1."create_time",
    t1."description",
    t1."guidance_prompt",
    t1."id",
    t1."is_archived",
    t1."is_deleted",
    t1."key",
    t1."name",
    t1."record_id",
    t1."resource",
    t1."resource_code",
    t1."resource_id",
    t1."scope_id",
    t1."scope_type",
    t1."similarity_threshold",
    t1."source_id",
    t1."source_name",
    t1."source_type",
    t1."status",
    t1."update_man",
    t1."update_time",
    t1."vector_similarity_weight",
    t1."visibility", t1."matched_documents" from (
        WITH input_kw AS (SELECT val,(val !~ '^[0-9A-Za-z\[\]]+$') AS is_fts FROM regexp_split_to_table(#{ctx.datacontext.keyword},'[, ]+') AS val WHERE val <> '')
   , raw_kw AS (SELECT val, val as kw, is_fts FROM input_kw  union SELECT DISTINCT lexeme AS val, val as kw, is_fts FROM input_kw i,  unnest(tsvector_to_array(to_tsvector('chinese_zh', i.val))) AS lexeme
                WHERE length(lexeme) >= 2 and is_fts)
   , raw_cnt AS (SELECT count(1) as cnt, count(DISTINCT kw) as kw from raw_kw)
   , doc_match AS (
   SELECT t.document_id, round(1.0 * COUNT(DISTINCT k.kw) / raw_cnt.kw, 2) + round(0.01 * COUNT(DISTINCT k.val) / raw_cnt.cnt, 4) - 0.01 as logic_rank,
                 max(case when k.is_fts then similarity(content, k.kw) else 0.99 end) as density_rank FROM ai_kb_chunk t JOIN raw_kw k ON t.content LIKE '%' || k.val || '%' , raw_cnt
                GROUP BY t.document_id, raw_cnt.kw, raw_cnt.cnt)
   , doc_agg AS (SELECT d.kb_id,  MAX(m.logic_rank) AS similarity_threshold, MAX(m.density_rank) AS vector_similarity_weight, 
   jsonb_path_query_array(
                                jsonb_agg(DISTINCT jsonb_build_object('id', d.id, 'name', d.name)),
                                '$[0 to 4]'
                        )::text AS matched_documents
                 FROM ai_kb_document d   JOIN doc_match m ON d.id = m.document_id  GROUP BY d.kb_id)
SELECT t1.id,t1.name,t1.update_time,t1.update_man,t1.create_time,t1.create_man,t1.description,t1.guidance_prompt,t1.category_id,t1.category_name,t1.resource_id,t1.resource_code,t1.resource,t1.record_id,
       t1.scope_id,t1.scope_type,t1.visibility,t1.status,t1.is_archived,t1.is_deleted,t1.key,t1.source_name,t1.source_id,t1.source_type,m.similarity_threshold,m.vector_similarity_weight,m.matched_documents
FROM ai_knowledge_base t1
         JOIN doc_agg m ON t1.id = m.kb_id
         order by m.similarity_threshold desc,m.vector_similarity_weight desc,t1.update_time desc
)  t1
WHERE ( #{ctx.datacontext.keyword} is not null )
```

#### 非星标知识库(unfavorite) :id=ai_knowledge_base-unfavorite
```sql
SELECT
t1."category_id",
t1."category_name",
t1."chat_model",
t1."chat_model_id",
t1."chunk_method",
t1."code_name",
t1."create_man",
t1."create_time",
t1."description",
t1."embedding_model",
t1."embedding_model_id",
t1."guidance_prompt",
t1."id",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."key",
t1."name",
t1."pageindex",
t1."record_id",
t11."_title" AS "record_title",
t1."rerank",
t1."rerank_model",
t1."rerank_model_id",
t1."resource",
t1."resource_code",
t1."resource_id",
t1."scope_id",
t1."scope_type",
t1."similarity_threshold",
t1."source_id",
t1."source_name",
t1."source_type",
t1."status",
t1."tag_sets",
t1."top_k",
t1."update_man",
t1."update_time",
t1."use_kg",
t1."vector_similarity_weight",
t1."visibility"
FROM "ai_knowledge_base" t1 
LEFT JOIN "data_record" t11 ON t1."record_id" = t11."_id" 

WHERE ( (select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) = '0'  AND  t1."is_deleted" = 0  AND  t1."is_archived" = 0 )
```

#### 操作用户(user) :id=ai_knowledge_base-user
```sql
SELECT
t1."category_id",
t1."category_name",
t1."chat_model",
t1."chat_model_id",
t1."chunk_method",
t1."code_name",
t1."create_man",
t1."create_time",
t1."description",
t1."embedding_model",
t1."embedding_model_id",
t1."guidance_prompt",
t1."id",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."key",
t1."name",
t1."pageindex",
t1."record_id",
t11."_title" AS "record_title",
t1."rerank",
t1."rerank_model",
t1."rerank_model_id",
t1."resource",
t1."resource_code",
t1."resource_id",
t1."scope_id",
t1."scope_type",
t1."similarity_threshold",
t1."source_id",
t1."source_name",
t1."source_type",
t1."status",
t1."tag_sets",
t1."top_k",
t1."update_man",
t1."update_time",
t1."use_kg",
t1."vector_similarity_weight",
t1."visibility"
FROM "ai_knowledge_base" t1 
LEFT JOIN "data_record" t11 ON t1."record_id" = t11."_id" 

WHERE EXISTS(SELECT * FROM "ai_kb_member" t21 
 WHERE 
 t1."id" = t21."kb_id"  AND  ( t21."user_id" = #{ctx.sessioncontext.srfpersonid}  AND  t21."role_id" = 'user' ) )
```

#### 启用知识库(VALID) :id=ai_knowledge_base-valid
```sql
SELECT
t1."category_id",
t1."category_name",
t1."chat_model",
t1."chat_model_id",
t1."chunk_method",
t1."code_name",
t1."create_man",
t1."create_time",
t1."description",
t1."embedding_model",
t1."embedding_model_id",
t1."guidance_prompt",
t1."id",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."key",
t1."meta_data",
t1."name",
t1."pageindex",
t1."parser_config",
t1."record_id",
t11."_title" AS "record_title",
t1."rerank",
t1."rerank_model",
t1."rerank_model_id",
t1."resource",
t1."resource_code",
t1."resource_id",
t1."scope_id",
t1."scope_type",
t1."similarity_threshold",
t1."source_id",
t1."source_name",
t1."source_type",
t1."status",
t1."tag_sets",
t1."top_k",
t1."update_man",
t1."update_time",
t1."use_kg",
t1."vector_similarity_weight",
t1."visibility"
FROM "ai_knowledge_base" t1 
LEFT JOIN "data_record" t11 ON t1."record_id" = t11."_id" 

```


## [知识库源(AI_KNOWLEDGE_SOURCE)](module/ai/ai_knowledge_source.md) :id=ai_knowledge_source

#### DEFAULT :id=ai_knowledge_source-Default
```sql
SELECT
t1."active",
t1."base_url",
t1."create_man",
t1."create_time",
t1."id",
t1."last_sync_time",
t1."name",
t1."password",
t1."type",
t1."update_man",
t1."update_time",
t1."user_name"
FROM "ai_knowledge_source" t1 

```

#### 默认（全部数据）(VIEW) :id=ai_knowledge_source-View
```sql
SELECT
t1."active",
t1."api_key",
t1."base_url",
t1."config",
t1."create_man",
t1."create_time",
t1."id",
t1."last_sync_time",
t1."name",
t1."password",
t1."type",
t1."update_man",
t1."update_time",
t1."user_name"
FROM "ai_knowledge_source" t1 

```


## [AI大模型(AI_MODEL)](module/ai/ai_model.md) :id=ai_model

#### DEFAULT :id=ai_model-Default
```sql
SELECT
t1."active",
t1."ai_credential_id",
t21."name" AS "ai_credential_name",
t1."api_base_url",
t1."code_name",
t1."create_man",
t1."create_time",
t1."desc_oss_image",
t1."id",
t1."max_context_tokens",
t1."max_output_tokens",
t1."model_capability",
t1."model_category",
t1."name",
t1."provider",
t11."name" AS "provider_name",
t1."update_man",
t1."update_time"
FROM "ai_model" t1 
LEFT JOIN "ai_model_provider" t11 ON t1."provider" = t11."id" 
LEFT JOIN "ai_credential" t21 ON t1."ai_credential_id" = t21."id" 

```

#### 默认（全部数据）(VIEW) :id=ai_model-View
```sql
SELECT
t21."bearer_token" AS "access_token",
t1."active",
t1."ai_credential_id",
t21."name" AS "ai_credential_name",
t1."api_base_url",
t1."code_name",
t1."create_man",
t1."create_time",
t1."desc_oss_image",
t1."extra_params",
t1."id",
t1."max_context_tokens",
t1."max_output_tokens",
t1."model_capability",
t1."model_category",
t1."name",
t1."oss_image_vl_prompt",
t1."provider",
t11."name" AS "provider_name",
t1."update_man",
t1."update_time"
FROM "ai_model" t1 
LEFT JOIN "ai_model_provider" t11 ON t1."provider" = t11."id" 
LEFT JOIN "ai_credential" t21 ON t1."ai_credential_id" = t21."id" 

```


## [模型提供商(AI_MODEL_PROVIDER)](module/ai/ai_model_provider.md) :id=ai_model_provider

#### DEFAULT :id=ai_model_provider-Default
```sql
SELECT
concat(t1."base_url",t1."default_version") AS "api_base_url",
t1."base_url",
t1."default_token",
t1."default_version",
(select count(1) from ai_credential  where id =t1."id") AS "has_credential",
t1."id",
t1."name",
t1."update_time"
FROM "ai_model_provider" t1 

```

#### 默认（全部数据）(VIEW) :id=ai_model_provider-View
```sql
SELECT
concat(t1."base_url",t1."default_version") AS "api_base_url",
t1."base_url",
t1."default_token",
t1."default_version",
(select count(1) from ai_credential  where id =t1."id") AS "has_credential",
t1."id",
t1."name",
t1."update_time"
FROM "ai_model_provider" t1 

```

#### 存在凭证(has_credential) :id=ai_model_provider-has_credential
```sql
SELECT
concat(t1."base_url",t1."default_version") AS "api_base_url",
t1."base_url",
t1."default_token",
t1."default_version",
(select count(1) from ai_credential  where id =t1."id") AS "has_credential",
t1."id",
t1."name",
t1."update_time"
FROM "ai_model_provider" t1 

WHERE ( (select count(1) from ai_credential  where id =t1."id") <> '0' )
```

#### 不存在凭证(no_has_credential) :id=ai_model_provider-no_has_credential
```sql
SELECT
concat(t1."base_url",t1."default_version") AS "api_base_url",
t1."base_url",
t1."default_token",
t1."default_version",
(select count(1) from ai_credential  where id =t1."id") AS "has_credential",
t1."id",
t1."name",
t1."update_time"
FROM "ai_model_provider" t1 

WHERE ( (select count(1) from ai_credential  where id =t1."id") = '0' )
```


## [智能审查报告(AI_REVIEW_REPORT)](module/ai/ai_review_report.md) :id=ai_review_report

#### Bykb_id_agent :id=ai_review_report-Bykb_id_agent
```sql
SELECT
t1."agent_tag",
t1."create_man",
t1."create_time",
t1."document_id",
t21."name" AS "document_name",
t1."id",
t1."kb_id",
t11."name" AS "kb_name",
t1."name",
t1."record_id",
t1."review_result",
t1."update_man",
t1."update_time"
FROM "ai_review_report" t1 
LEFT JOIN "ai_knowledge_base" t11 ON t1."kb_id" = t11."id" 
LEFT JOIN "ai_kb_document" t21 ON t1."document_id" = t21."id" 

WHERE ( t1."kb_id" = #{ctx.datacontext.kb_id}  AND  t1."agent_tag" = #{ctx.datacontext.agent_tag} )
```

#### DEFAULT :id=ai_review_report-Default
```sql
SELECT
t1."agent_tag",
t1."create_man",
t1."create_time",
t1."document_id",
t21."name" AS "document_name",
t1."id",
t1."kb_id",
t11."name" AS "kb_name",
t1."name",
t1."record_id",
t1."review_result",
t1."update_man",
t1."update_time"
FROM "ai_review_report" t1 
LEFT JOIN "ai_knowledge_base" t11 ON t1."kb_id" = t11."id" 
LEFT JOIN "ai_kb_document" t21 ON t1."document_id" = t21."id" 

```

#### 默认（全部数据）(VIEW) :id=ai_review_report-View
```sql
SELECT
t1."agent_tag",
t1."check_info",
t1."create_man",
t1."create_time",
t1."document_id",
t21."name" AS "document_name",
t1."id",
t1."kb_id",
t11."name" AS "kb_name",
t1."name",
t1."record_id",
t1."review_report",
t1."review_result",
t1."update_man",
t1."update_time"
FROM "ai_review_report" t1 
LEFT JOIN "ai_knowledge_base" t11 ON t1."kb_id" = t11."id" 
LEFT JOIN "ai_kb_document" t21 ON t1."document_id" = t21."id" 

```

#### reader :id=ai_review_report-reader
```sql
SELECT
t1."agent_tag",
t1."create_man",
t1."create_time",
t1."document_id",
t21."name" AS "document_name",
t1."id",
t1."kb_id",
t11."name" AS "kb_name",
t1."name",
t1."record_id",
t1."review_result",
t1."update_man",
t1."update_time"
FROM "ai_review_report" t1 
LEFT JOIN "ai_knowledge_base" t11 ON t1."kb_id" = t11."id" 
LEFT JOIN "ai_kb_document" t21 ON t1."document_id" = t21."id" 

WHERE ( ( t11."visibility" = 'public'  OR  ( t11."scope_id" = #{ctx.sessioncontext.srforgid}  AND  t11."scope_type" = 'organization' )  OR  EXISTS(SELECT 1 FROM AI_KB_MEMBER m 
 WHERE 
 t11.ID = m.KB_ID  AND  ( m.USER_ID = #{ctx.sessioncontext.srfpersonid} ) ) ) )
```


## [AI调用工具(AI_TOOL)](module/ai/ai_tool.md) :id=ai_tool

#### DEFAULT :id=ai_tool-Default
```sql
SELECT
t1."active",
t1."api_auth_type",
t1."api_headers",
t1."api_key",
t1."api_method",
t1."api_url",
t1."client_id",
t1."create_man",
t1."create_time",
t1."description",
t1."expiration_date",
t1."id",
t1."name",
t1."timeout",
t1."token_url",
t1."tool_tag",
t1."tool_type",
t1."update_man",
t1."update_time"
FROM "ai_tool" t1 

```

#### 默认（全部数据）(VIEW) :id=ai_tool-View
```sql
SELECT
t1."access_key",
t1."active",
t1."api_auth_type",
t1."api_headers",
t1."api_key",
t1."api_method",
t1."api_url",
t1."bearer_token",
t1."client_id",
t1."client_secret",
t1."create_man",
t1."create_time",
t1."description",
t1."expiration_date",
t1."id",
t1."input_schema",
t1."name",
t1."secret_key",
t1."skill_prompt",
t1."skill_references",
t1."skill_scripts",
t1."timeout",
t1."token_url",
t1."tool_tag",
t1."tool_type",
t1."update_man",
t1."update_time"
FROM "ai_tool" t1 

```

#### 内置扩展mcp服务(extension_mcp_server) :id=ai_tool-extension_mcp_server
```sql
SELECT
t1."active",
t1."api_auth_type",
t1."api_headers",
t1."api_key",
t1."api_method",
t1."api_url",
t1."client_id",
t1."create_man",
t1."create_time",
t1."description",
t1."expiration_date",
t1."id",
t1."name",
t1."timeout",
t1."token_url",
t1."tool_tag",
t1."tool_type",
t1."update_man",
t1."update_time"
FROM "ai_tool" t1 

WHERE ( t1."tool_type" = 'mcp_built_in_extension' )
```

#### 启用的技能数据(SKILL_VALID) :id=ai_tool-skill_valid
```sql
SELECT
t1."access_key",
t1."active",
t1."api_auth_type",
t1."api_headers",
t1."api_key",
t1."api_method",
t1."api_url",
t1."bearer_token",
t1."client_id",
t1."client_secret",
t1."create_man",
t1."create_time",
t1."description",
t1."expiration_date",
t1."id",
t1."input_schema",
t1."name",
t1."secret_key",
t1."skill_prompt",
t1."skill_references",
t1."skill_scripts",
t1."timeout",
t1."token_url",
t1."tool_tag",
t1."tool_type",
t1."update_man",
t1."update_time"
FROM "ai_tool" t1 

WHERE ( t1."tool_type" = 'skill' )
```


## [页面(PAGE)](module/Wiki/article_page.md) :id=article_page

#### 数据查询(DEFAULT) :id=article_page-Default
```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."cur_version_id",
t1."cur_version_name",
t1."format_type",
t1."icon",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_leaf",
t1."is_lock",
t1."is_published",
t1."is_shared",
t1."is_shared_subset",
t1."name",
t1."parent_id",
t1."published",
t1."publish_man",
t1."publish_name",
t1."publish_time",
CURRENT_DATE - t1."create_time"::date AS "recent_create_days",
t1."review_result_state",
t1."sequence",
concat(t11."identifier",'-',t1."identifier") AS "show_identifier",
t1."space_id",
t11."identifier" AS "space_identifier",
t11."name" AS "space_name",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "page" t1 
LEFT JOIN "space" t11 ON t1."space_id" = t11."id" 

```

#### 默认（全部数据）(VIEW) :id=article_page-View
```sql
SELECT
t1."access_password",
(SELECT COUNT( att.ID ) AS comment_count FROM page p LEFT JOIN attention att ON p.ID = att.OWNER_ID WHERE p.ID = t1."id") AS "attention_count",
t1."categories",
(SELECT COUNT( com.ID ) AS comment_count FROM page p LEFT JOIN comment com ON p.ID = com.PRINCIPAL_ID WHERE p.ID = t1."id") AS "comment_count",
t1."content",
t1."create_man",
t1."create_time",
t1."cur_version_id",
t1."cur_version_name",
t1."expiration_date",
t1."format_type",
t1."icon",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_leaf",
t1."is_lock",
t1."is_published",
t1."is_shared",
t1."is_shared_subset",
t1."name",
t1."parent_id",
t1."published",
t1."publish_content",
t1."publish_man",
t1."publish_name",
t1."publish_time",
CASE WHEN EXISTS (SELECT 1 FROM ( select id from page where is_shared = '1' ) AS ids WHERE ids.id = ANY(string_to_array(replace(t1.categories, '/', ','), ','))) THEN 1 ELSE 0 END AS "read_shared",
CURRENT_DATE - t1."create_time"::date AS "recent_create_days",
t1."review_result_state",
t1."sequence",
t1."shared_by",
t1."shared_time",
concat(t11."identifier",'-',t1."identifier") AS "show_identifier",
t1."space_id",
t11."identifier" AS "space_identifier",
t11."name" AS "space_name",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "page" t1 
LEFT JOIN "space" t11 ON t1."space_id" = t11."id" 

```

#### 高级搜索(advanced_search) :id=article_page-advanced_search
```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."cur_version_id",
t1."cur_version_name",
t1."format_type",
t1."icon",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_leaf",
t1."is_lock",
t1."is_published",
t1."is_shared",
t1."is_shared_subset",
t1."name",
t1."parent_id",
t1."published",
t1."publish_man",
t1."publish_name",
t1."publish_time",
CURRENT_DATE - t1."create_time"::date AS "recent_create_days",
t1."review_result_state",
t1."sequence",
concat(t11."identifier",'-',t1."identifier") AS "show_identifier",
t1."space_id",
t11."identifier" AS "space_identifier",
t11."name" AS "space_name",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "page" t1 
LEFT JOIN "space" t11 ON t1."space_id" = t11."id" 

WHERE ( t1."is_deleted" = 0  AND  exists(select 1 from space t2, space_member t3 where t1.space_id = t2.id and t2.id = t3.space_id and t3.user_id = #{ctx.sessioncontext.srfpersonid})  AND  t1."is_published" = 1  AND  t1."type" = '1' )
```

#### 全部共享页面查询(all_shared_pages) :id=article_page-all_shared_pages
```sql
SELECT
t1."expiration_date",
t1."id",
t1."is_shared",
t1."is_shared_subset",
t1."name",
t1."publish_name",
t1."shared_by",
t1."shared_time",
t1."space_id",
t1."update_man",
t1."update_time"
FROM "page" t1 

WHERE ( t1."is_shared" = '1'  AND  t1."is_deleted" = 0  AND  t1."is_published" = 1 )
```

#### 子页面(child_page) :id=article_page-child_page
```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."cur_version_id",
t1."cur_version_name",
t1."format_type",
t1."icon",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_leaf",
t1."is_lock",
t1."is_published",
t1."is_shared",
t1."is_shared_subset",
t1."name",
t1."parent_id",
t1."published",
t1."publish_man",
t1."publish_name",
t1."publish_time",
CURRENT_DATE - t1."create_time"::date AS "recent_create_days",
t1."review_result_state",
t1."sequence",
concat(t11."identifier",'-',t1."identifier") AS "show_identifier",
t1."space_id",
t11."identifier" AS "space_identifier",
t11."name" AS "space_name",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "page" t1 
LEFT JOIN "space" t11 ON t1."space_id" = t11."id" 

WHERE ( t1."parent_id" IS NOT NULL  AND  t1."is_published" = 1  AND  t1."is_deleted" = 0  AND  t1."is_archived" = 0 )
```

#### 选择共享页面(choose_shared) :id=article_page-choose_shared
```sql
SELECT
t1."icon",
t1."id",
t1."name",
t1."parent_id",
t1."publish_name",
t1."space_id"
FROM "page" t1 

WHERE ( t1."is_deleted" = 0  AND  t1."is_published" = 1 )
```

#### 草稿页面(draft_page) :id=article_page-draft_page
```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."cur_version_id",
t1."cur_version_name",
t1."format_type",
t1."icon",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_leaf",
t1."is_lock",
t1."is_published",
t1."is_shared",
t1."is_shared_subset",
t1."name",
t1."parent_id",
t1."published",
t1."publish_man",
t1."publish_name",
t1."publish_time",
CURRENT_DATE - t1."create_time"::date AS "recent_create_days",
t1."review_result_state",
t1."sequence",
concat(t11."identifier",'-',t1."identifier") AS "show_identifier",
t1."space_id",
t11."identifier" AS "space_identifier",
t11."name" AS "space_name",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "page" t1 
LEFT JOIN "space" t11 ON t1."space_id" = t11."id" 

WHERE ( t1."is_deleted" = 0  AND  t1."is_published" = 0  AND  t1."is_archived" = 0 )
```

#### 主页(home_page) :id=article_page-home_page
```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."cur_version_id",
t1."cur_version_name",
t1."format_type",
t1."icon",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_leaf",
t1."is_lock",
t1."is_published",
t1."is_shared",
t1."is_shared_subset",
t1."name",
t1."parent_id",
t1."published",
t1."publish_man",
t1."publish_name",
t1."publish_time",
CURRENT_DATE - t1."create_time"::date AS "recent_create_days",
t1."review_result_state",
t1."sequence",
concat(t11."identifier",'-',t1."identifier") AS "show_identifier",
t1."space_id",
t11."identifier" AS "space_identifier",
t11."name" AS "space_name",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "page" t1 
LEFT JOIN "space" t11 ON t1."space_id" = t11."id" 

WHERE ( t1."id" = #{ctx.webcontext.n_space_id_eq} )
```

#### 已删除页面(is_deleted) :id=article_page-is_deleted
```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."cur_version_id",
t1."cur_version_name",
t1."format_type",
t1."icon",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_leaf",
t1."is_lock",
t1."is_published",
t1."is_shared",
t1."is_shared_subset",
t1."name",
t1."parent_id",
t1."published",
t1."publish_man",
t1."publish_name",
t1."publish_time",
CURRENT_DATE - t1."create_time"::date AS "recent_create_days",
t1."review_result_state",
t1."sequence",
concat(t11."identifier",'-',t1."identifier") AS "show_identifier",
t1."space_id",
t11."identifier" AS "space_identifier",
t11."name" AS "space_name",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "page" t1 
LEFT JOIN "space" t11 ON t1."space_id" = t11."id" 

WHERE ( t1."is_deleted" = 1 )
```

#### 我的收藏(my_favorite_page) :id=article_page-my_favorite_page
```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."cur_version_id",
t1."cur_version_name",
t1."format_type",
t1."icon",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_leaf",
t1."is_lock",
t1."is_published",
t1."is_shared",
t1."is_shared_subset",
t1."name",
t1."parent_id",
t1."published",
t1."publish_man",
t1."publish_name",
t1."publish_time",
CURRENT_DATE - t1."create_time"::date AS "recent_create_days",
t1."review_result_state",
t1."sequence",
concat(t11."identifier",'-',t1."identifier") AS "show_identifier",
t1."space_id",
t11."identifier" AS "space_identifier",
t11."name" AS "space_name",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "page" t1 
LEFT JOIN "space" t11 ON t1."space_id" = t11."id" 

WHERE ( t11."is_deleted" = 0 ) AND ( t1."is_archived" = 0  AND  t1."is_deleted" = 0  AND  (select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) = '1' )
```

#### 过滤器默认查询(my_filter) :id=article_page-my_filter
```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."cur_version_id",
t1."cur_version_name",
t1."format_type",
t1."icon",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_leaf",
t1."is_lock",
t1."is_published",
t1."is_shared",
t1."is_shared_subset",
t1."name",
t1."parent_id",
t1."published",
t1."publish_man",
t1."publish_name",
t1."publish_time",
CURRENT_DATE - t1."create_time"::date AS "recent_create_days",
t1."review_result_state",
t1."sequence",
concat(t11."identifier",'-',t1."identifier") AS "show_identifier",
t1."space_id",
t11."identifier" AS "space_identifier",
t11."name" AS "space_name",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "page" t1 
LEFT JOIN "space" t11 ON t1."space_id" = t11."id" 

WHERE ( t11."is_deleted" = 0 ) AND ( t1."is_deleted" = 0  AND  t1."type" = '1'  AND  t1."is_archived" = 0  AND  t1."is_published" = 1 )
```

#### 无父页面(no_parent_page) :id=article_page-no_parent_page
```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."cur_version_id",
t1."cur_version_name",
t1."format_type",
t1."icon",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_leaf",
t1."is_lock",
t1."is_published",
t1."is_shared",
t1."is_shared_subset",
t1."name",
t1."parent_id",
t1."published",
t1."publish_man",
t1."publish_name",
t1."publish_time",
CURRENT_DATE - t1."create_time"::date AS "recent_create_days",
t1."review_result_state",
t1."sequence",
concat(t11."identifier",'-',t1."identifier") AS "show_identifier",
t1."space_id",
t11."identifier" AS "space_identifier",
t11."name" AS "space_name",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "page" t1 
LEFT JOIN "space" t11 ON t1."space_id" = t11."id" 

WHERE ( t1."parent_id" IS NULL  AND  t1."id" <> #{ctx.webcontext.n_space_id_eq}  AND  t1."is_archived" = 0  AND  t1."is_deleted" = 0  AND  t1."is_published" = 1 )
```

#### 正常(normal) :id=article_page-normal
```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."cur_version_id",
t1."cur_version_name",
t1."format_type",
t1."icon",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_leaf",
t1."is_lock",
t1."is_published",
t1."is_shared",
t1."is_shared_subset",
t1."name",
t1."parent_id",
t1."published",
t1."publish_man",
t1."publish_name",
t1."publish_time",
CURRENT_DATE - t1."create_time"::date AS "recent_create_days",
t1."review_result_state",
t1."sequence",
concat(t11."identifier",'-',t1."identifier") AS "show_identifier",
t1."space_id",
t11."identifier" AS "space_identifier",
t11."name" AS "space_name",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "page" t1 
LEFT JOIN "space" t11 ON t1."space_id" = t11."id" 

WHERE ( t1."is_deleted" = 0  AND  t1."is_archived" = 0  AND  t1."is_published" = 1 )
```

#### 仅页面(only_page) :id=article_page-only_page
```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."cur_version_id",
t1."cur_version_name",
t1."format_type",
t1."icon",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_leaf",
t1."is_lock",
t1."is_published",
t1."is_shared",
t1."is_shared_subset",
t1."name",
t1."parent_id",
t1."published",
t1."publish_man",
t1."publish_name",
t1."publish_time",
CURRENT_DATE - t1."create_time"::date AS "recent_create_days",
t1."review_result_state",
t1."sequence",
concat(t11."identifier",'-',t1."identifier") AS "show_identifier",
t1."space_id",
t11."identifier" AS "space_identifier",
t11."name" AS "space_name",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "page" t1 
LEFT JOIN "space" t11 ON t1."space_id" = t11."id" 

WHERE ( t1."is_deleted" = 0  AND  t1."is_published" = 1  AND  t1."type" = '1' )
```

#### public :id=article_page-public
```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."cur_version_id",
t1."cur_version_name",
t1."format_type",
t1."icon",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_leaf",
t1."is_lock",
t1."is_published",
t1."is_shared",
t1."is_shared_subset",
t1."name",
t1."parent_id",
t1."published",
t1."publish_man",
t1."publish_name",
t1."publish_time",
CURRENT_DATE - t1."create_time"::date AS "recent_create_days",
t1."review_result_state",
t1."sequence",
concat(t11."identifier",'-',t1."identifier") AS "show_identifier",
t1."space_id",
t11."identifier" AS "space_identifier",
t11."name" AS "space_name",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "page" t1 
LEFT JOIN "space" t11 ON t1."space_id" = t11."id" 

WHERE ( t11."visibility" = 'public' )
```

#### reader :id=article_page-reader
```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."cur_version_id",
t1."cur_version_name",
t1."format_type",
t1."icon",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_leaf",
t1."is_lock",
t1."is_published",
t1."is_shared",
t1."is_shared_subset",
t1."name",
t1."parent_id",
t1."published",
t1."publish_man",
t1."publish_name",
t1."publish_time",
CURRENT_DATE - t1."create_time"::date AS "recent_create_days",
t1."review_result_state",
t1."sequence",
concat(t11."identifier",'-',t1."identifier") AS "show_identifier",
t1."space_id",
t11."identifier" AS "space_identifier",
t11."name" AS "space_name",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "page" t1 
LEFT JOIN "space" t11 ON t1."space_id" = t11."id" 

WHERE EXISTS(SELECT * FROM "space_member" t21 
 WHERE 
 t11."id" = t21."space_id"  AND  ( t21."user_id" = #{ctx.sessioncontext.srfpersonid} ) )
```

#### 共享页面(shared_page) :id=article_page-shared_page
```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."cur_version_id",
t1."cur_version_name",
t1."format_type",
t1."icon",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_leaf",
t1."is_lock",
t1."is_published",
t1."is_shared",
t1."is_shared_subset",
t1."name",
t1."parent_id",
t1."published",
t1."publish_man",
t1."publish_name",
t1."publish_time",
CURRENT_DATE - t1."create_time"::date AS "recent_create_days",
t1."review_result_state",
t1."sequence",
concat(t11."identifier",'-',t1."identifier") AS "show_identifier",
t1."space_id",
t11."identifier" AS "space_identifier",
t11."name" AS "space_name",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "page" t1 
LEFT JOIN "space" t11 ON t1."space_id" = t11."id" 

WHERE ( t1."is_shared" = '1'  AND  t1."id" = #{ctx.webcontext.shared_page}  AND  t1."is_deleted" = 0  AND  t1."is_published" = 1 )
```

#### 共享自读权限(shared_reader) :id=article_page-shared_reader
```sql
SELECT
t1."id",
t1."is_shared",
CASE WHEN EXISTS (SELECT 1 FROM ( select id from page where is_shared = '1' ) AS ids WHERE ids.id = ANY(string_to_array(replace(t1.categories, '/', ','), ','))) THEN 1 ELSE 0 END AS "read_shared"
FROM "page" t1 

WHERE ( ( t1."is_shared" = '1'  OR  CASE WHEN EXISTS (SELECT 1 FROM ( select id from page where is_shared = '1' ) AS ids WHERE ids.id = ANY(string_to_array(replace(t1.categories, '/', ','), ','))) THEN 1 ELSE 0 END = '1' )  AND  t1."is_published" = 1  AND  t1."is_deleted" = 0 )
```

#### 共享搜索页面(shared_search) :id=article_page-shared_search
```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."cur_version_id",
t1."cur_version_name",
t1."format_type",
t1."icon",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_leaf",
t1."is_lock",
t1."is_published",
t1."is_shared",
t1."is_shared_subset",
t1."name",
t1."parent_id",
t1."published",
t1."publish_man",
t1."publish_name",
t1."publish_time",
CURRENT_DATE - t1."create_time"::date AS "recent_create_days",
t1."review_result_state",
t1."sequence",
concat(t11."identifier",'-',t1."identifier") AS "show_identifier",
t1."space_id",
t11."identifier" AS "space_identifier",
t11."name" AS "space_name",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "page" t1 
LEFT JOIN "space" t11 ON t1."space_id" = t11."id" 

WHERE ( t1."is_deleted" = 0  AND  t1."is_published" = 1  AND  t1."type" = '1'  AND  t1."categories" LIKE #{ctx.webcontext.shared_page} )
```

#### 共享子页面(shared_sub_pages) :id=article_page-shared_sub_pages
```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."cur_version_id",
t1."cur_version_name",
t1."format_type",
t1."icon",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_leaf",
t1."is_lock",
t1."is_published",
t1."is_shared",
t1."is_shared_subset",
t1."name",
t1."parent_id",
t1."published",
t1."publish_man",
t1."publish_name",
t1."publish_time",
CURRENT_DATE - t1."create_time"::date AS "recent_create_days",
t1."review_result_state",
t1."sequence",
concat(t11."identifier",'-',t1."identifier") AS "show_identifier",
t1."space_id",
t11."identifier" AS "space_identifier",
t11."name" AS "space_name",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "page" t1 
LEFT JOIN "space" t11 ON t1."space_id" = t11."id" 

WHERE ( t1."categories" LIKE #{ctx.webcontext.shared_page}  AND  t1."is_deleted" = 0  AND  t1."is_published" = 1 )
```

#### 与我共享(shared_with_me) :id=article_page-shared_with_me
```sql
SELECT
t1."expiration_date",
t1."id",
t1."is_shared",
t1."is_shared_subset",
t1."name",
t1."publish_name",
t1."shared_by",
t1."shared_time",
t1."space_id",
t1."update_man",
t1."update_time"
FROM "page" t1 
LEFT JOIN "space" t21 ON t1."space_id" = t21."id" 

WHERE EXISTS(SELECT * FROM "member" t11 
 WHERE 
 t1."id" = t11."owner_id"  AND  t11."owner_type" = 'PAGE'  AND  t11."owner_subtype" = 'SHARED'  AND  ( t11."user_id" = #{ctx.sessioncontext.srfuserid} ) ) AND ( t21."is_deleted" = 0 ) AND ( t1."is_deleted" = 0  AND  t1."is_published" = 1  AND  t1."is_shared" = '1' )
```

#### 与我共享编辑权限(shared_with_me_edit) :id=article_page-shared_with_me_edit
```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."cur_version_id",
t1."cur_version_name",
t1."format_type",
t1."icon",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_leaf",
t1."is_lock",
t1."is_published",
t1."is_shared",
t1."is_shared_subset",
t1."name",
t1."parent_id",
t1."published",
t1."publish_man",
t1."publish_name",
t1."publish_time",
CURRENT_DATE - t1."create_time"::date AS "recent_create_days",
t1."review_result_state",
t1."sequence",
concat(t11."identifier",'-',t1."identifier") AS "show_identifier",
t1."space_id",
t11."identifier" AS "space_identifier",
t11."name" AS "space_name",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "page" t1 
LEFT JOIN "space" t11 ON t1."space_id" = t11."id" 

WHERE EXISTS(SELECT * FROM "member" t21 
 WHERE 
 t1."id" = t21."owner_id"  AND  t21."owner_type" = 'PAGE'  AND  t21."owner_subtype" = 'SHARED'  AND  ( t21."user_id" = #{ctx.sessioncontext.srfpersonid}  AND  t21."role_id" = 'user' ) ) AND ( t1."is_shared" = '1'  AND  t1."is_published" = 1  AND  t1."is_deleted" = 0 )
```


## [附件(ATTACHMENT)](module/Base/attachment.md) :id=attachment

#### 数据查询(DEFAULT) :id=attachment-Default
```sql
SELECT
t1."create_man",
t1."create_time",
t1."file_id",
t1."id",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."parent_version_id",
t1."title",
t1."update_man",
t1."update_time"
FROM "attachment" t1 

```


## [关注(ATTENTION)](module/Base/attention.md) :id=attention

#### 数据查询(DEFAULT) :id=attention-Default
```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."title",
t1."type",
t1."update_man",
t1."update_time",
t1."user_id"
FROM "attention" t1 

```

#### 默认（全部数据）(VIEW) :id=attention-View
```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."title",
t1."type",
t1."update_man",
t1."update_time",
t1."user_id"
FROM "attention" t1 

```

#### 通过主数据标识查询通知对象(attention_by_ownerid) :id=attention-attention_by_ownerid
```sql
SELECT
t1."id",
t1."user_id"
FROM "attention" t1 

WHERE ( t1."owner_id" = #{ctx.webcontext.id}  AND  <choose><when test="ctx.webcontext.principal_id !=null ">  t1."owner_id" = #{ctx.webcontext.principal_id}  </when><otherwise>1=1</otherwise></choose>  AND  ( t1."type" = '30'  OR  t1."type" = '40' )  AND  t1."user_id" <> #{ctx.sessioncontext.srfpersonid} )
```

#### 评论提醒(comment_attention) :id=attention-comment_attention
```sql
SELECT
t1."id",
t1."user_id"
FROM "attention" t1 

WHERE ( exists(select 1 from `comment` t2 where t1.owner_id = t2.PRINCIPAL_ID and t2.id=#{ctx.webcontext.id})  AND  t1."type" = '40'  AND  t1."user_id" <> #{ctx.sessioncontext.srfpersonid} )
```

#### 通知对象(notify) :id=attention-notify
```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."title",
t1."type",
t1."update_man",
t1."update_time",
t1."user_id"
FROM "attention" t1 

WHERE ( t1."owner_id" = #{ctx.webcontext.principal_id} )
```


## [类别(CATEGORY)](module/Base/category.md) :id=category

#### 数据查询(DEFAULT) :id=category-Default
```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."id",
t1."is_deleted",
t1."is_leaf",
t1."is_leaf2",
t1."is_leaf3",
case when t1."is_leaf"+t1."is_leaf2"=2 then 1 else 0 end AS "leaf_flag",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."pid",
t1."section_id",
t11."name" AS "section_name",
t1."sequence",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2",
t1."wf_version_id"
FROM "category" t1 
LEFT JOIN "section" t11 ON t1."section_id" = t11."id" 

```

#### 默认（全部数据）(VIEW) :id=category-View
```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."id",
t1."is_deleted",
t1."is_leaf",
t1."is_leaf2",
t1."is_leaf3",
case when t1."is_leaf"+t1."is_leaf2"=2 then 1 else 0 end AS "leaf_flag",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."pid",
t1."section_id",
t11."name" AS "section_name",
t1."sequence",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2",
t1."wf_version_id"
FROM "category" t1 
LEFT JOIN "section" t11 ON t1."section_id" = t11."id" 

```

#### 知识库目录(ai_kb_category) :id=category-ai_kb_category
```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."id",
t1."is_deleted",
t1."is_leaf",
t1."is_leaf2",
t1."is_leaf3",
case when t1."is_leaf"+t1."is_leaf2"=2 then 1 else 0 end AS "leaf_flag",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."pid",
t1."section_id",
t11."name" AS "section_name",
t1."sequence",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2",
t1."wf_version_id"
FROM "category" t1 
LEFT JOIN "section" t11 ON t1."section_id" = t11."id" 

WHERE ( t1."owner_type" = 'ai_knowledge_base'  AND  t1."owner_subtype" = 'ai_knowledge_base' )
```

#### 知识库目录（顶级）(ai_kb_category_top) :id=category-ai_kb_category_top
```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."id",
t1."is_deleted",
t1."is_leaf",
t1."is_leaf2",
t1."is_leaf3",
case when t1."is_leaf"+t1."is_leaf2"=2 then 1 else 0 end AS "leaf_flag",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."pid",
t1."section_id",
t11."name" AS "section_name",
t1."sequence",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2",
t1."wf_version_id"
FROM "category" t1 
LEFT JOIN "section" t11 ON t1."section_id" = t11."id" 

WHERE ( t1."owner_type" = 'ai_knowledge_base'  AND  t1."owner_subtype" = 'ai_knowledge_base'  AND  t1."pid" IS NULL )
```

#### 检查名称是否重复(check_name) :id=category-check_name
```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."id",
t1."is_deleted",
t1."is_leaf",
t1."is_leaf2",
t1."is_leaf3",
case when t1."is_leaf"+t1."is_leaf2"=2 then 1 else 0 end AS "leaf_flag",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."pid",
t1."section_id",
t11."name" AS "section_name",
t1."sequence",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2",
t1."wf_version_id"
FROM "category" t1 
LEFT JOIN "section" t11 ON t1."section_id" = t11."id" 

WHERE ( <choose><when test="ctx.datacontext.id !=null ">  t1."id" <> #{ctx.datacontext.id}  </when><otherwise>1=1</otherwise></choose>  AND  <choose><when test="ctx.datacontext.name !=null ">  t1."name" = #{ctx.datacontext.name}  </when><otherwise>1=1</otherwise></choose>  AND  <choose><when test="ctx.datacontext.owner_id !=null ">  t1."owner_id" = #{ctx.datacontext.owner_id}  </when><otherwise>1=1</otherwise></choose>  AND  t1."owner_type" = #{ctx.datacontext.owner_type}  AND  <choose><when test="ctx.datacontext.owner_subtype !=null ">  t1."owner_subtype" = #{ctx.datacontext.owner_subtype}  </when><otherwise>1=1</otherwise></choose> )
```

#### 通用类别（代码表）(common_categories) :id=category-common_categories
```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."id",
t1."is_deleted",
t1."is_leaf",
t1."is_leaf2",
t1."is_leaf3",
case when t1."is_leaf"+t1."is_leaf2"=2 then 1 else 0 end AS "leaf_flag",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."pid",
t1."section_id",
t11."name" AS "section_name",
t1."sequence",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2",
t1."wf_version_id"
FROM "category" t1 
LEFT JOIN "section" t11 ON t1."section_id" = t11."id" 

WHERE ( <choose><when test="ctx.webcontext.product !=null ">  t1."owner_id" = #{ctx.webcontext.product}  </when><otherwise>1=1</otherwise></choose>  AND  <choose><when test="ctx.webcontext.project !=null ">  t1."owner_id" = #{ctx.webcontext.project}  </when><otherwise>1=1</otherwise></choose> )
```

#### 当前产品需求类别(cur_product_idea_category) :id=category-cur_product_idea_category
```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."id",
t1."is_deleted",
t1."is_leaf",
t1."is_leaf2",
t1."is_leaf3",
case when t1."is_leaf"+t1."is_leaf2"=2 then 1 else 0 end AS "leaf_flag",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."pid",
t1."section_id",
t11."name" AS "section_name",
t1."sequence",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2",
t1."wf_version_id"
FROM "category" t1 
LEFT JOIN "section" t11 ON t1."section_id" = t11."id" 

WHERE ( t1."owner_type" = 'product'  AND  t1."owner_subtype" = 'idea'  AND  t1."owner_id" = #{ctx.datacontext.product} )
```

#### 我的类别(my_category) :id=category-my_category
```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."id",
t1."is_deleted",
t1."is_leaf",
t1."is_leaf2",
t1."is_leaf3",
case when t1."is_leaf"+t1."is_leaf2"=2 then 1 else 0 end AS "leaf_flag",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."pid",
t1."section_id",
t11."name" AS "section_name",
t1."sequence",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2",
t1."wf_version_id"
FROM "category" t1 
LEFT JOIN "section" t11 ON t1."section_id" = t11."id" 

WHERE ( t1."create_man" = #{ctx.sessioncontext.srfpersonid} )
```

#### 无父类(no_parent) :id=category-no_parent
```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."id",
t1."is_deleted",
t1."is_leaf",
t1."is_leaf2",
t1."is_leaf3",
case when t1."is_leaf"+t1."is_leaf2"=2 then 1 else 0 end AS "leaf_flag",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."pid",
t1."section_id",
t11."name" AS "section_name",
t1."sequence",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2",
t1."wf_version_id"
FROM "category" t1 
LEFT JOIN "section" t11 ON t1."section_id" = t11."id" 

WHERE ( t1."pid" IS NULL )
```

#### 无分组的类别（且父标识不为空）(no_section) :id=category-no_section
```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."id",
t1."is_deleted",
t1."is_leaf",
t1."is_leaf2",
t1."is_leaf3",
case when t1."is_leaf"+t1."is_leaf2"=2 then 1 else 0 end AS "leaf_flag",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."pid",
t1."section_id",
t11."name" AS "section_name",
t1."sequence",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2",
t1."wf_version_id"
FROM "category" t1 
LEFT JOIN "section" t11 ON t1."section_id" = t11."id" 

WHERE ( t1."section_id" IS NULL  AND  t1."pid" IS NULL )
```

#### 职位类别(position_category) :id=category-position_category
```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."id",
t1."is_deleted",
t1."is_leaf",
t1."is_leaf2",
t1."is_leaf3",
case when t1."is_leaf"+t1."is_leaf2"=2 then 1 else 0 end AS "leaf_flag",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."pid",
t1."section_id",
t11."name" AS "section_name",
t1."sequence",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2",
t1."wf_version_id"
FROM "category" t1 
LEFT JOIN "section" t11 ON t1."section_id" = t11."id" 

WHERE ( t1."owner_type" = 'position' )
```

#### 主模块(product_idea_category) :id=category-product_idea_category
```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."id",
t1."is_deleted",
t1."is_leaf",
t1."is_leaf2",
t1."is_leaf3",
case when t1."is_leaf"+t1."is_leaf2"=2 then 1 else 0 end AS "leaf_flag",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."pid",
t1."section_id",
t11."name" AS "section_name",
t1."sequence",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2",
t1."wf_version_id"
FROM "category" t1 
LEFT JOIN "section" t11 ON t1."section_id" = t11."id" 

WHERE ( t1."pid" IS NULL )
```

#### 排期计划类别(product_plan) :id=category-product_plan
```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."id",
t1."is_deleted",
t1."is_leaf",
t1."is_leaf2",
t1."is_leaf3",
case when t1."is_leaf"+t1."is_leaf2"=2 then 1 else 0 end AS "leaf_flag",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."pid",
t1."section_id",
t11."name" AS "section_name",
t1."sequence",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2",
t1."wf_version_id"
FROM "category" t1 
LEFT JOIN "section" t11 ON t1."section_id" = t11."id" 

WHERE ( t1."owner_type" = 'product'  AND  t1."owner_subtype" = 'product_plan'  AND  <choose><when test="ctx.webcontext.product !=null ">  t1."owner_id" = #{ctx.webcontext.product}  </when><otherwise>1=1</otherwise></choose> )
```

#### 空间目录(space_category) :id=category-space_category
```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."id",
t1."is_deleted",
t1."is_leaf",
t1."is_leaf2",
t1."is_leaf3",
case when t1."is_leaf"+t1."is_leaf2"=2 then 1 else 0 end AS "leaf_flag",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."pid",
t1."section_id",
t11."name" AS "section_name",
t1."sequence",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2",
t1."wf_version_id"
FROM "category" t1 
LEFT JOIN "section" t11 ON t1."section_id" = t11."id" 

WHERE ( t1."owner_type" = 'space'  AND  t1."owner_subtype" = 'space' )
```

#### 空间目录（顶级）(space_category_top) :id=category-space_category_top
```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."id",
t1."is_deleted",
t1."is_leaf",
t1."is_leaf2",
t1."is_leaf3",
case when t1."is_leaf"+t1."is_leaf2"=2 then 1 else 0 end AS "leaf_flag",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."pid",
t1."section_id",
t11."name" AS "section_name",
t1."sequence",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2",
t1."wf_version_id"
FROM "category" t1 
LEFT JOIN "section" t11 ON t1."section_id" = t11."id" 

WHERE ( t1."owner_type" = 'space'  AND  t1."owner_subtype" = 'space'  AND  t1."pid" IS NULL )
```

#### 工作流类别(wf_category) :id=category-wf_category
```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."id",
t1."is_deleted",
t1."is_leaf",
t1."is_leaf2",
t1."is_leaf3",
case when t1."is_leaf"+t1."is_leaf2"=2 then 1 else 0 end AS "leaf_flag",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."pid",
t1."section_id",
t11."name" AS "section_name",
t1."sequence",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2",
t1."wf_version_id"
FROM "category" t1 
LEFT JOIN "section" t11 ON t1."section_id" = t11."id" 

WHERE ( t1."owner_type" = 'workflow'  AND  t1."is_deleted" = 0 )
```


## [类别设置(CATEGORY_SETTINGS)](module/Base/category_settings.md) :id=category_settings

#### DEFAULT :id=category_settings-Default
```sql
SELECT
t1."auto_gen_kb",
t11."name" AS "chat_model",
t1."chat_model_id",
t1."chunk_method",
t1."create_man",
t1."create_time",
t71."name" AS "embedding_model",
t1."embedding_model_id",
t1."enable",
t31."name" AS "flash_model",
t1."flash_model_id",
t1."guided_prompt_agent_id",
t1."id",
t51."name" AS "intent_model",
t1."intent_model_id",
t1."name",
t1."rerank",
t21."name" AS "rerank_model",
t1."rerank_model_id",
t61."name" AS "resource",
t61."resource_code",
t1."resource_id",
t1."similarity_threshold",
t1."source_id",
t1."source_name",
t1."top_k",
t1."update_man",
t1."update_time",
t1."use_kg",
t1."vector_similarity_weight",
t1."visibility",
t41."name" AS "vl_model",
t1."vl_model_id"
FROM "category_settings" t1 
LEFT JOIN "ai_model" t11 ON t1."chat_model_id" = t11."id" 
LEFT JOIN "ai_model" t21 ON t1."rerank_model_id" = t21."id" 
LEFT JOIN "ai_model" t31 ON t1."flash_model_id" = t31."id" 
LEFT JOIN "ai_model" t41 ON t1."vl_model_id" = t41."id" 
LEFT JOIN "ai_model" t51 ON t1."intent_model_id" = t51."id" 
LEFT JOIN "data_resource" t61 ON t1."resource_id" = t61."id" 
LEFT JOIN "ai_model" t71 ON t1."embedding_model_id" = t71."id" 

```

#### 默认（全部数据）(VIEW) :id=category_settings-View
```sql
SELECT
t1."auto_gen_kb",
t11."name" AS "chat_model",
t1."chat_model_id",
t1."chunk_method",
t1."configs",
t1."create_man",
t1."create_time",
t71."name" AS "embedding_model",
t1."embedding_model_id",
t1."enable",
t31."name" AS "flash_model",
t1."flash_model_id",
t1."guided_prompt_agent_id",
t1."id",
t51."name" AS "intent_model",
t1."intent_model_id",
t1."name",
t1."parser_config",
t1."rerank",
t21."name" AS "rerank_model",
t1."rerank_model_id",
t61."name" AS "resource",
t61."resource_code",
t1."resource_id",
t1."similarity_threshold",
t1."source_id",
t1."source_name",
t1."top_k",
t1."update_man",
t1."update_time",
t1."use_kg",
t1."vector_similarity_weight",
t1."visibility",
t41."name" AS "vl_model",
t1."vl_model_id"
FROM "category_settings" t1 
LEFT JOIN "ai_model" t11 ON t1."chat_model_id" = t11."id" 
LEFT JOIN "ai_model" t21 ON t1."rerank_model_id" = t21."id" 
LEFT JOIN "ai_model" t31 ON t1."flash_model_id" = t31."id" 
LEFT JOIN "ai_model" t41 ON t1."vl_model_id" = t41."id" 
LEFT JOIN "ai_model" t51 ON t1."intent_model_id" = t51."id" 
LEFT JOIN "data_resource" t61 ON t1."resource_id" = t61."id" 
LEFT JOIN "ai_model" t71 ON t1."embedding_model_id" = t71."id" 

```


## [评论(COMMENT)](module/Base/comment.md) :id=comment

#### 数据查询(DEFAULT) :id=comment-Default
```sql
SELECT
t1."content",
t1."create_man",
t1."create_time",
t1."id",
t1."is_top",
t1."name",
t1."owner_type",
t11."content" AS "pcontent",
t11."create_man" AS "pcreate_man",
t1."pid",
t1."principal_id",
t1."principal_name",
t1."principal_type",
t1."update_man",
t1."update_time"
FROM "comment" t1 
LEFT JOIN "comment" t11 ON t1."pid" = t11."id" 

```


## [通用规则(COMMON_FLOW)](module/Base/common_flow.md) :id=common_flow

#### DEFAULT :id=common_flow-Default
```sql
SELECT
t1."create_man",
t1."create_time",
t1."enable",
t1."id",
t1."name",
t1."update_man",
t1."update_time"
FROM "common_flow" t1 

```

#### 默认（全部数据）(VIEW) :id=common_flow-View
```sql
SELECT
t1."create_man",
t1."create_time",
t1."enable",
t1."id",
t1."name",
t1."update_man",
t1."update_time"
FROM "common_flow" t1 

```


## [数据记录(DATA_RECORD)](module/meta/data_record.md) :id=data_record

#### DEFAULT :id=data_record-Default
```sql
SELECT
t1."_create_time",
t1."_creator",
t1."_enabled",
t1."_id",
t1."_key",
t1."_ner_flag",
t1."_region",
t11."resource_code" AS "_resource_code",
t1."_resource_id",
t11."name" AS "_resource_name",
t1."_title",
t1."_updater",
t1."_update_time"
FROM "data_record" t1 
LEFT JOIN "data_resource" t11 ON t1."_resource_id" = t11."id" 

WHERE t1._enabled = 1
```

#### 默认（全部数据）(VIEW) :id=data_record-View
```sql
SELECT
t1."_create_time",
t1."_creator",
t1."_enabled",
t1."_id",
t1."_key",
t1."_ner_flag",
t1."_region",
t11."resource_code" AS "_resource_code",
t1."_resource_id",
t11."name" AS "_resource_name",
t1."_summary",
t1."_title",
t1."_updater",
t1."_update_time"
FROM "data_record" t1 
LEFT JOIN "data_resource" t11 ON t1."_resource_id" = t11."id" 

WHERE t1._enabled = 1
```


## [数据资源(DATA_RESOURCE)](module/meta/data_resource.md) :id=data_resource

#### DEFAULT :id=data_resource-Default
```sql
SELECT
t1."create_time",
t1."enabled",
t1."id",
t1."name",
t1."resource_code",
t1."sort",
t1."update_time"
FROM "data_resource" t1 

WHERE t1.enabled = 1
```

#### 默认（全部数据）(VIEW) :id=data_resource-View
```sql
SELECT
t1."create_time",
t1."enabled",
t1."id",
t1."name",
t1."resource_code",
t1."schema",
t1."sort",
t1."update_time"
FROM "data_resource" t1 

WHERE t1.enabled = 1
```


## [数据字典(DICTIONARY)](module/Base/dictionary_data.md) :id=dictionary_data

#### 数据查询(DEFAULT) :id=dictionary_data-Default
```sql
SELECT
t1."catalog",
t1."color",
t1."create_man",
t1."create_time",
t1."description",
t1."icon",
t1."id",
t1."is_system",
t1."name",
t1."sequence",
t1."style",
t1."type",
t1."update_man",
t1."update_time",
t1."val"
FROM "dictionary" t1 

```

#### 默认（全部数据）(VIEW) :id=dictionary_data-View
```sql
SELECT
t1."catalog",
t1."color",
t1."create_man",
t1."create_time",
t1."description",
t1."icon",
t1."id",
t1."is_system",
t1."name",
t1."sequence",
t1."style",
t1."type",
t1."update_man",
t1."update_time",
t1."val"
FROM "dictionary" t1 

```

#### 知识库文档导入方式(ai_kb_doc_import_method) :id=dictionary_data-ai_kb_doc_import_method
```sql
SELECT
t1."catalog",
t1."color",
t1."create_man",
t1."create_time",
t1."description",
t1."icon",
t1."id",
t1."is_system",
t1."name",
t1."sequence",
t1."style",
t1."type",
t1."update_man",
t1."update_time",
t1."val"
FROM "dictionary" t1 

WHERE ( t1."type" = 'ai_kb_doc_import_method' )
```


## [动态数据看板(DYNADASHBOARD)](module/Base/dyna_dashboard.md) :id=dyna_dashboard

#### 数据查询(DEFAULT) :id=dyna_dashboard-Default
```sql
SELECT
t1."appid",
t1."createdate",
t1."createman",
t1."dynadashboardid",
t1."dynadashboardname",
t1."example_chart",
t1."is_system",
t1."modelid",
t1."owner_id",
t1."owner_type",
t1."sequences",
t1."type",
t1."update_man",
t1."update_time",
t1."userid"
FROM "dynadashboard" t1 

```

#### 默认（全部数据）(VIEW) :id=dyna_dashboard-View
```sql
SELECT
t1."appid",
t1."createdate",
t1."createman",
t1."description",
t1."dynadashboardid",
t1."dynadashboardname",
t1."example_chart",
t1."is_system",
t1."model",
t1."modelid",
t1."owner_id",
t1."owner_type",
t1."sequences",
t1."type",
t1."update_man",
t1."update_time",
t1."userid"
FROM "dynadashboard" t1 

```

#### 示例图(example_chart) :id=dyna_dashboard-example_chart
```sql
SELECT
t1."appid",
t1."description",
t1."dynadashboardid",
t1."dynadashboardname",
t1."example_chart",
t1."is_system",
t1."modelid",
t1."sequences",
t1."type"
FROM "dynadashboard" t1 

WHERE ( t1."is_system" = 1 )
```

#### 系统仪表盘(is_system) :id=dyna_dashboard-is_system
```sql
SELECT
t1."appid",
t1."createdate",
t1."createman",
t1."dynadashboardid",
t1."dynadashboardname",
t1."example_chart",
t1."is_system",
t1."modelid",
t1."owner_id",
t1."owner_type",
t1."sequences",
t1."type",
t1."update_man",
t1."update_time",
t1."userid"
FROM "dynadashboard" t1 

WHERE ( t1."is_system" = 1 )
```

#### 我的看板(my_dashboard) :id=dyna_dashboard-my_dashboard
```sql
SELECT
t1."appid",
t1."createdate",
t1."createman",
t1."dynadashboardid",
t1."dynadashboardname",
t1."example_chart",
t1."is_system",
t1."modelid",
t1."owner_id",
t1."owner_type",
t1."sequences",
t1."type",
t1."update_man",
t1."update_time",
t1."userid"
FROM "dynadashboard" t1 

WHERE ( t1."createman" = #{ctx.sessioncontext.srfpersonid} )
```

#### 正常数据(normal) :id=dyna_dashboard-normal
```sql
SELECT
t1."appid",
t1."createdate",
t1."createman",
t1."dynadashboardid",
t1."dynadashboardname",
t1."example_chart",
t1."is_system",
t1."modelid",
t1."owner_id",
t1."owner_type",
t1."sequences",
t1."type",
t1."update_man",
t1."update_time",
t1."userid"
FROM "dynadashboard" t1 

```


## [扩展日志(EXTEND_LOG)](module/Base/extend_log.md) :id=extend_log

#### 数据查询(DEFAULT) :id=extend_log-Default
```sql
SELECT
t1."category",
t1."create_man",
t1."create_time",
t1."elapsed_time",
t1."end_at",
t1."id",
t1."level",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."start_at",
t1."state",
t1."update_man",
t1."update_time"
FROM "extend_log" t1 

```

#### 默认（全部数据）(VIEW) :id=extend_log-View
```sql
SELECT
t1."category",
t1."create_man",
t1."create_time",
t1."debug_info",
t1."elapsed_time",
t1."end_at",
t1."id",
t1."info",
t1."level",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."start_at",
t1."state",
t1."update_man",
t1."update_time"
FROM "extend_log" t1 

```


## [扩展执行计划(EXTEND_SCHEDULE)](module/Base/extend_schedule.md) :id=extend_schedule

#### DEFAULT :id=extend_schedule-Default
```sql
SELECT
t1."create_man",
t1."create_time",
t1."description",
t1."enable",
t1."id",
t1."name",
t1."next_trigger_time",
t1."principal_id",
t1."principal_name",
t1."principal_type",
t1."schedule_type",
t1."task_type",
t11."name" AS "task_type_name",
t1."timer_policy",
t1."update_man",
t1."update_time"
FROM "extend_schedule" t1 
LEFT JOIN "extend_task_type" t11 ON t1."task_type" = t11."id" 

```

#### 启用(VALID) :id=extend_schedule-Valid
```sql
SELECT
t1."create_man",
t1."create_time",
t1."description",
t1."enable",
t1."id",
t1."name",
t1."next_trigger_time",
t1."payload",
t1."principal_id",
t1."principal_name",
t1."principal_type",
t1."schedule_type",
t1."task_type",
t11."name" AS "task_type_name",
t1."timer_policy",
t1."update_man",
t1."update_time"
FROM "extend_schedule" t1 
LEFT JOIN "extend_task_type" t11 ON t1."task_type" = t11."id" 

```

#### 默认（全部数据）(VIEW) :id=extend_schedule-View
```sql
SELECT
t1."create_man",
t1."create_time",
t1."description",
t1."enable",
t1."id",
t1."name",
t1."next_trigger_time",
t1."payload",
t1."principal_id",
t1."principal_name",
t1."principal_type",
t1."schedule_type",
t1."task_type",
t11."name" AS "task_type_name",
t1."timer_policy",
t1."update_man",
t1."update_time"
FROM "extend_schedule" t1 
LEFT JOIN "extend_task_type" t11 ON t1."task_type" = t11."id" 

```


## [扩展计划任务(EXTEND_SCHEDULED_TASK)](module/Base/extend_scheduled_task.md) :id=extend_scheduled_task

#### DEFAULT :id=extend_scheduled_task-Default
```sql
SELECT
t1."create_man",
t1."create_time",
t1."description",
t1."enable",
t11."executor_tag",
t1."finished_at",
t1."id",
t1."max_retry",
t1."name",
t1."principal_id",
t1."principal_name",
t1."principal_type",
t1."result_message",
t1."retry_count",
t1."scheduled_at",
t1."schedule_id",
t1."started_at",
t1."status",
t1."task_type",
t11."name" AS "task_type_name",
t1."update_man",
t1."update_time"
FROM "extend_scheduled_task" t1 
LEFT JOIN "extend_task_type" t11 ON t1."task_type" = t11."id" 

```

#### 默认（全部数据）(VIEW) :id=extend_scheduled_task-View
```sql
SELECT
t1."create_man",
t1."create_time",
t1."description",
t1."enable",
t11."executor_tag",
t1."finished_at",
t1."id",
t1."max_retry",
t1."name",
t1."payload",
t1."principal_id",
t1."principal_name",
t1."principal_type",
t1."result",
t1."result_message",
t1."retry_count",
t1."scheduled_at",
t1."schedule_id",
t1."started_at",
t1."status",
t1."task_type",
t11."name" AS "task_type_name",
t1."update_man",
t1."update_time"
FROM "extend_scheduled_task" t1 
LEFT JOIN "extend_task_type" t11 ON t1."task_type" = t11."id" 

```


## [扩展计划任务历史(EXTEND_SCHEDULED_TASK_HIS)](module/Base/extend_scheduled_task_his.md) :id=extend_scheduled_task_his

#### DEFAULT :id=extend_scheduled_task_his-Default
```sql
SELECT
t1."create_man",
t1."create_time",
t1."description",
t1."enable",
t1."finished_at",
t1."id",
t1."max_retry",
t1."name",
t1."principal_id",
t1."principal_name",
t1."principal_type",
t1."result_message",
t1."retry_count",
t1."scheduled_at",
t1."started_at",
t1."status",
t1."task_type",
t11."name" AS "task_type_name",
t1."update_man",
t1."update_time"
FROM "extend_scheduled_task_his" t1 
LEFT JOIN "extend_task_type" t11 ON t1."task_type" = t11."id" 

```

#### 默认（全部数据）(VIEW) :id=extend_scheduled_task_his-View
```sql
SELECT
t1."create_man",
t1."create_time",
t1."description",
t1."enable",
t1."finished_at",
t1."id",
t1."max_retry",
t1."name",
t1."payload",
t1."principal_id",
t1."principal_name",
t1."principal_type",
t1."result",
t1."result_message",
t1."retry_count",
t1."scheduled_at",
t1."started_at",
t1."status",
t1."task_type",
t11."name" AS "task_type_name",
t1."update_man",
t1."update_time"
FROM "extend_scheduled_task_his" t1 
LEFT JOIN "extend_task_type" t11 ON t1."task_type" = t11."id" 

```


## [扩展任务类型(EXTEND_TASK_TYPE)](module/Base/extend_task_type.md) :id=extend_task_type

#### DEFAULT :id=extend_task_type-Default
```sql
SELECT
t1."create_man",
t1."create_time",
t1."description",
t1."executor_subtype",
t1."executor_tag",
t1."executor_type",
t1."id",
t1."max_retry",
t1."name",
t1."retryable",
t1."timeout_sec",
t1."update_man",
t1."update_time"
FROM "extend_task_type" t1 

```

#### 默认（全部数据）(VIEW) :id=extend_task_type-View
```sql
SELECT
t1."code",
t1."create_man",
t1."create_time",
t1."description",
t1."executor_config",
t1."executor_subtype",
t1."executor_tag",
t1."executor_type",
t1."id",
t1."max_retry",
t1."name",
t1."retryable",
t1."timeout_sec",
t1."update_man",
t1."update_time"
FROM "extend_task_type" t1 

```


## [收藏(FAVORITE)](module/Base/favorite.md) :id=favorite

#### 数据查询(DEFAULT) :id=favorite-Default
```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."update_man",
t1."update_time"
FROM "favorite" t1 

```

#### 默认（全部数据）(VIEW) :id=favorite-View
```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."update_man",
t1."update_time"
FROM "favorite" t1 

```

#### 我的收藏(my_favorite) :id=favorite-my_favorite
```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."update_man",
t1."update_time"
FROM "favorite" t1 

WHERE ( t1."create_man" = #{ctx.sessioncontext.srfpersonid} )
```


## [团队(GROUP)](module/Base/group.md) :id=group

#### 数据查询(DEFAULT) :id=group-Default
```sql
SELECT
t1."avatar",
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."name",
t1."section_id",
t11."name" AS "section_name",
t1."sequence",
t1."update_man",
t1."update_time",
t1."visibility"
FROM "user_group" t1 
LEFT JOIN "section" t11 ON t1."section_id" = t11."id" 

```

#### 默认（全部数据）(VIEW) :id=group-View
```sql
SELECT
t1."avatar",
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."name",
t1."section_id",
t11."name" AS "section_name",
t1."sequence",
t1."update_man",
t1."update_time",
t1."visibility"
FROM "user_group" t1 
LEFT JOIN "section" t11 ON t1."section_id" = t11."id" 

```

#### 无分组(no_section) :id=group-no_section
```sql
SELECT
t1."avatar",
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."name",
t1."section_id",
t11."name" AS "section_name",
t1."sequence",
t1."update_man",
t1."update_time",
t1."visibility"
FROM "user_group" t1 
LEFT JOIN "section" t11 ON t1."section_id" = t11."id" 

WHERE ( t1."section_id" IS NULL )
```

#### 公开(public) :id=group-public
```sql
SELECT
t1."avatar",
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."name",
t1."section_id",
t11."name" AS "section_name",
t1."sequence",
t1."update_man",
t1."update_time",
t1."visibility"
FROM "user_group" t1 
LEFT JOIN "section" t11 ON t1."section_id" = t11."id" 

WHERE ( t1."visibility" = 'public' )
```

#### 团队成员(user) :id=group-user
```sql
SELECT
t1."avatar",
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."name",
t1."section_id",
t11."name" AS "section_name",
t1."sequence",
t1."update_man",
t1."update_time",
t1."visibility"
FROM "user_group" t1 
LEFT JOIN "section" t11 ON t1."section_id" = t11."id" 

WHERE EXISTS(SELECT * FROM "member" t21 
 WHERE 
 t1."id" = t21."owner_id"  AND  t21."owner_type" = 'GROUP'  AND  t21."owner_subtype" = 'GROUP'  AND  ( t21."user_id" = #{ctx.sessioncontext.srfpersonid}  AND  t21."owner_type" = 'GROUP' ) )
```

#### 团队管理员(user_group_admin) :id=group-user_group_admin
```sql
SELECT
t1."avatar",
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."name",
t1."section_id",
t11."name" AS "section_name",
t1."sequence",
t1."update_man",
t1."update_time",
t1."visibility"
FROM "user_group" t1 
LEFT JOIN "section" t11 ON t1."section_id" = t11."id" 

WHERE EXISTS(SELECT * FROM "member" t21 
 WHERE 
 t1."id" = t21."owner_id"  AND  t21."owner_type" = 'GROUP'  AND  t21."owner_subtype" = 'GROUP'  AND  ( t21."user_id" = #{ctx.sessioncontext.srfpersonid}  AND  t21."owner_type" = 'GROUP'  AND  t21."role_id" = 'admin' ) )
```


## [效能成员(INSIGHT_MEMBER)](module/Insight/insight_member.md) :id=insight_member

#### 数据查询(DEFAULT) :id=insight_member-Default
```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."role_id",
t1."title",
t1."update_man",
t1."update_time",
t1."user_id"
FROM "member" t1 

```

#### 默认（全部数据）(VIEW) :id=insight_member-View
```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."role_id",
t1."title",
t1."update_man",
t1."update_time",
t1."user_id"
FROM "member" t1 

```


## [效能报表(INSIGHT_REPORT)](module/Insight/insight_report.md) :id=insight_report

#### 数据查询(DEFAULT) :id=insight_report-Default
```sql
SELECT
t1."app_tag",
t1."categories",
t1."category",
t1."chart_type",
t1."create_man",
t1."create_time",
t1."id",
t1."is_system",
t1."name",
t1."update_man",
t1."update_time",
t1."view_id",
t11."name" AS "view_name"
FROM "insight_report" t1 
LEFT JOIN "insight_view" t11 ON t1."view_id" = t11."id" 

```

#### 默认（全部数据）(VIEW) :id=insight_report-View
```sql
SELECT
t1."app_tag",
t1."categories",
t1."category",
t1."chart_type",
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."is_system",
t1."name",
t1."template_model",
t1."update_man",
t1."update_time",
t1."view_id",
t11."name" AS "view_name"
FROM "insight_report" t1 
LEFT JOIN "insight_view" t11 ON t1."view_id" = t11."id" 

```

#### 模板报表(is_system) :id=insight_report-is_system
```sql
SELECT
t1."app_tag",
t1."categories",
t1."category",
t1."chart_type",
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."is_system",
t1."name",
t1."template_model",
t1."update_man",
t1."update_time",
t1."view_id",
t11."name" AS "view_name"
FROM "insight_report" t1 
LEFT JOIN "insight_view" t11 ON t1."view_id" = t11."id" 

WHERE ( t1."is_system" = 1 )
```

#### 正常数据(normal) :id=insight_report-normal
```sql
SELECT
t1."app_tag",
t1."categories",
t1."category",
t1."chart_type",
t1."create_man",
t1."create_time",
t1."id",
t1."is_system",
t1."name",
t1."update_man",
t1."update_time",
t1."view_id",
t11."name" AS "view_name"
FROM "insight_report" t1 
LEFT JOIN "insight_view" t11 ON t1."view_id" = t11."id" 

```


## [效能视图(INSIGHT_VIEW)](module/Insight/insight_view.md) :id=insight_view

#### 数据查询(DEFAULT) :id=insight_view-Default
```sql
SELECT
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."name",
t1."scope_id",
t1."scope_type",
t1."update_man",
t1."update_time",
t1."visibility"
FROM "insight_view" t1 

```

#### 默认（全部数据）(VIEW) :id=insight_view-View
```sql
SELECT
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."name",
t1."scope_id",
t1."scope_type",
t1."update_man",
t1."update_time",
t1."visibility"
FROM "insight_view" t1 

```

#### 管理员(admin) :id=insight_view-admin
```sql
SELECT
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."name",
t1."scope_id",
t1."scope_type",
t1."update_man",
t1."update_time",
t1."visibility"
FROM "insight_view" t1 

WHERE EXISTS(SELECT * FROM "member" t11 
 WHERE 
 t1."id" = t11."owner_id"  AND  ( t11."user_id" = #{ctx.sessioncontext.srfpersonid}  AND  t11."role_id" = 'admin'  AND  t11."owner_type" = 'INSIGHT' ) )
```

#### 已删除(deleted) :id=insight_view-deleted
```sql
SELECT
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."name",
t1."scope_id",
t1."scope_type",
t1."update_man",
t1."update_time",
t1."visibility"
FROM "insight_view" t1 

WHERE ( t1."is_deleted" = 1 )
```

#### 星标页面(favorite) :id=insight_view-favorite
```sql
SELECT
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."name",
t1."scope_id",
t1."scope_type",
t1."update_man",
t1."update_time",
t1."visibility"
FROM "insight_view" t1 

WHERE ( t1."is_archived" = 0  AND  t1."is_deleted" = 0  AND  (select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) = '1' )
```

#### 正常状态(normal) :id=insight_view-normal
```sql
SELECT
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."name",
t1."scope_id",
t1."scope_type",
t1."update_man",
t1."update_time",
t1."visibility"
FROM "insight_view" t1 

WHERE ( t1."is_archived" = 0  AND  t1."is_deleted" = 0 )
```

#### 公开(public) :id=insight_view-public
```sql
SELECT
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."name",
t1."scope_id",
t1."scope_type",
t1."update_man",
t1."update_time",
t1."visibility"
FROM "insight_view" t1 

WHERE ( t1."visibility" = 'public' )
```

#### 只读用户(reader) :id=insight_view-reader
```sql
SELECT
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."name",
t1."scope_id",
t1."scope_type",
t1."update_man",
t1."update_time",
t1."visibility"
FROM "insight_view" t1 

WHERE EXISTS(SELECT * FROM "member" t11 
 WHERE 
 t1."id" = t11."owner_id"  AND  ( t11."user_id" = #{ctx.sessioncontext.srfpersonid}  AND  t11."role_id" = 'reader'  AND  t11."owner_type" = 'INSIGHT' ) )
```

#### 非星标(unfavorite) :id=insight_view-unfavorite
```sql
SELECT
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."name",
t1."scope_id",
t1."scope_type",
t1."update_man",
t1."update_time",
t1."visibility"
FROM "insight_view" t1 

WHERE ( t1."is_archived" = 0  AND  t1."is_deleted" = 0  AND  (select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) = '0' )
```

#### 操作用户(user) :id=insight_view-user
```sql
SELECT
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."name",
t1."scope_id",
t1."scope_type",
t1."update_man",
t1."update_time",
t1."visibility"
FROM "insight_view" t1 

WHERE EXISTS(SELECT * FROM "member" t11 
 WHERE 
 t1."id" = t11."owner_id"  AND  ( t11."user_id" = #{ctx.sessioncontext.srfpersonid}  AND  t11."role_id" = 'user'  AND  t11."owner_type" = 'INSIGHT' ) )
```

#### 团队管理员(user_group_admin) :id=insight_view-user_group_admin
```sql
SELECT
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."name",
t1."scope_id",
t1."scope_type",
t1."update_man",
t1."update_time",
t1."visibility"
FROM "insight_view" t1 

WHERE EXISTS(SELECT * FROM "member" t11 
 WHERE 
 t1."id" = t11."owner_id"  AND  t11."owner_type" = 'INSIGHT_VIEW'  AND  t11."owner_subtype" = 'GROUP'  AND  ( t11."user_id" = #{ctx.sessioncontext.srfpersonid}  AND  t11."owner_type" = 'GROUP'  AND  t11."role_id" = 'admin' ) )
```


## [成员(MEMBER)](module/Base/member.md) :id=member

#### 数据查询(DEFAULT) :id=member-Default
```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."position_id",
t11."name" AS "position_name",
t1."role_id",
t1."title",
t1."update_man",
t1."update_time",
t1."user_id"
FROM "member" t1 
LEFT JOIN "position" t11 ON t1."position_id" = t11."id" 

```

#### 默认（全部数据）(VIEW) :id=member-View
```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."position_id",
t11."name" AS "position_name",
t1."role_id",
t1."title",
t1."update_man",
t1."update_time",
t1."user_id"
FROM "member" t1 
LEFT JOIN "position" t11 ON t1."position_id" = t11."id" 

```

#### 未关注成员(no_attention) :id=member-no_attention
```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."position_id",
t11."name" AS "position_name",
t1."role_id",
t1."title",
t1."update_man",
t1."update_time",
t1."user_id"
FROM "member" t1 
LEFT JOIN "position" t11 ON t1."position_id" = t11."id" 

WHERE ( ( USER_ID NOT IN (SELECT user_id from attention t2 where t2.OWNER_ID = #{ctx.webcontext.principal_id} )) )
```

#### 共享页面_非空间成员(shared_page_member) :id=member-shared_page_member
```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."position_id",
t11."name" AS "position_name",
t1."role_id",
t1."title",
t1."update_man",
t1."update_time",
t1."user_id"
FROM "member" t1 
LEFT JOIN "position" t11 ON t1."position_id" = t11."id" 

WHERE ( t1."owner_id" = #{ctx.webcontext.shared_page}  AND  t1."owner_type" = 'PAGE'  AND  t1."owner_subtype" = 'SHARED' )
```

#### 团队管理员(user_group_admin) :id=member-user_group_admin
```sql
SELECT
t1."id",
t1."user_id"
FROM "member" t1 

WHERE ( t1."role_id" = 'admin'  AND  t1."owner_type" = 'GROUP' )
```


## [页面版本(PAGE_VERSION)](module/Wiki/page_version.md) :id=page_version

#### 数据查询(DEFAULT) :id=page_version-Default
```sql
SELECT
t1."create_man",
t1."create_time",
t1."data",
t1."id",
t1."identifier",
t1."is_named",
t1."name",
t1."owner_id",
t1."update_man",
t1."update_time"
FROM "version" t1 

```

#### 默认（全部数据）(VIEW) :id=page_version-View
```sql
SELECT
t1."create_man",
t1."create_time",
t1."data",
t1."id",
t1."identifier",
t1."is_named",
t1."name",
t1."owner_id",
t1."update_man",
t1."update_time"
FROM "version" t1 

```


## [文件夹(PORTFOLIO)](module/Base/portfolio.md) :id=portfolio

#### 数据查询(DEFAULT) :id=portfolio-Default
```sql
SELECT
t1."assignee_id",
t1."assignee_name",
t1."create_man",
t1."create_time",
t1."description",
t1."end_at",
t1."id",
t1."identifier",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."name",
t1."start_at",
t1."state",
t1."update_man",
t1."update_time"
FROM "portfolio" t1 

```

#### 默认（全部数据）(VIEW) :id=portfolio-View
```sql
SELECT
t1."assignee_id",
t1."assignee_name",
t1."create_man",
t1."create_time",
t1."description",
t1."end_at",
t1."id",
t1."identifier",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."name",
t1."start_at",
t1."state",
t1."update_man",
t1."update_time"
FROM "portfolio" t1 

```

#### 管理员(admin) :id=portfolio-admin
```sql
SELECT
t1."assignee_id",
t1."assignee_name",
t1."create_man",
t1."create_time",
t1."description",
t1."end_at",
t1."id",
t1."identifier",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."name",
t1."start_at",
t1."state",
t1."update_man",
t1."update_time"
FROM "portfolio" t1 

WHERE EXISTS(SELECT * FROM "portfolio_member" t11 
 WHERE 
 t1."id" = t11."portfolio_id"  AND  ( t11."user_id" = #{ctx.sessioncontext.srfpersonid}  AND  t11."role_id" = 'admin' ) )
```

#### 选择项目集(choose_project_portfolio) :id=portfolio-choose_project_portfolio
```sql
SELECT
t1."assignee_id",
t1."assignee_name",
t1."create_man",
t1."create_time",
t1."description",
t1."end_at",
t1."id",
t1."identifier",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."name",
t1."start_at",
t1."state",
t1."update_man",
t1."update_time"
FROM "portfolio" t1 

WHERE ( t1."is_deleted" = 0  AND  not exists(select 1 from `work` t2 where t2.id = t1.id and t2.portfolio_id = #{ctx.webcontext.portfolio})  AND  not exists(select 1 from `work` t2 where t1.id = t2.portfolio_id and t2.principal_type = 'project_portfolio')  AND  t1."id" <> #{ctx.webcontext.portfolio} )
```

#### 查询星标(favorite) :id=portfolio-favorite
```sql
SELECT
t1."assignee_id",
t1."assignee_name",
t1."create_man",
t1."create_time",
t1."description",
t1."end_at",
t1."id",
t1."identifier",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."name",
t1."start_at",
t1."state",
t1."update_man",
t1."update_time"
FROM "portfolio" t1 

WHERE ( t1."is_deleted" = 0  AND  (select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) = '1' )
```

#### 已删除的项目集(project_set_deleted) :id=portfolio-project_set_deleted
```sql
SELECT
t1."assignee_id",
t1."assignee_name",
t1."create_man",
t1."create_time",
t1."description",
t1."end_at",
t1."id",
t1."identifier",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."name",
t1."start_at",
t1."state",
t1."update_man",
t1."update_time"
FROM "portfolio" t1 

WHERE ( t1."is_deleted" = 1 )
```

#### 进行中的项目集(project_set_going) :id=portfolio-project_set_going
```sql
SELECT
t1."assignee_id",
t1."assignee_name",
t1."create_man",
t1."create_time",
t1."description",
t1."end_at",
t1."id",
t1."identifier",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."name",
t1."start_at",
t1."state",
t1."update_man",
t1."update_time"
FROM "portfolio" t1 

WHERE ( t1."is_deleted" = 0 )
```

#### 只读用户(reader) :id=portfolio-reader
```sql
SELECT
t1."assignee_id",
t1."assignee_name",
t1."create_man",
t1."create_time",
t1."description",
t1."end_at",
t1."id",
t1."identifier",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."name",
t1."start_at",
t1."state",
t1."update_man",
t1."update_time"
FROM "portfolio" t1 

WHERE EXISTS(SELECT * FROM "portfolio_member" t11 
 WHERE 
 t1."id" = t11."portfolio_id"  AND  ( t11."user_id" = #{ctx.sessioncontext.srfpersonid}  AND  t11."role_id" = 'reader' ) )
```

#### 普通成员(user) :id=portfolio-user
```sql
SELECT
t1."assignee_id",
t1."assignee_name",
t1."create_man",
t1."create_time",
t1."description",
t1."end_at",
t1."id",
t1."identifier",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."name",
t1."start_at",
t1."state",
t1."update_man",
t1."update_time"
FROM "portfolio" t1 

WHERE EXISTS(SELECT * FROM "portfolio_member" t11 
 WHERE 
 t1."id" = t11."portfolio_id"  AND  ( t11."user_id" = #{ctx.sessioncontext.srfpersonid}  AND  t11."role_id" = 'user' ) )
```

#### 工作下的项目集(work_project_portfolio) :id=portfolio-work_project_portfolio
```sql
SELECT
t1."assignee_id",
t1."assignee_name",
t1."create_man",
t1."create_time",
t1."description",
t1."end_at",
t1."id",
t1."identifier",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."name",
t1."start_at",
t1."state",
t1."update_man",
t1."update_time"
FROM "portfolio" t1 

WHERE ( exists(select 1 from `work` t2 where t2.principal_id= t1.id and t2.portfolio_id = #{ctx.webcontext.project_portfolio})  AND  t1."is_deleted" = 0 )
```


## [文件夹成员(PORTFOLIO_MEMBER)](module/Base/portfolio_member.md) :id=portfolio_member

#### 数据查询(DEFAULT) :id=portfolio_member-Default
```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."name",
t1."portfolio_id",
t11."identifier" AS "portfolio_identifier",
t11."name" AS "portfolio_name",
t1."role_id",
t1."update_man",
t1."update_time",
t1."user_id"
FROM "portfolio_member" t1 
LEFT JOIN "portfolio" t11 ON t1."portfolio_id" = t11."id" 

```

#### 默认（全部数据）(VIEW) :id=portfolio_member-View
```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."name",
t1."portfolio_id",
t11."identifier" AS "portfolio_identifier",
t11."name" AS "portfolio_name",
t1."role_id",
t1."update_man",
t1."update_time",
t1."user_id"
FROM "portfolio_member" t1 
LEFT JOIN "portfolio" t11 ON t1."portfolio_id" = t11."id" 

```

#### 当前项目集下成员(cur_project_set) :id=portfolio_member-cur_project_set
```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."name",
t1."portfolio_id",
t11."identifier" AS "portfolio_identifier",
t11."name" AS "portfolio_name",
t1."role_id",
t1."update_man",
t1."update_time",
t1."user_id"
FROM "portfolio_member" t1 
LEFT JOIN "portfolio" t11 ON t1."portfolio_id" = t11."id" 

WHERE ( t1."user_id" <> #{ctx.sessioncontext.srfpersonid}  AND  t1."portfolio_id" = #{ctx.datacontext.id} )
```


## [职位(POSITION)](module/Base/position.md) :id=position

#### 数据查询(DEFAULT) :id=position-Default
```sql
SELECT
t1."category_id",
t1."create_man",
t1."create_time",
t1."enable",
t1."id",
t1."name",
t1."sequence",
t1."update_man",
t1."update_time"
FROM "position" t1 

WHERE t1.enable = 1
```

#### 默认（全部数据）(VIEW) :id=position-View
```sql
SELECT
t1."category_id",
t1."create_man",
t1."create_time",
t1."enable",
t1."id",
t1."name",
t1."sequence",
t1."update_man",
t1."update_time"
FROM "position" t1 

WHERE t1.enable = 1
```

#### 无分组(no_category) :id=position-no_category
```sql
SELECT
t1."category_id",
t1."create_man",
t1."create_time",
t1."enable",
t1."id",
t1."name",
t1."sequence",
t1."update_man",
t1."update_time"
FROM "position" t1 

WHERE t1.enable = 1 AND ( t1."category_id" IS NULL )
```


## [最近访问(RECENT)](module/Base/recent.md) :id=recent

#### 数据查询(DEFAULT) :id=recent-Default
```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."identifier",
t1."is_deleted",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."recent_parent",
t1."recent_parent_identifier",
t1."recent_parent_name",
concat(t1."recent_parent_identifier",'-',t1."identifier") AS "show_identifier",
t1."type",
t1."update_man",
t1."update_time"
FROM "recent" t1 

```

#### 默认（全部数据）(VIEW) :id=recent-View
```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."identifier",
t1."is_deleted",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."recent_parent",
t1."recent_parent_identifier",
t1."recent_parent_name",
concat(t1."recent_parent_identifier",'-',t1."identifier") AS "show_identifier",
t1."type",
t1."update_man",
t1."update_time"
FROM "recent" t1 

```

#### 最近访问页面(recent_page) :id=recent-recent_page
```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."identifier",
t1."is_deleted",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."recent_parent",
t1."recent_parent_identifier",
t1."recent_parent_name",
concat(t1."recent_parent_identifier",'-',t1."identifier") AS "show_identifier",
t1."type",
t1."update_man",
t1."update_time"
FROM "recent" t1 

WHERE ( t1."owner_type" = 'space'  AND  t1."owner_subtype" = 'page'  AND  t1."update_man" = #{ctx.sessioncontext.srfpersonid}  AND  exists(SELECT 1 FROM page t3 
inner join space t4 on t4.id = t3.space_id and t4.is_deleted = 0
where t3.id = t1.owner_id and 
 t3.is_archived = 0 and t3.is_deleted =0) )
```

#### 最近使用(recent_use) :id=recent-recent_use
```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."identifier",
t1."is_deleted",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."recent_parent",
t1."recent_parent_identifier",
t1."recent_parent_name",
concat(t1."recent_parent_identifier",'-',t1."identifier") AS "show_identifier",
t1."type",
t1."update_man",
t1."update_time"
FROM "recent" t1 

WHERE ( t1."create_man" = #{ctx.sessioncontext.srfpersonid}  AND  t1."type" = '1'  AND  t1."is_deleted" = 0 )
```

#### 本人最新访问(user) :id=recent-user
```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."identifier",
t1."is_deleted",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."recent_parent",
t1."recent_parent_identifier",
t1."recent_parent_name",
concat(t1."recent_parent_identifier",'-',t1."identifier") AS "show_identifier",
t1."type",
t1."update_man",
t1."update_time"
FROM "recent" t1 

WHERE ( t1."create_man" = #{ctx.sessioncontext.srfpersonid} )
```


## [分组(SECTION)](module/Base/section.md) :id=section

#### 数据查询(DEFAULT) :id=section-Default
```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."is_leaf",
t1."is_leaf2",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."sequence",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "section" t1 

```

#### 默认（全部数据）(VIEW) :id=section-View
```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."is_leaf",
t1."is_leaf2",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."sequence",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "section" t1 

```

#### 检查名称是否重复(check_name) :id=section-check_name
```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."is_leaf",
t1."is_leaf2",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."sequence",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "section" t1 

WHERE ( t1."id" <> #{ctx.datacontext.id}  AND  t1."name" = #{ctx.datacontext.name}  AND  t1."owner_id" = #{ctx.datacontext.owner_id}  AND  t1."owner_type" = #{ctx.datacontext.owner_type}  AND  t1."owner_subtype" = #{ctx.datacontext.owner_subtype} )
```

#### 需求子产品(idea_section) :id=section-idea_section
```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."is_leaf",
t1."is_leaf2",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."sequence",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "section" t1 

WHERE ( t1."owner_subtype" = 'idea' )
```

#### 我的分组(my_section) :id=section-my_section
```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."is_leaf",
t1."is_leaf2",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."sequence",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "section" t1 

WHERE ( t1."create_man" = #{ctx.sessioncontext.srfpersonid} )
```

#### 产品排期分组(this_product_section) :id=section-this_product_section
```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."is_leaf",
t1."is_leaf2",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."sequence",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "section" t1 

WHERE ( t1."owner_id" = #{ctx.webcontext.productid}  AND  t1."owner_type" = 'product_plan' )
```


## [序列(SEQUENCE_GENERATOR)](module/Base/sequence_generator.md) :id=sequence_generator

#### 数据查询(DEFAULT) :id=sequence_generator-Default
```sql
SELECT
t1."create_man",
t1."create_time",
t1."current_value",
t1."group_tag",
t1."id",
t1."name",
t1."update_man",
t1."update_time"
FROM "sequence_generator" t1 

```

#### 默认（全部数据）(VIEW) :id=sequence_generator-View
```sql
SELECT
t1."create_man",
t1."create_time",
t1."current_value",
t1."group_tag",
t1."id",
t1."name",
t1."update_man",
t1."update_time"
FROM "sequence_generator" t1 

```


## [共享空间(SHARED_SPACE)](module/Wiki/shared_space.md) :id=shared_space

#### 数据查询(DEFAULT) :id=shared_space-Default
```sql
SELECT
t1."access_password",
t1."expiration_date",
t1."id",
t1."is_shared",
t1."name",
t1."scope_type",
t1."shared_by",
t1."shared_pages",
t1."shared_time",
t1."show_logo",
t1."show_title"
FROM "space" t1 

```

#### 默认（全部数据）(VIEW) :id=shared_space-View
```sql
SELECT
t1."access_password",
t1."expiration_date",
t1."id",
t1."is_shared",
t1."name",
t1."scope_type",
t1."shared_by",
t1."shared_pages",
t1."shared_time",
t1."show_logo",
t1."show_title"
FROM "space" t1 

```

#### 管理员(admin) :id=shared_space-admin
```sql
SELECT
t1."access_password",
t1."expiration_date",
t1."id",
t1."is_shared",
t1."name",
t1."scope_type",
t1."shared_by",
t1."shared_pages",
t1."shared_time",
t1."show_logo",
t1."show_title"
FROM "space" t1 

WHERE ( exists(select 1 from `space_member` t2 where t2.`SPACE_ID` = t1.`ID` and 
t2.ROLE_ID = 'admin' and t2.USER_ID = #{ctx.sessioncontext.srfpersonid}) )
```

#### 共享空间(shared) :id=shared_space-shared
```sql
SELECT
t1."access_password",
t1."expiration_date",
t1."id",
t1."is_shared",
t1."name",
t1."scope_type",
t1."shared_by",
t1."shared_pages",
t1."shared_time",
t1."show_logo",
t1."show_title"
FROM "space" t1 

WHERE ( t1."is_shared" <> '0' )
```


## [空间(SPACE)](module/Wiki/space.md) :id=space

#### 数据查询(DEFAULT) :id=space-Default
```sql
SELECT
t11."categories",
t1."category_id",
t11."name" AS "category_name",
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_shared",
t1."name",
t1."scope_id",
t1."scope_type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2",
t1."visibility"
FROM "space" t1 
LEFT JOIN "category" t11 ON t1."category_id" = t11."id" 

```

#### 默认（全部数据）(VIEW) :id=space-View
```sql
SELECT
t11."categories",
t1."category_id",
t11."name" AS "category_name",
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_shared",
t1."name",
t1."scope_id",
t1."scope_type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2",
t1."visibility"
FROM "space" t1 
LEFT JOIN "category" t11 ON t1."category_id" = t11."id" 

```

#### 管理员(admin) :id=space-admin
```sql
SELECT
t11."categories",
t1."category_id",
t11."name" AS "category_name",
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_shared",
t1."name",
t1."scope_id",
t1."scope_type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2",
t1."visibility"
FROM "space" t1 
LEFT JOIN "category" t11 ON t1."category_id" = t11."id" 

WHERE EXISTS(SELECT * FROM "space_member" t21 
 WHERE 
 t1."id" = t21."space_id"  AND  ( t21."user_id" = #{ctx.sessioncontext.srfpersonid}  AND  t21."role_id" = 'admin' ) )
```

#### 已归档(archived) :id=space-archived
```sql
SELECT
t11."categories",
t1."category_id",
t11."name" AS "category_name",
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_shared",
t1."name",
t1."scope_id",
t1."scope_type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2",
t1."visibility"
FROM "space" t1 
LEFT JOIN "category" t11 ON t1."category_id" = t11."id" 

WHERE ( t1."is_archived" = 1  AND  t1."is_deleted" = 0 )
```

#### 目录下空间(category_space) :id=space-category_space
```sql
SELECT
t11."categories",
t1."category_id",
t11."name" AS "category_name",
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_shared",
t1."name",
t1."scope_id",
t1."scope_type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2",
t1."visibility"
FROM "space" t1 
LEFT JOIN "category" t11 ON t1."category_id" = t11."id" 

WHERE ( t1."is_deleted" = 0  AND  ( t1."category_id" = #{ctx.webcontext.category_id}  OR  t11."categories" LIKE #{ctx.webcontext.category_id} ) )
```

#### 当前空间(cur_space) :id=space-cur_space
```sql
SELECT
t11."categories",
t1."category_id",
t11."name" AS "category_name",
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_shared",
t1."name",
t1."scope_id",
t1."scope_type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2",
t1."visibility"
FROM "space" t1 
LEFT JOIN "category" t11 ON t1."category_id" = t11."id" 

```

#### 当前空间(current) :id=space-current
```sql
SELECT
t11."categories",
t1."category_id",
t11."name" AS "category_name",
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_shared",
t1."name",
t1."scope_id",
t1."scope_type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2",
t1."visibility"
FROM "space" t1 
LEFT JOIN "category" t11 ON t1."category_id" = t11."id" 

WHERE ( <choose><when test="ctx.webcontext.space !=null ">  t1."id" = #{ctx.webcontext.space}  </when><otherwise>1=1</otherwise></choose> )
```

#### 已删除(deleted) :id=space-deleted
```sql
SELECT
t11."categories",
t1."category_id",
t11."name" AS "category_name",
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_shared",
t1."name",
t1."scope_id",
t1."scope_type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2",
t1."visibility"
FROM "space" t1 
LEFT JOIN "category" t11 ON t1."category_id" = t11."id" 

WHERE ( t1."is_deleted" = 1 )
```

#### 查询星标(favorite) :id=space-favorite
```sql
SELECT
t11."categories",
t1."category_id",
t11."name" AS "category_name",
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_shared",
t1."name",
t1."scope_id",
t1."scope_type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2",
t1."visibility"
FROM "space" t1 
LEFT JOIN "category" t11 ON t1."category_id" = t11."id" 

WHERE ( (select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) = '1'  AND  t1."is_deleted" = 0  AND  t1."is_archived" = 0 )
```

#### 查询星标（管理用户）(favorite_user) :id=space-favorite_user
```sql
SELECT
t11."categories",
t1."category_id",
t11."name" AS "category_name",
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_shared",
t1."name",
t1."scope_id",
t1."scope_type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2",
t1."visibility"
FROM "space" t1 
LEFT JOIN "category" t11 ON t1."category_id" = t11."id" 

WHERE EXISTS(SELECT * FROM "space_member" t21 
 WHERE 
 t1."id" = t21."space_id"  AND  ( t21."role_id" <> 'reader'  AND  t21."user_id" = #{ctx.sessioncontext.srfpersonid} ) ) AND ( (select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) = '1'  AND  t1."is_deleted" = 0  AND  t1."is_archived" = 0 )
```

#### 移动端非星标空间(mob_unfavorite) :id=space-mob_unfavorite
```sql
null
```

#### 未存在目录中的空间(no_category_space) :id=space-no_category_space
```sql
SELECT
t11."categories",
t1."category_id",
t11."name" AS "category_name",
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_shared",
t1."name",
t1."scope_id",
t1."scope_type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2",
t1."visibility"
FROM "space" t1 
LEFT JOIN "category" t11 ON t1."category_id" = t11."id" 

WHERE ( t1."is_deleted" = 0  AND  t1."is_archived" = 0  AND  t1."category_id" IS NULL )
```

#### 正常状态(normal) :id=space-normal
```sql
SELECT
t11."categories",
t1."category_id",
t11."name" AS "category_name",
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_shared",
t1."name",
t1."scope_id",
t1."scope_type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2",
t1."visibility"
FROM "space" t1 
LEFT JOIN "category" t11 ON t1."category_id" = t11."id" 

WHERE ( t1."is_deleted" = 0  AND  t1."is_archived" = 0 )
```

#### 公开(public) :id=space-public
```sql
SELECT
t11."categories",
t1."category_id",
t11."name" AS "category_name",
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_shared",
t1."name",
t1."scope_id",
t1."scope_type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2",
t1."visibility"
FROM "space" t1 
LEFT JOIN "category" t11 ON t1."category_id" = t11."id" 

WHERE ( t1."visibility" = 'public' )
```

#### 只读用户(reader) :id=space-reader
```sql
SELECT
t11."categories",
t1."category_id",
t11."name" AS "category_name",
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_shared",
t1."name",
t1."scope_id",
t1."scope_type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2",
t1."visibility"
FROM "space" t1 
LEFT JOIN "category" t11 ON t1."category_id" = t11."id" 

WHERE EXISTS(SELECT * FROM "space_member" t21 
 WHERE 
 t1."id" = t21."space_id"  AND  ( t21."user_id" = #{ctx.sessioncontext.srfpersonid}  AND  t21."role_id" = 'reader' ) )
```

#### 非星标空间(unfavorite) :id=space-unfavorite
```sql
SELECT
t11."categories",
t1."category_id",
t11."name" AS "category_name",
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_shared",
t1."name",
t1."scope_id",
t1."scope_type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2",
t1."visibility"
FROM "space" t1 
LEFT JOIN "category" t11 ON t1."category_id" = t11."id" 

WHERE ( t1."is_deleted" = 0  AND  (select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) = '0'  AND  t1."is_archived" = 0 )
```

#### 非星标空间（管理用户）(unfavorite_user) :id=space-unfavorite_user
```sql
SELECT
t11."categories",
t1."category_id",
t11."name" AS "category_name",
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_shared",
t1."name",
t1."scope_id",
t1."scope_type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2",
t1."visibility"
FROM "space" t1 
LEFT JOIN "category" t11 ON t1."category_id" = t11."id" 

WHERE EXISTS(SELECT * FROM "space_member" t21 
 WHERE 
 t1."id" = t21."space_id"  AND  ( t21."role_id" <> 'reader'  AND  t21."user_id" = #{ctx.sessioncontext.srfpersonid} ) ) AND ( t1."is_deleted" = 0  AND  (select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) = '0'  AND  t1."is_archived" = 0 )
```

#### 操作用户(user) :id=space-user
```sql
SELECT
t11."categories",
t1."category_id",
t11."name" AS "category_name",
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_shared",
t1."name",
t1."scope_id",
t1."scope_type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2",
t1."visibility"
FROM "space" t1 
LEFT JOIN "category" t11 ON t1."category_id" = t11."id" 

WHERE EXISTS(SELECT * FROM "space_member" t21 
 WHERE 
 t1."id" = t21."space_id"  AND  ( t21."user_id" = #{ctx.sessioncontext.srfpersonid}  AND  t21."role_id" = 'user' ) )
```


## [空间成员(SPACE_MEMBER)](module/Wiki/space_member.md) :id=space_member

#### 数据查询(DEFAULT) :id=space_member-Default
```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."name",
t1."role_id",
t1."space_id",
t11."identifier" AS "space_identifier",
t11."name" AS "space_name",
t1."title",
t1."update_man",
t1."update_time",
t1."user_id"
FROM "space_member" t1 
LEFT JOIN "space" t11 ON t1."space_id" = t11."id" 

```

#### 默认（全部数据）(VIEW) :id=space_member-View
```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."name",
t1."role_id",
t1."space_id",
t11."identifier" AS "space_identifier",
t11."name" AS "space_name",
t1."title",
t1."update_man",
t1."update_time",
t1."user_id"
FROM "space_member" t1 
LEFT JOIN "space" t11 ON t1."space_id" = t11."id" 

```

#### 当前空间下成员(cur_space) :id=space_member-cur_space
```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."name",
t1."role_id",
t1."space_id",
t11."identifier" AS "space_identifier",
t11."name" AS "space_name",
t1."title",
t1."update_man",
t1."update_time",
t1."user_id"
FROM "space_member" t1 
LEFT JOIN "space" t11 ON t1."space_id" = t11."id" 

WHERE ( t1."user_id" <> #{ctx.sessioncontext.srfpersonid}  AND  t1."space_id" = #{ctx.datacontext.id} )
```

#### 未关注用户(测试用例)(no_attention) :id=space_member-no_attention
```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."name",
t1."role_id",
t1."space_id",
t11."identifier" AS "space_identifier",
t11."name" AS "space_name",
t1."title",
t1."update_man",
t1."update_time",
t1."user_id"
FROM "space_member" t1 
LEFT JOIN "space" t11 ON t1."space_id" = t11."id" 

WHERE ( ( USER_ID NOT IN (SELECT user_id from attention t2 where t2.OWNER_ID = #{ctx.webcontext.test_case} )) )
```


## [页面模板(STENCIL)](module/Wiki/stencil.md) :id=stencil

#### 数据查询(DEFAULT) :id=stencil-Default
```sql
SELECT
t1."create_man",
t1."create_time",
t1."format_type",
t1."id",
t1."is_global",
t1."name",
t1."space_id",
t11."name" AS "space_name",
t1."update_man",
t1."update_time"
FROM "stencil" t1 
LEFT JOIN "space" t11 ON t1."space_id" = t11."id" 

```

#### 默认（全部数据）(VIEW) :id=stencil-View
```sql
SELECT
t1."content",
t1."create_man",
t1."create_time",
t1."format_type",
t1."id",
t1."is_global",
t1."name",
t1."space_id",
t11."name" AS "space_name",
t1."update_man",
t1."update_time"
FROM "stencil" t1 
LEFT JOIN "space" t11 ON t1."space_id" = t11."id" 

```

#### 非空间下模板(no_space_stencil) :id=stencil-no_space_stencil
```sql
SELECT
t1."create_man",
t1."create_time",
t1."format_type",
t1."id",
t1."is_global",
t1."name",
t1."space_id",
t11."name" AS "space_name",
t1."update_man",
t1."update_time"
FROM "stencil" t1 
LEFT JOIN "space" t11 ON t1."space_id" = t11."id" 

WHERE ( t1."space_id" IS NULL )
```

#### 只读用户(reader) :id=stencil-reader
```sql
SELECT
t1."create_man",
t1."create_time",
t1."format_type",
t1."id",
t1."is_global",
t1."name",
t1."space_id",
t11."name" AS "space_name",
t1."update_man",
t1."update_time"
FROM "stencil" t1 
LEFT JOIN "space" t11 ON t1."space_id" = t11."id" 

/*ALIAS.sp=t11*/
WHERE EXISTS(SELECT * FROM "space_member" t21 
 WHERE 
 t11."id" = t21."space_id"  AND  ( t21."user_id" = #{ctx.sessioncontext.srfpersonid} ) )
```

#### 空间下页面模板(space_stencil) :id=stencil-space_stencil
```sql
SELECT
t1."create_man",
t1."create_time",
t1."format_type",
t1."id",
t1."is_global",
t1."name",
t1."space_id",
t11."name" AS "space_name",
t1."update_man",
t1."update_time"
FROM "stencil" t1 
LEFT JOIN "space" t11 ON t1."space_id" = t11."id" 

WHERE ( t1."space_id" = #{ctx.webcontext.space} )
```


## [版本(VERSION)](module/Base/version.md) :id=version

#### 数据查询(DEFAULT) :id=version-Default
```sql
SELECT
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."identifier",
t1."is_named",
t1."manual",
t1."name",
t1."owner_id",
t1."owner_type",
t1."restorable",
t1."update_man",
t1."update_time"
FROM "version" t1 

```

#### 默认（全部数据）(VIEW) :id=version-View
```sql
SELECT
t1."create_man",
t1."create_time",
t1."data",
t1."description",
t1."id",
t1."identifier",
t1."is_named",
t1."manual",
t1."name",
t1."owner_id",
t1."owner_type",
t1."restorable",
t1."update_man",
t1."update_time"
FROM "version" t1 

```

#### 命名版本(name_version) :id=version-name_version
```sql
SELECT
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."identifier",
t1."is_named",
t1."manual",
t1."name",
t1."owner_id",
t1."owner_type",
t1."restorable",
t1."update_man",
t1."update_time"
FROM "version" t1 

WHERE ( t1."is_named" = 1 )
```

#### 所属对象版本(owner) :id=version-owner
```sql
SELECT
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."identifier",
t1."is_named",
t1."manual",
t1."name",
t1."owner_id",
t1."owner_type",
t1."restorable",
t1."update_man",
t1."update_time"
FROM "version" t1 

WHERE ( t1."owner_id" = #{ctx.datacontext.owner_id} )
```

