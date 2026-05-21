```sql
SELECT
t1."create_man",
t1."create_time",
t1."description",
t1."enable",
t1."id",
t1."name",
t1."next_trigger_time",
t1."principal_id",
t1."principal_name",
t1."principal_type",
t1."schedule_type",
t1."task_type",
t11."name" AS "task_type_name",
t1."timer_policy",
t1."update_man",
t1."update_time"
FROM "extend_schedule" t1 
LEFT JOIN "extend_task_type" t11 ON t1."task_type" = t11."id" 


```