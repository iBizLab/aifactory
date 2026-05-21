## 默认（全部数据）(View) <!-- {docsify-ignore-all} -->



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
> `PAYLOAD(任务执行参数)`
>
> `RESULT(执行结果)`






<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t1."create_man",
t1."create_time",
t1."description",
t1."enable",
t11."executor_tag",
t1."finished_at",
t1."id",
t1."max_retry",
t1."name",
t1."payload",
t1."principal_id",
t1."principal_name",
t1."principal_type",
t1."result",
t1."result_message",
t1."retry_count",
t1."scheduled_at",
t1."schedule_id",
t1."started_at",
t1."status",
t1."task_type",
t11."name" AS "task_type_name",
t1."update_man",
t1."update_time"
FROM "extend_scheduled_task" t1 
LEFT JOIN "extend_task_type" t11 ON t1."task_type" = t11."id" 


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