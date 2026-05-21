```sql
SELECT
t1."context_code_name",
t11."context_debug_data",
t1."context_id",
t1."id",
t1."name"
FROM "" t1 
LEFT JOIN "ai_agent_context" t11 ON t1."context_id" = t11."id" 


```