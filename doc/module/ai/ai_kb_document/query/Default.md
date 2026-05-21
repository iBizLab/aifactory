## DEFAULT(Default) <!-- {docsify-ignore-all} -->



<p class="panel-title"><b>查看SQL语句</b></p>
<br>

<el-row>
&nbsp;<el-tag @click="MYSQL5 = true">MYSQL5</el-tag>
&nbsp;<el-tag @click="POSTGRESQL = true">POSTGRESQL</el-tag>
</el-row>

<br>
<p class="panel-title"><b>是否默认查询</b></p>

* `是`

<p class="panel-title"><b>是否权限使用</b></p>

* `否`

<p class="panel-title"><b>是否自定义SQL</b></p>

* `否`

<p class="panel-title"><b>查询列级别</b></p>

* `默认（全部查询列）`






<el-dialog v-model="MYSQL5" title="MYSQL5">

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

</el-dialog>

<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t1."active",
t1."categories",
t1."chunk_method",
t1."chunk_num",
t1."create_man",
t1."create_time",
t1."custom_chunk",
t1."digest_code",
TO_CHAR(t1."create_time", 'YYYY-MM-DD') AS "doc_create_time",
t1."file",
t1."file_type",
t1."id",
t1."kb_id",
t11."name" AS "kb_name",
t1."key",
t1."name",
concat_ws('/',nullif(btrim(t1."categories", '/'),''),t1."name"||'.'||COALESCE(t1."file_type",'md')) AS "path",
CURRENT_DATE - t1."create_time"::date AS "recent_create_days",
t1."resource",
t1."sequence",
t1."size",
t1."source_id",
t1."source_type",
t1."status",
t1."sync_frequency",
t1."sync_id",
t11."tag_sets",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "ai_kb_document" t1 
LEFT JOIN "ai_knowledge_base" t11 ON t1."kb_id" = t11."id" 


```

</el-dialog>

<script>
 const { createApp } = Vue
  createApp({
    data() {
      return {
                MYSQL5 : false
                POSTGRESQL : false
        
      }
    },
    methods: {
    }
  }).use(ElementPlus).mount('#app')
</script>