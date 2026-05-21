## search(search) <!-- {docsify-ignore-all} -->



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

* `是`

<p class="panel-title"><b>查询列级别</b></p>

* `默认（全部查询列）`



### 查询条件

(`#{ctx.datacontext.keyword} is not null`)





<el-dialog v-model="MYSQL5" title="MYSQL5">

```sql
SELECT
t1.`CATEGORY_ID`,
t1.`CATEGORY_NAME`,
t1.`CHAT_MODEL`,
t1.`CHAT_MODEL_ID`,
t1.`CHUNK_METHOD`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`EMBEDDING_MODEL`,
t1.`EMBEDDING_MODEL_ID`,
t1.`GUIDANCE_PROMPT`,
t1.`ID`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`KEY`,
t1.`NAME`,
t1.`PAGEINDEX`,
t1.`RECORD_ID`,
t11.`_TITLE` AS `RECORD_TITLE`,
t1.`RERANK`,
t1.`RERANK_MODEL`,
t1.`RERANK_MODEL_ID`,
t1.`RESOURCE`,
t1.`RESOURCE_CODE`,
t1.`RESOURCE_ID`,
t1.`SCOPE_ID`,
t1.`SCOPE_TYPE`,
t1.`SIMILARITY_THRESHOLD`,
t1.`SOURCE_ID`,
t1.`SOURCE_NAME`,
t1.`SOURCE_TYPE`,
t1.`STATUS`,
t1.`TAG_SETS`,
t1.`TOP_K`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USE_KG`,
t1.`VECTOR_SIMILARITY_WEIGHT`,
t1.`VISIBILITY`
FROM `AI_KNOWLEDGE_BASE` t1 
LEFT JOIN `data_record` t11 ON t1.`RECORD_ID` = t11.`_ID` 

WHERE ( #{ctx.datacontext.keyword} is not null )
```

</el-dialog>

<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
    t1."category_id",
    t1."category_name",
    t1."create_man",
    t1."create_time",
    t1."description",
    t1."guidance_prompt",
    t1."id",
    t1."is_archived",
    t1."is_deleted",
    t1."key",
    t1."name",
    t1."record_id",
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
    t1."update_man",
    t1."update_time",
    t1."vector_similarity_weight",
    t1."visibility", t1."matched_documents" from (
        WITH input_kw AS (SELECT val,(val !~ '^[0-9A-Za-z\[\]]+$') AS is_fts FROM regexp_split_to_table(#{ctx.datacontext.keyword},'[, ]+') AS val WHERE val <> '')
   , raw_kw AS (SELECT val, val as kw, is_fts FROM input_kw  union SELECT DISTINCT lexeme AS val, val as kw, is_fts FROM input_kw i,  unnest(tsvector_to_array(to_tsvector('chinese_zh', i.val))) AS lexeme
                WHERE length(lexeme) >= 2 and is_fts)
   , raw_cnt AS (SELECT count(1) as cnt, count(DISTINCT kw) as kw from raw_kw)
   , doc_match AS (
   SELECT t.document_id, round(1.0 * COUNT(DISTINCT k.kw) / raw_cnt.kw, 2) + round(0.01 * COUNT(DISTINCT k.val) / raw_cnt.cnt, 4) - 0.01 as logic_rank,
                 max(case when k.is_fts then similarity(content, k.kw) else 0.99 end) as density_rank FROM ai_kb_chunk t JOIN raw_kw k ON t.content LIKE '%' || k.val || '%' , raw_cnt
                GROUP BY t.document_id, raw_cnt.kw, raw_cnt.cnt)
   , doc_agg AS (SELECT d.kb_id,  MAX(m.logic_rank) AS similarity_threshold, MAX(m.density_rank) AS vector_similarity_weight, 
   jsonb_path_query_array(
                                jsonb_agg(DISTINCT jsonb_build_object('id', d.id, 'name', d.name)),
                                '$[0 to 4]'
                        )::text AS matched_documents
                 FROM ai_kb_document d   JOIN doc_match m ON d.id = m.document_id  GROUP BY d.kb_id)
SELECT t1.id,t1.name,t1.update_time,t1.update_man,t1.create_time,t1.create_man,t1.description,t1.guidance_prompt,t1.category_id,t1.category_name,t1.resource_id,t1.resource_code,t1.resource,t1.record_id,
       t1.scope_id,t1.scope_type,t1.visibility,t1.status,t1.is_archived,t1.is_deleted,t1.key,t1.source_name,t1.source_id,t1.source_type,m.similarity_threshold,m.vector_similarity_weight,m.matched_documents
FROM ai_knowledge_base t1
         JOIN doc_agg m ON t1.id = m.kb_id
         order by m.similarity_threshold desc,m.vector_similarity_weight desc,t1.update_time desc
)  t1
WHERE ( #{ctx.datacontext.keyword} is not null )
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