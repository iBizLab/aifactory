```sql
SELECT
t11."categories",
t1."category_id",
t11."name" AS "category_name",
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_shared",
t1."name",
t1."scope_id",
t1."scope_type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2",
t1."visibility"
FROM "space" t1 
LEFT JOIN "category" t11 ON t1."category_id" = t11."id" 

WHERE ( t1."is_deleted" = 0  AND  (select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) = '0'  AND  t1."is_archived" = 0 )
```