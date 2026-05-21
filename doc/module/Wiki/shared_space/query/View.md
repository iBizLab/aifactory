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






<el-dialog v-model="MYSQL5" title="MYSQL5">

```sql
SELECT
t1.`ACCESS_PASSWORD`,
t1.`EXPIRATION_DATE`,
t1.`ID`,
t1.`IS_SHARED`,
t1.`NAME`,
t1.`SCOPE_TYPE`,
t1.`SHARED_BY`,
t1.`SHARED_PAGES`,
t1.`SHARED_TIME`,
t1.`SHOW_LOGO`,
t1.`SHOW_TITLE`
FROM `SPACE` t1 


```

</el-dialog>

<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t1."access_password",
t1."expiration_date",
t1."id",
t1."is_shared",
t1."name",
t1."scope_type",
t1."shared_by",
t1."shared_pages",
t1."shared_time",
t1."show_logo",
t1."show_title"
FROM "space" t1 


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