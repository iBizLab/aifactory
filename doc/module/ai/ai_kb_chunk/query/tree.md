## tree(tree) <!-- {docsify-ignore-all} -->



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

* `全部数据`

> [!ATTENTION|label:存在长文本属性]
>
> `CONTENT(块内容)`



### 查询条件

(`DOCUMENT_ID(知识库文档标识)` EQ `数据上下文.ai_kb_document`)





<el-dialog v-model="MYSQL5" title="MYSQL5">

```sql
SELECT
t11.`NAME` AS `DOCUMENT_NAME`,
t11.`TYPE` AS `DOCUMENT_TYPE`,
t1.`ID`,
t1.`NAME`,
t1.`PATH`,
t1.`PID`,
t1.`POSITIONS`,
t1.`SEQUENCE`,
t1.`SOURCE_COUNT`,
t1.`SOURCE_INDICES`,
t1.`TAGS`,
t1.`TYPE`
FROM `AI_KB_CHUNK` t1 
LEFT JOIN `AI_KB_DOCUMENT` t11 ON t1.`DOCUMENT_ID` = t11.`ID` 

WHERE ( <choose><when test="ctx.datacontext.ai_kb_document !=null ">  t1.`DOCUMENT_ID` = #{ctx.datacontext.ai_kb_document}  </when><otherwise>1=1</otherwise></choose> )
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
t11."parsed_content" AS "doc_parsed_content",
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
t1."source_indices",
t1."tags",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "ai_kb_chunk" t1 
LEFT JOIN "ai_kb_document" t11 ON t1."document_id" = t11."id" 
LEFT JOIN "ai_knowledge_base" t21 ON t11."kb_id" = t21."id" 

WHERE ( <choose><when test="ctx.datacontext.ai_kb_document !=null ">  t1."document_id" = #{ctx.datacontext.ai_kb_document}  </when><otherwise>1=1</otherwise></choose> )
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