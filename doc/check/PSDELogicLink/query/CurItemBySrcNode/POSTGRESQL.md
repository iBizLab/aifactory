```sql
SELECT
t1."dstpsdelogicnodeid",
t1."psdelogicid",
t1."psdelogiclinkid",
t1."psdelogiclinkname",
t1."srcpsdelogicnodeid"
FROM "" t1 

WHERE ( t1."srcpsdelogicnodeid" = #{ctx.datacontext.psdelogicnode} )
```