```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."name",
t1."portfolio_id",
t11."identifier" AS "portfolio_identifier",
t11."name" AS "portfolio_name",
t1."role_id",
t1."update_man",
t1."update_time",
t1."user_id"
FROM "portfolio_member" t1 
LEFT JOIN "portfolio" t11 ON t1."portfolio_id" = t11."id" 


```