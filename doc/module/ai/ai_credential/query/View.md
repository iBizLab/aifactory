## 默认（全部数据）(View) <!-- {docsify-ignore-all} -->



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
> `ACCESS_KEY(Access Key)`
>
> `BEARER_TOKEN(Bearer令牌)`
>
> `CLIENT_SECRET(客户端密钥)`
>
> `SECRET_KEY(安全密钥)`






<el-dialog v-model="MYSQL5" title="MYSQL5">

```sql
SELECT
t1.`ACCESS_KEY`,
t1.`ACTIVE`,
t1.`API_KEY`,
t1.`BEARER_TOKEN`,
t1.`CLIENT_ID`,
t1.`CLIENT_SECRET`,
t1.`CODE_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`CREDENTIAL_TYPE`,
t1.`DESCRIPTION`,
t1.`ID`,
t1.`NAME`,
t1.`PROVIDER`,
t1.`REGION`,
t1.`SCOPE`,
t1.`SECRET_KEY`,
t1.`TOKEN_URL`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_CREDENTIAL` t1 


```

</el-dialog>

<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t1."access_key",
t1."active",
t1."api_key",
t1."bearer_token",
t1."client_id",
t1."client_secret",
t1."code_name",
t1."create_man",
t1."create_time",
t1."credential_type",
t1."description",
t1."id",
t1."name",
t1."provider",
t1."region",
t1."scope",
t1."secret_key",
t1."token_url",
t1."update_man",
t1."update_time"
FROM "ai_credential" t1 


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