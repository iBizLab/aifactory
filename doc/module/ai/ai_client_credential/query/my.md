## my(my) <!-- {docsify-ignore-all} -->



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

(`USER_ID(用户标识)` EQ `用户上下文.srfpersonid`)





<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t1."access_strategy",
t1."access_types",
t1."active",
t1."create_man",
t1."create_time",
t1."description",
t1."expiration_date",
t1."id",
t1."name",
t1."update_man",
t1."update_time",
t1."user_id"
FROM "ai_client_credential" t1 

WHERE ( t1."user_id" = #{ctx.sessioncontext.srfpersonid} )
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