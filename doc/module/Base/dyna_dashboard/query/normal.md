## 正常数据(normal) <!-- {docsify-ignore-all} -->



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

> [!ATTENTION|label:存在长文本属性]
>
> `EXAMPLE_CHART(示例图)`






<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t1."appid",
t1."createdate",
t1."createman",
t1."dynadashboardid",
t1."dynadashboardname",
t1."example_chart",
t1."is_system",
t1."modelid",
t1."owner_id",
t1."owner_type",
t1."sequences",
t1."type",
t1."update_man",
t1."update_time",
t1."userid"
FROM "dynadashboard" t1 


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