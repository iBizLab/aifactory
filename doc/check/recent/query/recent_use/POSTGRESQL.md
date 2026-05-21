```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."identifier",
t1."is_deleted",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."recent_parent",
t1."recent_parent_identifier",
t1."recent_parent_name",
concat(t1."recent_parent_identifier",'-',t1."identifier") AS "show_identifier",
t1."type",
t1."update_man",
t1."update_time"
FROM "recent" t1 

WHERE ( t1."create_man" = #{ctx.sessioncontext.srfpersonid}  AND  t1."type" = '1'  AND  t1."is_deleted" = 0 )
```