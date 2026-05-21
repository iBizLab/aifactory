# 部门(SysDepartment) :id=SysDepartment
## 创建部门

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/sysdepartments" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`CREATE`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">deptid</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|部门标识|
|<el-row justify="space-between"><el-col :span="20">deptcode</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|部门代码|
|<el-row justify="space-between"><el-col :span="20">deptname</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|部门名称|
|<el-row justify="space-between"><el-col :span="20">parentdeptid</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上级部门|
|<el-row justify="space-between"><el-col :span="20">shortname</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|部门简称|
|<el-row justify="space-between"><el-col :span="20">deptlevel</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|部门级别|
|<el-row justify="space-between"><el-col :span="20">domains</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|区属|
|<el-row justify="space-between"><el-col :span="20">showorder</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|排序|
|<el-row justify="space-between"><el-col :span="20">bcode</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务编码|
|<el-row justify="space-between"><el-col :span="20">leaderid</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|分管领导标识|
|<el-row justify="space-between"><el-col :span="20">leadername</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|分管领导|
|<el-row justify="space-between"><el-col :span="20">orgid</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|单位|
|<el-row justify="space-between"><el-col :span="20">orgname</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|单位名称|
|<el-row justify="space-between"><el-col :span="20">parentdeptname</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上级部门|
|<el-row justify="space-between"><el-col :span="20">reserver</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留|
|<el-row justify="space-between"><el-col :span="20">reserver10</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留10|
|<el-row justify="space-between"><el-col :span="20">reserver11</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|保留11|
|<el-row justify="space-between"><el-col :span="20">reserver12</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|保留12|
|<el-row justify="space-between"><el-col :span="20">reserver13</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|保留13|
|<el-row justify="space-between"><el-col :span="20">reserver14</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|保留14|
|<el-row justify="space-between"><el-col :span="20">reserver15</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|保留15|
|<el-row justify="space-between"><el-col :span="20">reserver16</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|保留16|
|<el-row justify="space-between"><el-col :span="20">reserver17</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|保留17|
|<el-row justify="space-between"><el-col :span="20">reserver18</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|保留18|
|<el-row justify="space-between"><el-col :span="20">reserver19</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|保留19|
|<el-row justify="space-between"><el-col :span="20">reserver2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留2|
|<el-row justify="space-between"><el-col :span="20">reserver20</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|保留20|
|<el-row justify="space-between"><el-col :span="20">reserver3</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留3|
|<el-row justify="space-between"><el-col :span="20">reserver4</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留4|
|<el-row justify="space-between"><el-col :span="20">reserver5</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留5|
|<el-row justify="space-between"><el-col :span="20">reserver6</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留6|
|<el-row justify="space-between"><el-col :span="20">reserver7</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留7|
|<el-row justify="space-between"><el-col :span="20">reserver8</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留8|
|<el-row justify="space-between"><el-col :span="20">reserver9</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留9|
|<el-row justify="space-between"><el-col :span="20">dddeptid</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|钉钉部门标识|
|<el-row justify="space-between"><el-col :span="20">deptfullname</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|部门全称|
|<el-row justify="space-between"><el-col :span="20">deptleader</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|部门领导|
|<el-row justify="space-between"><el-col :span="20">deptleaderid</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|部门领导标识|
|<el-row justify="space-between"><el-col :span="20">isvalid</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|启用标志|
|<el-row justify="space-between"><el-col :span="20">wxworkdeptid</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|企业微信部门标识|



