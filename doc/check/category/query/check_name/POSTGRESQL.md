```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."id",
t1."is_deleted",
t1."is_leaf",
t1."is_leaf2",
t1."is_leaf3",
case when t1."is_leaf"+t1."is_leaf2"=2 then 1 else 0 end AS "leaf_flag",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."pid",
t1."section_id",
t11."name" AS "section_name",
t1."sequence",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2",
t1."wf_version_id"
FROM "category" t1 
LEFT JOIN "section" t11 ON t1."section_id" = t11."id" 

WHERE ( <choose><when test="ctx.datacontext.id !=null ">  t1."id" <> #{ctx.datacontext.id}  </when><otherwise>1=1</otherwise></choose>  AND  <choose><when test="ctx.datacontext.name !=null ">  t1."name" = #{ctx.datacontext.name}  </when><otherwise>1=1</otherwise></choose>  AND  <choose><when test="ctx.datacontext.owner_id !=null ">  t1."owner_id" = #{ctx.datacontext.owner_id}  </when><otherwise>1=1</otherwise></choose>  AND  t1."owner_type" = #{ctx.datacontext.owner_type}  AND  <choose><when test="ctx.datacontext.owner_subtype !=null ">  t1."owner_subtype" = #{ctx.datacontext.owner_subtype}  </when><otherwise>1=1</otherwise></choose> )
```