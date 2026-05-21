```sql
SELECT
t1."create_time",
t1."enabled",
t1."id",
t1."name",
t1."resource_code",
t1."sort",
t1."update_time"
FROM "data_resource" t1 

WHERE t1.enabled = 1
```