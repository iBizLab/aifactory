```sql
SELECT
t1."create_man",
t1."create_time",
t1."format_type",
t1."id",
t1."is_global",
t1."name",
t1."space_id",
t11."name" AS "space_name",
t1."update_man",
t1."update_time"
FROM "stencil" t1 
LEFT JOIN "space" t11 ON t1."space_id" = t11."id" 

/*ALIAS.sp=t11*/
WHERE EXISTS(SELECT * FROM "space_member" t21 
 WHERE 
 t11."id" = t21."space_id"  AND  ( t21."user_id" = #{ctx.sessioncontext.srfpersonid} ) )
```