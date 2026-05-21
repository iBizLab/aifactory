```sql
SELECT
t1."chunk_method",
t1."custom_chunk",
t1."id",
t1."name",
concat_ws('/',nullif(btrim(t1."categories", '/'),''),t1."name"||'.'||COALESCE(t1."file_type",'md')) AS "path",
t1."sequence",
t1."status",
t1."sync_id",
t1."type",
t1."update_time"
FROM "ai_kb_document" t1 


```