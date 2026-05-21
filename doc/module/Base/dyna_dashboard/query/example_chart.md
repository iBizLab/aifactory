## 示例图(example_chart) <!-- {docsify-ignore-all} -->



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
*  **属性组：**[示例图](#)
  * `IS_SYSTEM(是否系统类型)`
  * `EXAMPLE_CHART(示例图)`
  * `APPID(应用标识)`
  * `DYNADASHBOARDID(动态数据看板标识)`
  * `TYPE(看板类型)`
  * `MODELID(模型标识)`
  * `SEQUENCES(序号)`
  * `DYNADASHBOARDNAME(名称)`
  * `DESCRIPTION(描述)`

> [!ATTENTION|label:存在长文本属性]
>
> `EXAMPLE_CHART(示例图)`
>
> `DESCRIPTION(描述)`



### 查询条件

(`IS_SYSTEM(是否系统类型)` EQ `'1'`)





<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t1."appid",
t1."description",
t1."dynadashboardid",
t1."dynadashboardname",
t1."example_chart",
t1."is_system",
t1."modelid",
t1."sequences",
t1."type"
FROM "dynadashboard" t1 

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