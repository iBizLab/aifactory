## 数据查询(Default) <!-- {docsify-ignore-all} -->



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
t1."aiagenttag",
t1."codename",
t1."content",
t1."dstpsdlparamid",
t1."dstpsdlparamname",
t1."ispsdlparamid",
t1."ispsdlparamname",
t1."logicnodesubtype",
t1."logicnodetype",
t1."ordervalue",
t1."ospsdlparamid",
t1."ospsdlparamname",
t1."paralleloutput",
t1."param1",
t1."param10",
t1."param11",
t1."param12",
t1."param13",
t1."param7",
t1."param8",
t1."param9",
t1."psdelogicid",
t1."psdelogicnodeid",
t1."psdelogicnodename",
t1."pssysaichatagentid",
t1."pssysaifactoryid",
t1."pssysmsgtemplid",
t1."retpsdlparamid",
t1."retpsdlparamname",
t1."srcpsdlparamid",
t1."srcpsdlparamname",
t1."title",
t1."work_item_type_id",
t1."work_item_type_name"
FROM "" t1 


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