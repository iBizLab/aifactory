```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."position_id",
t11."name" AS "position_name",
t1."role_id",
t1."title",
t1."update_man",
t1."update_time",
t1."user_id"
FROM "member" t1 
LEFT JOIN "position" t11 ON t1."position_id" = t11."id" 

WHERE ( ( USER_ID NOT IN (SELECT user_id from attention t2 where t2.OWNER_ID = #{ctx.webcontext.principal_id} )) )
```