##### 请求示例： {docsify-ignore}
```json
{
  "deptid" : null,
  "deptcode" : null,
  "deptname" : null,
  "parentdeptid" : null,
  "shortname" : null,
  "deptlevel" : null,
  "domains" : null,
  "showorder" : null,
  "bcode" : null,
  "leaderid" : null,
  "leadername" : null,
  "orgid" : null,
  "orgname" : null,
  "parentdeptname" : null,
  "createdate" : null,
  "updatedate" : null,
  "reserver" : null,
  "reserver10" : null,
  "reserver11" : null,
  "reserver12" : null,
  "reserver13" : null,
  "reserver14" : null,
  "reserver15" : null,
  "reserver16" : null,
  "reserver17" : null,
  "reserver18" : null,
  "reserver19" : null,
  "reserver2" : null,
  "reserver20" : null,
  "reserver3" : null,
  "reserver4" : null,
  "reserver5" : null,
  "reserver6" : null,
  "reserver7" : null,
  "reserver8" : null,
  "reserver9" : null,
  "dddeptid" : null,
  "deptfullname" : null,
  "deptleader" : null,
  "deptleaderid" : null,
  "isvalid" : null,
  "wxworkdeptid" : null,
}
```


##### 响应示例： {docsify-ignore}
```json

{
  "deptid" : null,
  "deptcode" : null,
  "deptname" : null,
  "parentdeptid" : null,
  "shortname" : null,
  "deptlevel" : null,
  "domains" : null,
  "showorder" : null,
  "bcode" : null,
  "leaderid" : null,
  "leadername" : null,
  "orgid" : null,
  "orgname" : null,
  "parentdeptname" : null,
  "createdate" : null,
  "updatedate" : null,
  "reserver" : null,
  "reserver10" : null,
  "reserver11" : null,
  "reserver12" : null,
  "reserver13" : null,
  "reserver14" : null,
  "reserver15" : null,
  "reserver16" : null,
  "reserver17" : null,
  "reserver18" : null,
  "reserver19" : null,
  "reserver2" : null,
  "reserver20" : null,
  "reserver3" : null,
  "reserver4" : null,
  "reserver5" : null,
  "reserver6" : null,
  "reserver7" : null,
  "reserver8" : null,
  "reserver9" : null,
  "dddeptid" : null,
  "deptfullname" : null,
  "deptleader" : null,
  "deptleaderid" : null,
  "isvalid" : null,
  "wxworkdeptid" : null,
}

```

## 获取部门

<el-row>
<div style="width: 80px">
<el-alert center title="GET" type="success" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/sysdepartments/{key}" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|部门标识|




##### 响应示例： {docsify-ignore}
```json

{
  "deptid" : null,
  "deptcode" : null,
  "deptname" : null,
  "parentdeptid" : null,
  "shortname" : null,
  "deptlevel" : null,
  "domains" : null,
  "showorder" : null,
  "bcode" : null,
  "leaderid" : null,
  "leadername" : null,
  "orgid" : null,
  "orgname" : null,
  "parentdeptname" : null,
  "createdate" : null,
  "updatedate" : null,
  "reserver" : null,
  "reserver10" : null,
  "reserver11" : null,
  "reserver12" : null,
  "reserver13" : null,
  "reserver14" : null,
  "reserver15" : null,
  "reserver16" : null,
  "reserver17" : null,
  "reserver18" : null,
  "reserver19" : null,
  "reserver2" : null,
  "reserver20" : null,
  "reserver3" : null,
  "reserver4" : null,
  "reserver5" : null,
  "reserver6" : null,
  "reserver7" : null,
  "reserver8" : null,
  "reserver9" : null,
  "dddeptid" : null,
  "deptfullname" : null,
  "deptleader" : null,
  "deptleaderid" : null,
  "isvalid" : null,
  "wxworkdeptid" : null,
}

```

## 删除部门

<el-row>
<div style="width: 80px">
<el-alert center title="DELETE" type="error" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/sysdepartments/{key}" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`DELETE`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|部门标识|





## 更新部门

