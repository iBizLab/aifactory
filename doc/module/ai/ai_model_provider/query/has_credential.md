## 存在凭证(has_credential) <!-- {docsify-ignore-all} -->



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

(`HAS_CREDENTIAL(是否存在凭证)` NOTEQ `'0'`)





<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
concat(t1."base_url",t1."default_version") AS "api_base_url",
t1."base_url",
t1."default_token",
t1."default_version",
(select count(1) from ai_credential  where id =t1."id") AS "has_credential",
t1."id",
t1."name",
t1."update_time"
FROM "ai_model_provider" t1 

WHERE ( (select count(1) from ai_credential  where id =t1."id") <> '0' )
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