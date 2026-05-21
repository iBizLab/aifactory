# 部门(sys_department) :id=sys_department
## 创建部门

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/sys_departments" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`CREATE`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|标识|
|<el-row justify="space-between"><el-col :span="20">department_name</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|部门名称|
|<el-row justify="space-between"><el-col :span="20">dc</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|DC|
|<el-row justify="space-between"><el-col :span="20">department_number</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|部门编号|
|<el-row justify="space-between"><el-col :span="20">description</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|备注|
|<el-row justify="space-between"><el-col :span="20">is_leaf</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否叶子节点|
|<el-row justify="space-between"><el-col :span="20">short_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|简称|
|<el-row justify="space-between"><el-col :span="20">sort</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigInteger|排序|
|<el-row justify="space-between"><el-col :span="20">business_category</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务类别|
|<el-row justify="space-between"><el-col :span="20">parent_unit_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上级标识|
|<el-row justify="space-between"><el-col :span="20">parent_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上级部门标识|
|<el-row justify="space-between"><el-col :span="20">parent_unit_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上级名称|
|<el-row justify="space-between"><el-col :span="20">dn</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|DN|
|<el-row justify="space-between"><el-col :span="20">parent_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上级部门名称|
|<el-row justify="space-between"><el-col :span="20">organization_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|组织机构标识|
|<el-row justify="space-between"><el-col :span="20">organization_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|组织机构名称|
|<el-row justify="space-between"><el-col :span="20">organization_number</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|机构编号|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "department_name" : null,
  "creator" : null,
  "create_time" : null,
  "updater" : null,
  "update_time" : null,
  "dc" : null,
  "department_number" : null,
  "description" : null,
  "is_leaf" : null,
  "short_name" : null,
  "sort" : null,
  "business_category" : null,
  "parent_unit_id" : null,
  "parent_id" : null,
  "parent_unit_name" : null,
  "dn" : null,
  "parent_name" : null,
  "organization_id" : null,
  "organization_name" : null,
  "organization_number" : null,
}
```


##### 响应示例： {docsify-ignore}
```json

{
  "id" : null,
  "department_name" : null,
  "creator" : null,
  "create_time" : null,
  "updater" : null,
  "update_time" : null,
  "dc" : null,
  "department_number" : null,
  "description" : null,
  "is_leaf" : null,
  "short_name" : null,
  "sort" : null,
  "business_category" : null,
  "parent_unit_id" : null,
  "parent_id" : null,
  "parent_unit_name" : null,
  "dn" : null,
  "parent_name" : null,
  "organization_id" : null,
  "organization_name" : null,
  "organization_number" : null,
}

```

## 获取部门

<el-row>
<div style="width: 80px">
<el-alert center title="GET" type="success" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/sys_departments/{key}" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|标识|




##### 响应示例： {docsify-ignore}
```json

{
  "id" : null,
  "department_name" : null,
  "creator" : null,
  "create_time" : null,
  "updater" : null,
  "update_time" : null,
  "dc" : null,
  "department_number" : null,
  "description" : null,
  "is_leaf" : null,
  "short_name" : null,
  "sort" : null,
  "business_category" : null,
  "parent_unit_id" : null,
  "parent_id" : null,
  "parent_unit_name" : null,
  "dn" : null,
  "parent_name" : null,
  "organization_id" : null,
  "organization_name" : null,
  "organization_number" : null,
}

