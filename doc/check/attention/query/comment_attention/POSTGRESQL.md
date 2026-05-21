```sql
SELECT
t1."id",
t1."user_id"
FROM "attention" t1 

WHERE ( exists(select 1 from `comment` t2 where t1.owner_id = t2.PRINCIPAL_ID and t2.id=#{ctx.webcontext.id})  AND  t1."type" = '40'  AND  t1."user_id" <> #{ctx.sessioncontext.srfpersonid} )
```