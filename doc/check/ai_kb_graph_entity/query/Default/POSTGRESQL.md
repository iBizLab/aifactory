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