# MYSQL5 <!-- {docsify-ignore-all} -->

## [活动(ACTIVITY)](module/Base/activity.md) :id=activity

#### 数据查询(DEFAULT) :id=activity-Default
```sql
SELECT
t1.`AUDITTYPE`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`IPADDRESS`,
t1.`NAME`,
t1.`OBJECTID`,
t1.`OBJECTTYPE`,
t1.`OPPERSONID`,
t1.`OPPERSONNAME`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `ACTIVITY` t1 

```

#### 默认（全部数据）(VIEW) :id=activity-View
```sql
SELECT
t1.`AUDITINFO`,
t1.`AUDITTYPE`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`IPADDRESS`,
t1.`NAME`,
t1.`OBJECTID`,
t1.`OBJECTTYPE`,
t1.`OPPERSONID`,
t1.`OPPERSONNAME`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `ACTIVITY` t1 

```


## [智能体(AI_AGENT)](module/ai/ai_agent.md) :id=ai_agent

#### DEFAULT :id=ai_agent-Default
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

#### 默认（全部数据）(VIEW) :id=ai_agent-View
```sql
SELECT
t1.`ACTIVE`,
t1.`AI_MODEL_ID`,
t11.`NAME` AS `AI_MODEL_NAME`,
t1.`CODE_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`CUSTOM_SUGGESTION_PROMPT`,
t1.`DEFAULT_SYSTEM_PROMPT`,
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
t1.`SUGGESTED_QUESTIONS`,
t1.`TEMPERATURE`,
t1.`TOOL_EXCEED_MESSAGE`,
t1.`TOOL_MAX_CALLS`,
t1.`TOP_P`,
t1.`TRIMMING_STRATEGY`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`WELCOME_MESSAGE`
FROM `AI_AGENT` t1 
LEFT JOIN `AI_MODEL` t11 ON t1.`AI_MODEL_ID` = t11.`ID` 

```


## [智能体分配(AI_AGENT_ASSIGNMENT)](module/ai/ai_agent_assignment.md) :id=ai_agent_assignment

#### DEFAULT :id=ai_agent_assignment-Default
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

#### 系统的(System) :id=ai_agent_assignment-System
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

WHERE ( ( t1.`SYSTEM_FLAG` = 1  OR  t11.`SYSTEM_FLAG` = 1 ) )
```

#### 默认（全部数据）(VIEW) :id=ai_agent_assignment-View
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

#### bind :id=ai_agent_assignment-bind
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


## [智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context.md) :id=ai_agent_context

#### DEFAULT :id=ai_agent_context-Default
```sql
SELECT
t1.`ACTIVE`,
t1.`AI_AGENT_ID`,
t21.`NAME` AS `AI_AGENT_NAME`,
t1.`AI_MODEL_ID`,
t11.`NAME` AS `AI_MODEL_NAME`,
t1.`CODE_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
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
t1.`SYSTEM_FLAG`,
t1.`TEMPERATURE`,
t1.`TOOL_MAX_CALLS`,
t1.`TOP_P`,
t1.`TRIMMING_STRATEGY`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_AGENT_CONTEXT` t1 
LEFT JOIN `AI_MODEL` t11 ON t1.`AI_MODEL_ID` = t11.`ID` 
LEFT JOIN `AI_AGENT` t21 ON t1.`AI_AGENT_ID` = t21.`ID` 

```

#### 默认（全部数据）(VIEW) :id=ai_agent_context-View
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

#### 待绑定(bind) :id=ai_agent_context-bind

#### deep_research_agent :id=ai_agent_context-deep_research_agent

#### dynamic_agent :id=ai_agent_context-dynamic_agent

#### 业务过滤(filter) :id=ai_agent_context-filter
```sql
SELECT
t1.`ACTIVE`,
t1.`AI_AGENT_ID`,
t21.`NAME` AS `AI_AGENT_NAME`,
t1.`AI_MODEL_ID`,
t11.`NAME` AS `AI_MODEL_NAME`,
t1.`CODE_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
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
t1.`SYSTEM_FLAG`,
t1.`TEMPERATURE`,
t1.`TOOL_MAX_CALLS`,
t1.`TOP_P`,
t1.`TRIMMING_STRATEGY`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_AGENT_CONTEXT` t1 
LEFT JOIN `AI_MODEL` t11 ON t1.`AI_MODEL_ID` = t11.`ID` 
LEFT JOIN `AI_AGENT` t21 ON t1.`AI_AGENT_ID` = t21.`ID` 

WHERE ( ( FIND_IN_SET(#{ctx.webcontext.srfaiagentscope}, t1.`SCOPES`) > 0  OR  t1.`SCOPES` IS NULL ) )
```

#### flow智能体(flow_agents) :id=ai_agent_context-flow_agents

#### full_text_agent :id=ai_agent_context-full_text_agent

#### hub智能体(hub_agents) :id=ai_agent_context-hub_agents

#### lookup_agent :id=ai_agent_context-lookup_agent

#### skill智能体(skill_agents) :id=ai_agent_context-skill_agents

#### 系统的(system) :id=ai_agent_context-system


## [智能体会话(AI_AGENT_CONVERSATION)](module/ai/ai_agent_conversation.md) :id=ai_agent_conversation

#### DEFAULT :id=ai_agent_conversation-Default
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

#### 默认（全部数据）(VIEW) :id=ai_agent_conversation-View
```sql
SELECT
t11.`NAME` AS `AGENT_CONTEXT_NAME`,
t1.`AI_AGENT_CONTEXT_ID`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`IS_TOP`,
(SELECT MAX(m.create_time) FROM AI_AGENT_MESSAGE m LEFT JOIN AI_AGENT_CONVERSATION conv ON m.conversation_id = conv.id WHERE conv.id = t1.`ID`) AS `LAST_ACTIVE_AT`,
t1.`NAME`,
t1.`SCOPE`,
t1.`SEQUENCE`,
t1.`SESSION_ID`,
case t1.`TITLE` is null then t11.`NAME` else t1.`TITLE` end AS `SHOW_NAME`,
t1.`STATUS`,
t1.`TITLE`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_ID`
FROM `AI_AGENT_CONVERSATION` t1 
LEFT JOIN `AI_AGENT_CONTEXT` t11 ON t1.`AI_AGENT_CONTEXT_ID` = t11.`ID` 

```

#### 有效会话(active) :id=ai_agent_conversation-active
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

WHERE ( ( t1.`STATUS` = 'active'  OR  t1.`STATUS` = 'paused' ) )
```

#### 当前用户会话(cur_user_active) :id=ai_agent_conversation-cur_user_active
```sql
SELECT
t1.`AI_AGENT_CONTEXT_ID`,
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

WHERE ( ( t1.`STATUS` = 'active'  OR  t1.`STATUS` = 'paused' )  AND  t1.`USER_ID` = #{ctx.sessioncontext.srfpersonid}  AND  t1.`TYPE` = 'topic' )
```


## [智能体回复反馈(AI_AGENT_FEEDBACK)](module/ai/ai_agent_feedback.md) :id=ai_agent_feedback

#### DEFAULT :id=ai_agent_feedback-Default
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`FEEDBACK_CONTENT`,
t1.`FEEDBACK_TYPE`,
t1.`ID`,
t1.`MESSAGE_ID`,
t1.`NAME`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_ID`
FROM `AI_AGENT_FEEDBACK` t1 

```

#### 默认（全部数据）(VIEW) :id=ai_agent_feedback-View
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`FEEDBACK_CONTENT`,
t1.`FEEDBACK_TYPE`,
t1.`ID`,
t1.`MESSAGE_ID`,
t1.`NAME`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_ID`
FROM `AI_AGENT_FEEDBACK` t1 

```


## [智能体知识库引用(AI_AGENT_KNOWLEDGE_REL)](module/ai/ai_agent_knowledge_rel.md) :id=ai_agent_knowledge_rel

#### DEFAULT :id=ai_agent_knowledge_rel-Default
```sql
SELECT
t1.`AI_AGENT_ID`,
t21.`NAME` AS `AI_AGENT_NAME`,
t1.`AI_KNOWLEDGE_BASE_ID`,
t11.`NAME` AS `AI_KNOWLEDGE_BASE_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`NAME`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_AGENT_KNOWLEDGE_REL` t1 
LEFT JOIN `AI_KNOWLEDGE_BASE` t11 ON t1.`AI_KNOWLEDGE_BASE_ID` = t11.`ID` 
LEFT JOIN `AI_AGENT` t21 ON t1.`AI_AGENT_ID` = t21.`ID` 

```

#### 默认（全部数据）(VIEW) :id=ai_agent_knowledge_rel-View
```sql
SELECT
t1.`AI_AGENT_ID`,
t21.`NAME` AS `AI_AGENT_NAME`,
t1.`AI_KNOWLEDGE_BASE_ID`,
t11.`NAME` AS `AI_KNOWLEDGE_BASE_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`NAME`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_AGENT_KNOWLEDGE_REL` t1 
LEFT JOIN `AI_KNOWLEDGE_BASE` t11 ON t1.`AI_KNOWLEDGE_BASE_ID` = t11.`ID` 
LEFT JOIN `AI_AGENT` t21 ON t1.`AI_AGENT_ID` = t21.`ID` 

```


## [智能体记忆任务实例(AI_AGENT_MEMORY_TASK)](module/ai/ai_agent_memory_task.md) :id=ai_agent_memory_task

#### DEFAULT :id=ai_agent_memory_task-Default

#### 默认（全部数据）(VIEW) :id=ai_agent_memory_task-View

#### 待执行计划任务(PENDING_SCHEDULED) :id=ai_agent_memory_task-pending_scheduled


## [智能体会话消息(AI_AGENT_MESSAGE)](module/ai/ai_agent_message.md) :id=ai_agent_message

#### DEFAULT :id=ai_agent_message-Default
```sql
SELECT
t1.`CONTENT_TYPE`,
t1.`CONVERSATION_ID`,
t11.`NAME` AS `CONVERSATION_NAME`,
t11.`TITLE` AS `CONVERSATION_TITLE`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
(select count(1) from ai_agent_feedback t where t.user_id=#{ctx.sessioncontext.srfuserid} and t.message_id=t1.`ID` and t.feedback_type='dislike') AS `IS_DISLIKE`,
(select count(1) from ai_agent_feedback t where t.user_id=#{ctx.sessioncontext.srfuserid} and t.message_id=t1.`ID` and t.feedback_type='like') AS `IS_LIKE`,
t1.`NAME`,
t1.`SENDER_TYPE`,
t1.`SEQUENCE`,
t1.`STATUS`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_AGENT_MESSAGE` t1 
LEFT JOIN `AI_AGENT_CONVERSATION` t11 ON t1.`CONVERSATION_ID` = t11.`ID` 

