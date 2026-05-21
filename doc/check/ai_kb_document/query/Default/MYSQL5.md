```sql
SELECT
t1.`ACTIVE`,
t1.`CATEGORIES`,
t1.`CHUNK_METHOD`,
t1.`CHUNK_NUM`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`CUSTOM_CHUNK`,
TO_CHAR(t1.`CREATE_TIME`, 'YYYY-MM-DD') AS `DOC_CREATE_TIME`,
case when t1.`FILE_TYPE` = 'xls' or t1.`FILE_TYPE` = 'xlsx' then 'Excel'  when t1.`FILE_TYPE` = 'pdf'  then 'PDF'  when t1.`FILE_TYPE` = 'doc' or t1.`FILE_TYPE` = 'docx'  then 'Word' when t1.`FILE_TYPE` = 'pptx' or t1.`FILE_TYPE` = 'ppt' then  'PPT'  else  '其他'  end AS `DOC_TYPE`,
t1.`FILE`,
t1.`FILE_TYPE`,
t1.`ID`,
t1.`KB_ID`,
t11.`NAME` AS `KB_NAME`,
t1.`KEY`,
t1.`NAME`,
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
t1.`UPDATE_TIME`
FROM `AI_KB_DOCUMENT` t1 
LEFT JOIN `AI_KNOWLEDGE_BASE` t11 ON t1.`KB_ID` = t11.`ID` 


```