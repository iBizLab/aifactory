```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."title",
t1."type",
t1."update_man",
t1."update_time",
t1."user_id"
FROM "attention" t1 

WHERE ( t1."owner_id" = #{ctx.webcontext.principal_id} )
```