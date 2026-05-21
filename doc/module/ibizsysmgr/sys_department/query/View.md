## 默认（全部数据）(View) <!-- {docsify-ignore-all} -->



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

* `全部数据`






<el-dialog v-model="MYSQL5" title="MYSQL5">

```sql
SELECT
t1.`BUSINESS_CATEGORY`,
t1.`CREATE_TIME`,
t1.`CREATOR`,
t1.`DC`,
t1.`DEPARTMENT_NAME`,
t1.`DEPARTMENT_NUMBER`,
t1.`DESCRIPTION`,
concat_ws(',',t1.`DEPARTMENT_NAME`,t1.`PARENT_NAME`,t1.`ORGANIZATION_NAME`) AS `DN`,
t1.`ENABLED`,
t1.`ID`,
t1.`IS_LEAF`,
t1.`ORGANIZATION_ID`,
t1.`ORGANIZATION_NAME`,
t1.`ORGANIZATION_NUMBER`,
t1.`PARENT_ID`,
t1.`PARENT_NAME`,
case when t1.`PARENT_ID` is null or t1.`PARENT_ID`='' then t1.`ORGANIZATION_ID` else t1.`PARENT_ID` end AS `PARENT_UNIT_ID`,
case when t1.`PARENT_NAME` is null or t1.`PARENT_NAME`='' then t1.`ORGANIZATION_NAME` else t1.`PARENT_NAME` end AS `PARENT_UNIT_NAME`,
t1.`SHORT_NAME`,
t1.`SORT`,
t1.`UPDATER`,
t1.`UPDATE_TIME`
FROM `` t1 

WHERE t1.ENABLED = 1
```

</el-dialog>

<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t1."business_category",
t1."create_time",
t1."creator",
t1."dc",
t1."department_name",
t1."department_number",
t1."description",
concat_ws(',',t1."department_name",t1."parent_name",t1."organization_name") AS "dn",
t1."enabled",
t1."id",
t1."is_leaf",
t1."organization_id",
t1."organization_name",
t1."organization_number",
t1."parent_id",
t1."parent_name",
case when t1."parent_id" is null or t1."parent_id"='' then t1."organization_id" else t1."parent_id" end AS "parent_unit_id",
case when t1."parent_name" is null or t1."parent_name"='' then t1."organization_name" else t1."parent_name" end AS "parent_unit_name",
t1."short_name",
t1."sort",
t1."updater",
t1."update_time"
FROM "" t1 

WHERE t1.enabled = 1
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