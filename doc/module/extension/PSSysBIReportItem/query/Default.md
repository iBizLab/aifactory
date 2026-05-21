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
t1."aggtype",
t1."birepitemtag",
t1."birepitemtag2",
t1."birepitemtype",
t1."placement",
t1."placetype",
t1."pssysbicubedimensionid",
t1."pssysbicubedimensionname",
t1."pssysbicubeid",
t1."pssysbicubemeasureid",
t1."pssysbicubemeasurename",
t1."pssysbicubename",
t1."pssysbireportid",
t1."pssysbireportitemid",
t1."pssysbireportitemname",
t1."reftype",
t1."stddatatype",
t1."validflag",
t1."valueformat"
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