```sql
SELECT
t1."category_id",
t1."create_man",
t1."create_time",
t1."enable",
t1."id",
t1."name",
t1."sequence",
t1."update_man",
t1."update_time"
FROM "position" t1 

WHERE t1.enable = 1 AND ( t1."category_id" IS NULL )
```