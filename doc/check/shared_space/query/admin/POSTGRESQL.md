```sql
SELECT
t1."access_password",
t1."expiration_date",
t1."id",
t1."is_shared",
t1."name",
t1."scope_type",
t1."shared_by",
t1."shared_pages",
t1."shared_time",
t1."show_logo",
t1."show_title"
FROM "space" t1 

WHERE ( exists(select 1 from `space_member` t2 where t2.`SPACE_ID` = t1.`ID` and 
t2.ROLE_ID = 'admin' and t2.USER_ID = #{ctx.sessioncontext.srfpersonid}) )
```