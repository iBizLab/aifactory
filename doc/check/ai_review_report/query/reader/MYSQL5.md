```sql
SELECT
t1.`AGENT_TAG`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DOCUMENT_ID`,
t21.`NAME` AS `DOCUMENT_NAME`,
t1.`ID`,
t1.`KB_ID`,
t11.`NAME` AS `KB_NAME`,
t1.`NAME`,
t1.`RECORD_ID`,
t1.`REVIEW_RESULT`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_REVIEW_REPORT` t1 
LEFT JOIN `AI_KNOWLEDGE_BASE` t11 ON t1.`KB_ID` = t11.`ID` 
LEFT JOIN `AI_KB_DOCUMENT` t21 ON t1.`DOCUMENT_ID` = t21.`ID` 

WHERE ( ( t11.`VISIBILITY` = 'public'  OR  ( t11.`SCOPE_ID` = #{ctx.sessioncontext.srforgid}  AND  t11.`SCOPE_TYPE` = 'organization' )  OR  EXISTS(SELECT 1 FROM AI_KB_MEMBER m 
 WHERE 
 t11.ID = m.KB_ID  AND  ( m.USER_ID = #{ctx.sessioncontext.srfpersonid} ) ) ) )
```