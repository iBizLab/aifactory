## 只读用户(reader) <!-- {docsify-ignore-all} -->



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




### 查询连接
* **PORTFOLIO_MEMBER存在1:N（EXISTS (SELECT)）DER1N_PORTFOLIO_MEMBER_PORTFOLIO_PORTFOLIO_ID**<br>
连接关系：[DER1N_PORTFOLIO_MEMBER_PORTFOLIO_PORTFOLIO_ID](der/DER1N_PORTFOLIO_MEMBER_PORTFOLIO_PORTFOLIO_ID)<br>
连接实体：[文件夹](module/Base/portfolio)<br>
连接条件：(`USER_ID(登录名)` EQ `用户上下文.srfpersonid` AND `ROLE_ID(角色)` EQ `'reader'`)<br>




<el-dialog v-model="MYSQL5" title="MYSQL5">

```sql
SELECT
t1.`ASSIGNEE_ID`,
t1.`ASSIGNEE_NAME`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DESCRIPTION`,
t1.`END_AT`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`NAME`,
t1.`START_AT`,
t1.`STATE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `PORTFOLIO` t1 

WHERE EXISTS(SELECT * FROM `PORTFOLIO_MEMBER` t11 
 WHERE 
 t1.`ID` = t11.`PORTFOLIO_ID`  AND  ( t11.`USER_ID` = #{ctx.sessioncontext.srfpersonid}  AND  t11.`ROLE_ID` = 'reader' ) )
```

</el-dialog>

<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t1."assignee_id",
t1."assignee_name",
t1."create_man",
t1."create_time",
t1."description",
t1."end_at",
t1."id",
t1."identifier",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."name",
t1."start_at",
t1."state",
t1."update_man",
t1."update_time"
FROM "portfolio" t1 

WHERE EXISTS(SELECT * FROM "portfolio_member" t11 
 WHERE 
 t1."id" = t11."portfolio_id"  AND  ( t11."user_id" = #{ctx.sessioncontext.srfpersonid}  AND  t11."role_id" = 'reader' ) )
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