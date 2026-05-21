## DEFAULT(Default) <!-- {docsify-ignore-all} -->



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






<el-dialog v-model="MYSQL5" title="MYSQL5">

```sql
SELECT
t1.`CHUNK_OVERLAP`,
t1.`CHUNK_SIZE`,
t1.`ID`,
t1.`KEEP_SEPARATOR`,
t1.`MAX_CHUNK_COUNT_PER_DOC`,
t1.`NAME`,
t1.`PRE_PROCESS_RULES`,
t1.`SEPARATOR`
FROM `` t1 


```

</el-dialog>

<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t1."auto_keywords",
t1."auto_questions",
t1."chunk_overlap",
t1."chunk_overlap_num",
t1."chunk_size",
t1."chunk_token_num",
t1."delimiter",
t1."extraction_sub_prompt",
t1."html4excel",
t1."id",
t1."ignore_parsing_image",
t1."ignore_parsing_oss_link",
t1."keep_separator",
t1."layout_recognize",
t1."max_chunk_count_per_doc",
t1."name",
t1."pre_process_rules",
t1."separator",
t1."task_page_size"
FROM "" t1 


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