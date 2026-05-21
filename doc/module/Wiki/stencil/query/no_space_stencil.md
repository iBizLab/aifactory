## 非空间下模板(no_space_stencil) <!-- {docsify-ignore-all} -->



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

* `默认（全部查询列）`



### 查询条件

(`SPACE_ID(空间标识)` ISNULL)





<el-dialog v-model="MYSQL5" title="MYSQL5">

```sql
SELECT
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`FORMAT_TYPE`,
t1.`ID`,
t1.`IS_GLOBAL`,
t1.`NAME`,
t1.`SPACE_ID`,
t11.`NAME` AS `SPACE_NAME`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `STENCIL` t1 
LEFT JOIN `SPACE` t11 ON t1.`SPACE_ID` = t11.`ID` 

WHERE ( t1.`SPACE_ID` IS NULL )
```

</el-dialog>

<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t1."create_man",
t1."create_time",
t1."format_type",
t1."id",
t1."is_global",
t1."name",
t1."space_id",
t11."name" AS "space_name",
t1."update_man",
t1."update_time"
FROM "stencil" t1 
LEFT JOIN "space" t11 ON t1."space_id" = t11."id" 

WHERE ( t1."space_id" IS NULL )
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