```

## 删除部门

<el-row>
<div style="width: 80px">
<el-alert center title="DELETE" type="error" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/sys_departments/{key}" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`DELETE`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|标识|





## 更新部门

<el-row>
<div style="width: 80px">
<el-alert center title="PUT" type="warning" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/sys_departments/{key}" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`UPDATE`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|标识|



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|标识|
|<el-row justify="space-between"><el-col :span="20">department_name</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|部门名称|
|<el-row justify="space-between"><el-col :span="20">dc</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|DC|
|<el-row justify="space-between"><el-col :span="20">department_number</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|部门编号|
|<el-row justify="space-between"><el-col :span="20">description</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|备注|
|<el-row justify="space-between"><el-col :span="20">is_leaf</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否叶子节点|
|<el-row justify="space-between"><el-col :span="20">short_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|简称|
|<el-row justify="space-between"><el-col :span="20">sort</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigInteger|排序|
|<el-row justify="space-between"><el-col :span="20">business_category</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务类别|
|<el-row justify="space-between"><el-col :span="20">parent_unit_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上级标识|
|<el-row justify="space-between"><el-col :span="20">parent_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上级部门标识|
|<el-row justify="space-between"><el-col :span="20">parent_unit_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上级名称|
|<el-row justify="space-between"><el-col :span="20">dn</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|DN|
|<el-row justify="space-between"><el-col :span="20">parent_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上级部门名称|
|<el-row justify="space-between"><el-col :span="20">organization_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|组织机构标识|
|<el-row justify="space-between"><el-col :span="20">organization_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|组织机构名称|
|<el-row justify="space-between"><el-col :span="20">organization_number</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|机构编号|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "department_name" : null,
  "creator" : null,
  "create_time" : null,
  "updater" : null,
  "update_time" : null,
  "dc" : null,
  "department_number" : null,
  "description" : null,
  "is_leaf" : null,
  "short_name" : null,
  "sort" : null,
  "business_category" : null,
  "parent_unit_id" : null,
  "parent_id" : null,
  "parent_unit_name" : null,
  "dn" : null,
  "parent_name" : null,
  "organization_id" : null,
  "organization_name" : null,
  "organization_number" : null,
}
```


##### 响应示例： {docsify-ignore}
```json

{
  "id" : null,
  "department_name" : null,
  "creator" : null,
  "create_time" : null,
  "updater" : null,
  "update_time" : null,
  "dc" : null,
  "department_number" : null,
  "description" : null,
  "is_leaf" : null,
  "short_name" : null,
  "sort" : null,
  "business_category" : null,
  "parent_unit_id" : null,
  "parent_id" : null,
  "parent_unit_name" : null,
  "dn" : null,
  "parent_name" : null,
  "organization_id" : null,
  "organization_name" : null,
  "organization_number" : null,
}

```

## 检查部门主键

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/sys_departments/checkkey" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`CREATE`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|标识|
|<el-row justify="space-between"><el-col :span="20">department_name</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|部门名称|
|<el-row justify="space-between"><el-col :span="20">dc</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|DC|
|<el-row justify="space-between"><el-col :span="20">department_number</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|部门编号|
|<el-row justify="space-between"><el-col :span="20">description</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|备注|
|<el-row justify="space-between"><el-col :span="20">is_leaf</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否叶子节点|
|<el-row justify="space-between"><el-col :span="20">short_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|简称|
|<el-row justify="space-between"><el-col :span="20">sort</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigInteger|排序|
|<el-row justify="space-between"><el-col :span="20">business_category</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务类别|
|<el-row justify="space-between"><el-col :span="20">parent_unit_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上级标识|
|<el-row justify="space-between"><el-col :span="20">parent_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上级部门标识|
|<el-row justify="space-between"><el-col :span="20">parent_unit_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上级名称|
|<el-row justify="space-between"><el-col :span="20">dn</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|DN|
|<el-row justify="space-between"><el-col :span="20">parent_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上级部门名称|
|<el-row justify="space-between"><el-col :span="20">organization_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|组织机构标识|
|<el-row justify="space-between"><el-col :span="20">organization_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|组织机构名称|
|<el-row justify="space-between"><el-col :span="20">organization_number</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|机构编号|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "department_name" : null,
  "creator" : null,
  "create_time" : null,
  "updater" : null,
  "update_time" : null,
  "dc" : null,
  "department_number" : null,
  "description" : null,
  "is_leaf" : null,
  "short_name" : null,
  "sort" : null,
  "business_category" : null,
  "parent_unit_id" : null,
  "parent_id" : null,
  "parent_unit_name" : null,
  "dn" : null,
  "parent_name" : null,
  "organization_id" : null,
  "organization_name" : null,
  "organization_number" : null,
}
```


##### 响应示例： {docsify-ignore}
```json
Integer
```

## 获取部门草稿

<el-row>
<div style="width: 80px">
<el-alert center title="GET" type="success" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/sys_departments/getdraft" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`CREATE`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|标识|
|<el-row justify="space-between"><el-col :span="20">department_name</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|部门名称|
|<el-row justify="space-between"><el-col :span="20">dc</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|DC|
|<el-row justify="space-between"><el-col :span="20">department_number</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|部门编号|
|<el-row justify="space-between"><el-col :span="20">description</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|备注|
|<el-row justify="space-between"><el-col :span="20">is_leaf</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否叶子节点|
|<el-row justify="space-between"><el-col :span="20">short_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|简称|
|<el-row justify="space-between"><el-col :span="20">sort</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigInteger|排序|
|<el-row justify="space-between"><el-col :span="20">business_category</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务类别|
|<el-row justify="space-between"><el-col :span="20">parent_unit_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上级标识|
|<el-row justify="space-between"><el-col :span="20">parent_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上级部门标识|
|<el-row justify="space-between"><el-col :span="20">parent_unit_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上级名称|
|<el-row justify="space-between"><el-col :span="20">dn</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|DN|
|<el-row justify="space-between"><el-col :span="20">parent_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上级部门名称|
|<el-row justify="space-between"><el-col :span="20">organization_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|组织机构标识|
|<el-row justify="space-between"><el-col :span="20">organization_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|组织机构名称|
|<el-row justify="space-between"><el-col :span="20">organization_number</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|机构编号|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "department_name" : null,
  "creator" : null,
  "create_time" : null,
  "updater" : null,
  "update_time" : null,
  "dc" : null,
  "department_number" : null,
  "description" : null,
  "is_leaf" : null,
  "short_name" : null,
  "sort" : null,
  "business_category" : null,
  "parent_unit_id" : null,
  "parent_id" : null,
  "parent_unit_name" : null,
  "dn" : null,
  "parent_name" : null,
  "organization_id" : null,
  "organization_name" : null,
  "organization_number" : null,
}
```


