```sql
SELECT
t1."create_man",
t1."create_time",
t1."description",
t1."enable",
t11."executor_tag",
t1."finished_at",
t1."id",
t1."max_retry",
t1."name",
t1."payload",
t1."principal_id",
t1."principal_name",
t1."principal_type",
t1."result",
t1."result_message",
t1."retry_count",
t1."scheduled_at",
t1."schedule_id",
t1."started_at",
t1."status",
t1."task_type",
t11."name" AS "task_type_name",
t1."update_man",
t1."update_time"
FROM "extend_scheduled_task" t1 
LEFT JOIN "extend_task_type" t11 ON t1."task_type" = t11."id" 


```