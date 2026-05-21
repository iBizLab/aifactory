## 数据查询(Default) <!-- {docsify-ignore-all} -->



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

> [!ATTENTION|label:存在长文本属性]
>
> `CONTENT(内容)`






<el-dialog v-model="MYSQL5" title="MYSQL5">

```sql
SELECT
t1.`CONTENT`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`IS_TOP`,
t1.`NAME`,
t1.`OWNER_TYPE`,
t11.`CONTENT` AS `PCONTENT`,
t11.`CREATE_MAN` AS `PCREATE_MAN`,
t1.`PID`,
t1.`PRINCIPAL_ID`,
t1.`PRINCIPAL_NAME`,
t1.`PRINCIPAL_TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `COMMENT` t1 
LEFT JOIN `COMMENT` t11 ON t1.`PID` = t11.`ID` 


```

</el-dialog>

<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t1."content",
t1."create_man",
t1."create_time",
t1."id",
t1."is_top",
t1."name",
t1."owner_type",
t11."content" AS "pcontent",
t11."create_man" AS "pcreate_man",
t1."pid",
t1."principal_id",
t1."principal_name",
t1."principal_type",
t1."update_man",
t1."update_time"
FROM "comment" t1 
LEFT JOIN "comment" t11 ON t1."pid" = t11."id" 


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