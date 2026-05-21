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