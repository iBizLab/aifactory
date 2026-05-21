```sql
SELECT
concat(t1."base_url",t1."default_version") AS "api_base_url",
t1."base_url",
t1."default_token",
t1."default_version",
(select count(1) from ai_credential  where id =t1."id") AS "has_credential",
t1."id",
t1."name",
t1."update_time"
FROM "ai_model_provider" t1 

WHERE ( (select count(1) from ai_credential  where id =t1."id") = '0' )
```