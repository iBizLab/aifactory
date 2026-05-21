```sql
SELECT
t1."avatar",
t1."create_time",
t1."creator",
t1."dc",
t1."description",
t1."display_name",
concat_ws(',',t1."display_name",t1."organization_name") AS "dn",
t1."employee_number",
t1."employee_type",
t1."enable",
t1."id",
t1."identification_number",
t1."mail",
t1."mdepartment_id",
t1."mdepartment_name",
t1."mobile",
t1."organization_id",
t1."organization_name",
t1."postal_address",
t1."status",
t1."telephone_number",
t1."title",
t1."uid",
t1."updater",
t1."update_time",
t1."user_password"
FROM "" t1 

WHERE t1.enable = 1
```