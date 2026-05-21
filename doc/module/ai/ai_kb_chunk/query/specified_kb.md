## 指定知识库(specified_kb) <!-- {docsify-ignore-all} -->



<p class="panel-title"><b>查看SQL语句</b></p>
<br>

<el-row>
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



### 查询条件

(`PID(父分块标识)` ISNULL)



### 查询连接
* **AI_KB_DOCUMENT相关N:1（INNER JOIN）DER1N_AI_KB_CHUNK_AI_KB_DOCUMENT_DOCUMENT_ID**<br>
连接关系：[DER1N_AI_KB_CHUNK_AI_KB_DOCUMENT_DOCUMENT_ID](der/DER1N_AI_KB_CHUNK_AI_KB_DOCUMENT_DOCUMENT_ID)<br>
连接实体：[知识库文档](module/ai/ai_kb_document)<br>
    * **AI_KNOWLEDGE_BASE相关N:1（INNER JOIN）DER1N_AI_KB_DOCUMENT_AI_KNOWLEDGE_BASE_KB_ID**<br>
连接关系：[DER1N_AI_KB_DOCUMENT_AI_KNOWLEDGE_BASE_KB_ID](der/DER1N_AI_KB_DOCUMENT_AI_KNOWLEDGE_BASE_KB_ID)<br>
连接实体：[知识库](module/ai/ai_knowledge_base)<br>
连接条件：(`ID(知识库标识)` EQ `数据上下文.kb_id`)<br>




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

WHERE ( t21."id" = #{ctx.datacontext.kb_id} ) AND ( t1."pid" IS NULL )
```

</el-dialog>

<script>
 const { createApp } = Vue
  createApp({
    data() {
      return {
                POSTGRESQL : false
        
      }
    },
    methods: {
    }
  }).use(ElementPlus).mount('#app')
</script>