## 默认（全部数据）(View) <!-- {docsify-ignore-all} -->



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

* `全部数据`

> [!ATTENTION|label:存在长文本属性]
>
> `CONFIGS(configs)`






<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t1."auto_gen_kb",
t11."name" AS "chat_model",
t1."chat_model_id",
t1."chunk_method",
t1."configs",
t1."create_man",
t1."create_time",
t71."name" AS "embedding_model",
t1."embedding_model_id",
t1."enable",
t31."name" AS "flash_model",
t1."flash_model_id",
t1."guided_prompt_agent_id",
t1."id",
t51."name" AS "intent_model",
t1."intent_model_id",
t1."name",
t1."parser_config",
t1."rerank",
t21."name" AS "rerank_model",
t1."rerank_model_id",
t61."name" AS "resource",
t61."resource_code",
t1."resource_id",
t1."similarity_threshold",
t1."source_id",
t1."source_name",
t1."top_k",
t1."update_man",
t1."update_time",
t1."use_kg",
t1."vector_similarity_weight",
t1."visibility",
t41."name" AS "vl_model",
t1."vl_model_id"
FROM "category_settings" t1 
LEFT JOIN "ai_model" t11 ON t1."chat_model_id" = t11."id" 
LEFT JOIN "ai_model" t21 ON t1."rerank_model_id" = t21."id" 
LEFT JOIN "ai_model" t31 ON t1."flash_model_id" = t31."id" 
LEFT JOIN "ai_model" t41 ON t1."vl_model_id" = t41."id" 
LEFT JOIN "ai_model" t51 ON t1."intent_model_id" = t51."id" 
LEFT JOIN "data_resource" t61 ON t1."resource_id" = t61."id" 
LEFT JOIN "ai_model" t71 ON t1."embedding_model_id" = t71."id" 


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