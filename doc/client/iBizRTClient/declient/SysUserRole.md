# 用户角色关系(SysUserRole) :id=SysUserRole
## SYS_USER_ROLE__DEACTION__SAVE

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/sysuserroles/{key}" type="info" :closable="false" ></el-alert>
</div>
</el-row>
用于映射ebsx接口save（携带key），标准模式接口不输出key，如：/entity/{key}/save

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|主键|







<script>
 const { createApp } = Vue
  createApp({
    data() {
      return {

      }
    },
    methods: {

    }
  }).use(ElementPlus).mount('#app')
</script>