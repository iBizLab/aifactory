```sql
SELECT
t1."_create_time",
t1."_creator",
t1."_enabled",
t1."_id",
t1."_key",
t1."_ner_flag",
t1."_region",
t11."resource_code" AS "_resource_code",
t1."_resource_id",
t11."name" AS "_resource_name",
t1."_summary",
t1."_title",
t1."_updater",
t1."_update_time"
FROM "data_record" t1 
LEFT JOIN "data_resource" t11 ON t1."_resource_id" = t11."id" 

WHERE t1._enabled = 1
```