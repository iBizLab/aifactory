```sql
SELECT
t1."id",
t1."is_shared",
CASE WHEN EXISTS (SELECT 1 FROM ( select id from page where is_shared = '1' ) AS ids WHERE ids.id = ANY(string_to_array(replace(t1.categories, '/', ','), ','))) THEN 1 ELSE 0 END AS "read_shared"
FROM "page" t1 

WHERE ( ( t1."is_shared" = '1'  OR  CASE WHEN EXISTS (SELECT 1 FROM ( select id from page where is_shared = '1' ) AS ids WHERE ids.id = ANY(string_to_array(replace(t1.categories, '/', ','), ','))) THEN 1 ELSE 0 END = '1' )  AND  t1."is_published" = 1  AND  t1."is_deleted" = 0 )
```