## 选择项目集资源成员 <!-- {docsify-ignore-all} -->

   项目集资源分配下设置成员：当前项目下成员/部门/团队

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
state "开始" as Begin <<start>> [[$./choose_portfolio_resource#begin {"开始"}]]




@enduml
```


### 处理步骤说明

#### 开始 :id=Begin<sup class="footnote-symbol"> <font color=gray size=1>[开始]</font></sup>



*- N/A*


### 实体逻辑参数

|    中文名   |    代码名    |  数据类型    |  实体   |备注 |
| --------| --------| -------- | -------- | --------   |
|传入变量(<i class="fa fa-check"/></i>)|Default|过滤器|||
|成员循环变量|for_member|数据对象|[成员(MEMBER)](module/Base/member.md)||
|项目集成员循环变量|for_portfolio_member|数据对象|[文件夹成员(PORTFOLIO_MEMBER)](module/Base/portfolio_member.md)||
|部门成员循环临时变量|for_user_obj|数据对象|[企业用户(USER)](module/Base/user.md)||
|团队成员分页查询结果变量|group_page|分页查询|||
|项目集成员过滤器|portfolio_member_filter|过滤器|||
|项目集成员分页查询结果变量|portfolio_member_page|分页查询|||
|用户过滤器|user_filter|过滤器|||
|部门成员分页查询结果变量|user_page|分页查询|||