<el-row>
<div style="width: 80px">
<el-alert center title="PUT" type="warning" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/sysdepartments/{key}" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`UPDATE`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|部门标识|



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">deptid</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|部门标识|
|<el-row justify="space-between"><el-col :span="20">deptcode</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|部门代码|
|<el-row justify="space-between"><el-col :span="20">deptname</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|部门名称|
|<el-row justify="space-between"><el-col :span="20">parentdeptid</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上级部门|
|<el-row justify="space-between"><el-col :span="20">shortname</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|部门简称|
|<el-row justify="space-between"><el-col :span="20">deptlevel</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|部门级别|
|<el-row justify="space-between"><el-col :span="20">domains</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|区属|
|<el-row justify="space-between"><el-col :span="20">showorder</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|排序|
|<el-row justify="space-between"><el-col :span="20">bcode</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务编码|
|<el-row justify="space-between"><el-col :span="20">leaderid</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|分管领导标识|
|<el-row justify="space-between"><el-col :span="20">leadername</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|分管领导|
|<el-row justify="space-between"><el-col :span="20">orgid</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|单位|
|<el-row justify="space-between"><el-col :span="20">orgname</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|单位名称|
|<el-row justify="space-between"><el-col :span="20">parentdeptname</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上级部门|
|<el-row justify="space-between"><el-col :span="20">reserver</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留|
|<el-row justify="space-between"><el-col :span="20">reserver10</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留10|
|<el-row justify="space-between"><el-col :span="20">reserver11</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|保留11|
|<el-row justify="space-between"><el-col :span="20">reserver12</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|保留12|
|<el-row justify="space-between"><el-col :span="20">reserver13</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|保留13|
|<el-row justify="space-between"><el-col :span="20">reserver14</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|保留14|
|<el-row justify="space-between"><el-col :span="20">reserver15</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|保留15|
|<el-row justify="space-between"><el-col :span="20">reserver16</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|保留16|
|<el-row justify="space-between"><el-col :span="20">reserver17</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|保留17|
|<el-row justify="space-between"><el-col :span="20">reserver18</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|保留18|
|<el-row justify="space-between"><el-col :span="20">reserver19</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|保留19|
|<el-row justify="space-between"><el-col :span="20">reserver2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留2|
|<el-row justify="space-between"><el-col :span="20">reserver20</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|保留20|
|<el-row justify="space-between"><el-col :span="20">reserver3</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留3|
|<el-row justify="space-between"><el-col :span="20">reserver4</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留4|
|<el-row justify="space-between"><el-col :span="20">reserver5</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留5|
|<el-row justify="space-between"><el-col :span="20">reserver6</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留6|
|<el-row justify="space-between"><el-col :span="20">reserver7</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留7|
|<el-row justify="space-between"><el-col :span="20">reserver8</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留8|
|<el-row justify="space-between"><el-col :span="20">reserver9</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留9|
|<el-row justify="space-between"><el-col :span="20">dddeptid</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|钉钉部门标识|
|<el-row justify="space-between"><el-col :span="20">deptfullname</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|部门全称|
|<el-row justify="space-between"><el-col :span="20">deptleader</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|部门领导|
|<el-row justify="space-between"><el-col :span="20">deptleaderid</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|部门领导标识|
|<el-row justify="space-between"><el-col :span="20">isvalid</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|启用标志|
|<el-row justify="space-between"><el-col :span="20">wxworkdeptid</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|企业微信部门标识|



##### 请求示例： {docsify-ignore}
```json
{
  "deptid" : null,
  "deptcode" : null,
  "deptname" : null,
  "parentdeptid" : null,
  "shortname" : null,
  "deptlevel" : null,
  "domains" : null,
  "showorder" : null,
  "bcode" : null,
  "leaderid" : null,
  "leadername" : null,
  "orgid" : null,
  "orgname" : null,
  "parentdeptname" : null,
  "createdate" : null,
  "updatedate" : null,
  "reserver" : null,
  "reserver10" : null,
  "reserver11" : null,
  "reserver12" : null,
  "reserver13" : null,
  "reserver14" : null,
  "reserver15" : null,
  "reserver16" : null,
  "reserver17" : null,
  "reserver18" : null,
  "reserver19" : null,
  "reserver2" : null,
  "reserver20" : null,
  "reserver3" : null,
  "reserver4" : null,
  "reserver5" : null,
  "reserver6" : null,
  "reserver7" : null,
  "reserver8" : null,
  "reserver9" : null,
  "dddeptid" : null,
  "deptfullname" : null,
  "deptleader" : null,
  "deptleaderid" : null,
  "isvalid" : null,
  "wxworkdeptid" : null,
}
```


