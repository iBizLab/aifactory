```sql
SELECT
t1."id",
concat_ws('/',nullif(btrim(t1."categories", '/'),''),t1."name"||'.'||COALESCE(t1."file_type",'md')) AS "path",
t1."size"
FROM "ai_kb_document" t1 


```