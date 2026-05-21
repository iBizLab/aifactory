```sql
SELECT
t1."assignee_id",
t1."assignee_name",
t1."create_man",
t1."create_time",
t1."description",
t1."end_at",
t1."id",
t1."identifier",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."name",
t1."start_at",
t1."state",
t1."update_man",
t1."update_time"
FROM "portfolio" t1 

WHERE ( exists(select 1 from `work` t2 where t2.principal_id= t1.id and t2.portfolio_id = #{ctx.webcontext.project_portfolio})  AND  t1."is_deleted" = 0 )
```