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
t1.`ACTIVE`,
t1.`CONFIDENCE`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`ID`,
t1.`KB_ID`,
t1.`NAME`,
t1.`OBJECT_ID`,
t1.`PREDICATE`,
t1.`SUBJECT_ID`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `AI_KB_GRAPH_RELATION` t1 


```

</el-dialog>

<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t1."active",
t1."confidence",
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."kb_id",
t31."name" AS "kb_name",
t1."name",
t1."object_id",
t21."name" AS "object_name",
t1."predicate",
t1."subject_id",
t11."name" AS "subject_name",
t1."update_man",
t1."update_time"
FROM "ai_kb_graph_relation" t1 
LEFT JOIN "ai_kb_graph_entity" t11 ON t1."subject_id" = t11."id" 
LEFT JOIN "ai_kb_graph_entity" t21 ON t1."object_id" = t21."id" 
LEFT JOIN "ai_knowledge_base" t31 ON t1."kb_id" = t31."id" 


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