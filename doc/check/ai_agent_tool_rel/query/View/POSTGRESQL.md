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