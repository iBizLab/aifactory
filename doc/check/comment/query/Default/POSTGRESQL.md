```sql
SELECT
t1."content",
t1."create_man",
t1."create_time",
t1."id",
t1."is_top",
t1."name",
t1."owner_type",
t11."content" AS "pcontent",
t11."create_man" AS "pcreate_man",
t1."pid",
t1."principal_id",
t1."principal_name",
t1."principal_type",
t1."update_man",
t1."update_time"
FROM "comment" t1 
LEFT JOIN "comment" t11 ON t1."pid" = t11."id" 


```