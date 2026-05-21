```sql
SELECT
t1."avatar",
t1."create_man",
t1."create_time",
t1."department_id",
t1."display_name",
t1."email",
t1."employee_number",
t1."id",
t1."job_id",
t1."mobile",
t1."name",
t1."open_user_tag",
t1."organization_id",
t1."status",
t1."title",
t1."update_man",
t1."update_time"
FROM "" t1 

WHERE ( t1."id" = #{ctx.sessioncontext.srfpersonid} )
```