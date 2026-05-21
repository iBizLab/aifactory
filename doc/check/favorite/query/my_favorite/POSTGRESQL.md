```sql
SELECT
t1."create_man",
t1."create_time",
t1."id",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."update_man",
t1."update_time"
FROM "favorite" t1 

WHERE ( t1."create_man" = #{ctx.sessioncontext.srfpersonid} )
```