## 项目集组件权限计数器 <!-- {docsify-ignore-all} -->

   获取项目集组件权限

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
state "开始" as Begin <<start>> [[$./portfolio_addon_authority#begin {"开始"}]]




@enduml
```


### 处理步骤说明

#### 开始 :id=Begin<sup class="footnote-symbol"> <font color=gray size=1>[开始]</font></sup>



*- N/A*


### 实体逻辑参数

|    中文名   |    代码名    |  数据类型    |  实体   |备注 |
| --------| --------| -------- | -------- | --------   |
|传入变量(<i class="fa fa-check"/></i>)|Default|数据对象|[文件夹(PORTFOLIO)](module/Base/portfolio.md)||
|计数结果|result|数据对象|[文件夹(PORTFOLIO)](module/Base/portfolio.md)||