##### 响应示例： {docsify-ignore}
```json

{
  "deptid" : null,
  "deptcode" : null,
  "deptname" : null,
  "parentdeptid" : null,
  "shortname" : null,
  "deptlevel" : null,
  "domains" : null,
  "showorder" : null,
  "bcode" : null,
  "leaderid" : null,
  "leadername" : null,
  "orgid" : null,
  "orgname" : null,
  "parentdeptname" : null,
  "createdate" : null,
  "updatedate" : null,
  "reserver" : null,
  "reserver10" : null,
  "reserver11" : null,
  "reserver12" : null,
  "reserver13" : null,
  "reserver14" : null,
  "reserver15" : null,
  "reserver16" : null,
  "reserver17" : null,
  "reserver18" : null,
  "reserver19" : null,
  "reserver2" : null,
  "reserver20" : null,
  "reserver3" : null,
  "reserver4" : null,
  "reserver5" : null,
  "reserver6" : null,
  "reserver7" : null,
  "reserver8" : null,
  "reserver9" : null,
  "dddeptid" : null,
  "deptfullname" : null,
  "deptleader" : null,
  "deptleaderid" : null,
  "isvalid" : null,
  "wxworkdeptid" : null,
}

```

## 检查部门主键

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/sysdepartments/checkkey" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`CREATE`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">deptid</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|部门标识|
|<el-row justify="space-between"><el-col :span="20">deptcode</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|部门代码|
|<el-row justify="space-between"><el-col :span="20">deptname</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|部门名称|
|<el-row justify="space-between"><el-col :span="20">parentdeptid</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上级部门|
|<el-row justify="space-between"><el-col :span="20">shortname</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|部门简称|
|<el-row justify="space-between"><el-col :span="20">deptlevel</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|部门级别|
|<el-row justify="space-between"><el-col :span="20">domains</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|区属|
|<el-row justify="space-between"><el-col :span="20">showorder</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|排序|
|<el-row justify="space-between"><el-col :span="20">bcode</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务编码|
|<el-row justify="space-between"><el-col :span="20">leaderid</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|分管领导标识|
|<el-row justify="space-between"><el-col :span="20">leadername</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|分管领导|
|<el-row justify="space-between"><el-col :span="20">orgid</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|单位|
|<el-row justify="space-between"><el-col :span="20">orgname</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|单位名称|
|<el-row justify="space-between"><el-col :span="20">parentdeptname</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上级部门|
|<el-row justify="space-between"><el-col :span="20">reserver</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留|
|<el-row justify="space-between"><el-col :span="20">reserver10</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留10|
|<el-row justify="space-between"><el-col :span="20">reserver11</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|保留11|
|<el-row justify="space-between"><el-col :span="20">reserver12</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|保留12|
|<el-row justify="space-between"><el-col :span="20">reserver13</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|保留13|
|<el-row justify="space-between"><el-col :span="20">reserver14</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|保留14|
|<el-row justify="space-between"><el-col :span="20">reserver15</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|保留15|
|<el-row justify="space-between"><el-col :span="20">reserver16</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|保留16|
|<el-row justify="space-between"><el-col :span="20">reserver17</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|保留17|
|<el-row justify="space-between"><el-col :span="20">reserver18</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|保留18|
|<el-row justify="space-between"><el-col :span="20">reserver19</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|保留19|
|<el-row justify="space-between"><el-col :span="20">reserver2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留2|
|<el-row justify="space-between"><el-col :span="20">reserver20</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|保留20|
|<el-row justify="space-between"><el-col :span="20">reserver3</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留3|
|<el-row justify="space-between"><el-col :span="20">reserver4</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留4|
|<el-row justify="space-between"><el-col :span="20">reserver5</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留5|
|<el-row justify="space-between"><el-col :span="20">reserver6</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留6|
|<el-row justify="space-between"><el-col :span="20">reserver7</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留7|
|<el-row justify="space-between"><el-col :span="20">reserver8</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留8|
|<el-row justify="space-between"><el-col :span="20">reserver9</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留9|
|<el-row justify="space-between"><el-col :span="20">dddeptid</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|钉钉部门标识|
|<el-row justify="space-between"><el-col :span="20">deptfullname</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|部门全称|
|<el-row justify="space-between"><el-col :span="20">deptleader</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|部门领导|
|<el-row justify="space-between"><el-col :span="20">deptleaderid</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|部门领导标识|
|<el-row justify="space-between"><el-col :span="20">isvalid</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|启用标志|
|<el-row justify="space-between"><el-col :span="20">wxworkdeptid</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|企业微信部门标识|



