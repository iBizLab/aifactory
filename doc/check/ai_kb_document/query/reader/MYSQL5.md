```sql
SELECT
t1.`ACTIVE`,
t1.`CATEGORIES`,
t1.`CHUNK_METHOD`,
t1.`CHUNK_NUM`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`CUSTOM_CHUNK`,
t1.`DIGEST_CODE`,
TO_CHAR(t1.`CREATE_TIME`, 'YYYY-MM-DD') AS `DOC_CREATE_TIME`,
t1.`FILE`,
t1.`FILE_TYPE`,
t1.`ID`,
t1.`KB_ID`,
t11.`NAME` AS `KB_NAME`,
t1.`KEY`,
t1.`NAME`,
concat_ws('/',nullif(btrim(t1.`CATEGORIES`, '/'),''),t1.`NAME`||'.'||COALESCE(t1.`FILE_TYPE`,'md')) AS `PATH`,
CURRENT_DATE - t1.`CREATE_TIME`::date AS `RECENT_CREATE_DAYS`,
t1.`RESOURCE`,
t1.`SEQUENCE`,
t1.`SIZE`,
t1.`SOURCE_ID`,
t1.`SOURCE_TYPE`,
t1.`STATUS`,
t1.`SYNC_FREQUENCY`,
t1.`SYNC_ID`,
t11.`TAG_SETS`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`
FROM `AI_KB_DOCUMENT` t1 
LEFT JOIN `AI_KNOWLEDGE_BASE` t11 ON t1.`KB_ID` = t11.`ID` 

WHERE ( ( t11.`VISIBILITY` = 'public'  OR  ( t11.`SCOPE_ID` = #{ctx.sessioncontext.srforgid}  AND  t11.`SCOPE_TYPE` = 'organization' )  OR  EXISTS(SELECT 1 FROM AI_KB_MEMBER m 
 WHERE 
 t11.ID = m.KB_ID  AND  ( m.USER_ID = #{ctx.sessioncontext.srfpersonid} ) )  OR  ( t11.`SCOPE_TYPE` = 'user_group'  AND  t11.`SCOPE_ID` = #{ctx.sessioncontext.srfgroup_user} ) ) )
```