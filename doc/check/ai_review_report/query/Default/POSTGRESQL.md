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