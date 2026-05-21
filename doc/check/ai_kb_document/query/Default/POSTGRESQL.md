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