```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."is_leaf",
t1."is_leaf2",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."sequence",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "section" t1 

WHERE ( t1."id" <> #{ctx.datacontext.id}  AND  t1."name" = #{ctx.datacontext.name}  AND  t1."owner_id" = #{ctx.datacontext.owner_id}  AND  t1."owner_type" = #{ctx.datacontext.owner_type}  AND  t1."owner_subtype" = #{ctx.datacontext.owner_subtype} )
```