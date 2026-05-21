```sql
SELECT
t1."app_tag",
t1."categories",
t1."category",
t1."chart_type",
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."is_system",
t1."name",
t1."template_model",
t1."update_man",
t1."update_time",
t1."view_id",
t11."name" AS "view_name"
FROM "insight_report" t1 
LEFT JOIN "insight_view" t11 ON t1."view_id" = t11."id" 

WHERE ( t1."is_system" = 1 )
```