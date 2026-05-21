## 源节点相关连线(CurItemBySrcNode) <!-- {docsify-ignore-all} -->



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

(`SRCPSDELOGICNODEID(源节点)` EQ `数据上下文.PSDELOGICNODE`)





<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t1."dstpsdelogicnodeid",
t1."psdelogicid",
t1."psdelogiclinkid",
t1."psdelogiclinkname",
t1."srcpsdelogicnodeid"
FROM "" t1 

WHERE ( t1."srcpsdelogicnodeid" = #{ctx.datacontext.psdelogicnode} )
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