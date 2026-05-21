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




### 查询连接
* **AI_KNOWLEDGE_BASE相关N:1（INNER JOIN）DER1N_AI_REVIEW_REPORT_AI_KNOWLEDGE_BASE_KB_ID**<br>
连接关系：[DER1N_AI_REVIEW_REPORT_AI_KNOWLEDGE_BASE_KB_ID](der/DER1N_AI_REVIEW_REPORT_AI_KNOWLEDGE_BASE_KB_ID)<br>
连接实体：[知识库](module/ai/ai_knowledge_base)<br>
连接条件：((`VISIBILITY(可见范围)` EQ `'public'` OR (`SCOPE_ID(所属对象)` EQ `用户上下文.srforgid` AND `SCOPE_TYPE(所属)` EQ `'organization'`) OR `EXISTS(SELECT 1 FROM AI_KB_MEMBER m 
 WHERE 
 t11.ID = m.KB_ID  AND  ( m.USER_ID = #{ctx.sessioncontext.srfpersonid} ) )`))<br>




<el-dialog v-model="MYSQL5" title="MYSQL5">

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

</el-dialog>

<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t1."agent_tag",
t1."create_man",
t1."create_time",
t1."document_id",
t21."name" AS "document_name",
t1."id",
t1."kb_id",
t11."name" AS "kb_name",
t1."name",
t1."record_id",
t1."review_result",
t1."update_man",
t1."update_time"
FROM "ai_review_report" t1 
LEFT JOIN "ai_knowledge_base" t11 ON t1."kb_id" = t11."id" 
LEFT JOIN "ai_kb_document" t21 ON t1."document_id" = t21."id" 

WHERE ( ( t11."visibility" = 'public'  OR  ( t11."scope_id" = #{ctx.sessioncontext.srforgid}  AND  t11."scope_type" = 'organization' )  OR  EXISTS(SELECT 1 FROM AI_KB_MEMBER m 
 WHERE 
 t11.ID = m.KB_ID  AND  ( m.USER_ID = #{ctx.sessioncontext.srfpersonid} ) ) ) )
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