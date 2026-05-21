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