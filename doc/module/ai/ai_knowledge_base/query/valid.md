## 启用知识库(valid) <!-- {docsify-ignore-all} -->



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
> `META_DATA(文档元数据)`






<el-dialog v-model="MYSQL5" title="MYSQL5">

```sql
SELECT
t1.`CHUNK_METHOD`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`EMBEDDING_MODEL`,
t1.`ID`,
t1.`META_DATA`,
t1.`NAME`,
t1.`PARSER_CONFIG`,
t1.`SOURCE_ID`,
t1.`SOURCE_NAME`,
t1.`TAG_SETS`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`VISIBILITY`
FROM `AI_KNOWLEDGE_BASE` t1 


```

</el-dialog>

<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t1."category_id",
t1."category_name",
t1."chat_model",
t1."chat_model_id",
t1."chunk_method",
t1."code_name",
t1."create_man",
t1."create_time",
t1."description",
t1."embedding_model",
t1."embedding_model_id",
t1."guidance_prompt",
t1."id",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."key",
t1."meta_data",
t1."name",
t1."pageindex",
t1."parser_config",
t1."record_id",
t11."_title" AS "record_title",
t1."rerank",
t1."rerank_model",
t1."rerank_model_id",
t1."resource",
t1."resource_code",
t1."resource_id",
t1."scope_id",
t1."scope_type",
t1."similarity_threshold",
t1."source_id",
t1."source_name",
t1."source_type",
t1."status",
t1."tag_sets",
t1."top_k",
t1."update_man",
t1."update_time",
t1."use_kg",
t1."vector_similarity_weight",
t1."visibility"
FROM "ai_knowledge_base" t1 
LEFT JOIN "data_record" t11 ON t1."record_id" = t11."_id" 


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