```sql
SELECT
t1.`CHUNK_METHOD`,
t1.`CUSTOM_CHUNK`,
t1.`ID`,
t1.`NAME`,
concat_ws('/',nullif(btrim(t1.`CATEGORIES`, '/'),''),t1.`NAME`||'.'||COALESCE(t1.`FILE_TYPE`,'md')) AS `PATH`,
t1.`SEQUENCE`,
t1.`STATUS`,
t1.`SYNC_ID`,
t1.`TYPE`,
t1.`UPDATE_TIME`
FROM `AI_KB_DOCUMENT` t1 


```