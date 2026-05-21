```sql
SELECT
t1."appid",
t1."description",
t1."dynadashboardid",
t1."dynadashboardname",
t1."example_chart",
t1."is_system",
t1."modelid",
t1."sequences",
t1."type"
FROM "dynadashboard" t1 

WHERE ( t1."is_system" = 1 )
```