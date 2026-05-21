```sql
SELECT
t1."id",
t1."user_id"
FROM "attention" t1 

WHERE ( t1."owner_id" = #{ctx.webcontext.id}  AND  <choose><when test="ctx.webcontext.principal_id !=null ">  t1."owner_id" = #{ctx.webcontext.principal_id}  </when><otherwise>1=1</otherwise></choose>  AND  ( t1."type" = '30'  OR  t1."type" = '40' )  AND  t1."user_id" <> #{ctx.sessioncontext.srfpersonid} )
```