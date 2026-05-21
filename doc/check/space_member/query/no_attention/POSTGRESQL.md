```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."name",
t1."role_id",
t1."space_id",
t11."identifier" AS "space_identifier",
t11."name" AS "space_name",
t1."title",
t1."update_man",
t1."update_time",
t1."user_id"
FROM "space_member" t1 
LEFT JOIN "space" t11 ON t1."space_id" = t11."id" 

WHERE ( ( USER_ID NOT IN (SELECT user_id from attention t2 where t2.OWNER_ID = #{ctx.webcontext.test_case} )) )
```