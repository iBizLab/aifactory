## reader(reader) <!-- {docsify-ignore-all} -->



<p class="panel-title"><b>查看SQL语句</b></p>
<br>

<el-row>
&nbsp;<el-tag @click="MYSQL5 = true">MYSQL5</el-tag>
&nbsp;<el-tag @click="POSTGRESQL = true">POSTGRESQL</el-tag>
</el-row>

<br>
<p class="panel-title"><b>是否默认查询</b></p>

* `否`

<p class="panel-title"><b>是否权限使用</b></p>

* `否`

<p class="panel-title"><b>是否自定义SQL</b></p>

* `否`

<p class="panel-title"><b>查询列级别</b></p>

* `默认（全部查询列）`

> [!ATTENTION|label:存在长文本属性]
>
> `CONTENT(块内容)`




### 查询连接
* **AI_KB_DOCUMENT相关N:1（INNER JOIN）DER1N_AI_KB_CHUNK_AI_KB_DOCUMENT_DOCUMENT_ID**<br>
连接关系：[DER1N_AI_KB_CHUNK_AI_KB_DOCUMENT_DOCUMENT_ID](der/DER1N_AI_KB_CHUNK_AI_KB_DOCUMENT_DOCUMENT_ID)<br>
连接实体：[知识库文档](module/ai/ai_kb_document)<br>
    * **AI_KNOWLEDGE_BASE相关N:1（INNER JOIN）DER1N_AI_KB_DOCUMENT_AI_KNOWLEDGE_BASE_KB_ID**<br>
连接关系：[DER1N_AI_KB_DOCUMENT_AI_KNOWLEDGE_BASE_KB_ID](der/DER1N_AI_KB_DOCUMENT_AI_KNOWLEDGE_BASE_KB_ID)<br>
连接实体：[知识库](module/ai/ai_knowledge_base)<br>
连接条件：((`VISIBILITY(可见范围)` EQ `'public'` OR (`SCOPE_TYPE(所属)` EQ `'organization'` AND `SCOPE_ID(所属对象)` EQ `用户上下文.srforgid`) OR `EXISTS(SELECT 1 FROM AI_KB_MEMBER m 
 WHERE 
 t21.ID = m.KB_ID  AND  ( m.USER_ID = #{ctx.sessioncontext.srfpersonid} ) )`))<br>




<el-dialog v-model="MYSQL5" title="MYSQL5">

```sql
SELECT
t1.`ACTIVE`,
t11.`CATEGORIES`,
t1.`CHUNK_TYPE`,
t1.`CONTENT`,
t1.`CONTENT_PREVIEW`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DOCUMENT_ID`,
t11.`NAME` AS `DOCUMENT_NAME`,
t11.`SEQUENCE` AS `DOCUMENT_SEQUENCE`,
t11.`TYPE` AS `DOCUMENT_TYPE`,
t11.`FILE` AS `DOC_FILE`,
t11.`NAME` AS `DOC_NAME`,
t1.`ID`,
t11.`KB_ID`,
t21.`NAME` AS `KB_NAME`,
t1.`KEYWORDS`,
t1.`KEY_QUESTIONS`,
t1.`META_DATA`,
t1.`NAME`,
t1.`PATH`,
t1.`PID`,
t1.`POSITIONS`,
t1.`SEQUENCE`,
t1.`SOURCE_COUNT`,
t1.`TAGS`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`
FROM `AI_KB_CHUNK` t1 
LEFT JOIN `AI_KB_DOCUMENT` t11 ON t1.`DOCUMENT_ID` = t11.`ID` 
LEFT JOIN `AI_KNOWLEDGE_BASE` t21 ON t11.`KB_ID` = t21.`ID` 

WHERE ( ( t21.`VISIBILITY` = 'public'  OR  ( t21.`SCOPE_TYPE` = 'organization'  AND  t21.`SCOPE_ID` = #{ctx.sessioncontext.srforgid} )  OR  EXISTS(SELECT 1 FROM AI_KB_MEMBER m 
 WHERE 
 t21.ID = m.KB_ID  AND  ( m.USER_ID = #{ctx.sessioncontext.srfpersonid} ) ) ) )
```

</el-dialog>

<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t1."active",
t11."categories",
t1."chunk_type",
t1."content",
t1."content_preview",
t1."create_man",
t1."create_time",
t1."document_id",
t11."name" AS "document_name",
t11."sequence" AS "document_sequence",
t11."type" AS "document_type",
t11."file" AS "doc_file",
t11."name" AS "doc_name",
t1."id",
t11."kb_id",
t21."name" AS "kb_name",
t1."keywords",
t1."key_questions",
t1."meta_data",
t1."name",
t1."path",
t1."pid",
t1."positions",
t1."sequence",
t1."source_count",
t1."tags",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "ai_kb_chunk" t1 
LEFT JOIN "ai_kb_document" t11 ON t1."document_id" = t11."id" 
LEFT JOIN "ai_knowledge_base" t21 ON t11."kb_id" = t21."id" 

WHERE ( ( t21."visibility" = 'public'  OR  ( t21."scope_type" = 'organization'  AND  t21."scope_id" = #{ctx.sessioncontext.srforgid} )  OR  EXISTS(SELECT 1 FROM AI_KB_MEMBER m 
 WHERE 
 t21.ID = m.KB_ID  AND  ( m.USER_ID = #{ctx.sessioncontext.srfpersonid} ) ) ) )
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