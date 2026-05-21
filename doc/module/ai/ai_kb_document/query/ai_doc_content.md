## AI文档内容(ai_doc_content) <!-- {docsify-ignore-all} -->



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
*  **属性组：**[AI文档内容属性组](#)
  * `INTELLIGENT_ANALYSIS(智能分析)`
  * `ID(知识库文档标识)`
  * `NAME(文档名称)`
  * `PARSED_CONTENT(解析内容)`
  * `KEYWORDS(关键字)`
  * `CONTENT(内容)`

> [!ATTENTION|label:存在长文本属性]
>
> `PARSED_CONTENT(解析内容)`
>
> `CONTENT(内容)`






<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t1."content",
t1."id",
t1."name",
t1."parsed_content"
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