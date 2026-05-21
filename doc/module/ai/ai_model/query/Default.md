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
t1.`AI_CREDENTIAL_ID`,
t11.`NAME` AS `AI_CREDENTIAL_NAME`,
t1.`API_BASE_URL`,
t1.`CODE_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESC_OSS_IMAGE`,
t1.`ID`,
t1.`MAX_CONTEXT_TOKENS`,
t1.`MAX_OUTPUT_TOKENS`,
t1.`MODEL_CAPABILITY`,
t1.`MODEL_CATEGORY`,
t1.`NAME`,
t1.`PROVIDER`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_MODEL` t1 
LEFT JOIN `AI_CREDENTIAL` t11 ON t1.`AI_CREDENTIAL_ID` = t11.`ID` 


```

</el-dialog>

<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t1."active",
t1."ai_credential_id",
t21."name" AS "ai_credential_name",
t1."api_base_url",
t1."code_name",
t1."create_man",
t1."create_time",
t1."desc_oss_image",
t1."id",
t1."max_context_tokens",
t1."max_output_tokens",
t1."model_capability",
t1."model_category",
t1."name",
t1."provider",
t11."name" AS "provider_name",
t1."update_man",
t1."update_time"
FROM "ai_model" t1 
LEFT JOIN "ai_model_provider" t11 ON t1."provider" = t11."id" 
LEFT JOIN "ai_credential" t21 ON t1."ai_credential_id" = t21."id" 


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