##### 响应示例： {docsify-ignore}
```json

{
  "id" : null,
  "department_name" : null,
  "creator" : null,
  "create_time" : null,
  "updater" : null,
  "update_time" : null,
  "dc" : null,
  "department_number" : null,
  "description" : null,
  "is_leaf" : null,
  "short_name" : null,
  "sort" : null,
  "business_category" : null,
  "parent_unit_id" : null,
  "parent_id" : null,
  "parent_unit_name" : null,
  "dn" : null,
  "parent_name" : null,
  "organization_id" : null,
  "organization_name" : null,
  "organization_number" : null,
}

```

## 保存部门

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/sys_departments/save" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`CREATE`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|标识|
|<el-row justify="space-between"><el-col :span="20">department_name</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|部门名称|
|<el-row justify="space-between"><el-col :span="20">dc</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|DC|
|<el-row justify="space-between"><el-col :span="20">department_number</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|部门编号|
|<el-row justify="space-between"><el-col :span="20">description</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|备注|
|<el-row justify="space-between"><el-col :span="20">is_leaf</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否叶子节点|
|<el-row justify="space-between"><el-col :span="20">short_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|简称|
|<el-row justify="space-between"><el-col :span="20">sort</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigInteger|排序|
|<el-row justify="space-between"><el-col :span="20">business_category</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务类别|
|<el-row justify="space-between"><el-col :span="20">parent_unit_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上级标识|
|<el-row justify="space-between"><el-col :span="20">parent_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上级部门标识|
|<el-row justify="space-between"><el-col :span="20">parent_unit_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上级名称|
|<el-row justify="space-between"><el-col :span="20">dn</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|DN|
|<el-row justify="space-between"><el-col :span="20">parent_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上级部门名称|
|<el-row justify="space-between"><el-col :span="20">organization_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|组织机构标识|
|<el-row justify="space-between"><el-col :span="20">organization_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|组织机构名称|
|<el-row justify="space-between"><el-col :span="20">organization_number</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|机构编号|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "department_name" : null,
  "creator" : null,
  "create_time" : null,
  "updater" : null,
  "update_time" : null,
  "dc" : null,
  "department_number" : null,
  "description" : null,
  "is_leaf" : null,
  "short_name" : null,
  "sort" : null,
  "business_category" : null,
  "parent_unit_id" : null,
  "parent_id" : null,
  "parent_unit_name" : null,
  "dn" : null,
  "parent_name" : null,
  "organization_id" : null,
  "organization_name" : null,
  "organization_number" : null,
}
```


##### 响应示例： {docsify-ignore}
```json

