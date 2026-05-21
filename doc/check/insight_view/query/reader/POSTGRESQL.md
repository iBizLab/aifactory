```sql
SELECT
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."name",
t1."scope_id",
t1."scope_type",
t1."update_man",
t1."update_time",
t1."visibility"
FROM "insight_view" t1 

WHERE EXISTS(SELECT * FROM "member" t11 
 WHERE 
 t1."id" = t11."owner_id"  AND  ( t11."user_id" = #{ctx.sessioncontext.srfpersonid}  AND  t11."role_id" = 'reader'  AND  t11."owner_type" = 'INSIGHT' ) )
```