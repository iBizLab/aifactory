```sql
SELECT
t1."expiration_date",
t1."id",
t1."is_shared",
t1."is_shared_subset",
t1."name",
t1."publish_name",
t1."shared_by",
t1."shared_time",
t1."space_id",
t1."update_man",
t1."update_time"
FROM "page" t1 

WHERE ( t1."is_shared" = '1'  AND  t1."is_deleted" = 0  AND  t1."is_published" = 1 )
```