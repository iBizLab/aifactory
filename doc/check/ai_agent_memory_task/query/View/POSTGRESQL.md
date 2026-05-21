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