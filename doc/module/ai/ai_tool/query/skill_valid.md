## 启用的技能数据(skill_valid) <!-- {docsify-ignore-all} -->

插件使用

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
> `ACCESS_KEY(访问密钥)`
>
> `BEARER_TOKEN(Bearer令牌)`
>
> `CLIENT_SECRET(客户端密钥)`
>
> `INPUT_SCHEMA(输入参数 Schema)`
>
> `SECRET_KEY(安全密钥)`
>
> `SKILL_PROMPT(技能提示词)`



### 查询条件

(`TOOL_TYPE(工具类型)` EQ `'skill'`)





<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t1."access_key",
t1."active",
t1."api_auth_type",
t1."api_headers",
t1."api_key",
t1."api_method",
t1."api_url",
t1."bearer_token",
t1."client_id",
t1."client_secret",
t1."create_man",
t1."create_time",
t1."description",
t1."expiration_date",
t1."id",
t1."input_schema",
t1."name",
t1."secret_key",
t1."skill_prompt",
t1."skill_references",
t1."skill_scripts",
t1."timeout",
t1."token_url",
t1."tool_tag",
t1."tool_type",
t1."update_man",
t1."update_time"
FROM "ai_tool" t1 

WHERE ( t1."tool_type" = 'skill' )
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