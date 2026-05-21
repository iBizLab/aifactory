## 知识库目录(ai_kb_category) <!-- {docsify-ignore-all} -->



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

(`OWNER_TYPE(所属数据对象)` EQ `'ai_knowledge_base'` AND `OWNER_SUBTYPE(所属对象子类型)` EQ `'ai_knowledge_base'`)





<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."id",
t1."is_deleted",
t1."is_leaf",
t1."is_leaf2",
t1."is_leaf3",
case when t1."is_leaf"+t1."is_leaf2"=2 then 1 else 0 end AS "leaf_flag",
t1."name",
t1."owner_id",
t1."owner_subtype",
t1."owner_type",
t1."pid",
t1."section_id",
t11."name" AS "section_name",
t1."sequence",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2",
t1."wf_version_id"
FROM "category" t1 
LEFT JOIN "section" t11 ON t1."section_id" = t11."id" 

WHERE ( t1."owner_type" = 'ai_knowledge_base'  AND  t1."owner_subtype" = 'ai_knowledge_base' )
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