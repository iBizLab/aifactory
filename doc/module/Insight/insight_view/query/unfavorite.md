## 非星标(unfavorite) <!-- {docsify-ignore-all} -->



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

(`IS_ARCHIVED(是否已归档)` EQ `'0'` AND `IS_DELETED(是否已删除)` EQ `'0'` AND `IS_FAVORITE(是否星标)` EQ `'0'`)





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

WHERE ( t1."is_archived" = 0  AND  t1."is_deleted" = 0  AND  (select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) = '0' )
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