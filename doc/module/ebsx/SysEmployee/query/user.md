## 当前用户(user) <!-- {docsify-ignore-all} -->



<p class="panel-title"><b>查看SQL语句</b></p>
<br>

<el-row>
&nbsp;<el-tag @click="MYSQL5 = true">MYSQL5</el-tag>
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

(`USERID(用户标识)` EQ `用户上下文.srfpersonid`)





<el-dialog v-model="MYSQL5" title="MYSQL5">

```sql
SELECT
t1.`ADDR`,
t1.`AVATAR`,
t1.`BCODE`,
t1.`BIRTHDAY`,
t1.`CERTCODE`,
t1.`CREATEDATE`,
t1.`DDUNIONID`,
t1.`DDUSERID`,
t1.`DOMAINS`,
t1.`EMAIL`,
t1.`ENABLE`,
t1.`FONTSIZE`,
t1.`IPADDR`,
t1.`LANG`,
t1.`LOGINNAME`,
t1.`MDEPTID`,
t1.`MDEPTNAME`,
t1.`MEMO`,
t1.`MSGTYPE`,
t1.`NICKNAME`,
t1.`ORGID`,
t1.`ORGNAME`,
t1.`PASSWORD`,
t1.`PERSONNAME`,
t1.`PHONE`,
t1.`POSTID`,
t1.`POSTNAME`,
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
t1.`SEX`,
t1.`SHOWORDER`,
t1.`STATE`,
t1.`SUPERUSER`,
t1.`THEME`,
t1.`UAAUSERID`,
t1.`UPDATEDATE`,
t1.`USERCODE`,
t1.`USERICON`,
t1.`USERID`,
t1.`USERNAME`,
t1.`WXWORKUNIONID`,
t1.`WXWORKUSERID`
FROM `` t1 

WHERE ( t1.`USERID` = #{ctx.sessioncontext.srfpersonid} )
```

</el-dialog>

<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t1."addr",
t1."avatar",
t1."bcode",
t1."birthday",
t1."certcode",
t1."createdate",
t1."ddunionid",
t1."dduserid",
t1."domains",
t1."email",
t1."enable",
t1."fontsize",
t1."ipaddr",
t1."lang",
t1."loginname",
t1."mdeptid",
t1."mdeptname",
t1."memo",
t1."msgtype",
t1."nickname",
t1."orgid",
t1."orgname",
t1."password",
t1."personname",
t1."phone",
t1."postid",
t1."postname",
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
t1."sex",
t1."showorder",
t1."state",
t1."superuser",
t1."theme",
t1."uaauserid",
t1."updatedate",
t1."usercode",
t1."usericon",
t1."userid",
t1."username",
t1."wxworkunionid",
t1."wxworkuserid"
FROM "" t1 

WHERE ( t1."userid" = #{ctx.sessioncontext.srfpersonid} )
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