##### 请求示例： {docsify-ignore}
```json
{
  "deptid" : null,
  "deptcode" : null,
  "deptname" : null,
  "parentdeptid" : null,
  "shortname" : null,
  "deptlevel" : null,
  "domains" : null,
  "showorder" : null,
  "bcode" : null,
  "leaderid" : null,
  "leadername" : null,
  "orgid" : null,
  "orgname" : null,
  "parentdeptname" : null,
  "createdate" : null,
  "updatedate" : null,
  "reserver" : null,
  "reserver10" : null,
  "reserver11" : null,
  "reserver12" : null,
  "reserver13" : null,
  "reserver14" : null,
  "reserver15" : null,
  "reserver16" : null,
  "reserver17" : null,
  "reserver18" : null,
  "reserver19" : null,
  "reserver2" : null,
  "reserver20" : null,
  "reserver3" : null,
  "reserver4" : null,
  "reserver5" : null,
  "reserver6" : null,
  "reserver7" : null,
  "reserver8" : null,
  "reserver9" : null,
  "dddeptid" : null,
  "deptfullname" : null,
  "deptleader" : null,
  "deptleaderid" : null,
  "isvalid" : null,
  "wxworkdeptid" : null,
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
<el-alert title="/sysdepartments/getdraft" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`CREATE`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">deptid</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|部门标识|
|<el-row justify="space-between"><el-col :span="20">deptcode</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|部门代码|
|<el-row justify="space-between"><el-col :span="20">deptname</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|部门名称|
|<el-row justify="space-between"><el-col :span="20">parentdeptid</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上级部门|
|<el-row justify="space-between"><el-col :span="20">shortname</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|部门简称|
|<el-row justify="space-between"><el-col :span="20">deptlevel</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|部门级别|
|<el-row justify="space-between"><el-col :span="20">domains</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|区属|
|<el-row justify="space-between"><el-col :span="20">showorder</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|排序|
|<el-row justify="space-between"><el-col :span="20">bcode</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务编码|
|<el-row justify="space-between"><el-col :span="20">leaderid</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|分管领导标识|
|<el-row justify="space-between"><el-col :span="20">leadername</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|分管领导|
|<el-row justify="space-between"><el-col :span="20">orgid</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|单位|
|<el-row justify="space-between"><el-col :span="20">orgname</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|单位名称|
|<el-row justify="space-between"><el-col :span="20">parentdeptname</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上级部门|
|<el-row justify="space-between"><el-col :span="20">reserver</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留|
|<el-row justify="space-between"><el-col :span="20">reserver10</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留10|
|<el-row justify="space-between"><el-col :span="20">reserver11</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|保留11|
|<el-row justify="space-between"><el-col :span="20">reserver12</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|保留12|
|<el-row justify="space-between"><el-col :span="20">reserver13</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|保留13|
|<el-row justify="space-between"><el-col :span="20">reserver14</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|保留14|
|<el-row justify="space-between"><el-col :span="20">reserver15</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|保留15|
|<el-row justify="space-between"><el-col :span="20">reserver16</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|保留16|
|<el-row justify="space-between"><el-col :span="20">reserver17</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|保留17|
|<el-row justify="space-between"><el-col :span="20">reserver18</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|保留18|
|<el-row justify="space-between"><el-col :span="20">reserver19</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|保留19|
|<el-row justify="space-between"><el-col :span="20">reserver2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留2|
|<el-row justify="space-between"><el-col :span="20">reserver20</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|保留20|
|<el-row justify="space-between"><el-col :span="20">reserver3</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留3|
|<el-row justify="space-between"><el-col :span="20">reserver4</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留4|
|<el-row justify="space-between"><el-col :span="20">reserver5</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留5|
|<el-row justify="space-between"><el-col :span="20">reserver6</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留6|
|<el-row justify="space-between"><el-col :span="20">reserver7</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留7|
|<el-row justify="space-between"><el-col :span="20">reserver8</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留8|
|<el-row justify="space-between"><el-col :span="20">reserver9</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留9|
|<el-row justify="space-between"><el-col :span="20">dddeptid</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|钉钉部门标识|
|<el-row justify="space-between"><el-col :span="20">deptfullname</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|部门全称|
|<el-row justify="space-between"><el-col :span="20">deptleader</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|部门领导|
|<el-row justify="space-between"><el-col :span="20">deptleaderid</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|部门领导标识|
|<el-row justify="space-between"><el-col :span="20">isvalid</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|启用标志|
|<el-row justify="space-between"><el-col :span="20">wxworkdeptid</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|企业微信部门标识|



##### 请求示例： {docsify-ignore}
```json
{
  "deptid" : null,
  "deptcode" : null,
  "deptname" : null,
  "parentdeptid" : null,
  "shortname" : null,
  "deptlevel" : null,
  "domains" : null,
  "showorder" : null,
  "bcode" : null,
  "leaderid" : null,
  "leadername" : null,
  "orgid" : null,
  "orgname" : null,
  "parentdeptname" : null,
  "createdate" : null,
  "updatedate" : null,
  "reserver" : null,
  "reserver10" : null,
  "reserver11" : null,
  "reserver12" : null,
  "reserver13" : null,
  "reserver14" : null,
  "reserver15" : null,
  "reserver16" : null,
  "reserver17" : null,
  "reserver18" : null,
  "reserver19" : null,
  "reserver2" : null,
  "reserver20" : null,
  "reserver3" : null,
  "reserver4" : null,
  "reserver5" : null,
  "reserver6" : null,
  "reserver7" : null,
  "reserver8" : null,
  "reserver9" : null,
  "dddeptid" : null,
  "deptfullname" : null,
  "deptleader" : null,
  "deptleaderid" : null,
  "isvalid" : null,
  "wxworkdeptid" : null,
}
```


##### 响应示例： {docsify-ignore}
```json

