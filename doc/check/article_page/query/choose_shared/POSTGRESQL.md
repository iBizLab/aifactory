```sql
SELECT
t1."icon",
t1."id",
t1."name",
t1."parent_id",
t1."publish_name",
t1."space_id"
FROM "page" t1 

WHERE ( t1."is_deleted" = 0  AND  t1."is_published" = 1 )
```