```

#### 默认（全部数据）(VIEW) :id=ai_agent_message-View
```sql
SELECT
t1.`CONTENT`,
t1.`CONTENT_TYPE`,
t1.`CONVERSATION_ID`,
t11.`NAME` AS `CONVERSATION_NAME`,
t11.`TITLE` AS `CONVERSATION_TITLE`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
(select count(1) from ai_agent_feedback t where t.user_id=#{ctx.sessioncontext.srfuserid} and t.message_id=t1.`ID` and t.feedback_type='dislike') AS `IS_DISLIKE`,
(select count(1) from ai_agent_feedback t where t.user_id=#{ctx.sessioncontext.srfuserid} and t.message_id=t1.`ID` and t.feedback_type='like') AS `IS_LIKE`,
t1.`METADATA`,
t1.`NAME`,
t1.`SENDER_TYPE`,
t1.`SEQUENCE`,
t1.`STATUS`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_AGENT_MESSAGE` t1 
LEFT JOIN `AI_AGENT_CONVERSATION` t11 ON t1.`CONVERSATION_ID` = t11.`ID` 

```


## [智能体工具引用(AI_AGENT_TOOL_REL)](module/ai/ai_agent_tool_rel.md) :id=ai_agent_tool_rel

#### DEFAULT :id=ai_agent_tool_rel-Default
```sql
SELECT
t1.`AI_AGENT_ID`,
t21.`NAME` AS `AI_AGENT_NAME`,
t1.`AI_TOOL_ID`,
t11.`NAME` AS `AI_TOOL_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`NAME`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_AGENT_TOOL_REL` t1 
LEFT JOIN `AI_TOOL` t11 ON t1.`AI_TOOL_ID` = t11.`ID` 
LEFT JOIN `AI_AGENT` t21 ON t1.`AI_AGENT_ID` = t21.`ID` 

```

#### 默认（全部数据）(VIEW) :id=ai_agent_tool_rel-View
```sql
SELECT
t1.`AI_AGENT_ID`,
t21.`NAME` AS `AI_AGENT_NAME`,
t1.`AI_TOOL_ID`,
t11.`NAME` AS `AI_TOOL_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`NAME`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_AGENT_TOOL_REL` t1 
LEFT JOIN `AI_TOOL` t11 ON t1.`AI_TOOL_ID` = t11.`ID` 
LEFT JOIN `AI_AGENT` t21 ON t1.`AI_AGENT_ID` = t21.`ID` 

```


## [AI客户端凭证(AI_CLIENT_CREDENTIAL)](module/ai/ai_client_credential.md) :id=ai_client_credential

#### DEFAULT :id=ai_client_credential-Default

#### 默认（全部数据）(VIEW) :id=ai_client_credential-View

#### my :id=ai_client_credential-my


## [AI凭证(AI_CREDENTIAL)](module/ai/ai_credential.md) :id=ai_credential

#### DEFAULT :id=ai_credential-Default
```sql
SELECT
t1.`ACTIVE`,
t1.`API_KEY`,
t1.`CLIENT_ID`,
t1.`CODE_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`CREDENTIAL_TYPE`,
t1.`DESCRIPTION`,
t1.`ID`,
t1.`NAME`,
t1.`PROVIDER`,
t1.`REGION`,
t1.`SCOPE`,
t1.`TOKEN_URL`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_CREDENTIAL` t1 

```

#### 默认（全部数据）(VIEW) :id=ai_credential-View
```sql
SELECT
t1.`ACCESS_KEY`,
t1.`ACTIVE`,
t1.`API_KEY`,
t1.`BEARER_TOKEN`,
t1.`CLIENT_ID`,
t1.`CLIENT_SECRET`,
t1.`CODE_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`CREDENTIAL_TYPE`,
t1.`DESCRIPTION`,
t1.`ID`,
t1.`NAME`,
t1.`PROVIDER`,
t1.`REGION`,
t1.`SCOPE`,
t1.`SECRET_KEY`,
t1.`TOKEN_URL`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_CREDENTIAL` t1 

```


## [知识库文档分块(AI_KB_CHUNK)](module/ai/ai_kb_chunk.md) :id=ai_kb_chunk

#### DEFAULT :id=ai_kb_chunk-Default
```sql
SELECT
t1.`ACTIVE`,
t1.`CONTENT`,
t1.`CONTENT_PREVIEW`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DOCUMENT_ID`,
t11.`NAME` AS `DOCUMENT_NAME`,
t1.`ID`,
t1.`KEYWORDS`,
t1.`KEY_QUESTIONS`,
t1.`NAME`,
t1.`POSITIONS`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_KB_CHUNK` t1 
LEFT JOIN `AI_KB_DOCUMENT` t11 ON t1.`DOCUMENT_ID` = t11.`ID` 

```

#### 默认（全部数据）(VIEW) :id=ai_kb_chunk-View
```sql
SELECT
t1.`ACTIVE`,
t1.`CONTENT`,
t1.`CONTENT_PREVIEW`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DOCUMENT_ID`,
t11.`NAME` AS `DOCUMENT_NAME`,
t1.`ID`,
t1.`KEYWORDS`,
t1.`KEY_QUESTIONS`,
t1.`NAME`,
t1.`POSITIONS`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_KB_CHUNK` t1 
LEFT JOIN `AI_KB_DOCUMENT` t11 ON t1.`DOCUMENT_ID` = t11.`ID` 

```

#### reader :id=ai_kb_chunk-reader
```sql
SELECT
t1.`ACTIVE`,
t11.`CATEGORIES`,
t1.`CHUNK_TYPE`,
t1.`CONTENT`,
t1.`CONTENT_PREVIEW`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DOCUMENT_ID`,
t11.`NAME` AS `DOCUMENT_NAME`,
t11.`SEQUENCE` AS `DOCUMENT_SEQUENCE`,
t11.`TYPE` AS `DOCUMENT_TYPE`,
t11.`FILE` AS `DOC_FILE`,
t11.`NAME` AS `DOC_NAME`,
t1.`ID`,
t11.`KB_ID`,
t21.`NAME` AS `KB_NAME`,
t1.`KEYWORDS`,
t1.`KEY_QUESTIONS`,
t1.`META_DATA`,
t1.`NAME`,
t1.`PATH`,
t1.`PID`,
t1.`POSITIONS`,
t1.`SEQUENCE`,
t1.`SOURCE_COUNT`,
t1.`TAGS`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`
FROM `AI_KB_CHUNK` t1 
LEFT JOIN `AI_KB_DOCUMENT` t11 ON t1.`DOCUMENT_ID` = t11.`ID` 
LEFT JOIN `AI_KNOWLEDGE_BASE` t21 ON t11.`KB_ID` = t21.`ID` 

WHERE ( ( t21.`VISIBILITY` = 'public'  OR  ( t21.`SCOPE_TYPE` = 'organization'  AND  t21.`SCOPE_ID` = #{ctx.sessioncontext.srforgid} )  OR  EXISTS(SELECT 1 FROM AI_KB_MEMBER m 
 WHERE 
 t21.ID = m.KB_ID  AND  ( m.USER_ID = #{ctx.sessioncontext.srfpersonid} ) ) ) )
```

#### 指定知识库(specified_kb) :id=ai_kb_chunk-specified_kb

#### tree :id=ai_kb_chunk-tree
```sql
SELECT
t11.`NAME` AS `DOCUMENT_NAME`,
t11.`TYPE` AS `DOCUMENT_TYPE`,
t1.`ID`,
t1.`NAME`,
t1.`PATH`,
t1.`PID`,
t1.`POSITIONS`,
t1.`SEQUENCE`,
t1.`SOURCE_COUNT`,
t1.`SOURCE_INDICES`,
t1.`TAGS`,
t1.`TYPE`
FROM `AI_KB_CHUNK` t1 
LEFT JOIN `AI_KB_DOCUMENT` t11 ON t1.`DOCUMENT_ID` = t11.`ID` 

WHERE ( <choose><when test="ctx.datacontext.ai_kb_document !=null ">  t1.`DOCUMENT_ID` = #{ctx.datacontext.ai_kb_document}  </when><otherwise>1=1</otherwise></choose> )
```

#### 启用(VALID) :id=ai_kb_chunk-valid
```sql
SELECT
t1.`ACTIVE`,
t1.`CONTENT`,
t1.`CONTENT_PREVIEW`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DOCUMENT_ID`,
t11.`NAME` AS `DOCUMENT_NAME`,
t11.`TYPE` AS `DOCUMENT_TYPE`,
t1.`ID`,
t11.`KB_ID`,
t1.`KEYWORDS`,
t1.`KEY_QUESTIONS`,
t1.`NAME`,
t1.`PATH`,
t1.`PID`,
t1.`POSITIONS`,
t1.`SEQUENCE`,
t1.`SOURCE_COUNT`,
t1.`SOURCE_INDICES`,
t1.`TAGS`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_KB_CHUNK` t1 
LEFT JOIN `AI_KB_DOCUMENT` t11 ON t1.`DOCUMENT_ID` = t11.`ID` 

WHERE ( t1.`ACTIVE` = 1 )
```


## [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document.md) :id=ai_kb_document

#### DEFAULT :id=ai_kb_document-Default
```sql
SELECT
t1.`ACTIVE`,
t1.`CATEGORIES`,
t1.`CHUNK_METHOD`,
t1.`CHUNK_NUM`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`CUSTOM_CHUNK`,
TO_CHAR(t1.`CREATE_TIME`, 'YYYY-MM-DD') AS `DOC_CREATE_TIME`,
case when t1.`FILE_TYPE` = 'xls' or t1.`FILE_TYPE` = 'xlsx' then 'Excel'  when t1.`FILE_TYPE` = 'pdf'  then 'PDF'  when t1.`FILE_TYPE` = 'doc' or t1.`FILE_TYPE` = 'docx'  then 'Word' when t1.`FILE_TYPE` = 'pptx' or t1.`FILE_TYPE` = 'ppt' then  'PPT'  else  '其他'  end AS `DOC_TYPE`,
t1.`FILE`,
t1.`FILE_TYPE`,
t1.`ID`,
t1.`KB_ID`,
t11.`NAME` AS `KB_NAME`,
t1.`KEY`,
t1.`NAME`,
CURRENT_DATE - t1.`CREATE_TIME`::date AS `RECENT_CREATE_DAYS`,
t1.`RESOURCE`,
t1.`SEQUENCE`,
t1.`SIZE`,
t1.`SOURCE_ID`,
t1.`SOURCE_TYPE`,
t1.`STATUS`,
t1.`SYNC_FREQUENCY`,
t1.`SYNC_ID`,
t11.`TAG_SETS`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_KB_DOCUMENT` t1 
LEFT JOIN `AI_KNOWLEDGE_BASE` t11 ON t1.`KB_ID` = t11.`ID` 

```

#### 默认（全部数据）(VIEW) :id=ai_kb_document-View
```sql
SELECT
t1.`ACTIVE`,
t1.`CHUNK_METHOD`,
t1.`CHUNK_NUM`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`CUSTOM_CHUNK`,
t1.`FILE`,
t1.`FILE_TYPE`,
t1.`ID`,
t1.`KB_ID`,
t11.`NAME` AS `KB_NAME`,
t1.`META_DATA`,
t1.`NAME`,
t1.`PARSER_CONFIG`,
t1.`SIZE`,
t1.`SOURCE_ID`,
t1.`SOURCE_TYPE`,
t1.`STATUS`,
t1.`SYNC_FREQUENCY`,
t1.`SYNC_ID`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_KB_DOCUMENT` t1 
LEFT JOIN `AI_KNOWLEDGE_BASE` t11 ON t1.`KB_ID` = t11.`ID` 

```

#### AI文档内容(ai_doc_content) :id=ai_kb_document-ai_doc_content

#### AI文档清单(ai_doc_list) :id=ai_kb_document-ai_doc_list

#### 当前知识库(cur_kb) :id=ai_kb_document-cur_kb

#### exp_list :id=ai_kb_document-exp_list
```sql
null
```

#### 数据查询(ls) :id=ai_kb_document-ls

#### 过滤器查询(my_filter) :id=ai_kb_document-my_filter

#### reader :id=ai_kb_document-reader
```sql
SELECT
t1.`ACTIVE`,
t1.`CATEGORIES`,
t1.`CHUNK_METHOD`,
t1.`CHUNK_NUM`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`CUSTOM_CHUNK`,
t1.`DIGEST_CODE`,
TO_CHAR(t1.`CREATE_TIME`, 'YYYY-MM-DD') AS `DOC_CREATE_TIME`,
t1.`FILE`,
t1.`FILE_TYPE`,
t1.`ID`,
t1.`KB_ID`,
t11.`NAME` AS `KB_NAME`,
t1.`KEY`,
t1.`NAME`,
concat_ws('/',nullif(btrim(t1.`CATEGORIES`, '/'),''),t1.`NAME`||'.'||COALESCE(t1.`FILE_TYPE`,'md')) AS `PATH`,
CURRENT_DATE - t1.`CREATE_TIME`::date AS `RECENT_CREATE_DAYS`,
t1.`RESOURCE`,
t1.`SEQUENCE`,
t1.`SIZE`,
t1.`SOURCE_ID`,
t1.`SOURCE_TYPE`,
t1.`STATUS`,
t1.`SYNC_FREQUENCY`,
t1.`SYNC_ID`,
t11.`TAG_SETS`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`
FROM `AI_KB_DOCUMENT` t1 
LEFT JOIN `AI_KNOWLEDGE_BASE` t11 ON t1.`KB_ID` = t11.`ID` 

WHERE ( ( t11.`VISIBILITY` = 'public'  OR  ( t11.`SCOPE_ID` = #{ctx.sessioncontext.srforgid}  AND  t11.`SCOPE_TYPE` = 'organization' )  OR  EXISTS(SELECT 1 FROM AI_KB_MEMBER m 
 WHERE 
 t11.ID = m.KB_ID  AND  ( m.USER_ID = #{ctx.sessioncontext.srfpersonid} ) )  OR  ( t11.`SCOPE_TYPE` = 'user_group'  AND  t11.`SCOPE_ID` = #{ctx.sessioncontext.srfgroup_user} ) ) )
```

#### 最近文档(recent) :id=ai_kb_document-recent

#### 资源分类(resource_classification) :id=ai_kb_document-resource_classification
```sql
null
```

#### 选中的数据(selected_data) :id=ai_kb_document-selected_data

#### 简单查询(simple) :id=ai_kb_document-simple
```sql
SELECT
t1.`CHUNK_METHOD`,
t1.`CUSTOM_CHUNK`,
t1.`ID`,
t1.`NAME`,
concat_ws('/',nullif(btrim(t1.`CATEGORIES`, '/'),''),t1.`NAME`||'.'||COALESCE(t1.`FILE_TYPE`,'md')) AS `PATH`,
t1.`SEQUENCE`,
t1.`STATUS`,
t1.`SYNC_ID`,
t1.`TYPE`,
t1.`UPDATE_TIME`
FROM `AI_KB_DOCUMENT` t1 

```

#### 未解析文档(UNPARSED) :id=ai_kb_document-unparsed
```sql
SELECT
t1.`ACTIVE`,
t1.`CHUNK_METHOD`,
t1.`CHUNK_NUM`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`CUSTOM_CHUNK`,
t1.`FILE`,
t1.`FILE_TYPE`,
t1.`ID`,
t1.`KB_ID`,
t1.`META_DATA`,
t1.`NAME`,
t1.`PARSED_CONTENT`,
t1.`PARSER_CONFIG`,
t1.`PARSE_ERROR`,
t1.`SIZE`,
t1.`SOURCE_ID`,
t1.`SOURCE_TYPE`,
t1.`STATUS`,
t1.`SYNC_FREQUENCY`,
t1.`SYNC_ID`,
t11.`TAG_SETS`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_KB_DOCUMENT` t1 
LEFT JOIN `AI_KNOWLEDGE_BASE` t11 ON t1.`KB_ID` = t11.`ID` 

WHERE ( t1.`ACTIVE` = 1  AND  t1.`STATUS` = '3'  AND  ( t1.`PARSED_CONTENT` IS NOT NULL  OR  t1.`FILE` IS NOT NULL ) )
```


## [知识库文档同步(AI_KB_DOCUMENT_SYNC)](module/ai/ai_kb_document_sync.md) :id=ai_kb_document_sync

#### DEFAULT :id=ai_kb_document_sync-Default
```sql
SELECT
t1.`AI_KNOWLEDGE_BASE_ID`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`NAME`,
t1.`SOURCE_ID`,
t1.`SOURCE_TYPE`,
t1.`SYNC_FREQUENCY`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_KB_DOCUMENT_SYNC` t1 

```

#### 默认（全部数据）(VIEW) :id=ai_kb_document_sync-View
```sql
SELECT
t1.`AI_KNOWLEDGE_BASE_ID`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`NAME`,
t1.`SOURCE_ID`,
t1.`SOURCE_TYPE`,
t1.`SYNC_FREQUENCY`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_KB_DOCUMENT_SYNC` t1 

```


## [知识库图谱实体(AI_KB_GRAPH_ENTITY)](module/ai/ai_kb_graph_entity.md) :id=ai_kb_graph_entity

#### DEFAULT :id=ai_kb_graph_entity-Default
```sql
SELECT
t1.`CONFIDENCE`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`KB_ID`,
t1.`NAME`,
t1.`NORMALIZED_NAME`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_KB_GRAPH_ENTITY` t1 

```

#### 默认（全部数据）(VIEW) :id=ai_kb_graph_entity-View
```sql
SELECT
t1.`CONFIDENCE`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`KB_ID`,
t1.`NAME`,
t1.`NORMALIZED_NAME`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_KB_GRAPH_ENTITY` t1 

```

#### 实体类型(cur_entity_type) :id=ai_kb_graph_entity-cur_entity_type
```sql
SELECT
t1.`CONFIDENCE`,
t1.`CONTEXT`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`DOCUMENT_ID`,
t21.`NAME` AS `DOCUMENT_NAME`,
t1.`ID`,
t1.`KB_ID`,
t11.`NAME` AS `KB_NAME`,
t1.`KEYWORDS`,
t1.`NAME`,
t1.`NORMALIZED_NAME`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_KB_GRAPH_ENTITY` t1 
LEFT JOIN `AI_KNOWLEDGE_BASE` t11 ON t1.`KB_ID` = t11.`ID` 
LEFT JOIN `AI_KB_DOCUMENT` t21 ON t1.`DOCUMENT_ID` = t21.`ID` 

WHERE ( <choose><when test="ctx.datacontext.ai_knowledge_base !=null ">  t1.`KB_ID` = #{ctx.datacontext.ai_knowledge_base}  </when><otherwise>1=1</otherwise></choose> )
```

#### 当前数据库实体(cur_kb) :id=ai_kb_graph_entity-cur_kb
```sql
SELECT
t1.`CONFIDENCE`,
t1.`CONTEXT`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`DOCUMENT_ID`,
t21.`NAME` AS `DOCUMENT_NAME`,
t1.`ID`,
t1.`KB_ID`,
t11.`NAME` AS `KB_NAME`,
t1.`KEYWORDS`,
t1.`NAME`,
t1.`NORMALIZED_NAME`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_KB_GRAPH_ENTITY` t1 
LEFT JOIN `AI_KNOWLEDGE_BASE` t11 ON t1.`KB_ID` = t11.`ID` 
LEFT JOIN `AI_KB_DOCUMENT` t21 ON t1.`DOCUMENT_ID` = t21.`ID` 

WHERE ( t1.`KB_ID` = #{ctx.datacontext.ai_knowledge_base} )
```


## [知识库图谱实体文档分块(AI_KB_GRAPH_ENTITY_CHUNK)](module/ai/ai_kb_graph_entity_chunk.md) :id=ai_kb_graph_entity_chunk

#### DEFAULT :id=ai_kb_graph_entity_chunk-Default
```sql
SELECT
t1.`CHUNK_ID`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ENTITY_ID`,
t1.`ID`,
t1.`NAME`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_KB_GRAPH_ENTITY_CHUNK` t1 

```

#### 默认（全部数据）(VIEW) :id=ai_kb_graph_entity_chunk-View
```sql
SELECT
t1.`CHUNK_ID`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ENTITY_ID`,
t1.`ID`,
t1.`NAME`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_KB_GRAPH_ENTITY_CHUNK` t1 

```


## [知识库图谱实体类型(AI_KB_GRAPH_ENTITY_TYPE)](module/ai/ai_kb_graph_entity_type.md) :id=ai_kb_graph_entity_type

#### DEFAULT :id=ai_kb_graph_entity_type-Default
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`ID`,
t1.`NAME`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`VALUE`
FROM `AI_KB_GRAPH_ENTITY_TYPE` t1 

```

#### 默认（全部数据）(VIEW) :id=ai_kb_graph_entity_type-View
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`ID`,
t1.`NAME`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`VALUE`
FROM `AI_KB_GRAPH_ENTITY_TYPE` t1 

```

#### 数据查询(VALID) :id=ai_kb_graph_entity_type-valid


## [知识库图谱关系(AI_KB_GRAPH_RELATION)](module/ai/ai_kb_graph_relation.md) :id=ai_kb_graph_relation

#### DEFAULT :id=ai_kb_graph_relation-Default
```sql
SELECT
t1.`ACTIVE`,
t1.`CONFIDENCE`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`KB_ID`,
t1.`NAME`,
t1.`OBJECT_ID`,
t1.`PREDICATE`,
t1.`SUBJECT_ID`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_KB_GRAPH_RELATION` t1 

```

#### 默认（全部数据）(VIEW) :id=ai_kb_graph_relation-View
```sql
SELECT
t1.`ACTIVE`,
t1.`CONFIDENCE`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`KB_ID`,
t1.`NAME`,
t1.`OBJECT_ID`,
t1.`PREDICATE`,
t1.`SUBJECT_ID`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_KB_GRAPH_RELATION` t1 

```

#### 当前数据库(cur_kb) :id=ai_kb_graph_relation-cur_kb
```sql
SELECT
t1.`ACTIVE`,
t1.`CONFIDENCE`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`ID`,
t1.`KB_ID`,
t31.`NAME` AS `KB_NAME`,
t1.`NAME`,
t1.`OBJECT_ID`,
t21.`NAME` AS `OBJECT_NAME`,
t1.`PREDICATE`,
t1.`SUBJECT_ID`,
t11.`NAME` AS `SUBJECT_NAME`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_KB_GRAPH_RELATION` t1 
LEFT JOIN `AI_KB_GRAPH_ENTITY` t11 ON t1.`SUBJECT_ID` = t11.`ID` 
LEFT JOIN `AI_KB_GRAPH_ENTITY` t21 ON t1.`OBJECT_ID` = t21.`ID` 
LEFT JOIN `AI_KNOWLEDGE_BASE` t31 ON t1.`KB_ID` = t31.`ID` 

WHERE ( <choose><when test="ctx.datacontext.ai_knowledge_base !=null ">  t1.`KB_ID` = #{ctx.datacontext.ai_knowledge_base}  </when><otherwise>1=1</otherwise></choose> )
```


## [知识库图谱关系文档分块(AI_KB_GRAPH_RELATION_CHUNK)](module/ai/ai_kb_graph_relation_chunk.md) :id=ai_kb_graph_relation_chunk

#### DEFAULT :id=ai_kb_graph_relation_chunk-Default
```sql
SELECT
t1.`CHUNK_ID`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`NAME`,
t1.`RELATION_ID`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_KB_GRAPH_RELATION_CHUNK` t1 

```

#### 默认（全部数据）(VIEW) :id=ai_kb_graph_relation_chunk-View
```sql
SELECT
t1.`CHUNK_ID`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`NAME`,
t1.`RELATION_ID`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_KB_GRAPH_RELATION_CHUNK` t1 

```


## [知识库成员(AI_KB_MEMBER)](module/ai/ai_kb_member.md) :id=ai_kb_member

#### DEFAULT :id=ai_kb_member-Default
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ENABLE`,
t1.`ID`,
t1.`KB_ID`,
t1.`NAME`,
t1.`ROLE_ID`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_ID`
FROM `AI_KB_MEMBER` t1 

```

#### 默认（全部数据）(VIEW) :id=ai_kb_member-View
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ENABLE`,
t1.`ID`,
t1.`KB_ID`,
t1.`NAME`,
t1.`ROLE_ID`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_ID`
FROM `AI_KB_MEMBER` t1 

```

#### 启用(VALID) :id=ai_kb_member-valid


## [知识库检索记录(AI_KB_SEARCH_QUERY)](module/ai/ai_kb_search_query.md) :id=ai_kb_search_query

#### DEFAULT :id=ai_kb_search_query-Default
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`FEEDBACK`,
t1.`ID`,
t1.`IS_ANSWERED`,
t1.`IS_KNOWLEDGE_GAP`,
t1.`NAME`,
t1.`NORMALIZED_QUERY`,
t1.`SOURCE`,
t1.`TAGS`,
t1.`TOTAL_DURATION`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_ID`,
t1.`USER_SATISFACTION`
FROM `AI_KB_SEARCH_QUERY` t1 

```

#### 默认（全部数据）(VIEW) :id=ai_kb_search_query-View
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`FEEDBACK`,
t1.`ID`,
t1.`IS_ANSWERED`,
t1.`IS_KNOWLEDGE_GAP`,
t1.`NAME`,
t1.`NORMALIZED_QUERY`,
t1.`RAW_QUERY`,
t1.`RETRIEVAL_CONFIG`,
t1.`SOURCE`,
t1.`SOURCE_METADATA`,
t1.`TAGS`,
t1.`TOTAL_DURATION`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_ID`,
t1.`USER_SATISFACTION`
FROM `AI_KB_SEARCH_QUERY` t1 

```


## [知识库检索结果(AI_KB_SEARCH_RESULT)](module/ai/ai_kb_search_result.md) :id=ai_kb_search_result

#### DEFAULT :id=ai_kb_search_result-Default
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DOCUMENT_ID`,
t1.`ID`,
t1.`KB_ID`,
t1.`NAME`,
t1.`QUERY_ID`,
t1.`RANK`,
t1.`RETRIEVAL_MODE`,
t1.`SIMILARITY`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_KB_SEARCH_RESULT` t1 

```

#### 默认（全部数据）(VIEW) :id=ai_kb_search_result-View
```sql
SELECT
t1.`CHUNK_SNAPSHOTS`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DOCUMENT_ID`,
t1.`HIT_CONTENT`,
t1.`ID`,
t1.`KB_ID`,
t1.`MERGED_CONTENT`,
t1.`NAME`,
t1.`QUERY_ID`,
t1.`RANK`,
t1.`RETRIEVAL_MODE`,
t1.`SIMILARITY`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_KB_SEARCH_RESULT` t1 

```


## [知识库标签(AI_KB_TAG)](module/ai/ai_kb_tag.md) :id=ai_kb_tag

#### DEFAULT :id=ai_kb_tag-Default
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ENABLE`,
t1.`ID`,
t1.`NAME`,
t1.`SET_ID`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`VALUE`
FROM `AI_KB_TAG` t1 

```

#### 默认（全部数据）(VIEW) :id=ai_kb_tag-View
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ENABLE`,
t1.`ID`,
t1.`NAME`,
t1.`SET_ID`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`VALUE`
FROM `AI_KB_TAG` t1 

```

#### 启用(VALID) :id=ai_kb_tag-valid


## [知识库标签集(AI_KB_TAG_SET)](module/ai/ai_kb_tag_set.md) :id=ai_kb_tag_set

#### DEFAULT :id=ai_kb_tag_set-Default
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ENABLE`,
t1.`ID`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`SCOPE`,
t1.`SOURCE_ID`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_KB_TAG_SET` t1 

```

#### 默认（全部数据）(VIEW) :id=ai_kb_tag_set-View
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ENABLE`,
t1.`ID`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`SCOPE`,
t1.`SOURCE_ID`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_KB_TAG_SET` t1 

```


## [知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base.md) :id=ai_knowledge_base

#### CurSelected :id=ai_knowledge_base-CurSelected

#### DEFAULT :id=ai_knowledge_base-Default
```sql
SELECT
t1.`CATEGORY_ID`,
t1.`CATEGORY_NAME`,
t1.`CHAT_MODEL`,
t1.`CHAT_MODEL_ID`,
t1.`CHUNK_METHOD`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`EMBEDDING_MODEL`,
t1.`EMBEDDING_MODEL_ID`,
t1.`GUIDANCE_PROMPT`,
t1.`ID`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`KEY`,
t1.`NAME`,
t1.`PAGEINDEX`,
t1.`RECORD_ID`,
t11.`_TITLE` AS `RECORD_TITLE`,
t1.`RERANK`,
t1.`RERANK_MODEL`,
t1.`RERANK_MODEL_ID`,
t1.`RESOURCE`,
t1.`RESOURCE_CODE`,
t1.`RESOURCE_ID`,
t1.`SCOPE_ID`,
t1.`SCOPE_TYPE`,
t1.`SIMILARITY_THRESHOLD`,
t1.`SOURCE_ID`,
t1.`SOURCE_NAME`,
t1.`STATUS`,
t1.`TAG_SETS`,
t1.`TOP_K`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USE_KG`,
t1.`VECTOR_SIMILARITY_WEIGHT`,
t1.`VISIBILITY`
FROM `AI_KNOWLEDGE_BASE` t1 
LEFT JOIN `data_record` t11 ON t1.`RECORD_ID` = t11.`_ID` 

```

#### 默认（全部数据）(VIEW) :id=ai_knowledge_base-View
```sql
SELECT
t1.`CHUNK_METHOD`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`EMBEDDING_MODEL`,
t1.`ID`,
t1.`NAME`,
t1.`PARSER_CONFIG`,
t1.`SOURCE_ID`,
t11.`NAME` AS `SOURCE_NAME`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_KNOWLEDGE_BASE` t1 
LEFT JOIN `AI_KNOWLEDGE_SOURCE` t11 ON t1.`SOURCE_ID` = t11.`ID` 

```

#### 管理员(admin) :id=ai_knowledge_base-admin
```sql
SELECT
t1.`CHUNK_METHOD`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`EMBEDDING_MODEL`,
t1.`ID`,
t1.`NAME`,
t1.`SOURCE_ID`,
t1.`SOURCE_NAME`,
t1.`TAG_SETS`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`VISIBILITY`
FROM `AI_KNOWLEDGE_BASE` t1 

WHERE EXISTS(SELECT * FROM `AI_KB_MEMBER` t11 
 WHERE 
 t1.`ID` = t11.`KB_ID`  AND  ( t11.`USER_ID` = #{ctx.sessioncontext.srfpersonid}  AND  t11.`ROLE_ID` = 'reader' ) )
```

#### 目录下的知识库(category_ai_kb) :id=ai_knowledge_base-category_ai_kb

#### 已删除(deleted) :id=ai_knowledge_base-deleted
```sql
SELECT
t1.`CHUNK_METHOD`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`EMBEDDING_MODEL`,
t1.`GUIDANCE_PROMPT`,
t1.`ID`,
t1.`IS_DELETED`,
t1.`NAME`,
t1.`RERANK`,
t1.`SIMILARITY_THRESHOLD`,
t1.`SOURCE_ID`,
t1.`SOURCE_NAME`,
t1.`TAG_SETS`,
t1.`TOP_K`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USE_KG`,
t1.`VECTOR_SIMILARITY_WEIGHT`,
t1.`VISIBILITY`
FROM `AI_KNOWLEDGE_BASE` t1 

WHERE ( t1.`IS_DELETED` = 1 )
```

#### 查询星标(favorite) :id=ai_knowledge_base-favorite

#### 组管理员(group_admin) :id=ai_knowledge_base-group_admin

#### 组管理员(group_user) :id=ai_knowledge_base-group_user

#### 组织私有库(org) :id=ai_knowledge_base-org

#### 公开(public) :id=ai_knowledge_base-public
```sql
SELECT
t1.`CHUNK_METHOD`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`EMBEDDING_MODEL`,
t1.`ID`,
t1.`NAME`,
t1.`SOURCE_ID`,
t1.`SOURCE_NAME`,
t1.`TAG_SETS`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`VISIBILITY`
FROM `AI_KNOWLEDGE_BASE` t1 

```

#### 只读用户(reader) :id=ai_knowledge_base-reader
```sql
SELECT
t1.`CHUNK_METHOD`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`EMBEDDING_MODEL`,
t1.`ID`,
t1.`NAME`,
t1.`SOURCE_ID`,
t1.`SOURCE_NAME`,
t1.`TAG_SETS`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`VISIBILITY`
FROM `AI_KNOWLEDGE_BASE` t1 

WHERE EXISTS(SELECT * FROM `AI_KB_MEMBER` t11 
 WHERE 
 t1.`ID` = t11.`KB_ID`  AND  ( t11.`USER_ID` = #{ctx.sessioncontext.srfpersonid}  AND  t11.`ROLE_ID` = 'reader' ) )
```

#### search :id=ai_knowledge_base-search
```sql
SELECT
t1.`CATEGORY_ID`,
t1.`CATEGORY_NAME`,
t1.`CHAT_MODEL`,
t1.`CHAT_MODEL_ID`,
t1.`CHUNK_METHOD`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`EMBEDDING_MODEL`,
t1.`EMBEDDING_MODEL_ID`,
t1.`GUIDANCE_PROMPT`,
t1.`ID`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`KEY`,
t1.`NAME`,
t1.`PAGEINDEX`,
t1.`RECORD_ID`,
t11.`_TITLE` AS `RECORD_TITLE`,
t1.`RERANK`,
t1.`RERANK_MODEL`,
t1.`RERANK_MODEL_ID`,
t1.`RESOURCE`,
t1.`RESOURCE_CODE`,
t1.`RESOURCE_ID`,
t1.`SCOPE_ID`,
t1.`SCOPE_TYPE`,
t1.`SIMILARITY_THRESHOLD`,
t1.`SOURCE_ID`,
t1.`SOURCE_NAME`,
t1.`SOURCE_TYPE`,
t1.`STATUS`,
t1.`TAG_SETS`,
t1.`TOP_K`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USE_KG`,
t1.`VECTOR_SIMILARITY_WEIGHT`,
t1.`VISIBILITY`
FROM `AI_KNOWLEDGE_BASE` t1 
LEFT JOIN `data_record` t11 ON t1.`RECORD_ID` = t11.`_ID` 

WHERE ( #{ctx.datacontext.keyword} is not null )
```

#### 非星标知识库(unfavorite) :id=ai_knowledge_base-unfavorite

#### 操作用户(user) :id=ai_knowledge_base-user
```sql
SELECT
t1.`CHUNK_METHOD`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`EMBEDDING_MODEL`,
t1.`ID`,
t1.`NAME`,
t1.`SOURCE_ID`,
t1.`SOURCE_NAME`,
t1.`TAG_SETS`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`VISIBILITY`
FROM `AI_KNOWLEDGE_BASE` t1 

WHERE EXISTS(SELECT * FROM `AI_KB_MEMBER` t11 
 WHERE 
 t1.`ID` = t11.`KB_ID`  AND  ( t11.`USER_ID` = #{ctx.sessioncontext.srfpersonid}  AND  t11.`ROLE_ID` = 'reader' ) )
```

#### 启用知识库(VALID) :id=ai_knowledge_base-valid
```sql
SELECT
t1.`CHUNK_METHOD`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`EMBEDDING_MODEL`,
t1.`ID`,
t1.`META_DATA`,
t1.`NAME`,
t1.`PARSER_CONFIG`,
t1.`SOURCE_ID`,
t1.`SOURCE_NAME`,
t1.`TAG_SETS`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`VISIBILITY`
FROM `AI_KNOWLEDGE_BASE` t1 

```


## [知识库源(AI_KNOWLEDGE_SOURCE)](module/ai/ai_knowledge_source.md) :id=ai_knowledge_source

#### DEFAULT :id=ai_knowledge_source-Default
```sql
SELECT
t1.`ACTIVE`,
t1.`BASE_URL`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`LAST_SYNC_TIME`,
t1.`NAME`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_KNOWLEDGE_SOURCE` t1 

```

#### 默认（全部数据）(VIEW) :id=ai_knowledge_source-View
```sql
SELECT
t1.`ACTIVE`,
t1.`API_KEY`,
t1.`BASE_URL`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`LAST_SYNC_TIME`,
t1.`NAME`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_KNOWLEDGE_SOURCE` t1 

```


## [AI大模型(AI_MODEL)](module/ai/ai_model.md) :id=ai_model

#### DEFAULT :id=ai_model-Default
```sql
SELECT
t1.`ACTIVE`,
t1.`AI_CREDENTIAL_ID`,
t11.`NAME` AS `AI_CREDENTIAL_NAME`,
t1.`API_BASE_URL`,
t1.`CODE_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESC_OSS_IMAGE`,
t1.`ID`,
t1.`MAX_CONTEXT_TOKENS`,
t1.`MAX_OUTPUT_TOKENS`,
t1.`MODEL_CAPABILITY`,
t1.`MODEL_CATEGORY`,
t1.`NAME`,
t1.`PROVIDER`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_MODEL` t1 
LEFT JOIN `AI_CREDENTIAL` t11 ON t1.`AI_CREDENTIAL_ID` = t11.`ID` 

```

#### 默认（全部数据）(VIEW) :id=ai_model-View
```sql
SELECT
t1.`ACTIVE`,
t1.`AI_CREDENTIAL_ID`,
t11.`NAME` AS `AI_CREDENTIAL_NAME`,
t1.`API_BASE_URL`,
t1.`CODE_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESC_OSS_IMAGE`,
t1.`EXTRA_PARAMS`,
t1.`ID`,
t1.`MAX_CONTEXT_TOKENS`,
t1.`MAX_OUTPUT_TOKENS`,
t1.`MODEL_CAPABILITY`,
t1.`MODEL_CATEGORY`,
t1.`NAME`,
t1.`PROVIDER`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_MODEL` t1 
LEFT JOIN `AI_CREDENTIAL` t11 ON t1.`AI_CREDENTIAL_ID` = t11.`ID` 

```


## [模型提供商(AI_MODEL_PROVIDER)](module/ai/ai_model_provider.md) :id=ai_model_provider

#### DEFAULT :id=ai_model_provider-Default

#### 默认（全部数据）(VIEW) :id=ai_model_provider-View

#### 存在凭证(has_credential) :id=ai_model_provider-has_credential

#### 不存在凭证(no_has_credential) :id=ai_model_provider-no_has_credential


## [智能审查报告(AI_REVIEW_REPORT)](module/ai/ai_review_report.md) :id=ai_review_report

#### Bykb_id_agent :id=ai_review_report-Bykb_id_agent

#### DEFAULT :id=ai_review_report-Default

#### 默认（全部数据）(VIEW) :id=ai_review_report-View

#### reader :id=ai_review_report-reader
```sql
SELECT
t1.`AGENT_TAG`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DOCUMENT_ID`,
t21.`NAME` AS `DOCUMENT_NAME`,
t1.`ID`,
t1.`KB_ID`,
t11.`NAME` AS `KB_NAME`,
t1.`NAME`,
t1.`RECORD_ID`,
t1.`REVIEW_RESULT`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_REVIEW_REPORT` t1 
LEFT JOIN `AI_KNOWLEDGE_BASE` t11 ON t1.`KB_ID` = t11.`ID` 
LEFT JOIN `AI_KB_DOCUMENT` t21 ON t1.`DOCUMENT_ID` = t21.`ID` 

WHERE ( ( t11.`VISIBILITY` = 'public'  OR  ( t11.`SCOPE_ID` = #{ctx.sessioncontext.srforgid}  AND  t11.`SCOPE_TYPE` = 'organization' )  OR  EXISTS(SELECT 1 FROM AI_KB_MEMBER m 
 WHERE 
 t11.ID = m.KB_ID  AND  ( m.USER_ID = #{ctx.sessioncontext.srfpersonid} ) ) ) )
```


## [AI调用工具(AI_TOOL)](module/ai/ai_tool.md) :id=ai_tool

#### DEFAULT :id=ai_tool-Default
```sql
SELECT
t1.`API_AUTH_TYPE`,
t1.`API_HEADERS`,
t1.`API_KEY`,
t1.`API_METHOD`,
t1.`API_URL`,
t1.`CLIENT_ID`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`NAME`,
t1.`TIMEOUT`,
t1.`TOKEN_URL`,
t1.`TOOL_TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_TOOL` t1 

```

#### 默认（全部数据）(VIEW) :id=ai_tool-View
```sql
SELECT
t1.`ACCESS_KEY`,
t1.`API_AUTH_TYPE`,
t1.`API_HEADERS`,
t1.`API_KEY`,
t1.`API_METHOD`,
t1.`API_URL`,
t1.`BEARER_TOKEN`,
t1.`CLIENT_ID`,
t1.`CLIENT_SECRET`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`INPUT_SCHEMA`,
t1.`NAME`,
t1.`SECRET_KEY`,
t1.`TIMEOUT`,
t1.`TOKEN_URL`,
t1.`TOOL_TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_TOOL` t1 

```

#### 内置扩展mcp服务(extension_mcp_server) :id=ai_tool-extension_mcp_server
```sql
SELECT
t1.`ACTIVE`,
t1.`API_AUTH_TYPE`,
t1.`API_HEADERS`,
t1.`API_KEY`,
t1.`API_METHOD`,
t1.`API_URL`,
t1.`CLIENT_ID`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`EXPIRATION_DATE`,
t1.`ID`,
t1.`NAME`,
t1.`TIMEOUT`,
t1.`TOKEN_URL`,
t1.`TOOL_TAG`,
t1.`TOOL_TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_TOOL` t1 

WHERE ( t1.`TOOL_TYPE` = 'mcp_built_in_extension' )
```

#### 启用的技能数据(SKILL_VALID) :id=ai_tool-skill_valid


## [页面(PAGE)](module/Wiki/article_page.md) :id=article_page

#### 数据查询(DEFAULT) :id=article_page-Default
```sql
SELECT
t1.`CATEGORIES`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`CUR_VERSION_ID`,
t1.`CUR_VERSION_NAME`,
t1.`FORMAT_TYPE`,
t1.`ICON`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_LEAF`,
t1.`IS_LOCK`,
t1.`IS_PUBLISHED`,
t1.`IS_SHARED`,
t1.`IS_SHARED_SUBSET`,
t1.`NAME`,
t1.`PARENT_ID`,
t1.`PUBLISHED`,
t1.`PUBLISH_MAN`,
t1.`PUBLISH_NAME`,
t1.`PUBLISH_TIME`,
DATEDIFF(CURDATE(), t1.`CREATE_TIME`) AS `RECENT_CREATE_DAYS`,
t1.`REVIEW_RESULT_STATE`,
t1.`SEQUENCE`,
concat(t11.`IDENTIFIER`,'-',t1.`IDENTIFIER`) AS `SHOW_IDENTIFIER`,
t1.`SPACE_ID`,
t11.`IDENTIFIER` AS `SPACE_IDENTIFIER`,
t11.`NAME` AS `SPACE_NAME`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`
FROM `PAGE` t1 
LEFT JOIN `SPACE` t11 ON t1.`SPACE_ID` = t11.`ID` 

```

#### 默认（全部数据）(VIEW) :id=article_page-View
```sql
SELECT
t1.`ACCESS_PASSWORD`,
(SELECT COUNT( att.ID ) AS comment_count FROM page p LEFT JOIN `attention` att ON p.ID = att.OWNER_ID WHERE p.ID = t1.`ID`) AS `ATTENTION_COUNT`,
t1.`CATEGORIES`,
(SELECT COUNT( com.ID ) AS comment_count FROM page p LEFT JOIN `comment` com ON p.ID = com.PRINCIPAL_ID WHERE p.ID = t1.`ID`) AS `COMMENT_COUNT`,
t1.`CONTENT`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`CUR_VERSION_ID`,
t1.`CUR_VERSION_NAME`,
t1.`EXPIRATION_DATE`,
t1.`FORMAT_TYPE`,
t1.`ICON`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_LEAF`,
t1.`IS_LOCK`,
t1.`IS_PUBLISHED`,
t1.`IS_SHARED`,
t1.`IS_SHARED_SUBSET`,
t1.`NAME`,
t1.`PARENT_ID`,
t1.`PUBLISHED`,
t1.`PUBLISH_CONTENT`,
t1.`PUBLISH_MAN`,
t1.`PUBLISH_NAME`,
t1.`PUBLISH_TIME`,
CASE WHEN EXISTS (SELECT 1 FROM ( select id from page where is_shared = '1' ) AS ids WHERE FIND_IN_SET(ids.id, REPLACE(t1.`CATEGORIES`, '/', ','))) THEN 1 ELSE 0 END AS `READ_SHARED`,
DATEDIFF(CURDATE(), t1.`CREATE_TIME`) AS `RECENT_CREATE_DAYS`,
t1.`REVIEW_RESULT_STATE`,
t1.`SEQUENCE`,
t1.`SHARED_BY`,
t1.`SHARED_TIME`,
concat(t11.`IDENTIFIER`,'-',t1.`IDENTIFIER`) AS `SHOW_IDENTIFIER`,
t1.`SPACE_ID`,
t11.`IDENTIFIER` AS `SPACE_IDENTIFIER`,
t11.`NAME` AS `SPACE_NAME`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`
FROM `PAGE` t1 
LEFT JOIN `SPACE` t11 ON t1.`SPACE_ID` = t11.`ID` 

```

#### 高级搜索(advanced_search) :id=article_page-advanced_search
```sql
SELECT
t1.`CATEGORIES`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`CUR_VERSION_ID`,
t1.`CUR_VERSION_NAME`,
t1.`FORMAT_TYPE`,
t1.`ICON`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_LEAF`,
t1.`IS_LOCK`,
t1.`IS_PUBLISHED`,
t1.`IS_SHARED`,
t1.`IS_SHARED_SUBSET`,
t1.`NAME`,
t1.`PARENT_ID`,
t1.`PUBLISHED`,
t1.`PUBLISH_MAN`,
t1.`PUBLISH_NAME`,
t1.`PUBLISH_TIME`,
DATEDIFF(CURDATE(), t1.`CREATE_TIME`) AS `RECENT_CREATE_DAYS`,
t1.`REVIEW_RESULT_STATE`,
t1.`SEQUENCE`,
concat(t11.`IDENTIFIER`,'-',t1.`IDENTIFIER`) AS `SHOW_IDENTIFIER`,
t1.`SPACE_ID`,
t11.`IDENTIFIER` AS `SPACE_IDENTIFIER`,
t11.`NAME` AS `SPACE_NAME`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`
FROM `PAGE` t1 
LEFT JOIN `SPACE` t11 ON t1.`SPACE_ID` = t11.`ID` 

WHERE ( t1.`IS_DELETED` = 0  AND  exists(select 1 from space t2, space_member t3 where t1.space_id = t2.id and t2.id = t3.space_id and t3.user_id = #{ctx.sessioncontext.srfpersonid})  AND  t1.`IS_PUBLISHED` = 1  AND  t1.`TYPE` = '1' )
```

#### 全部共享页面查询(all_shared_pages) :id=article_page-all_shared_pages
```sql
SELECT
t1.`EXPIRATION_DATE`,
t1.`ID`,
t1.`IS_SHARED`,
t1.`IS_SHARED_SUBSET`,
t1.`NAME`,
t1.`PUBLISH_NAME`,
t1.`SHARED_BY`,
t1.`SHARED_TIME`,
t1.`SPACE_ID`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `PAGE` t1 

WHERE ( t1.`IS_SHARED` = '1'  AND  t1.`IS_DELETED` = 0  AND  t1.`IS_PUBLISHED` = 1 )
```

#### 子页面(child_page) :id=article_page-child_page
```sql
SELECT
t1.`CATEGORIES`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`CUR_VERSION_ID`,
t1.`CUR_VERSION_NAME`,
t1.`FORMAT_TYPE`,
t1.`ICON`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_LEAF`,
t1.`IS_LOCK`,
t1.`IS_PUBLISHED`,
t1.`IS_SHARED`,
t1.`IS_SHARED_SUBSET`,
t1.`NAME`,
t1.`PARENT_ID`,
t1.`PUBLISHED`,
t1.`PUBLISH_MAN`,
t1.`PUBLISH_NAME`,
t1.`PUBLISH_TIME`,
DATEDIFF(CURDATE(), t1.`CREATE_TIME`) AS `RECENT_CREATE_DAYS`,
t1.`REVIEW_RESULT_STATE`,
t1.`SEQUENCE`,
concat(t11.`IDENTIFIER`,'-',t1.`IDENTIFIER`) AS `SHOW_IDENTIFIER`,
t1.`SPACE_ID`,
t11.`IDENTIFIER` AS `SPACE_IDENTIFIER`,
t11.`NAME` AS `SPACE_NAME`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`
FROM `PAGE` t1 
LEFT JOIN `SPACE` t11 ON t1.`SPACE_ID` = t11.`ID` 

WHERE ( t1.`PARENT_ID` IS NOT NULL  AND  t1.`IS_PUBLISHED` = 1  AND  t1.`IS_DELETED` = 0  AND  t1.`IS_ARCHIVED` = 0 )
```

#### 选择共享页面(choose_shared) :id=article_page-choose_shared
```sql
SELECT
t1.`ICON`,
t1.`ID`,
t1.`NAME`,
t1.`PARENT_ID`,
t1.`PUBLISH_NAME`,
t1.`SPACE_ID`
FROM `PAGE` t1 

WHERE ( t1.`IS_DELETED` = 0  AND  t1.`IS_PUBLISHED` = 1 )
```

#### 草稿页面(draft_page) :id=article_page-draft_page
```sql
SELECT
t1.`CATEGORIES`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`CUR_VERSION_ID`,
t1.`CUR_VERSION_NAME`,
t1.`FORMAT_TYPE`,
t1.`ICON`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_LEAF`,
t1.`IS_LOCK`,
t1.`IS_PUBLISHED`,
t1.`IS_SHARED`,
t1.`IS_SHARED_SUBSET`,
t1.`NAME`,
t1.`PARENT_ID`,
t1.`PUBLISHED`,
t1.`PUBLISH_MAN`,
t1.`PUBLISH_NAME`,
t1.`PUBLISH_TIME`,
DATEDIFF(CURDATE(), t1.`CREATE_TIME`) AS `RECENT_CREATE_DAYS`,
t1.`REVIEW_RESULT_STATE`,
t1.`SEQUENCE`,
concat(t11.`IDENTIFIER`,'-',t1.`IDENTIFIER`) AS `SHOW_IDENTIFIER`,
t1.`SPACE_ID`,
t11.`IDENTIFIER` AS `SPACE_IDENTIFIER`,
t11.`NAME` AS `SPACE_NAME`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`
FROM `PAGE` t1 
LEFT JOIN `SPACE` t11 ON t1.`SPACE_ID` = t11.`ID` 

WHERE ( t1.`IS_DELETED` = 0  AND  t1.`IS_PUBLISHED` = 0  AND  t1.`IS_ARCHIVED` = 0 )
```

#### 主页(home_page) :id=article_page-home_page
```sql
SELECT
t1.`CATEGORIES`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`CUR_VERSION_ID`,
t1.`CUR_VERSION_NAME`,
t1.`FORMAT_TYPE`,
t1.`ICON`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_LEAF`,
t1.`IS_LOCK`,
t1.`IS_PUBLISHED`,
t1.`IS_SHARED`,
t1.`IS_SHARED_SUBSET`,
t1.`NAME`,
t1.`PARENT_ID`,
t1.`PUBLISHED`,
t1.`PUBLISH_MAN`,
t1.`PUBLISH_NAME`,
t1.`PUBLISH_TIME`,
DATEDIFF(CURDATE(), t1.`CREATE_TIME`) AS `RECENT_CREATE_DAYS`,
t1.`REVIEW_RESULT_STATE`,
t1.`SEQUENCE`,
concat(t11.`IDENTIFIER`,'-',t1.`IDENTIFIER`) AS `SHOW_IDENTIFIER`,
t1.`SPACE_ID`,
t11.`IDENTIFIER` AS `SPACE_IDENTIFIER`,
t11.`NAME` AS `SPACE_NAME`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`
FROM `PAGE` t1 
LEFT JOIN `SPACE` t11 ON t1.`SPACE_ID` = t11.`ID` 

WHERE ( t1.`ID` = #{ctx.webcontext.n_space_id_eq} )
```

#### 已删除页面(is_deleted) :id=article_page-is_deleted
```sql
SELECT
t1.`CATEGORIES`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`CUR_VERSION_ID`,
t1.`CUR_VERSION_NAME`,
t1.`FORMAT_TYPE`,
t1.`ICON`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_LEAF`,
t1.`IS_LOCK`,
t1.`IS_PUBLISHED`,
t1.`IS_SHARED`,
t1.`IS_SHARED_SUBSET`,
t1.`NAME`,
t1.`PARENT_ID`,
t1.`PUBLISHED`,
t1.`PUBLISH_MAN`,
t1.`PUBLISH_NAME`,
t1.`PUBLISH_TIME`,
DATEDIFF(CURDATE(), t1.`CREATE_TIME`) AS `RECENT_CREATE_DAYS`,
t1.`REVIEW_RESULT_STATE`,
t1.`SEQUENCE`,
concat(t11.`IDENTIFIER`,'-',t1.`IDENTIFIER`) AS `SHOW_IDENTIFIER`,
t1.`SPACE_ID`,
t11.`IDENTIFIER` AS `SPACE_IDENTIFIER`,
t11.`NAME` AS `SPACE_NAME`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`
FROM `PAGE` t1 
LEFT JOIN `SPACE` t11 ON t1.`SPACE_ID` = t11.`ID` 

WHERE ( t1.`IS_DELETED` = 1 )
```

#### 我的收藏(my_favorite_page) :id=article_page-my_favorite_page
```sql
SELECT
t1.`CATEGORIES`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`CUR_VERSION_ID`,
t1.`CUR_VERSION_NAME`,
t1.`FORMAT_TYPE`,
t1.`ICON`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_LEAF`,
t1.`IS_LOCK`,
t1.`IS_PUBLISHED`,
t1.`IS_SHARED`,
t1.`IS_SHARED_SUBSET`,
t1.`NAME`,
t1.`PARENT_ID`,
t1.`PUBLISHED`,
t1.`PUBLISH_MAN`,
t1.`PUBLISH_NAME`,
t1.`PUBLISH_TIME`,
DATEDIFF(CURDATE(), t1.`CREATE_TIME`) AS `RECENT_CREATE_DAYS`,
t1.`REVIEW_RESULT_STATE`,
t1.`SEQUENCE`,
concat(t11.`IDENTIFIER`,'-',t1.`IDENTIFIER`) AS `SHOW_IDENTIFIER`,
t1.`SPACE_ID`,
t11.`IDENTIFIER` AS `SPACE_IDENTIFIER`,
t11.`NAME` AS `SPACE_NAME`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`
FROM `PAGE` t1 
LEFT JOIN `SPACE` t11 ON t1.`SPACE_ID` = t11.`ID` 

WHERE ( t11.`IS_DELETED` = 0 ) AND ( t1.`IS_ARCHIVED` = 0  AND  t1.`IS_DELETED` = 0  AND  (select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) = '1' )
```

#### 过滤器默认查询(my_filter) :id=article_page-my_filter
```sql
SELECT
t1.`CATEGORIES`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`CUR_VERSION_ID`,
t1.`CUR_VERSION_NAME`,
t1.`FORMAT_TYPE`,
t1.`ICON`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_LEAF`,
t1.`IS_LOCK`,
t1.`IS_PUBLISHED`,
t1.`IS_SHARED`,
t1.`IS_SHARED_SUBSET`,
t1.`NAME`,
t1.`PARENT_ID`,
t1.`PUBLISHED`,
t1.`PUBLISH_MAN`,
t1.`PUBLISH_NAME`,
t1.`PUBLISH_TIME`,
DATEDIFF(CURDATE(), t1.`CREATE_TIME`) AS `RECENT_CREATE_DAYS`,
t1.`REVIEW_RESULT_STATE`,
t1.`SEQUENCE`,
concat(t11.`IDENTIFIER`,'-',t1.`IDENTIFIER`) AS `SHOW_IDENTIFIER`,
t1.`SPACE_ID`,
t11.`IDENTIFIER` AS `SPACE_IDENTIFIER`,
t11.`NAME` AS `SPACE_NAME`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`
FROM `PAGE` t1 
LEFT JOIN `SPACE` t11 ON t1.`SPACE_ID` = t11.`ID` 

WHERE ( t11.`IS_DELETED` = 0 ) AND ( t1.`IS_DELETED` = 0  AND  t1.`TYPE` = '1'  AND  t1.`IS_ARCHIVED` = 0  AND  t1.`IS_PUBLISHED` = 1 )
```

#### 无父页面(no_parent_page) :id=article_page-no_parent_page
```sql
SELECT
t1.`CATEGORIES`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`CUR_VERSION_ID`,
t1.`CUR_VERSION_NAME`,
t1.`FORMAT_TYPE`,
t1.`ICON`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_LEAF`,
t1.`IS_LOCK`,
t1.`IS_PUBLISHED`,
t1.`IS_SHARED`,
t1.`IS_SHARED_SUBSET`,
t1.`NAME`,
t1.`PARENT_ID`,
t1.`PUBLISHED`,
t1.`PUBLISH_MAN`,
t1.`PUBLISH_NAME`,
t1.`PUBLISH_TIME`,
DATEDIFF(CURDATE(), t1.`CREATE_TIME`) AS `RECENT_CREATE_DAYS`,
t1.`REVIEW_RESULT_STATE`,
t1.`SEQUENCE`,
concat(t11.`IDENTIFIER`,'-',t1.`IDENTIFIER`) AS `SHOW_IDENTIFIER`,
t1.`SPACE_ID`,
t11.`IDENTIFIER` AS `SPACE_IDENTIFIER`,
t11.`NAME` AS `SPACE_NAME`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`
FROM `PAGE` t1 
LEFT JOIN `SPACE` t11 ON t1.`SPACE_ID` = t11.`ID` 

WHERE ( t1.`PARENT_ID` IS NULL  AND  t1.`ID` <> #{ctx.webcontext.n_space_id_eq}  AND  t1.`IS_ARCHIVED` = 0  AND  t1.`IS_DELETED` = 0  AND  t1.`IS_PUBLISHED` = 1 )
```

#### 正常(normal) :id=article_page-normal
```sql
SELECT
t1.`CATEGORIES`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`CUR_VERSION_ID`,
t1.`CUR_VERSION_NAME`,
t1.`FORMAT_TYPE`,
t1.`ICON`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_LEAF`,
t1.`IS_LOCK`,
t1.`IS_PUBLISHED`,
t1.`IS_SHARED`,
t1.`IS_SHARED_SUBSET`,
t1.`NAME`,
t1.`PARENT_ID`,
t1.`PUBLISHED`,
t1.`PUBLISH_MAN`,
t1.`PUBLISH_NAME`,
t1.`PUBLISH_TIME`,
DATEDIFF(CURDATE(), t1.`CREATE_TIME`) AS `RECENT_CREATE_DAYS`,
t1.`REVIEW_RESULT_STATE`,
t1.`SEQUENCE`,
concat(t11.`IDENTIFIER`,'-',t1.`IDENTIFIER`) AS `SHOW_IDENTIFIER`,
t1.`SPACE_ID`,
t11.`IDENTIFIER` AS `SPACE_IDENTIFIER`,
t11.`NAME` AS `SPACE_NAME`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`
FROM `PAGE` t1 
LEFT JOIN `SPACE` t11 ON t1.`SPACE_ID` = t11.`ID` 

WHERE ( t1.`IS_DELETED` = 0  AND  t1.`IS_ARCHIVED` = 0  AND  t1.`IS_PUBLISHED` = 1 )
```

#### 仅页面(only_page) :id=article_page-only_page
```sql
SELECT
t1.`CATEGORIES`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`CUR_VERSION_ID`,
t1.`CUR_VERSION_NAME`,
t1.`FORMAT_TYPE`,
t1.`ICON`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_LEAF`,
t1.`IS_LOCK`,
t1.`IS_PUBLISHED`,
t1.`IS_SHARED`,
t1.`IS_SHARED_SUBSET`,
t1.`NAME`,
t1.`PARENT_ID`,
t1.`PUBLISHED`,
t1.`PUBLISH_MAN`,
t1.`PUBLISH_NAME`,
t1.`PUBLISH_TIME`,
DATEDIFF(CURDATE(), t1.`CREATE_TIME`) AS `RECENT_CREATE_DAYS`,
t1.`REVIEW_RESULT_STATE`,
t1.`SEQUENCE`,
concat(t11.`IDENTIFIER`,'-',t1.`IDENTIFIER`) AS `SHOW_IDENTIFIER`,
t1.`SPACE_ID`,
t11.`IDENTIFIER` AS `SPACE_IDENTIFIER`,
t11.`NAME` AS `SPACE_NAME`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`
FROM `PAGE` t1 
LEFT JOIN `SPACE` t11 ON t1.`SPACE_ID` = t11.`ID` 

WHERE ( t1.`IS_DELETED` = 0  AND  t1.`IS_PUBLISHED` = 1  AND  t1.`TYPE` = '1' )
```

#### public :id=article_page-public
```sql
SELECT
t1.`CATEGORIES`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`CUR_VERSION_ID`,
t1.`CUR_VERSION_NAME`,
t1.`FORMAT_TYPE`,
t1.`ICON`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_LEAF`,
t1.`IS_LOCK`,
t1.`IS_PUBLISHED`,
t1.`IS_SHARED`,
t1.`IS_SHARED_SUBSET`,
t1.`NAME`,
t1.`PARENT_ID`,
t1.`PUBLISHED`,
t1.`PUBLISH_MAN`,
t1.`PUBLISH_NAME`,
t1.`PUBLISH_TIME`,
DATEDIFF(CURDATE(), t1.`CREATE_TIME`) AS `RECENT_CREATE_DAYS`,
t1.`REVIEW_RESULT_STATE`,
t1.`SEQUENCE`,
concat(t11.`IDENTIFIER`,'-',t1.`IDENTIFIER`) AS `SHOW_IDENTIFIER`,
t1.`SPACE_ID`,
t11.`IDENTIFIER` AS `SPACE_IDENTIFIER`,
t11.`NAME` AS `SPACE_NAME`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`
FROM `PAGE` t1 
LEFT JOIN `SPACE` t11 ON t1.`SPACE_ID` = t11.`ID` 

WHERE ( t11.`VISIBILITY` = 'public' )
```

#### reader :id=article_page-reader
```sql
SELECT
t1.`CATEGORIES`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`CUR_VERSION_ID`,
t1.`CUR_VERSION_NAME`,
t1.`FORMAT_TYPE`,
t1.`ICON`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_LEAF`,
t1.`IS_LOCK`,
t1.`IS_PUBLISHED`,
t1.`IS_SHARED`,
t1.`IS_SHARED_SUBSET`,
t1.`NAME`,
t1.`PARENT_ID`,
t1.`PUBLISHED`,
t1.`PUBLISH_MAN`,
t1.`PUBLISH_NAME`,
t1.`PUBLISH_TIME`,
DATEDIFF(CURDATE(), t1.`CREATE_TIME`) AS `RECENT_CREATE_DAYS`,
t1.`REVIEW_RESULT_STATE`,
t1.`SEQUENCE`,
concat(t11.`IDENTIFIER`,'-',t1.`IDENTIFIER`) AS `SHOW_IDENTIFIER`,
t1.`SPACE_ID`,
t11.`IDENTIFIER` AS `SPACE_IDENTIFIER`,
t11.`NAME` AS `SPACE_NAME`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`
FROM `PAGE` t1 
LEFT JOIN `SPACE` t11 ON t1.`SPACE_ID` = t11.`ID` 

WHERE EXISTS(SELECT * FROM `SPACE_MEMBER` t21 
 WHERE 
 t11.`ID` = t21.`SPACE_ID`  AND  ( t21.`USER_ID` = #{ctx.sessioncontext.srfpersonid} ) )
```

#### 共享页面(shared_page) :id=article_page-shared_page
```sql
SELECT
t1.`CATEGORIES`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`CUR_VERSION_ID`,
t1.`CUR_VERSION_NAME`,
t1.`FORMAT_TYPE`,
t1.`ICON`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_LEAF`,
t1.`IS_LOCK`,
t1.`IS_PUBLISHED`,
t1.`IS_SHARED`,
t1.`IS_SHARED_SUBSET`,
t1.`NAME`,
t1.`PARENT_ID`,
t1.`PUBLISHED`,
t1.`PUBLISH_MAN`,
t1.`PUBLISH_NAME`,
t1.`PUBLISH_TIME`,
DATEDIFF(CURDATE(), t1.`CREATE_TIME`) AS `RECENT_CREATE_DAYS`,
t1.`REVIEW_RESULT_STATE`,
t1.`SEQUENCE`,
concat(t11.`IDENTIFIER`,'-',t1.`IDENTIFIER`) AS `SHOW_IDENTIFIER`,
t1.`SPACE_ID`,
t11.`IDENTIFIER` AS `SPACE_IDENTIFIER`,
t11.`NAME` AS `SPACE_NAME`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`
FROM `PAGE` t1 
LEFT JOIN `SPACE` t11 ON t1.`SPACE_ID` = t11.`ID` 

WHERE ( t1.`IS_SHARED` = '1'  AND  t1.`ID` = #{ctx.webcontext.shared_page}  AND  t1.`IS_DELETED` = 0  AND  t1.`IS_PUBLISHED` = 1 )
```

#### 共享自读权限(shared_reader) :id=article_page-shared_reader
```sql
SELECT
t1.`ID`,
t1.`IS_SHARED`,
CASE WHEN EXISTS (SELECT 1 FROM ( select id from page where is_shared = '1' ) AS ids WHERE FIND_IN_SET(ids.id, REPLACE(t1.`CATEGORIES`, '/', ','))) THEN 1 ELSE 0 END AS `READ_SHARED`
FROM `PAGE` t1 

WHERE ( ( t1.`IS_SHARED` = '1'  OR  CASE WHEN EXISTS (SELECT 1 FROM ( select id from page where is_shared = '1' ) AS ids WHERE FIND_IN_SET(ids.id, REPLACE(t1.`CATEGORIES`, '/', ','))) THEN 1 ELSE 0 END = '1' )  AND  t1.`IS_PUBLISHED` = 1  AND  t1.`IS_DELETED` = 0 )
```

#### 共享搜索页面(shared_search) :id=article_page-shared_search
```sql
SELECT
t1.`CATEGORIES`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`CUR_VERSION_ID`,
t1.`CUR_VERSION_NAME`,
t1.`FORMAT_TYPE`,
t1.`ICON`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_LEAF`,
t1.`IS_LOCK`,
t1.`IS_PUBLISHED`,
t1.`IS_SHARED`,
t1.`IS_SHARED_SUBSET`,
t1.`NAME`,
t1.`PARENT_ID`,
t1.`PUBLISHED`,
t1.`PUBLISH_MAN`,
t1.`PUBLISH_NAME`,
t1.`PUBLISH_TIME`,
DATEDIFF(CURDATE(), t1.`CREATE_TIME`) AS `RECENT_CREATE_DAYS`,
t1.`REVIEW_RESULT_STATE`,
t1.`SEQUENCE`,
concat(t11.`IDENTIFIER`,'-',t1.`IDENTIFIER`) AS `SHOW_IDENTIFIER`,
t1.`SPACE_ID`,
t11.`IDENTIFIER` AS `SPACE_IDENTIFIER`,
t11.`NAME` AS `SPACE_NAME`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`
FROM `PAGE` t1 
LEFT JOIN `SPACE` t11 ON t1.`SPACE_ID` = t11.`ID` 

WHERE ( t1.`IS_DELETED` = 0  AND  t1.`IS_PUBLISHED` = 1  AND  t1.`TYPE` = '1'  AND  t1.`CATEGORIES` LIKE CONCAT('%',#{ctx.webcontext.shared_page},'%') )
```

#### 共享子页面(shared_sub_pages) :id=article_page-shared_sub_pages
```sql
SELECT
t1.`CATEGORIES`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`CUR_VERSION_ID`,
t1.`CUR_VERSION_NAME`,
t1.`FORMAT_TYPE`,
t1.`ICON`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_LEAF`,
t1.`IS_LOCK`,
t1.`IS_PUBLISHED`,
t1.`IS_SHARED`,
t1.`IS_SHARED_SUBSET`,
t1.`NAME`,
t1.`PARENT_ID`,
t1.`PUBLISHED`,
t1.`PUBLISH_MAN`,
t1.`PUBLISH_NAME`,
t1.`PUBLISH_TIME`,
DATEDIFF(CURDATE(), t1.`CREATE_TIME`) AS `RECENT_CREATE_DAYS`,
t1.`REVIEW_RESULT_STATE`,
t1.`SEQUENCE`,
concat(t11.`IDENTIFIER`,'-',t1.`IDENTIFIER`) AS `SHOW_IDENTIFIER`,
t1.`SPACE_ID`,
t11.`IDENTIFIER` AS `SPACE_IDENTIFIER`,
t11.`NAME` AS `SPACE_NAME`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`
FROM `PAGE` t1 
LEFT JOIN `SPACE` t11 ON t1.`SPACE_ID` = t11.`ID` 

WHERE ( t1.`CATEGORIES` LIKE CONCAT('%',#{ctx.webcontext.shared_page},'%')  AND  t1.`IS_DELETED` = 0  AND  t1.`IS_PUBLISHED` = 1 )
```

#### 与我共享(shared_with_me) :id=article_page-shared_with_me
```sql
SELECT
t1.`EXPIRATION_DATE`,
t1.`ID`,
t1.`IS_SHARED`,
t1.`IS_SHARED_SUBSET`,
t1.`NAME`,
t1.`PUBLISH_NAME`,
t1.`SHARED_BY`,
t1.`SHARED_TIME`,
t1.`SPACE_ID`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `PAGE` t1 
LEFT JOIN `SPACE` t21 ON t1.`SPACE_ID` = t21.`ID` 

WHERE EXISTS(SELECT * FROM `MEMBER` t11 
 WHERE 
 t1.`ID` = t11.`OWNER_ID`  AND  t11.`OWNER_TYPE` = 'PAGE'  AND  t11.`OWNER_SUBTYPE` = 'SHARED'  AND  ( t11.`USER_ID` = #{ctx.sessioncontext.srfuserid} ) ) AND ( t21.`IS_DELETED` = 0 ) AND ( t1.`IS_DELETED` = 0  AND  t1.`IS_PUBLISHED` = 1  AND  t1.`IS_SHARED` = '1' )
```

#### 与我共享编辑权限(shared_with_me_edit) :id=article_page-shared_with_me_edit
```sql
SELECT
t1.`CATEGORIES`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`CUR_VERSION_ID`,
t1.`CUR_VERSION_NAME`,
t1.`FORMAT_TYPE`,
t1.`ICON`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_LEAF`,
t1.`IS_LOCK`,
t1.`IS_PUBLISHED`,
t1.`IS_SHARED`,
t1.`IS_SHARED_SUBSET`,
t1.`NAME`,
t1.`PARENT_ID`,
t1.`PUBLISHED`,
t1.`PUBLISH_MAN`,
t1.`PUBLISH_NAME`,
t1.`PUBLISH_TIME`,
DATEDIFF(CURDATE(), t1.`CREATE_TIME`) AS `RECENT_CREATE_DAYS`,
t1.`REVIEW_RESULT_STATE`,
t1.`SEQUENCE`,
concat(t11.`IDENTIFIER`,'-',t1.`IDENTIFIER`) AS `SHOW_IDENTIFIER`,
t1.`SPACE_ID`,
t11.`IDENTIFIER` AS `SPACE_IDENTIFIER`,
t11.`NAME` AS `SPACE_NAME`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`
FROM `PAGE` t1 
LEFT JOIN `SPACE` t11 ON t1.`SPACE_ID` = t11.`ID` 

WHERE EXISTS(SELECT * FROM `MEMBER` t21 
 WHERE 
 t1.`ID` = t21.`OWNER_ID`  AND  t21.`OWNER_TYPE` = 'PAGE'  AND  t21.`OWNER_SUBTYPE` = 'SHARED'  AND  ( t21.`USER_ID` = #{ctx.sessioncontext.srfpersonid}  AND  t21.`ROLE_ID` = 'user' ) ) AND ( t1.`IS_SHARED` = '1'  AND  t1.`IS_PUBLISHED` = 1  AND  t1.`IS_DELETED` = 0 )
```


## [附件(ATTACHMENT)](module/Base/attachment.md) :id=attachment

#### 数据查询(DEFAULT) :id=attachment-Default
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`FILE_ID`,
t1.`ID`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_SUBTYPE`,
t1.`OWNER_TYPE`,
t1.`PARENT_VERSION_ID`,
t1.`TITLE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `ATTACHMENT` t1 

```


## [关注(ATTENTION)](module/Base/attention.md) :id=attention

#### 数据查询(DEFAULT) :id=attention-Default
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_SUBTYPE`,
t1.`OWNER_TYPE`,
t1.`TITLE`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_ID`
FROM `ATTENTION` t1 

```

#### 默认（全部数据）(VIEW) :id=attention-View
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_SUBTYPE`,
t1.`OWNER_TYPE`,
t1.`TITLE`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_ID`
FROM `ATTENTION` t1 

```

#### 通过主数据标识查询通知对象(attention_by_ownerid) :id=attention-attention_by_ownerid
```sql
SELECT
t1.`ID`,
t1.`USER_ID`
FROM `ATTENTION` t1 

WHERE ( t1.`OWNER_ID` = #{ctx.webcontext.id}  AND  <choose><when test="ctx.webcontext.principal_id !=null ">  t1.`OWNER_ID` = #{ctx.webcontext.principal_id}  </when><otherwise>1=1</otherwise></choose>  AND  ( t1.`TYPE` = '30'  OR  t1.`TYPE` = '40' )  AND  t1.`USER_ID` <> #{ctx.sessioncontext.srfpersonid} )
```

#### 评论提醒(comment_attention) :id=attention-comment_attention
```sql
SELECT
t1.`ID`,
t1.`USER_ID`
FROM `ATTENTION` t1 

WHERE ( exists(select 1 from `comment` t2 where t1.owner_id = t2.PRINCIPAL_ID and t2.id=#{ctx.webcontext.id})  AND  t1.`TYPE` = '40'  AND  t1.`USER_ID` <> #{ctx.sessioncontext.srfpersonid} )
```

#### 通知对象(notify) :id=attention-notify
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_SUBTYPE`,
t1.`OWNER_TYPE`,
t1.`TITLE`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_ID`
FROM `ATTENTION` t1 

WHERE ( t1.`OWNER_ID` = #{ctx.webcontext.principal_id} )
```


## [类别(CATEGORY)](module/Base/category.md) :id=category

#### 数据查询(DEFAULT) :id=category-Default
```sql
SELECT
t1.`CATEGORIES`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`IS_DELETED`,
t1.`IS_LEAF`,
t1.`IS_LEAF2`,
t1.`IS_LEAF3`,
case when t1.`IS_LEAF`+t1.`IS_LEAF2`=2 then 1 else 0 end AS `LEAF_FLAG`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_SUBTYPE`,
t1.`OWNER_TYPE`,
t1.`PID`,
t1.`SECTION_ID`,
t11.`NAME` AS `SECTION_NAME`,
t1.`SEQUENCE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`,
t1.`WF_VERSION_ID`
FROM `CATEGORY` t1 
LEFT JOIN `SECTION` t11 ON t1.`SECTION_ID` = t11.`ID` 

```

#### 默认（全部数据）(VIEW) :id=category-View
```sql
SELECT
t1.`CATEGORIES`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`IS_DELETED`,
t1.`IS_LEAF`,
t1.`IS_LEAF2`,
t1.`IS_LEAF3`,
case when t1.`IS_LEAF`+t1.`IS_LEAF2`=2 then 1 else 0 end AS `LEAF_FLAG`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_SUBTYPE`,
t1.`OWNER_TYPE`,
t1.`PID`,
t1.`SECTION_ID`,
t11.`NAME` AS `SECTION_NAME`,
t1.`SEQUENCE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`,
t1.`WF_VERSION_ID`
FROM `CATEGORY` t1 
LEFT JOIN `SECTION` t11 ON t1.`SECTION_ID` = t11.`ID` 

```

#### 知识库目录(ai_kb_category) :id=category-ai_kb_category

#### 知识库目录（顶级）(ai_kb_category_top) :id=category-ai_kb_category_top

#### 检查名称是否重复(check_name) :id=category-check_name
```sql
SELECT
t1.`CATEGORIES`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`IS_DELETED`,
t1.`IS_LEAF`,
t1.`IS_LEAF2`,
t1.`IS_LEAF3`,
case when t1.`IS_LEAF`+t1.`IS_LEAF2`=2 then 1 else 0 end AS `LEAF_FLAG`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_SUBTYPE`,
t1.`OWNER_TYPE`,
t1.`PID`,
t1.`SECTION_ID`,
t11.`NAME` AS `SECTION_NAME`,
t1.`SEQUENCE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`,
t1.`WF_VERSION_ID`
FROM `CATEGORY` t1 
LEFT JOIN `SECTION` t11 ON t1.`SECTION_ID` = t11.`ID` 

WHERE ( <choose><when test="ctx.datacontext.id !=null ">  t1.`ID` <> #{ctx.datacontext.id}  </when><otherwise>1=1</otherwise></choose>  AND  <choose><when test="ctx.datacontext.name !=null ">  t1.`NAME` = #{ctx.datacontext.name}  </when><otherwise>1=1</otherwise></choose>  AND  <choose><when test="ctx.datacontext.owner_id !=null ">  t1.`OWNER_ID` = #{ctx.datacontext.owner_id}  </when><otherwise>1=1</otherwise></choose>  AND  t1.`OWNER_TYPE` = #{ctx.datacontext.owner_type}  AND  <choose><when test="ctx.datacontext.owner_subtype !=null ">  t1.`OWNER_SUBTYPE` = #{ctx.datacontext.owner_subtype}  </when><otherwise>1=1</otherwise></choose> )
```

#### 通用类别（代码表）(common_categories) :id=category-common_categories
```sql
SELECT
t1.`CATEGORIES`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`IS_DELETED`,
t1.`IS_LEAF`,
t1.`IS_LEAF2`,
t1.`IS_LEAF3`,
case when t1.`IS_LEAF`+t1.`IS_LEAF2`=2 then 1 else 0 end AS `LEAF_FLAG`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_SUBTYPE`,
t1.`OWNER_TYPE`,
t1.`PID`,
t1.`SECTION_ID`,
t11.`NAME` AS `SECTION_NAME`,
t1.`SEQUENCE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`,
t1.`WF_VERSION_ID`
FROM `CATEGORY` t1 
LEFT JOIN `SECTION` t11 ON t1.`SECTION_ID` = t11.`ID` 

WHERE ( <choose><when test="ctx.webcontext.product !=null ">  t1.`OWNER_ID` = #{ctx.webcontext.product}  </when><otherwise>1=1</otherwise></choose>  AND  <choose><when test="ctx.webcontext.project !=null ">  t1.`OWNER_ID` = #{ctx.webcontext.project}  </when><otherwise>1=1</otherwise></choose> )
```

#### 当前产品需求类别(cur_product_idea_category) :id=category-cur_product_idea_category
```sql
SELECT
t1.`CATEGORIES`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`IS_DELETED`,
t1.`IS_LEAF`,
t1.`IS_LEAF2`,
t1.`IS_LEAF3`,
case when t1.`IS_LEAF`+t1.`IS_LEAF2`=2 then 1 else 0 end AS `LEAF_FLAG`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_SUBTYPE`,
t1.`OWNER_TYPE`,
t1.`PID`,
t1.`SECTION_ID`,
t11.`NAME` AS `SECTION_NAME`,
t1.`SEQUENCE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`,
t1.`WF_VERSION_ID`
FROM `CATEGORY` t1 
LEFT JOIN `SECTION` t11 ON t1.`SECTION_ID` = t11.`ID` 

WHERE ( t1.`OWNER_TYPE` = 'product'  AND  t1.`OWNER_SUBTYPE` = 'idea'  AND  t1.`OWNER_ID` = #{ctx.datacontext.product} )
```

#### 我的类别(my_category) :id=category-my_category
```sql
SELECT
t1.`CATEGORIES`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`IS_DELETED`,
t1.`IS_LEAF`,
t1.`IS_LEAF2`,
t1.`IS_LEAF3`,
case when t1.`IS_LEAF`+t1.`IS_LEAF2`=2 then 1 else 0 end AS `LEAF_FLAG`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_SUBTYPE`,
t1.`OWNER_TYPE`,
t1.`PID`,
t1.`SECTION_ID`,
t11.`NAME` AS `SECTION_NAME`,
t1.`SEQUENCE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`,
t1.`WF_VERSION_ID`
FROM `CATEGORY` t1 
LEFT JOIN `SECTION` t11 ON t1.`SECTION_ID` = t11.`ID` 

WHERE ( t1.`CREATE_MAN` = #{ctx.sessioncontext.srfpersonid} )
```

#### 无父类(no_parent) :id=category-no_parent
```sql
SELECT
t1.`CATEGORIES`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`IS_DELETED`,
t1.`IS_LEAF`,
t1.`IS_LEAF2`,
t1.`IS_LEAF3`,
case when t1.`IS_LEAF`+t1.`IS_LEAF2`=2 then 1 else 0 end AS `LEAF_FLAG`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_SUBTYPE`,
t1.`OWNER_TYPE`,
t1.`PID`,
t1.`SECTION_ID`,
t11.`NAME` AS `SECTION_NAME`,
t1.`SEQUENCE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`,
t1.`WF_VERSION_ID`
FROM `CATEGORY` t1 
LEFT JOIN `SECTION` t11 ON t1.`SECTION_ID` = t11.`ID` 

WHERE ( t1.`PID` IS NULL )
```

#### 无分组的类别（且父标识不为空）(no_section) :id=category-no_section
```sql
SELECT
t1.`CATEGORIES`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`IS_DELETED`,
t1.`IS_LEAF`,
t1.`IS_LEAF2`,
t1.`IS_LEAF3`,
case when t1.`IS_LEAF`+t1.`IS_LEAF2`=2 then 1 else 0 end AS `LEAF_FLAG`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_SUBTYPE`,
t1.`OWNER_TYPE`,
t1.`PID`,
t1.`SECTION_ID`,
t11.`NAME` AS `SECTION_NAME`,
t1.`SEQUENCE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`,
t1.`WF_VERSION_ID`
FROM `CATEGORY` t1 
LEFT JOIN `SECTION` t11 ON t1.`SECTION_ID` = t11.`ID` 

WHERE ( t1.`SECTION_ID` IS NULL  AND  t1.`PID` IS NULL )
```

#### 职位类别(position_category) :id=category-position_category
```sql
SELECT
t1.`CATEGORIES`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`IS_DELETED`,
t1.`IS_LEAF`,
t1.`IS_LEAF2`,
t1.`IS_LEAF3`,
case when t1.`IS_LEAF`+t1.`IS_LEAF2`=2 then 1 else 0 end AS `LEAF_FLAG`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_SUBTYPE`,
t1.`OWNER_TYPE`,
t1.`PID`,
t1.`SECTION_ID`,
t11.`NAME` AS `SECTION_NAME`,
t1.`SEQUENCE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`,
t1.`WF_VERSION_ID`
FROM `CATEGORY` t1 
LEFT JOIN `SECTION` t11 ON t1.`SECTION_ID` = t11.`ID` 

WHERE ( t1.`OWNER_TYPE` = 'position' )
```

#### 主模块(product_idea_category) :id=category-product_idea_category
```sql
SELECT
t1.`CATEGORIES`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`IS_DELETED`,
t1.`IS_LEAF`,
t1.`IS_LEAF2`,
t1.`IS_LEAF3`,
case when t1.`IS_LEAF`+t1.`IS_LEAF2`=2 then 1 else 0 end AS `LEAF_FLAG`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_SUBTYPE`,
t1.`OWNER_TYPE`,
t1.`PID`,
t1.`SECTION_ID`,
t11.`NAME` AS `SECTION_NAME`,
t1.`SEQUENCE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`,
t1.`WF_VERSION_ID`
FROM `CATEGORY` t1 
LEFT JOIN `SECTION` t11 ON t1.`SECTION_ID` = t11.`ID` 

WHERE ( t1.`PID` IS NULL )
```

#### 排期计划类别(product_plan) :id=category-product_plan
```sql
SELECT
t1.`CATEGORIES`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`IS_DELETED`,
t1.`IS_LEAF`,
t1.`IS_LEAF2`,
t1.`IS_LEAF3`,
case when t1.`IS_LEAF`+t1.`IS_LEAF2`=2 then 1 else 0 end AS `LEAF_FLAG`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_SUBTYPE`,
t1.`OWNER_TYPE`,
t1.`PID`,
t1.`SECTION_ID`,
t11.`NAME` AS `SECTION_NAME`,
t1.`SEQUENCE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`,
t1.`WF_VERSION_ID`
FROM `CATEGORY` t1 
LEFT JOIN `SECTION` t11 ON t1.`SECTION_ID` = t11.`ID` 

WHERE ( t1.`OWNER_TYPE` = 'product'  AND  t1.`OWNER_SUBTYPE` = 'product_plan'  AND  <choose><when test="ctx.webcontext.product !=null ">  t1.`OWNER_ID` = #{ctx.webcontext.product}  </when><otherwise>1=1</otherwise></choose> )
```

#### 空间目录(space_category) :id=category-space_category
```sql
SELECT
t1.`CATEGORIES`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`IS_DELETED`,
t1.`IS_LEAF`,
t1.`IS_LEAF2`,
t1.`IS_LEAF3`,
case when t1.`IS_LEAF`+t1.`IS_LEAF2`=2 then 1 else 0 end AS `LEAF_FLAG`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_SUBTYPE`,
t1.`OWNER_TYPE`,
t1.`PID`,
t1.`SECTION_ID`,
t11.`NAME` AS `SECTION_NAME`,
t1.`SEQUENCE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`,
t1.`WF_VERSION_ID`
FROM `CATEGORY` t1 
LEFT JOIN `SECTION` t11 ON t1.`SECTION_ID` = t11.`ID` 

WHERE ( t1.`OWNER_TYPE` = 'space'  AND  t1.`OWNER_SUBTYPE` = 'space' )
```

#### 空间目录（顶级）(space_category_top) :id=category-space_category_top
```sql
SELECT
t1.`CATEGORIES`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`IS_DELETED`,
t1.`IS_LEAF`,
t1.`IS_LEAF2`,
t1.`IS_LEAF3`,
case when t1.`IS_LEAF`+t1.`IS_LEAF2`=2 then 1 else 0 end AS `LEAF_FLAG`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_SUBTYPE`,
t1.`OWNER_TYPE`,
t1.`PID`,
t1.`SECTION_ID`,
t11.`NAME` AS `SECTION_NAME`,
t1.`SEQUENCE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`,
t1.`WF_VERSION_ID`
FROM `CATEGORY` t1 
LEFT JOIN `SECTION` t11 ON t1.`SECTION_ID` = t11.`ID` 

WHERE ( t1.`OWNER_TYPE` = 'space'  AND  t1.`OWNER_SUBTYPE` = 'space'  AND  t1.`PID` IS NULL )
```

#### 工作流类别(wf_category) :id=category-wf_category
```sql
SELECT
t1.`CATEGORIES`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`IS_DELETED`,
t1.`IS_LEAF`,
t1.`IS_LEAF2`,
t1.`IS_LEAF3`,
case when t1.`IS_LEAF`+t1.`IS_LEAF2`=2 then 1 else 0 end AS `LEAF_FLAG`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_SUBTYPE`,
t1.`OWNER_TYPE`,
t1.`PID`,
t1.`SECTION_ID`,
t11.`NAME` AS `SECTION_NAME`,
t1.`SEQUENCE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`,
t1.`WF_VERSION_ID`
FROM `CATEGORY` t1 
LEFT JOIN `SECTION` t11 ON t1.`SECTION_ID` = t11.`ID` 

WHERE ( t1.`OWNER_TYPE` = 'workflow'  AND  t1.`IS_DELETED` = 0 )
```


## [类别设置(CATEGORY_SETTINGS)](module/Base/category_settings.md) :id=category_settings

#### DEFAULT :id=category_settings-Default

#### 默认（全部数据）(VIEW) :id=category_settings-View


## [评论(COMMENT)](module/Base/comment.md) :id=comment

#### 数据查询(DEFAULT) :id=comment-Default
```sql
SELECT
t1.`CONTENT`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`IS_TOP`,
t1.`NAME`,
t1.`OWNER_TYPE`,
t11.`CONTENT` AS `PCONTENT`,
t11.`CREATE_MAN` AS `PCREATE_MAN`,
t1.`PID`,
t1.`PRINCIPAL_ID`,
t1.`PRINCIPAL_NAME`,
t1.`PRINCIPAL_TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `COMMENT` t1 
LEFT JOIN `COMMENT` t11 ON t1.`PID` = t11.`ID` 

```


## [通用规则(COMMON_FLOW)](module/Base/common_flow.md) :id=common_flow

#### DEFAULT :id=common_flow-Default

#### 默认（全部数据）(VIEW) :id=common_flow-View


## [数据记录(DATA_RECORD)](module/meta/data_record.md) :id=data_record

#### DEFAULT :id=data_record-Default

#### 默认（全部数据）(VIEW) :id=data_record-View


## [数据资源(DATA_RESOURCE)](module/meta/data_resource.md) :id=data_resource

#### DEFAULT :id=data_resource-Default

#### 默认（全部数据）(VIEW) :id=data_resource-View


## [数据字典(DICTIONARY)](module/Base/dictionary_data.md) :id=dictionary_data

#### 数据查询(DEFAULT) :id=dictionary_data-Default
```sql
SELECT
t1.`CATALOG`,
t1.`COLOR`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`ICON`,
t1.`ID`,
t1.`IS_SYSTEM`,
t1.`NAME`,
t1.`SEQUENCE`,
t1.`STYLE`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`VAL`
FROM `DICTIONARY` t1 

```

#### 默认（全部数据）(VIEW) :id=dictionary_data-View
```sql
SELECT
t1.`CATALOG`,
t1.`COLOR`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`ICON`,
t1.`ID`,
t1.`IS_SYSTEM`,
t1.`NAME`,
t1.`SEQUENCE`,
t1.`STYLE`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`VAL`
FROM `DICTIONARY` t1 

```

#### 知识库文档导入方式(ai_kb_doc_import_method) :id=dictionary_data-ai_kb_doc_import_method
```sql
SELECT
t1.`CATALOG`,
t1.`COLOR`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`ICON`,
t1.`ID`,
t1.`IS_SYSTEM`,
t1.`NAME`,
t1.`SEQUENCE`,
t1.`STYLE`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`VAL`
FROM `DICTIONARY` t1 

WHERE ( t1.`TYPE` = 'ai_kb_doc_import_method' )
```


## [动态数据看板(DYNADASHBOARD)](module/Base/dyna_dashboard.md) :id=dyna_dashboard

#### 数据查询(DEFAULT) :id=dyna_dashboard-Default

#### 默认（全部数据）(VIEW) :id=dyna_dashboard-View

#### 示例图(example_chart) :id=dyna_dashboard-example_chart

#### 系统仪表盘(is_system) :id=dyna_dashboard-is_system

#### 我的看板(my_dashboard) :id=dyna_dashboard-my_dashboard

#### 正常数据(normal) :id=dyna_dashboard-normal


## [扩展日志(EXTEND_LOG)](module/Base/extend_log.md) :id=extend_log

#### 数据查询(DEFAULT) :id=extend_log-Default

#### 默认（全部数据）(VIEW) :id=extend_log-View


## [扩展执行计划(EXTEND_SCHEDULE)](module/Base/extend_schedule.md) :id=extend_schedule

#### DEFAULT :id=extend_schedule-Default

#### 启用(VALID) :id=extend_schedule-Valid

#### 默认（全部数据）(VIEW) :id=extend_schedule-View


## [扩展计划任务(EXTEND_SCHEDULED_TASK)](module/Base/extend_scheduled_task.md) :id=extend_scheduled_task

#### DEFAULT :id=extend_scheduled_task-Default

#### 默认（全部数据）(VIEW) :id=extend_scheduled_task-View


## [扩展计划任务历史(EXTEND_SCHEDULED_TASK_HIS)](module/Base/extend_scheduled_task_his.md) :id=extend_scheduled_task_his

#### DEFAULT :id=extend_scheduled_task_his-Default

#### 默认（全部数据）(VIEW) :id=extend_scheduled_task_his-View


## [扩展任务类型(EXTEND_TASK_TYPE)](module/Base/extend_task_type.md) :id=extend_task_type

#### DEFAULT :id=extend_task_type-Default

#### 默认（全部数据）(VIEW) :id=extend_task_type-View


## [收藏(FAVORITE)](module/Base/favorite.md) :id=favorite

#### 数据查询(DEFAULT) :id=favorite-Default
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_SUBTYPE`,
t1.`OWNER_TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `FAVORITE` t1 

```

#### 默认（全部数据）(VIEW) :id=favorite-View
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_SUBTYPE`,
t1.`OWNER_TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `FAVORITE` t1 

```

#### 我的收藏(my_favorite) :id=favorite-my_favorite
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_SUBTYPE`,
t1.`OWNER_TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `FAVORITE` t1 

WHERE ( t1.`CREATE_MAN` = #{ctx.sessioncontext.srfpersonid} )
```


## [团队(GROUP)](module/Base/group.md) :id=group

#### 数据查询(DEFAULT) :id=group-Default
```sql
SELECT
t1.`AVATAR`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`ID`,
t1.`NAME`,
t1.`SECTION_ID`,
t11.`NAME` AS `SECTION_NAME`,
t1.`SEQUENCE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`VISIBILITY`
FROM `USER_GROUP` t1 
LEFT JOIN `SECTION` t11 ON t1.`SECTION_ID` = t11.`ID` 

```

#### 默认（全部数据）(VIEW) :id=group-View
```sql
SELECT
t1.`AVATAR`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`ID`,
t1.`NAME`,
t1.`SECTION_ID`,
t11.`NAME` AS `SECTION_NAME`,
t1.`SEQUENCE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`VISIBILITY`
FROM `USER_GROUP` t1 
LEFT JOIN `SECTION` t11 ON t1.`SECTION_ID` = t11.`ID` 

```

#### 无分组(no_section) :id=group-no_section
```sql
SELECT
t1.`AVATAR`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`ID`,
t1.`NAME`,
t1.`SECTION_ID`,
t11.`NAME` AS `SECTION_NAME`,
t1.`SEQUENCE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`VISIBILITY`
FROM `USER_GROUP` t1 
LEFT JOIN `SECTION` t11 ON t1.`SECTION_ID` = t11.`ID` 

WHERE ( t1.`SECTION_ID` IS NULL )
```

#### 公开(public) :id=group-public
```sql
SELECT
t1.`AVATAR`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`ID`,
t1.`NAME`,
t1.`SECTION_ID`,
t11.`NAME` AS `SECTION_NAME`,
t1.`SEQUENCE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`VISIBILITY`
FROM `USER_GROUP` t1 
LEFT JOIN `SECTION` t11 ON t1.`SECTION_ID` = t11.`ID` 

WHERE ( t1.`VISIBILITY` = 'public' )
```

#### 团队成员(user) :id=group-user
```sql
SELECT
t1.`AVATAR`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`ID`,
t1.`NAME`,
t1.`SECTION_ID`,
t11.`NAME` AS `SECTION_NAME`,
t1.`SEQUENCE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`VISIBILITY`
FROM `USER_GROUP` t1 
LEFT JOIN `SECTION` t11 ON t1.`SECTION_ID` = t11.`ID` 

WHERE EXISTS(SELECT * FROM `MEMBER` t21 
 WHERE 
 t1.`ID` = t21.`OWNER_ID`  AND  t21.`OWNER_TYPE` = 'GROUP'  AND  t21.`OWNER_SUBTYPE` = 'GROUP'  AND  ( t21.`USER_ID` = #{ctx.sessioncontext.srfpersonid}  AND  t21.`OWNER_TYPE` = 'GROUP' ) )
```

#### 团队管理员(user_group_admin) :id=group-user_group_admin
```sql
SELECT
t1.`AVATAR`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`ID`,
t1.`NAME`,
t1.`SECTION_ID`,
t11.`NAME` AS `SECTION_NAME`,
t1.`SEQUENCE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`VISIBILITY`
FROM `USER_GROUP` t1 
LEFT JOIN `SECTION` t11 ON t1.`SECTION_ID` = t11.`ID` 

WHERE EXISTS(SELECT * FROM `MEMBER` t21 
 WHERE 
 t1.`ID` = t21.`OWNER_ID`  AND  t21.`OWNER_TYPE` = 'GROUP'  AND  t21.`OWNER_SUBTYPE` = 'GROUP'  AND  ( t21.`USER_ID` = #{ctx.sessioncontext.srfpersonid}  AND  t21.`OWNER_TYPE` = 'GROUP'  AND  t21.`ROLE_ID` = 'admin' ) )
```


## [效能成员(INSIGHT_MEMBER)](module/Insight/insight_member.md) :id=insight_member

#### 数据查询(DEFAULT) :id=insight_member-Default

#### 默认（全部数据）(VIEW) :id=insight_member-View


## [效能报表(INSIGHT_REPORT)](module/Insight/insight_report.md) :id=insight_report

#### 数据查询(DEFAULT) :id=insight_report-Default

#### 默认（全部数据）(VIEW) :id=insight_report-View

#### 模板报表(is_system) :id=insight_report-is_system

#### 正常数据(normal) :id=insight_report-normal


## [效能视图(INSIGHT_VIEW)](module/Insight/insight_view.md) :id=insight_view

#### 数据查询(DEFAULT) :id=insight_view-Default

#### 默认（全部数据）(VIEW) :id=insight_view-View

#### 管理员(admin) :id=insight_view-admin

#### 已删除(deleted) :id=insight_view-deleted

#### 星标页面(favorite) :id=insight_view-favorite

#### 正常状态(normal) :id=insight_view-normal

#### 公开(public) :id=insight_view-public

#### 只读用户(reader) :id=insight_view-reader

#### 非星标(unfavorite) :id=insight_view-unfavorite

#### 操作用户(user) :id=insight_view-user

#### 团队管理员(user_group_admin) :id=insight_view-user_group_admin


## [成员(MEMBER)](module/Base/member.md) :id=member

#### 数据查询(DEFAULT) :id=member-Default
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_SUBTYPE`,
t1.`OWNER_TYPE`,
t1.`POSITION_ID`,
t11.`NAME` AS `POSITION_NAME`,
t1.`ROLE_ID`,
t1.`TITLE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_ID`
FROM `MEMBER` t1 
LEFT JOIN `POSITION` t11 ON t1.`POSITION_ID` = t11.`ID` 

```

#### 默认（全部数据）(VIEW) :id=member-View
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_SUBTYPE`,
t1.`OWNER_TYPE`,
t1.`POSITION_ID`,
t11.`NAME` AS `POSITION_NAME`,
t1.`ROLE_ID`,
t1.`TITLE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_ID`
FROM `MEMBER` t1 
LEFT JOIN `POSITION` t11 ON t1.`POSITION_ID` = t11.`ID` 

```

#### 未关注成员(no_attention) :id=member-no_attention
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_SUBTYPE`,
t1.`OWNER_TYPE`,
t1.`POSITION_ID`,
t11.`NAME` AS `POSITION_NAME`,
t1.`ROLE_ID`,
t1.`TITLE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_ID`
FROM `MEMBER` t1 
LEFT JOIN `POSITION` t11 ON t1.`POSITION_ID` = t11.`ID` 

WHERE ( ( USER_ID NOT IN (SELECT user_id from attention t2 where t2.OWNER_ID = #{ctx.webcontext.principal_id} )) )
```

#### 共享页面_非空间成员(shared_page_member) :id=member-shared_page_member
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_SUBTYPE`,
t1.`OWNER_TYPE`,
t1.`POSITION_ID`,
t11.`NAME` AS `POSITION_NAME`,
t1.`ROLE_ID`,
t1.`TITLE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_ID`
FROM `MEMBER` t1 
LEFT JOIN `POSITION` t11 ON t1.`POSITION_ID` = t11.`ID` 

WHERE ( t1.`OWNER_ID` = #{ctx.webcontext.shared_page}  AND  t1.`OWNER_TYPE` = 'PAGE'  AND  t1.`OWNER_SUBTYPE` = 'SHARED' )
```

#### 团队管理员(user_group_admin) :id=member-user_group_admin
```sql
SELECT
t1.`ID`,
t1.`USER_ID`
FROM `MEMBER` t1 

WHERE ( t1.`ROLE_ID` = 'admin'  AND  t1.`OWNER_TYPE` = 'GROUP' )
```


## [页面版本(PAGE_VERSION)](module/Wiki/page_version.md) :id=page_version

#### 数据查询(DEFAULT) :id=page_version-Default
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DATA`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_NAMED`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `version` t1 

```

#### 默认（全部数据）(VIEW) :id=page_version-View
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DATA`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_NAMED`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `version` t1 

```


## [文件夹(PORTFOLIO)](module/Base/portfolio.md) :id=portfolio

#### 数据查询(DEFAULT) :id=portfolio-Default
```sql
SELECT
t1.`ASSIGNEE_ID`,
t1.`ASSIGNEE_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`END_AT`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`NAME`,
t1.`START_AT`,
t1.`STATE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `PORTFOLIO` t1 

```

#### 默认（全部数据）(VIEW) :id=portfolio-View
```sql
SELECT
t1.`ASSIGNEE_ID`,
t1.`ASSIGNEE_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`END_AT`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`NAME`,
t1.`START_AT`,
t1.`STATE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `PORTFOLIO` t1 

```

#### 管理员(admin) :id=portfolio-admin
```sql
SELECT
t1.`ASSIGNEE_ID`,
t1.`ASSIGNEE_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`END_AT`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`NAME`,
t1.`START_AT`,
t1.`STATE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `PORTFOLIO` t1 

WHERE EXISTS(SELECT * FROM `PORTFOLIO_MEMBER` t11 
 WHERE 
 t1.`ID` = t11.`PORTFOLIO_ID`  AND  ( t11.`USER_ID` = #{ctx.sessioncontext.srfpersonid}  AND  t11.`ROLE_ID` = 'admin' ) )
```

#### 选择项目集(choose_project_portfolio) :id=portfolio-choose_project_portfolio
```sql
SELECT
t1.`ASSIGNEE_ID`,
t1.`ASSIGNEE_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`END_AT`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`NAME`,
t1.`START_AT`,
t1.`STATE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `PORTFOLIO` t1 

WHERE ( t1.`IS_DELETED` = 0  AND  not exists(select 1 from `work` t2 where t2.id = t1.id and t2.portfolio_id = #{ctx.webcontext.portfolio})  AND  not exists(select 1 from `work` t2 where t1.id = t2.portfolio_id and t2.principal_type = 'project_portfolio')  AND  t1.`ID` <> #{ctx.webcontext.portfolio} )
```

#### 查询星标(favorite) :id=portfolio-favorite
```sql
SELECT
t1.`ASSIGNEE_ID`,
t1.`ASSIGNEE_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`END_AT`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`NAME`,
t1.`START_AT`,
t1.`STATE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `PORTFOLIO` t1 

WHERE ( t1.`IS_DELETED` = 0  AND  (select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) = '1' )
```

#### 已删除的项目集(project_set_deleted) :id=portfolio-project_set_deleted
```sql
SELECT
t1.`ASSIGNEE_ID`,
t1.`ASSIGNEE_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`END_AT`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`NAME`,
t1.`START_AT`,
t1.`STATE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `PORTFOLIO` t1 

WHERE ( t1.`IS_DELETED` = 1 )
```

#### 进行中的项目集(project_set_going) :id=portfolio-project_set_going
```sql
SELECT
t1.`ASSIGNEE_ID`,
t1.`ASSIGNEE_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`END_AT`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`NAME`,
t1.`START_AT`,
t1.`STATE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `PORTFOLIO` t1 

WHERE ( t1.`IS_DELETED` = 0 )
```

#### 只读用户(reader) :id=portfolio-reader
```sql
SELECT
t1.`ASSIGNEE_ID`,
t1.`ASSIGNEE_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`END_AT`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`NAME`,
t1.`START_AT`,
t1.`STATE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `PORTFOLIO` t1 

WHERE EXISTS(SELECT * FROM `PORTFOLIO_MEMBER` t11 
 WHERE 
 t1.`ID` = t11.`PORTFOLIO_ID`  AND  ( t11.`USER_ID` = #{ctx.sessioncontext.srfpersonid}  AND  t11.`ROLE_ID` = 'reader' ) )
```

#### 普通成员(user) :id=portfolio-user
```sql
SELECT
t1.`ASSIGNEE_ID`,
t1.`ASSIGNEE_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`END_AT`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`NAME`,
t1.`START_AT`,
t1.`STATE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `PORTFOLIO` t1 

WHERE EXISTS(SELECT * FROM `PORTFOLIO_MEMBER` t11 
 WHERE 
 t1.`ID` = t11.`PORTFOLIO_ID`  AND  ( t11.`USER_ID` = #{ctx.sessioncontext.srfpersonid}  AND  t11.`ROLE_ID` = 'user' ) )
```

#### 工作下的项目集(work_project_portfolio) :id=portfolio-work_project_portfolio
```sql
SELECT
t1.`ASSIGNEE_ID`,
t1.`ASSIGNEE_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`END_AT`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`NAME`,
t1.`START_AT`,
t1.`STATE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `PORTFOLIO` t1 

WHERE ( exists(select 1 from `work` t2 where t2.principal_id= t1.id and t2.portfolio_id = #{ctx.webcontext.project_portfolio})  AND  t1.`IS_DELETED` = 0 )
```


## [文件夹成员(PORTFOLIO_MEMBER)](module/Base/portfolio_member.md) :id=portfolio_member

#### 数据查询(DEFAULT) :id=portfolio_member-Default
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`NAME`,
t1.`PORTFOLIO_ID`,
t11.`IDENTIFIER` AS `PORTFOLIO_IDENTIFIER`,
t11.`NAME` AS `PORTFOLIO_NAME`,
t1.`ROLE_ID`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_ID`
FROM `PORTFOLIO_MEMBER` t1 
LEFT JOIN `PORTFOLIO` t11 ON t1.`PORTFOLIO_ID` = t11.`ID` 

```

#### 默认（全部数据）(VIEW) :id=portfolio_member-View
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`NAME`,
t1.`PORTFOLIO_ID`,
t11.`IDENTIFIER` AS `PORTFOLIO_IDENTIFIER`,
t11.`NAME` AS `PORTFOLIO_NAME`,
t1.`ROLE_ID`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_ID`
FROM `PORTFOLIO_MEMBER` t1 
LEFT JOIN `PORTFOLIO` t11 ON t1.`PORTFOLIO_ID` = t11.`ID` 

```

#### 当前项目集下成员(cur_project_set) :id=portfolio_member-cur_project_set
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`NAME`,
t1.`PORTFOLIO_ID`,
t11.`IDENTIFIER` AS `PORTFOLIO_IDENTIFIER`,
t11.`NAME` AS `PORTFOLIO_NAME`,
t1.`ROLE_ID`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_ID`
FROM `PORTFOLIO_MEMBER` t1 
LEFT JOIN `PORTFOLIO` t11 ON t1.`PORTFOLIO_ID` = t11.`ID` 

WHERE ( t1.`USER_ID` <> #{ctx.sessioncontext.srfpersonid}  AND  t1.`PORTFOLIO_ID` = #{ctx.datacontext.id} )
```


## [职位(POSITION)](module/Base/position.md) :id=position

#### 数据查询(DEFAULT) :id=position-Default
```sql
SELECT
t1.`CATEGORY_ID`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ENABLE`,
t1.`ID`,
t1.`NAME`,
t1.`SEQUENCE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `POSITION` t1 

WHERE t1.ENABLE = 1
```

#### 默认（全部数据）(VIEW) :id=position-View
```sql
SELECT
t1.`CATEGORY_ID`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ENABLE`,
t1.`ID`,
t1.`NAME`,
t1.`SEQUENCE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `POSITION` t1 

WHERE t1.ENABLE = 1
```

#### 无分组(no_category) :id=position-no_category
```sql
SELECT
t1.`CATEGORY_ID`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ENABLE`,
t1.`ID`,
t1.`NAME`,
t1.`SEQUENCE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `POSITION` t1 

WHERE t1.ENABLE = 1 AND ( t1.`CATEGORY_ID` IS NULL )
```


## [最近访问(RECENT)](module/Base/recent.md) :id=recent

#### 数据查询(DEFAULT) :id=recent-Default
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_DELETED`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_SUBTYPE`,
t1.`OWNER_TYPE`,
t1.`RECENT_PARENT`,
t1.`RECENT_PARENT_IDENTIFIER`,
t1.`RECENT_PARENT_NAME`,
concat(t1.`RECENT_PARENT_IDENTIFIER`,'-',t1.`IDENTIFIER`) AS `SHOW_IDENTIFIER`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `RECENT` t1 

```

#### 默认（全部数据）(VIEW) :id=recent-View
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_DELETED`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_SUBTYPE`,
t1.`OWNER_TYPE`,
t1.`RECENT_PARENT`,
t1.`RECENT_PARENT_IDENTIFIER`,
t1.`RECENT_PARENT_NAME`,
concat(t1.`RECENT_PARENT_IDENTIFIER`,'-',t1.`IDENTIFIER`) AS `SHOW_IDENTIFIER`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `RECENT` t1 

```

#### 最近访问页面(recent_page) :id=recent-recent_page
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_DELETED`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_SUBTYPE`,
t1.`OWNER_TYPE`,
t1.`RECENT_PARENT`,
t1.`RECENT_PARENT_IDENTIFIER`,
t1.`RECENT_PARENT_NAME`,
concat(t1.`RECENT_PARENT_IDENTIFIER`,'-',t1.`IDENTIFIER`) AS `SHOW_IDENTIFIER`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `RECENT` t1 

WHERE ( t1.`OWNER_TYPE` = 'space'  AND  t1.`OWNER_SUBTYPE` = 'page'  AND  t1.`UPDATE_MAN` = #{ctx.sessioncontext.srfpersonid}  AND  exists(SELECT 1 FROM page t3 
inner join space t4 on t4.id = t3.space_id and t4.is_deleted = 0
where t3.id = t1.owner_id and 
 t3.is_archived = 0 and t3.is_deleted =0) )
```

#### 最近使用(recent_use) :id=recent-recent_use
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_DELETED`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_SUBTYPE`,
t1.`OWNER_TYPE`,
t1.`RECENT_PARENT`,
t1.`RECENT_PARENT_IDENTIFIER`,
t1.`RECENT_PARENT_NAME`,
concat(t1.`RECENT_PARENT_IDENTIFIER`,'-',t1.`IDENTIFIER`) AS `SHOW_IDENTIFIER`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `RECENT` t1 

WHERE ( t1.`CREATE_MAN` = #{ctx.sessioncontext.srfpersonid}  AND  t1.`TYPE` = '1'  AND  t1.`IS_DELETED` = 0 )
```

#### 本人最新访问(user) :id=recent-user
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_DELETED`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_SUBTYPE`,
t1.`OWNER_TYPE`,
t1.`RECENT_PARENT`,
t1.`RECENT_PARENT_IDENTIFIER`,
t1.`RECENT_PARENT_NAME`,
concat(t1.`RECENT_PARENT_IDENTIFIER`,'-',t1.`IDENTIFIER`) AS `SHOW_IDENTIFIER`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `RECENT` t1 

WHERE ( t1.`CREATE_MAN` = #{ctx.sessioncontext.srfpersonid} )
```


## [分组(SECTION)](module/Base/section.md) :id=section

#### 数据查询(DEFAULT) :id=section-Default
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`IS_LEAF`,
t1.`IS_LEAF2`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_SUBTYPE`,
t1.`OWNER_TYPE`,
t1.`SEQUENCE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`
FROM `SECTION` t1 

```

#### 默认（全部数据）(VIEW) :id=section-View
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`IS_LEAF`,
t1.`IS_LEAF2`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_SUBTYPE`,
t1.`OWNER_TYPE`,
t1.`SEQUENCE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`
FROM `SECTION` t1 

```

#### 检查名称是否重复(check_name) :id=section-check_name
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`IS_LEAF`,
t1.`IS_LEAF2`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_SUBTYPE`,
t1.`OWNER_TYPE`,
t1.`SEQUENCE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`
FROM `SECTION` t1 

WHERE ( t1.`ID` <> #{ctx.datacontext.id}  AND  t1.`NAME` = #{ctx.datacontext.name}  AND  t1.`OWNER_ID` = #{ctx.datacontext.owner_id}  AND  t1.`OWNER_TYPE` = #{ctx.datacontext.owner_type}  AND  t1.`OWNER_SUBTYPE` = #{ctx.datacontext.owner_subtype} )
```

#### 需求子产品(idea_section) :id=section-idea_section
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`IS_LEAF`,
t1.`IS_LEAF2`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_SUBTYPE`,
t1.`OWNER_TYPE`,
t1.`SEQUENCE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`
FROM `SECTION` t1 

WHERE ( t1.`OWNER_SUBTYPE` = 'idea' )
```

#### 我的分组(my_section) :id=section-my_section
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`IS_LEAF`,
t1.`IS_LEAF2`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_SUBTYPE`,
t1.`OWNER_TYPE`,
t1.`SEQUENCE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`
FROM `SECTION` t1 

WHERE ( t1.`CREATE_MAN` = #{ctx.sessioncontext.srfpersonid} )
```

#### 产品排期分组(this_product_section) :id=section-this_product_section
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`IS_LEAF`,
t1.`IS_LEAF2`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_SUBTYPE`,
t1.`OWNER_TYPE`,
t1.`SEQUENCE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`
FROM `SECTION` t1 

WHERE ( t1.`OWNER_ID` = #{ctx.webcontext.productid}  AND  t1.`OWNER_TYPE` = 'product_plan' )
```


## [序列(SEQUENCE_GENERATOR)](module/Base/sequence_generator.md) :id=sequence_generator

#### 数据查询(DEFAULT) :id=sequence_generator-Default
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`CURRENT_VALUE`,
t1.`GROUP_TAG`,
t1.`ID`,
t1.`NAME`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `SEQUENCE_GENERATOR` t1 

```

#### 默认（全部数据）(VIEW) :id=sequence_generator-View
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`CURRENT_VALUE`,
t1.`GROUP_TAG`,
t1.`ID`,
t1.`NAME`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `SEQUENCE_GENERATOR` t1 

```


## [共享空间(SHARED_SPACE)](module/Wiki/shared_space.md) :id=shared_space

#### 数据查询(DEFAULT) :id=shared_space-Default
```sql
SELECT
t1.`ACCESS_PASSWORD`,
t1.`EXPIRATION_DATE`,
t1.`ID`,
t1.`IS_SHARED`,
t1.`NAME`,
t1.`SCOPE_TYPE`,
t1.`SHARED_BY`,
t1.`SHARED_PAGES`,
t1.`SHARED_TIME`,
t1.`SHOW_LOGO`,
t1.`SHOW_TITLE`
FROM `SPACE` t1 

```

#### 默认（全部数据）(VIEW) :id=shared_space-View
```sql
SELECT
t1.`ACCESS_PASSWORD`,
t1.`EXPIRATION_DATE`,
t1.`ID`,
t1.`IS_SHARED`,
t1.`NAME`,
t1.`SCOPE_TYPE`,
t1.`SHARED_BY`,
t1.`SHARED_PAGES`,
t1.`SHARED_TIME`,
t1.`SHOW_LOGO`,
t1.`SHOW_TITLE`
FROM `SPACE` t1 

```

#### 管理员(admin) :id=shared_space-admin
```sql
SELECT
t1.`ACCESS_PASSWORD`,
t1.`EXPIRATION_DATE`,
t1.`ID`,
t1.`IS_SHARED`,
t1.`NAME`,
t1.`SCOPE_TYPE`,
t1.`SHARED_BY`,
t1.`SHARED_PAGES`,
t1.`SHARED_TIME`,
t1.`SHOW_LOGO`,
t1.`SHOW_TITLE`
FROM `SPACE` t1 

WHERE ( exists(select 1 from `space_member` t2 where t2.`SPACE_ID` = t1.`ID` and 
t2.ROLE_ID = 'admin' and t2.USER_ID = #{ctx.sessioncontext.srfpersonid}) )
```

#### 共享空间(shared) :id=shared_space-shared
```sql
SELECT
t1.`ACCESS_PASSWORD`,
t1.`EXPIRATION_DATE`,
t1.`ID`,
t1.`IS_SHARED`,
t1.`NAME`,
t1.`SCOPE_TYPE`,
t1.`SHARED_BY`,
t1.`SHARED_PAGES`,
t1.`SHARED_TIME`,
t1.`SHOW_LOGO`,
t1.`SHOW_TITLE`
FROM `SPACE` t1 

WHERE ( t1.`IS_SHARED` <> '0' )
```


## [空间(SPACE)](module/Wiki/space.md) :id=space

#### 数据查询(DEFAULT) :id=space-Default
```sql
SELECT
t11.`CATEGORIES`,
t1.`CATEGORY_ID`,
t11.`NAME` AS `CATEGORY_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_SHARED`,
t1.`NAME`,
t1.`SCOPE_ID`,
t1.`SCOPE_TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`,
t1.`VISIBILITY`
FROM `SPACE` t1 
LEFT JOIN `CATEGORY` t11 ON t1.`CATEGORY_ID` = t11.`ID` 

```

#### 默认（全部数据）(VIEW) :id=space-View
```sql
SELECT
t11.`CATEGORIES`,
t1.`CATEGORY_ID`,
t11.`NAME` AS `CATEGORY_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_SHARED`,
t1.`NAME`,
t1.`SCOPE_ID`,
t1.`SCOPE_TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`,
t1.`VISIBILITY`
FROM `SPACE` t1 
LEFT JOIN `CATEGORY` t11 ON t1.`CATEGORY_ID` = t11.`ID` 

```

#### 管理员(admin) :id=space-admin
```sql
SELECT
t11.`CATEGORIES`,
t1.`CATEGORY_ID`,
t11.`NAME` AS `CATEGORY_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_SHARED`,
t1.`NAME`,
t1.`SCOPE_ID`,
t1.`SCOPE_TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`,
t1.`VISIBILITY`
FROM `SPACE` t1 
LEFT JOIN `CATEGORY` t11 ON t1.`CATEGORY_ID` = t11.`ID` 

WHERE EXISTS(SELECT * FROM `SPACE_MEMBER` t21 
 WHERE 
 t1.`ID` = t21.`SPACE_ID`  AND  ( t21.`USER_ID` = #{ctx.sessioncontext.srfpersonid}  AND  t21.`ROLE_ID` = 'admin' ) )
```

#### 已归档(archived) :id=space-archived
```sql
SELECT
t11.`CATEGORIES`,
t1.`CATEGORY_ID`,
t11.`NAME` AS `CATEGORY_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_SHARED`,
t1.`NAME`,
t1.`SCOPE_ID`,
t1.`SCOPE_TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`,
t1.`VISIBILITY`
FROM `SPACE` t1 
LEFT JOIN `CATEGORY` t11 ON t1.`CATEGORY_ID` = t11.`ID` 

WHERE ( t1.`IS_ARCHIVED` = 1  AND  t1.`IS_DELETED` = 0 )
```

#### 目录下空间(category_space) :id=space-category_space
```sql
SELECT
t11.`CATEGORIES`,
t1.`CATEGORY_ID`,
t11.`NAME` AS `CATEGORY_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_SHARED`,
t1.`NAME`,
t1.`SCOPE_ID`,
t1.`SCOPE_TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`,
t1.`VISIBILITY`
FROM `SPACE` t1 
LEFT JOIN `CATEGORY` t11 ON t1.`CATEGORY_ID` = t11.`ID` 

WHERE ( t1.`IS_DELETED` = 0  AND  ( t1.`CATEGORY_ID` = #{ctx.webcontext.category_id}  OR  t11.`CATEGORIES` LIKE CONCAT('%',#{ctx.webcontext.category_id},'%') ) )
```

#### 当前空间(cur_space) :id=space-cur_space
```sql
SELECT
t11.`CATEGORIES`,
t1.`CATEGORY_ID`,
t11.`NAME` AS `CATEGORY_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_SHARED`,
t1.`NAME`,
t1.`SCOPE_ID`,
t1.`SCOPE_TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`,
t1.`VISIBILITY`
FROM `SPACE` t1 
LEFT JOIN `CATEGORY` t11 ON t1.`CATEGORY_ID` = t11.`ID` 

```

#### 当前空间(current) :id=space-current
```sql
SELECT
t11.`CATEGORIES`,
t1.`CATEGORY_ID`,
t11.`NAME` AS `CATEGORY_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_SHARED`,
t1.`NAME`,
t1.`SCOPE_ID`,
t1.`SCOPE_TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`,
t1.`VISIBILITY`
FROM `SPACE` t1 
LEFT JOIN `CATEGORY` t11 ON t1.`CATEGORY_ID` = t11.`ID` 

WHERE ( <choose><when test="ctx.webcontext.space !=null ">  t1.`ID` = #{ctx.webcontext.space}  </when><otherwise>1=1</otherwise></choose> )
```

#### 已删除(deleted) :id=space-deleted
```sql
SELECT
t11.`CATEGORIES`,
t1.`CATEGORY_ID`,
t11.`NAME` AS `CATEGORY_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_SHARED`,
t1.`NAME`,
t1.`SCOPE_ID`,
t1.`SCOPE_TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`,
t1.`VISIBILITY`
FROM `SPACE` t1 
LEFT JOIN `CATEGORY` t11 ON t1.`CATEGORY_ID` = t11.`ID` 

WHERE ( t1.`IS_DELETED` = 1 )
```

#### 查询星标(favorite) :id=space-favorite
```sql
SELECT
t11.`CATEGORIES`,
t1.`CATEGORY_ID`,
t11.`NAME` AS `CATEGORY_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_SHARED`,
t1.`NAME`,
t1.`SCOPE_ID`,
t1.`SCOPE_TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`,
t1.`VISIBILITY`
FROM `SPACE` t1 
LEFT JOIN `CATEGORY` t11 ON t1.`CATEGORY_ID` = t11.`ID` 

WHERE ( (select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) = '1'  AND  t1.`IS_DELETED` = 0  AND  t1.`IS_ARCHIVED` = 0 )
```

#### 查询星标（管理用户）(favorite_user) :id=space-favorite_user
```sql
SELECT
t11.`CATEGORIES`,
t1.`CATEGORY_ID`,
t11.`NAME` AS `CATEGORY_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_SHARED`,
t1.`NAME`,
t1.`SCOPE_ID`,
t1.`SCOPE_TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`,
t1.`VISIBILITY`
FROM `SPACE` t1 
LEFT JOIN `CATEGORY` t11 ON t1.`CATEGORY_ID` = t11.`ID` 

WHERE EXISTS(SELECT * FROM `SPACE_MEMBER` t21 
 WHERE 
 t1.`ID` = t21.`SPACE_ID`  AND  ( t21.`ROLE_ID` <> 'reader'  AND  t21.`USER_ID` = #{ctx.sessioncontext.srfpersonid} ) ) AND ( (select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) = '1'  AND  t1.`IS_DELETED` = 0  AND  t1.`IS_ARCHIVED` = 0 )
```

#### 移动端非星标空间(mob_unfavorite) :id=space-mob_unfavorite
```sql
SELECT
t11.`CATEGORIES`,
t1.`CATEGORY_ID`,
t11.`NAME` AS `CATEGORY_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_SHARED`,
t1.`NAME`,
t1.`SCOPE_ID`,
t1.`SCOPE_TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`VISIBILITY`
FROM `SPACE` t1 
LEFT JOIN `CATEGORY` t11 ON t1.`CATEGORY_ID` = t11.`ID` 
where 
 t1.`IS_DELETED` = 0  AND  (select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) = '0'  AND  t1.`IS_ARCHIVED` = 0 
 ORDER BY t1.`UPDATE_TIME` DESC


```

#### 未存在目录中的空间(no_category_space) :id=space-no_category_space
```sql
SELECT
t11.`CATEGORIES`,
t1.`CATEGORY_ID`,
t11.`NAME` AS `CATEGORY_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_SHARED`,
t1.`NAME`,
t1.`SCOPE_ID`,
t1.`SCOPE_TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`,
t1.`VISIBILITY`
FROM `SPACE` t1 
LEFT JOIN `CATEGORY` t11 ON t1.`CATEGORY_ID` = t11.`ID` 

WHERE ( t1.`IS_DELETED` = 0  AND  t1.`IS_ARCHIVED` = 0  AND  t1.`CATEGORY_ID` IS NULL )
```

#### 正常状态(normal) :id=space-normal
```sql
SELECT
t11.`CATEGORIES`,
t1.`CATEGORY_ID`,
t11.`NAME` AS `CATEGORY_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_SHARED`,
t1.`NAME`,
t1.`SCOPE_ID`,
t1.`SCOPE_TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`,
t1.`VISIBILITY`
FROM `SPACE` t1 
LEFT JOIN `CATEGORY` t11 ON t1.`CATEGORY_ID` = t11.`ID` 

WHERE ( t1.`IS_DELETED` = 0  AND  t1.`IS_ARCHIVED` = 0 )
```

#### 公开(public) :id=space-public
```sql
SELECT
t11.`CATEGORIES`,
t1.`CATEGORY_ID`,
t11.`NAME` AS `CATEGORY_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_SHARED`,
t1.`NAME`,
t1.`SCOPE_ID`,
t1.`SCOPE_TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`,
t1.`VISIBILITY`
FROM `SPACE` t1 
LEFT JOIN `CATEGORY` t11 ON t1.`CATEGORY_ID` = t11.`ID` 

WHERE ( t1.`VISIBILITY` = 'public' )
```

#### 只读用户(reader) :id=space-reader
```sql
SELECT
t11.`CATEGORIES`,
t1.`CATEGORY_ID`,
t11.`NAME` AS `CATEGORY_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_SHARED`,
t1.`NAME`,
t1.`SCOPE_ID`,
t1.`SCOPE_TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`,
t1.`VISIBILITY`
FROM `SPACE` t1 
LEFT JOIN `CATEGORY` t11 ON t1.`CATEGORY_ID` = t11.`ID` 

WHERE EXISTS(SELECT * FROM `SPACE_MEMBER` t21 
 WHERE 
 t1.`ID` = t21.`SPACE_ID`  AND  ( t21.`USER_ID` = #{ctx.sessioncontext.srfpersonid}  AND  t21.`ROLE_ID` = 'reader' ) )
```

#### 非星标空间(unfavorite) :id=space-unfavorite
```sql
SELECT
t11.`CATEGORIES`,
t1.`CATEGORY_ID`,
t11.`NAME` AS `CATEGORY_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_SHARED`,
t1.`NAME`,
t1.`SCOPE_ID`,
t1.`SCOPE_TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`,
t1.`VISIBILITY`
FROM `SPACE` t1 
LEFT JOIN `CATEGORY` t11 ON t1.`CATEGORY_ID` = t11.`ID` 

WHERE ( t1.`IS_DELETED` = 0  AND  (select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) = '0'  AND  t1.`IS_ARCHIVED` = 0 )
```

#### 非星标空间（管理用户）(unfavorite_user) :id=space-unfavorite_user
```sql
SELECT
t11.`CATEGORIES`,
t1.`CATEGORY_ID`,
t11.`NAME` AS `CATEGORY_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_SHARED`,
t1.`NAME`,
t1.`SCOPE_ID`,
t1.`SCOPE_TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`,
t1.`VISIBILITY`
FROM `SPACE` t1 
LEFT JOIN `CATEGORY` t11 ON t1.`CATEGORY_ID` = t11.`ID` 

WHERE EXISTS(SELECT * FROM `SPACE_MEMBER` t21 
 WHERE 
 t1.`ID` = t21.`SPACE_ID`  AND  ( t21.`ROLE_ID` <> 'reader'  AND  t21.`USER_ID` = #{ctx.sessioncontext.srfpersonid} ) ) AND ( t1.`IS_DELETED` = 0  AND  (select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) = '0'  AND  t1.`IS_ARCHIVED` = 0 )
```

#### 操作用户(user) :id=space-user
```sql
SELECT
t11.`CATEGORIES`,
t1.`CATEGORY_ID`,
t11.`NAME` AS `CATEGORY_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_SHARED`,
t1.`NAME`,
t1.`SCOPE_ID`,
t1.`SCOPE_TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`,
t1.`VISIBILITY`
FROM `SPACE` t1 
LEFT JOIN `CATEGORY` t11 ON t1.`CATEGORY_ID` = t11.`ID` 

WHERE EXISTS(SELECT * FROM `SPACE_MEMBER` t21 
 WHERE 
 t1.`ID` = t21.`SPACE_ID`  AND  ( t21.`USER_ID` = #{ctx.sessioncontext.srfpersonid}  AND  t21.`ROLE_ID` = 'user' ) )
```


## [空间成员(SPACE_MEMBER)](module/Wiki/space_member.md) :id=space_member

#### 数据查询(DEFAULT) :id=space_member-Default
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`NAME`,
t1.`ROLE_ID`,
t1.`SPACE_ID`,
t11.`IDENTIFIER` AS `SPACE_IDENTIFIER`,
t11.`NAME` AS `SPACE_NAME`,
t1.`TITLE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_ID`
FROM `SPACE_MEMBER` t1 
LEFT JOIN `SPACE` t11 ON t1.`SPACE_ID` = t11.`ID` 

```

#### 默认（全部数据）(VIEW) :id=space_member-View
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`NAME`,
t1.`ROLE_ID`,
t1.`SPACE_ID`,
t11.`IDENTIFIER` AS `SPACE_IDENTIFIER`,
t11.`NAME` AS `SPACE_NAME`,
t1.`TITLE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_ID`
FROM `SPACE_MEMBER` t1 
LEFT JOIN `SPACE` t11 ON t1.`SPACE_ID` = t11.`ID` 

```

#### 当前空间下成员(cur_space) :id=space_member-cur_space
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`NAME`,
t1.`ROLE_ID`,
t1.`SPACE_ID`,
t11.`IDENTIFIER` AS `SPACE_IDENTIFIER`,
t11.`NAME` AS `SPACE_NAME`,
t1.`TITLE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_ID`
FROM `SPACE_MEMBER` t1 
LEFT JOIN `SPACE` t11 ON t1.`SPACE_ID` = t11.`ID` 

WHERE ( t1.`USER_ID` <> #{ctx.sessioncontext.srfpersonid}  AND  t1.`SPACE_ID` = #{ctx.datacontext.id} )
```

#### 未关注用户(测试用例)(no_attention) :id=space_member-no_attention
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`NAME`,
t1.`ROLE_ID`,
t1.`SPACE_ID`,
t11.`IDENTIFIER` AS `SPACE_IDENTIFIER`,
t11.`NAME` AS `SPACE_NAME`,
t1.`TITLE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_ID`
FROM `SPACE_MEMBER` t1 
LEFT JOIN `SPACE` t11 ON t1.`SPACE_ID` = t11.`ID` 

WHERE ( ( USER_ID NOT IN (SELECT user_id from attention t2 where t2.OWNER_ID = #{ctx.webcontext.test_case} )) )
```


## [页面模板(STENCIL)](module/Wiki/stencil.md) :id=stencil

#### 数据查询(DEFAULT) :id=stencil-Default
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`FORMAT_TYPE`,
t1.`ID`,
t1.`IS_GLOBAL`,
t1.`NAME`,
t1.`SPACE_ID`,
t11.`NAME` AS `SPACE_NAME`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `STENCIL` t1 
LEFT JOIN `SPACE` t11 ON t1.`SPACE_ID` = t11.`ID` 

```

#### 默认（全部数据）(VIEW) :id=stencil-View
```sql
SELECT
t1.`CONTENT`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`FORMAT_TYPE`,
t1.`ID`,
t1.`IS_GLOBAL`,
t1.`NAME`,
t1.`SPACE_ID`,
t11.`NAME` AS `SPACE_NAME`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `STENCIL` t1 
LEFT JOIN `SPACE` t11 ON t1.`SPACE_ID` = t11.`ID` 

```

#### 非空间下模板(no_space_stencil) :id=stencil-no_space_stencil
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`FORMAT_TYPE`,
t1.`ID`,
t1.`IS_GLOBAL`,
t1.`NAME`,
t1.`SPACE_ID`,
t11.`NAME` AS `SPACE_NAME`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `STENCIL` t1 
LEFT JOIN `SPACE` t11 ON t1.`SPACE_ID` = t11.`ID` 

WHERE ( t1.`SPACE_ID` IS NULL )
```

#### 只读用户(reader) :id=stencil-reader
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`FORMAT_TYPE`,
t1.`ID`,
t1.`IS_GLOBAL`,
t1.`NAME`,
t1.`SPACE_ID`,
t11.`NAME` AS `SPACE_NAME`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `STENCIL` t1 
LEFT JOIN `SPACE` t11 ON t1.`SPACE_ID` = t11.`ID` 

/*ALIAS.sp=t11*/
WHERE EXISTS(SELECT * FROM `SPACE_MEMBER` t21 
 WHERE 
 t11.`ID` = t21.`SPACE_ID`  AND  ( t21.`USER_ID` = #{ctx.sessioncontext.srfpersonid} ) )
```

#### 空间下页面模板(space_stencil) :id=stencil-space_stencil
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`FORMAT_TYPE`,
t1.`ID`,
t1.`IS_GLOBAL`,
t1.`NAME`,
t1.`SPACE_ID`,
t11.`NAME` AS `SPACE_NAME`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `STENCIL` t1 
LEFT JOIN `SPACE` t11 ON t1.`SPACE_ID` = t11.`ID` 

WHERE ( t1.`SPACE_ID` = #{ctx.webcontext.space} )
```


## [版本(VERSION)](module/Base/version.md) :id=version

#### 数据查询(DEFAULT) :id=version-Default
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_NAMED`,
t1.`MANUAL`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_TYPE`,
t1.`RESTORABLE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `VERSION` t1 

```

#### 默认（全部数据）(VIEW) :id=version-View
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DATA`,
t1.`DESCRIPTION`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_NAMED`,
t1.`MANUAL`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_TYPE`,
t1.`RESTORABLE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `VERSION` t1 

```

#### 命名版本(name_version) :id=version-name_version
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_NAMED`,
t1.`MANUAL`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_TYPE`,
t1.`RESTORABLE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `VERSION` t1 

WHERE ( t1.`IS_NAMED` = 1 )
```

#### 所属对象版本(owner) :id=version-owner
```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_NAMED`,
t1.`MANUAL`,
t1.`NAME`,
t1.`OWNER_ID`,
t1.`OWNER_TYPE`,
t1.`RESTORABLE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `VERSION` t1 

WHERE ( t1.`OWNER_ID` = #{ctx.datacontext.owner_id} )
```

