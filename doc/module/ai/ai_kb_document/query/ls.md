## 数据查询(ls) <!-- {docsify-ignore-all} -->



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

* `指定属性组`
*  **属性组：**[ls](#)
  * `ID(知识库文档标识)`
  * `SIZE(内容大小)`
  * `PATH(路径)`






<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t1."id",
concat_ws('/',nullif(btrim(t1."categories", '/'),''),t1."name"||'.'||COALESCE(t1."file_type",'md')) AS "path",
t1."size"
FROM "ai_kb_document" t1 


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