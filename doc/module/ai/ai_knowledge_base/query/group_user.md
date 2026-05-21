## 组管理员(group_user) <!-- {docsify-ignore-all} -->



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



### 查询条件

(`SCOPE_TYPE(所属)` EQ `'user_group'` AND `SCOPE_ID(所属对象)` IN `用户上下文.srfgroup_user`)





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
t1."name",
t1."pageindex",
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

WHERE ( t1."scope_type" = 'user_group'  AND  t1."scope_id" IN (#{ctx.sessioncontext.srfgroup_user}) )
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