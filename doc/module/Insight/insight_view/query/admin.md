## 管理员(admin) <!-- {docsify-ignore-all} -->



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




### 查询连接
* **INSIGHT_MEMBER存在1:N（EXISTS (SELECT)DER1N_INSIGHT_MEMBER_INSIGHT_VIEW_OWNER_ID**<br>
连接关系：[DER1N_INSIGHT_MEMBER_INSIGHT_VIEW_OWNER_ID](der/DER1N_INSIGHT_MEMBER_INSIGHT_VIEW_OWNER_ID)<br>
连接实体：[效能视图](module/Insight/insight_view)<br>
连接条件：(`USER_ID(用户标识)` EQ `用户上下文.srfpersonid` AND `ROLE_ID(角色)` EQ `'admin'` AND `OWNER_TYPE(所属数据对象)` EQ `'INSIGHT'`)<br>




<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."name",
t1."scope_id",
t1."scope_type",
t1."update_man",
t1."update_time",
t1."visibility"
FROM "insight_view" t1 

WHERE EXISTS(SELECT * FROM "member" t11 
 WHERE 
 t1."id" = t11."owner_id"  AND  ( t11."user_id" = #{ctx.sessioncontext.srfpersonid}  AND  t11."role_id" = 'admin'  AND  t11."owner_type" = 'INSIGHT' ) )
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