{
  "id" : null,
  "department_name" : null,
  "creator" : null,
  "create_time" : null,
  "updater" : null,
  "update_time" : null,
  "dc" : null,
  "department_number" : null,
  "description" : null,
  "is_leaf" : null,
  "short_name" : null,
  "sort" : null,
  "business_category" : null,
  "parent_unit_id" : null,
  "parent_id" : null,
  "parent_unit_name" : null,
  "dn" : null,
  "parent_name" : null,
  "organization_id" : null,
  "organization_name" : null,
  "organization_number" : null,
}

```

## 数据集

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/sys_departments/fetchdefault" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_department_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|部门名称|
|<el-row justify="space-between"><el-col :span="20">n_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标识|



##### 请求示例： {docsify-ignore}
```json
{
  "page" : 0,
  "size" : 20,
  "sort" : null,
  "n_department_name_like" : null,
  "n_id_eq" : null,
}
```


##### 响应示例： {docsify-ignore}
```json
[
  {
    "id" : null,
    "department_name" : null,
    "creator" : null,
    "create_time" : null,
    "updater" : null,
    "update_time" : null,
    "dc" : null,
    "department_number" : null,
    "description" : null,
    "is_leaf" : null,
    "short_name" : null,
    "sort" : null,
    "business_category" : null,
    "parent_unit_id" : null,
    "parent_id" : null,
    "parent_unit_name" : null,
    "dn" : null,
    "parent_name" : null,
    "organization_id" : null,
    "organization_name" : null,
    "organization_number" : null,
  }
]
```



## 下载导入模板
<el-row>
<div style="width: 80px">
<el-alert center title="GET" type="success" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/sys_departments/importtemplate" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 查询参数 {docsify-ignore}

|字段col300|类型col150|备注col400|
|---|---|----|
| srfimporttag | String | 导入标识 |



## 数据导出

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/sys_departments/exportdata/{param},/sys_departments/exportdata/{param}/{key}" type="info" :closable="false" ></el-alert>
</div>
</el-row>

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|param|String|导出集合方法名称|
|key|String|数据主键|

##### 查询参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|srfexporttag|String|导出模板标识|

##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|page|Integer|page|
|size|Integer|分页大小|
|n_xxx_eq|String|过滤参数|


## 数据导入

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/sys_departments/importdata" type="info" :closable="false" ></el-alert>
</div>
</el-row>

##### 查询参数 {docsify-ignore}

|字段col300|类型col150|备注col400|
|---|---|----|
| srfimporttag | String | 导入标识 |

##### 请求参数 {docsify-ignore}

|字段col300|类型col150|备注col400|
|---|---|----|
| file | file | 导入数据文具 |

## 数据导入（返回错误excel）

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/sys_departments/importdata2" type="info" :closable="false" ></el-alert>
</div>
</el-row>

##### 查询参数 {docsify-ignore}

|字段col300|类型col150|备注col400|
|---|---|----|
| srfimporttag | String | 导入标识 |

##### 请求参数 {docsify-ignore}

|字段col300|类型col150|备注col400|
|---|---|----|
| file | file | 导入数据文具 |

## 自定义表头导入（异步）
<el-row>
<div style="width: 80px">
<el-alert center title="GET" type="success" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/sys_departments/asyncimportdata2" type="info" :closable="false" ></el-alert>
</div>
</el-row>

##### 查询参数 {docsify-ignore}

|字段col300|类型col150|备注col400|
|---|---|----|
| srfimporttag | String | 导入标识 |
| srfossfileid | String | 导入文件 |
| srfimportschemaid | String | 表头定义 |


## 数据打印
<el-row>
<div style="width: 80px">
<el-alert center title="GET" type="success" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/sys_departments/printdata/{key}" type="info" :closable="false" ></el-alert>
</div>
</el-row>

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|数据主键|

##### 查询参数 {docsify-ignore}

|字段col300|类型col150|备注col400|
|---|---|----|
| srfprinttag | String | 打印标识 |
| srfcontenttype | String | 打印类型 |



## 报表打印

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/sys_departments/report" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 查询参数 {docsify-ignore}

|字段col300|类型col150|备注col400|
|---|---|----|
| srfreporttag | String | 报表标识 |
| srfcontenttype | String | 报表类型 |




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