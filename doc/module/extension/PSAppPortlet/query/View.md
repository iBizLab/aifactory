## 默认（全部数据）(View) <!-- {docsify-ignore-all} -->



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

* `全部数据`






<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t1."codename",
t1."dynamodelflag",
t1."memo",
t1."portlettype",
t1."psappportletid",
t1."psappportletname",
t1."psdechartid",
t1."psdechartname",
t1."psdedataviewid",
t1."psdedataviewname",
t1."psdeformid",
t1."psdeformname",
t1."psdeid",
t1."psdelistid",
t1."psdelistname",
t1."psdename",
t1."psdereportid",
t1."psdereportname",
t1."psdetoolbarid",
t1."psdetoolbarname",
t1."psdeuagroupid",
t1."psdeuagroupname",
t1."psdeviewid",
t1."psdeviewname",
t1."pssysappid",
t1."pssysappname",
t1."pssyscalendarid",
t1."pssyscalendarname",
t1."pssysmapviewid",
t1."pssysmapviewname",
t1."pssysportletcatid",
t1."pssysportletcatname",
t1."showtitlebar",
t1."validflag"
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