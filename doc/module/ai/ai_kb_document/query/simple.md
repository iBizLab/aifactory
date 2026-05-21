## 简单查询(simple) <!-- {docsify-ignore-all} -->



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

* `指定属性组`
*  **属性组：**[基础数据](#)
  * `NAME(文档名称)`
  * `UPDATE_TIME(更新时间)`
  * `SYNC_ID(文档同步标识)`
  * `CHUNK_METHOD(切片方法)`
  * `TYPE(文档类型)`
  * `STATUS(状态)`
  * `CUSTOM_CHUNK(自定义切片)`
  * `PATH(路径)`
  * `SEQUENCE(序号)`






<el-dialog v-model="MYSQL5" title="MYSQL5">

```sql
SELECT
t1.`CHUNK_METHOD`,
t1.`CUSTOM_CHUNK`,
t1.`ID`,
t1.`NAME`,
concat_ws('/',nullif(btrim(t1.`CATEGORIES`, '/'),''),t1.`NAME`||'.'||COALESCE(t1.`FILE_TYPE`,'md')) AS `PATH`,
t1.`SEQUENCE`,
t1.`STATUS`,
t1.`SYNC_ID`,
t1.`TYPE`,
t1.`UPDATE_TIME`
FROM `AI_KB_DOCUMENT` t1 


```

</el-dialog>

<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t1."chunk_method",
t1."custom_chunk",
t1."id",
t1."name",
concat_ws('/',nullif(btrim(t1."categories", '/'),''),t1."name"||'.'||COALESCE(t1."file_type",'md')) AS "path",
t1."sequence",
t1."status",
t1."sync_id",
t1."type",
t1."update_time"
FROM "ai_kb_document" t1 


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