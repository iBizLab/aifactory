## 数据查询(Default) <!-- {docsify-ignore-all} -->



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
t1.`BCODE`,
t1.`CREATEDATE`,
t1.`DDDEPTID`,
t1.`DEPTCODE`,
t1.`DEPTFULLNAME`,
t1.`DEPTID`,
t1.`DEPTLEADER`,
t1.`DEPTLEADERID`,
t1.`DEPTLEVEL`,
t1.`DEPTNAME`,
t1.`DOMAINS`,
t1.`ENABLE`,
t1.`ISVALID`,
t1.`LEADERID`,
t1.`LEADERNAME`,
t1.`ORGID`,
t1.`ORGNAME`,
t1.`PDEPTID`,
t1.`PDEPTNAME`,
t1.`RESERVER`,
t1.`RESERVER11`,
t1.`RESERVER12`,
t1.`RESERVER13`,
t1.`RESERVER14`,
t1.`RESERVER15`,
t1.`RESERVER16`,
t1.`RESERVER17`,
t1.`RESERVER18`,
t1.`RESERVER19`,
t1.`RESERVER2`,
t1.`RESERVER20`,
t1.`RESERVER3`,
t1.`RESERVER4`,
t1.`RESERVER5`,
t1.`RESERVER6`,
t1.`RESERVER7`,
t1.`RESERVER8`,
t1.`SHORTNAME`,
t1.`SHOWORDER`,
t1.`UPDATEDATE`,
t1.`WXWORKDEPTID`
FROM `` t1 


```

</el-dialog>

<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t1."bcode",
t1."createdate",
t1."dddeptid",
t1."deptcode",
t1."deptfullname",
t1."deptid",
t1."deptleader",
t1."deptleaderid",
t1."deptlevel",
t1."deptname",
t1."domains",
t1."enable",
t1."isvalid",
t1."leaderid",
t1."leadername",
t1."orgid",
t1."orgname",
t1."pdeptid",
t1."pdeptname",
t1."reserver",
t1."reserver11",
t1."reserver12",
t1."reserver13",
t1."reserver14",
t1."reserver15",
t1."reserver16",
t1."reserver17",
t1."reserver18",
t1."reserver19",
t1."reserver2",
t1."reserver20",
t1."reserver3",
t1."reserver4",
t1."reserver5",
t1."reserver6",
t1."reserver7",
t1."reserver8",
t1."shortname",
t1."showorder",
t1."updatedate",
t1."wxworkdeptid"
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