{
  "deptid" : null,
  "deptcode" : null,
  "deptname" : null,
  "parentdeptid" : null,
  "shortname" : null,
  "deptlevel" : null,
  "domains" : null,
  "showorder" : null,
  "bcode" : null,
  "leaderid" : null,
  "leadername" : null,
  "orgid" : null,
  "orgname" : null,
  "parentdeptname" : null,
  "createdate" : null,
  "updatedate" : null,
  "reserver" : null,
  "reserver10" : null,
  "reserver11" : null,
  "reserver12" : null,
  "reserver13" : null,
  "reserver14" : null,
  "reserver15" : null,
  "reserver16" : null,
  "reserver17" : null,
  "reserver18" : null,
  "reserver19" : null,
  "reserver2" : null,
  "reserver20" : null,
  "reserver3" : null,
  "reserver4" : null,
  "reserver5" : null,
  "reserver6" : null,
  "reserver7" : null,
  "reserver8" : null,
  "reserver9" : null,
  "dddeptid" : null,
  "deptfullname" : null,
  "deptleader" : null,
  "deptleaderid" : null,
  "isvalid" : null,
  "wxworkdeptid" : null,
}

```

## 保存部门

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/sysdepartments/save" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`CREATE`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">deptid</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|部门标识|
|<el-row justify="space-between"><el-col :span="20">deptcode</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|部门代码|
|<el-row justify="space-between"><el-col :span="20">deptname</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|部门名称|
|<el-row justify="space-between"><el-col :span="20">parentdeptid</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上级部门|
|<el-row justify="space-between"><el-col :span="20">shortname</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|部门简称|
|<el-row justify="space-between"><el-col :span="20">deptlevel</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|部门级别|
|<el-row justify="space-between"><el-col :span="20">domains</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|区属|
|<el-row justify="space-between"><el-col :span="20">showorder</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|排序|
|<el-row justify="space-between"><el-col :span="20">bcode</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务编码|
|<el-row justify="space-between"><el-col :span="20">leaderid</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|分管领导标识|
|<el-row justify="space-between"><el-col :span="20">leadername</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|分管领导|
|<el-row justify="space-between"><el-col :span="20">orgid</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|单位|
|<el-row justify="space-between"><el-col :span="20">orgname</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|单位名称|
|<el-row justify="space-between"><el-col :span="20">parentdeptname</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上级部门|
|<el-row justify="space-between"><el-col :span="20">reserver</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留|
|<el-row justify="space-between"><el-col :span="20">reserver10</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留10|
|<el-row justify="space-between"><el-col :span="20">reserver11</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|保留11|
|<el-row justify="space-between"><el-col :span="20">reserver12</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|保留12|
|<el-row justify="space-between"><el-col :span="20">reserver13</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|保留13|
|<el-row justify="space-between"><el-col :span="20">reserver14</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|保留14|
|<el-row justify="space-between"><el-col :span="20">reserver15</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|保留15|
|<el-row justify="space-between"><el-col :span="20">reserver16</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|保留16|
|<el-row justify="space-between"><el-col :span="20">reserver17</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|保留17|
|<el-row justify="space-between"><el-col :span="20">reserver18</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|保留18|
|<el-row justify="space-between"><el-col :span="20">reserver19</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|保留19|
|<el-row justify="space-between"><el-col :span="20">reserver2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留2|
|<el-row justify="space-between"><el-col :span="20">reserver20</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Timestamp|保留20|
|<el-row justify="space-between"><el-col :span="20">reserver3</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留3|
|<el-row justify="space-between"><el-col :span="20">reserver4</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留4|
|<el-row justify="space-between"><el-col :span="20">reserver5</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留5|
|<el-row justify="space-between"><el-col :span="20">reserver6</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留6|
|<el-row justify="space-between"><el-col :span="20">reserver7</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留7|
|<el-row justify="space-between"><el-col :span="20">reserver8</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留8|
|<el-row justify="space-between"><el-col :span="20">reserver9</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|保留9|
|<el-row justify="space-between"><el-col :span="20">dddeptid</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|钉钉部门标识|
|<el-row justify="space-between"><el-col :span="20">deptfullname</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|部门全称|
|<el-row justify="space-between"><el-col :span="20">deptleader</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|部门领导|
|<el-row justify="space-between"><el-col :span="20">deptleaderid</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|部门领导标识|
|<el-row justify="space-between"><el-col :span="20">isvalid</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|启用标志|
|<el-row justify="space-between"><el-col :span="20">wxworkdeptid</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|企业微信部门标识|



##### 请求示例： {docsify-ignore}
```json
{
  "deptid" : null,
  "deptcode" : null,
  "deptname" : null,
  "parentdeptid" : null,
  "shortname" : null,
  "deptlevel" : null,
  "domains" : null,
  "showorder" : null,
  "bcode" : null,
  "leaderid" : null,
  "leadername" : null,
  "orgid" : null,
  "orgname" : null,
  "parentdeptname" : null,
  "createdate" : null,
  "updatedate" : null,
  "reserver" : null,
  "reserver10" : null,
  "reserver11" : null,
  "reserver12" : null,
  "reserver13" : null,
  "reserver14" : null,
  "reserver15" : null,
  "reserver16" : null,
  "reserver17" : null,
  "reserver18" : null,
  "reserver19" : null,
  "reserver2" : null,
  "reserver20" : null,
  "reserver3" : null,
  "reserver4" : null,
  "reserver5" : null,
  "reserver6" : null,
  "reserver7" : null,
  "reserver8" : null,
  "reserver9" : null,
  "dddeptid" : null,
  "deptfullname" : null,
  "deptleader" : null,
  "deptleaderid" : null,
  "isvalid" : null,
  "wxworkdeptid" : null,
}
```


##### 响应示例： {docsify-ignore}
```json

