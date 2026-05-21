## DEFAULT(Default) <!-- {docsify-ignore-all} -->



<p class="panel-title"><b>查看SQL语句</b></p>
<br>

<el-row>
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






<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t1."_create_time",
t1."_creator",
t1."_enabled",
t1."_id",
t1."_key",
t1."_ner_flag",
t1."_region",
t11."resource_code" AS "_resource_code",
t1."_resource_id",
t11."name" AS "_resource_name",
t1."_title",
t1."_updater",
t1."_update_time"
FROM "data_record" t1 
LEFT JOIN "data_resource" t11 ON t1."_resource_id" = t11."id" 

WHERE t1._enabled = 1
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