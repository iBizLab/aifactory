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
t1.`AVATAR`,
t1.`CREATE_MAN`,
t1.`CREATE_TIME`,
t1.`DEPARTMENT_ID`,
t1.`DISPLAY_NAME`,
t1.`EMAIL`,
t1.`EMPLOYEE_NUMBER`,
t1.`ID`,
t1.`JOB_ID`,
t1.`MOBILE`,
t1.`NAME`,
t1.`OPEN_USER_TAG`,
t1.`ORGANIZATION_ID`,
t1.`PASSWORD`,
t1.`STATUS`,
t1.`TITLE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`
FROM `` t1 


```

</el-dialog>

<el-dialog v-model="POSTGRESQL" title="POSTGRESQL">

```sql
SELECT
t1."avatar",
t1."create_man",
t1."create_time",
t1."department_id",
t1."display_name",
t1."email",
t1."employee_number",
t1."id",
t1."job_id",
t1."mobile",
t1."name",
t1."open_user_tag",
t1."organization_id",
t1."password",
t1."status",
t1."title",
t1."update_man",
t1."update_time"
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