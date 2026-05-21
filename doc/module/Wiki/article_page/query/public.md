## public(public) <!-- {docsify-ignore-all} -->



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
* **SPACE相关N:1（INNER JOIN）DER1N_PAGE_SPACE_SPACE_ID**<br>
连接关系：[DER1N_PAGE_SPACE_SPACE_ID](der/DER1N_PAGE_SPACE_SPACE_ID)<br>
连接实体：[空间](module/Wiki/space)<br>
连接条件：(`VISIBILITY(可见范围)` EQ `'public'`)<br>




<el-dialog v-model="MYSQL5" title="MYSQL5">

```sql
SELECT
t1.`CATEGORIES`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`CUR_VERSION_ID`,
t1.`CUR_VERSION_NAME`,
t1.`FORMAT_TYPE`,
t1.`ICON`,
t1.`ID`,
t1.`IDENTIFIER`,
t1.`IS_ARCHIVED`,
t1.`IS_DELETED`,
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1.`ID` ) AS `IS_FAVORITE`,
t1.`IS_LEAF`,
t1.`IS_LOCK`,
t1.`IS_PUBLISHED`,
t1.`IS_SHARED`,
t1.`IS_SHARED_SUBSET`,
t1.`NAME`,
t1.`PARENT_ID`,
t1.`PUBLISHED`,
t1.`PUBLISH_MAN`,
t1.`PUBLISH_NAME`,
t1.`PUBLISH_TIME`,
DATEDIFF(CURDATE(), t1.`CREATE_TIME`) AS `RECENT_CREATE_DAYS`,
t1.`REVIEW_RESULT_STATE`,
t1.`SEQUENCE`,
concat(t11.`IDENTIFIER`,'-',t1.`IDENTIFIER`) AS `SHOW_IDENTIFIER`,
t1.`SPACE_ID`,
t11.`IDENTIFIER` AS `SPACE_IDENTIFIER`,
t11.`NAME` AS `SPACE_NAME`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USER_TAG`,
t1.`USER_TAG2`
FROM `PAGE` t1 
LEFT JOIN `SPACE` t11 ON t1.`SPACE_ID` = t11.`ID` 

WHERE ( t11.`VISIBILITY` = 'public' )
```

</el-dialog>

<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."cur_version_id",
t1."cur_version_name",
t1."format_type",
t1."icon",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_leaf",
t1."is_lock",
t1."is_published",
t1."is_shared",
t1."is_shared_subset",
t1."name",
t1."parent_id",
t1."published",
t1."publish_man",
t1."publish_name",
t1."publish_time",
CURRENT_DATE - t1."create_time"::date AS "recent_create_days",
t1."review_result_state",
t1."sequence",
concat(t11."identifier",'-',t1."identifier") AS "show_identifier",
t1."space_id",
t11."identifier" AS "space_identifier",
t11."name" AS "space_name",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "page" t1 
LEFT JOIN "space" t11 ON t1."space_id" = t11."id" 

WHERE ( t11."visibility" = 'public' )
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