{
  "deptid" : null,
  "deptcode" : null,
  "deptname" : null,
  "parentdeptid" : null,
  "shortname" : null,
  "deptlevel" : null,
  "domains" : null,
  "showorder" : null,
  "bcode" : null,
  "leaderid" : null,
  "leadername" : null,
  "orgid" : null,
  "orgname" : null,
  "parentdeptname" : null,
  "createdate" : null,
  "updatedate" : null,
  "reserver" : null,
  "reserver10" : null,
  "reserver11" : null,
  "reserver12" : null,
  "reserver13" : null,
  "reserver14" : null,
  "reserver15" : null,
  "reserver16" : null,
  "reserver17" : null,
  "reserver18" : null,
  "reserver19" : null,
  "reserver2" : null,
  "reserver20" : null,
  "reserver3" : null,
  "reserver4" : null,
  "reserver5" : null,
  "reserver6" : null,
  "reserver7" : null,
  "reserver8" : null,
  "reserver9" : null,
  "dddeptid" : null,
  "deptfullname" : null,
  "deptleader" : null,
  "deptleaderid" : null,
  "isvalid" : null,
  "wxworkdeptid" : null,
}

```

## 数据集

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/sysdepartments/fetchdefault" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_deptid_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|部门标识|
|<el-row justify="space-between"><el-col :span="20">n_deptname_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|部门名称|



##### 请求示例： {docsify-ignore}
```json
{
  "page" : 0,
  "size" : 20,
  "sort" : null,
  "n_deptid_eq" : null,
  "n_deptname_like" : null,
}
```


##### 响应示例： {docsify-ignore}
```json
[
  {
    "deptid" : null,
    "deptcode" : null,
    "deptname" : null,
    "parentdeptid" : null,
    "shortname" : null,
    "deptlevel" : null,
    "domains" : null,
    "showorder" : null,
    "bcode" : null,
    "leaderid" : null,
    "leadername" : null,
    "orgid" : null,
    "orgname" : null,
    "parentdeptname" : null,
    "createdate" : null,
    "updatedate" : null,
    "reserver" : null,
    "reserver10" : null,
    "reserver11" : null,
    "reserver12" : null,
    "reserver13" : null,
    "reserver14" : null,
    "reserver15" : null,
    "reserver16" : null,
    "reserver17" : null,
    "reserver18" : null,
    "reserver19" : null,
    "reserver2" : null,
    "reserver20" : null,
    "reserver3" : null,
    "reserver4" : null,
    "reserver5" : null,
    "reserver6" : null,
    "reserver7" : null,
    "reserver8" : null,
    "reserver9" : null,
    "dddeptid" : null,
    "deptfullname" : null,
    "deptleader" : null,
    "deptleaderid" : null,
    "isvalid" : null,
    "wxworkdeptid" : null,
  }
]
```



## 下载导入模板
<el-row>
<div style="width: 80px">
<el-alert center title="GET" type="success" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/sysdepartments/importtemplate" type="info" :closable="false" ></el-alert>
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
<el-alert title="/sysdepartments/exportdata/{param},/sysdepartments/exportdata/{param}/{key}" type="info" :closable="false" ></el-alert>
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
<el-alert title="/sysdepartments/importdata" type="info" :closable="false" ></el-alert>
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
<el-alert title="/sysdepartments/importdata2" type="info" :closable="false" ></el-alert>
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
<el-alert title="/sysdepartments/asyncimportdata2" type="info" :closable="false" ></el-alert>
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
<el-alert title="/sysdepartments/printdata/{key}" type="info" :closable="false" ></el-alert>
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
<el-alert title="/sysdepartments/report" type="info" :closable="false" ></el-alert>
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