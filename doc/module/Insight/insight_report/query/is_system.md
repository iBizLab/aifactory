## 模板报表(is_system) <!-- {docsify-ignore-all} -->



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
> `DESCRIPTION(描述)`
>
> `TEMPLATE_MODEL(模板模型)`



### 查询条件

(`IS_SYSTEM(是否系统类型)` EQ `'1'`)





<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t1."app_tag",
t1."categories",
t1."category",
t1."chart_type",
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."is_system",
t1."name",
t1."template_model",
t1."update_man",
t1."update_time",
t1."view_id",
t11."name" AS "view_name"
FROM "insight_report" t1 
LEFT JOIN "insight_view" t11 ON t1."view_id" = t11."id" 

WHERE ( t1."is_system" = 1 )
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