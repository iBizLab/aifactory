```sql
SELECT
t1."id",
t1."user_id"
FROM "member" t1 

WHERE ( t1."role_id" = 'admin'  AND  t1."owner_type" = 'GROUP' )
```