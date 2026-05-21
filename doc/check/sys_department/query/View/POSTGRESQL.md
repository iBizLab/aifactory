```sql
SELECT
t1."business_category",
t1."create_time",
t1."creator",
t1."dc",
t1."department_name",
t1."department_number",
t1."description",
concat_ws(',',t1."department_name",t1."parent_name",t1."organization_name") AS "dn",
t1."enabled",
t1."id",
t1."is_leaf",
t1."organization_id",
t1."organization_name",
t1."organization_number",
t1."parent_id",
t1."parent_name",
case when t1."parent_id" is null or t1."parent_id"='' then t1."organization_id" else t1."parent_id" end AS "parent_unit_id",
case when t1."parent_name" is null or t1."parent_name"='' then t1."organization_name" else t1."parent_name" end AS "parent_unit_name",
t1."short_name",
t1."sort",
t1."updater",
t1."update_time"
FROM "" t1 

WHERE t1.enabled = 1
```