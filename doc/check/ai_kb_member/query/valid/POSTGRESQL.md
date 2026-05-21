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