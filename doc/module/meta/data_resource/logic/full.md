## full <!-- {docsify-ignore-all} -->

   

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
state "开始" as Begin <<start>> [[$./full#begin {"开始"}]]
state "将schema绑定至新对象" as BINDPARAM_01  [[$./full#bindparam_01 {"将schema绑定至新对象"}]]
state "填充DEFINITION" as PREPAREPARAM_01  [[$./full#prepareparam_01 {"填充DEFINITION"}]]
state "结束" as END_01 <<end>> [[$./full#end_01 {"结束"}]]


Begin --> BINDPARAM_01
BINDPARAM_01 --> PREPAREPARAM_01
PREPAREPARAM_01 --> END_01


@enduml
```


### 处理步骤说明

#### 开始 :id=Begin<sup class="footnote-symbol"> <font color=gray size=1>[开始]</font></sup>



*- N/A*
#### 将schema绑定至新对象 :id=BINDPARAM_01<sup class="footnote-symbol"> <font color=gray size=1>[绑定参数]</font></sup>



绑定参数`Default(传入变量)` 到 `schema`
#### 填充DEFINITION :id=PREPAREPARAM_01<sup class="footnote-symbol"> <font color=gray size=1>[准备参数]</font></sup>



1. 将`schema.DEFINITION` 设置给  `Default(传入变量).DEFINITION(definition)`

#### 结束 :id=END_01<sup class="footnote-symbol"> <font color=gray size=1>[结束]</font></sup>



返回 `Default(传入变量)`



### 实体逻辑参数

|    中文名   |    代码名    |  数据类型    |  实体   |备注 |
| --------| --------| -------- | -------- | --------   |
|传入变量(<i class="fa fa-check"/></i>)|Default|数据对象|[数据资源(DATA_RESOURCE)](module/meta/data_resource.md)||
|schema|schema|数据对象|||
