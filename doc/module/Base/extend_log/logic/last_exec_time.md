## 获取最后一次成功执行时间戳 <!-- {docsify-ignore-all} -->

   

### 处理过程

```plantuml
@startuml
hide empty description
<style>
root {
  HyperlinkColor #42b983
}
</style>

hide empty description
state "开始" as Begin <<start>> [[$./last_exec_time#begin {"开始"}]]
state "准备参数" as PREPAREPARAM_01  [[$./last_exec_time#prepareparam_01 {"准备参数"}]]
state "查询记录" as DEDATAQUERY_01  [[$./last_exec_time#dedataquery_01 {"查询记录"}]]
state "绑定参数" as BINDPARAM_01  [[$./last_exec_time#bindparam_01 {"绑定参数"}]]
state "赋值最后一次成功执行时间" as PREPAREPARAM_02  [[$./last_exec_time#prepareparam_02 {"赋值最后一次成功执行时间"}]]
state "结束" as END_01 <<end>> [[$./last_exec_time#end_01 {"结束"}]]


Begin --> PREPAREPARAM_01
PREPAREPARAM_01 --> DEDATAQUERY_01
DEDATAQUERY_01 --> END_01 : [[$./last_exec_time#dedataquery_01-end_01{无记录} 无记录]]
DEDATAQUERY_01 --> BINDPARAM_01 : [[$./last_exec_time#dedataquery_01-bindparam_01{有记录} 有记录]]
BINDPARAM_01 --> PREPAREPARAM_02
PREPAREPARAM_02 --> END_01


@enduml
```


### 处理步骤说明

#### 开始 :id=Begin<sup class="footnote-symbol"> <font color=gray size=1>[开始]</font></sup>



*- N/A*
#### 准备参数 :id=PREPAREPARAM_01<sup class="footnote-symbol"> <font color=gray size=1>[准备参数]</font></sup>



1. 将`Default(传入变量).owner_id(所属数据标识)` 设置给  `log_filter.n_owner_id_eq`
2. 将`SUCCESS` 设置给  `log_filter.n_state_eq`
3. 将`PSDELOGIC` 设置给  `log_filter.n_owner_subtype_eq`
4. 将`end_at,desc` 设置给  `log_filter.sort`
5. 将`1` 设置给  `log_filter.size`

#### 查询记录 :id=DEDATAQUERY_01<sup class="footnote-symbol"> <font color=gray size=1>[实体数据查询]</font></sup>



调用实体 [扩展日志(EXTEND_LOG)](module/Base/extend_log.md) 数据查询 [数据查询(DEFAULT)](module/Base/extend_log#数据查询) ，查询参数为`log_filter`

将执行结果返回给参数`log_page`

#### 绑定参数 :id=BINDPARAM_01<sup class="footnote-symbol"> <font color=gray size=1>[绑定参数]</font></sup>



绑定参数`log_page` 到 `last_extend_log`
#### 赋值最后一次成功执行时间 :id=PREPAREPARAM_02<sup class="footnote-symbol"> <font color=gray size=1>[准备参数]</font></sup>



1. 将`last_extend_log.END_AT(结束时间)` 设置给  `Default(传入变量).last_exec_time`

#### 结束 :id=END_01<sup class="footnote-symbol"> <font color=gray size=1>[结束]</font></sup>



返回 `Default(传入变量)`


### 连接条件说明
#### 无记录 :id=DEDATAQUERY_01-END_01

`log_page(log_page).size` EQ `0`
#### 有记录 :id=DEDATAQUERY_01-BINDPARAM_01

`log_page(log_page).size` GT `0`


### 实体逻辑参数

|    中文名   |    代码名    |  数据类型    |  实体   |备注 |
| --------| --------| -------- | -------- | --------   |
|传入变量(<i class="fa fa-check"/></i>)|Default|数据对象|[扩展日志(EXTEND_LOG)](module/Base/extend_log.md)||
|last_extend_log|last_extend_log|数据对象|[扩展日志(EXTEND_LOG)](module/Base/extend_log.md)||
|log_filter|log_filter|过滤器|||
|log_page|log_page|分页查询|||
