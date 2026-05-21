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
t1."applyflag",
t1."attachtopsdeactionid",
t1."attachtopsdeactionname",
t1."attachtopsdedatasetid",
t1."attachtopsdedatasetname",
t1."codename",
t1."createdate",
t1."createman",
t1."dynamodelflag",
t1."eventmodel",
t1."events",
t1."extension_tag",
t1."extension_tag2",
t1."extension_tag3",
t1."extension_tag4",
t1."ignoreexception",
t1."logicsubtype",
t1."logictag",
t1."logictag2",
t1."logictag3",
t1."logictag4",
t1."logictype",
t1."memo",
t1."ordervalue",
t1."psdeid",
t1."psdelogicid",
t1."psdelogiclinks",
t1."psdelogicname",
t1."psdelogicnodes",
t1."psdelogicparams",
t1."psdename",
t1."threadmode",
t1."timerpolicy",
t1."updatedate",
t1."updateman",
t1."usertag",
t1."usertag2",
t1."usertag3",
t1."usertag4",
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