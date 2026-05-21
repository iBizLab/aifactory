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
t1."avatarurl",
t1."category",
t1."createdate",
t1."createman",
t1."currentversion",
t1."fullname",
t1."fullpath",
t1."funcsn",
t1."funcstate",
t1."functag",
t1."functag2",
t1."functype",
t1."funcurl",
t1."httpurltorepo",
t1."memo",
t1."ordervalue",
t1."path",
t1."pscoreprdfuncid",
t1."pscoreprdfuncname",
t1."pscoreprdid",
t1."pscoreprdname",
t1."settings",
t1."settingurl",
t1."updatedate",
t1."updateman",
t1."vers"
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