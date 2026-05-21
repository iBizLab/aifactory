```sql
SELECT
t1."avatar",
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."name",
t1."section_id",
t11."name" AS "section_name",
t1."sequence",
t1."update_man",
t1."update_time",
t1."visibility"
FROM "user_group" t1 
LEFT JOIN "section" t11 ON t1."section_id" = t11."id" 

WHERE ( t1."visibility" = 'public' )
```