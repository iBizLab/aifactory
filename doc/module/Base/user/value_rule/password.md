## 密码(PASSWORD) <!-- {docsify-ignore-all} -->

   

### 两次密码不一致 :id=PASSWORD

```plantuml
@startuml
hide empty description
<style>
root {
  HyperlinkColor #42b983
}
</style>

state "start" as start  <<start>>
state "end" as end <<end>>
state "[条件组]OR" as 2aca13bd0cdd10008872916a68aaf9df [[$./password#a2aca13bd0cdd10008872916a68aaf9df {"[条件组]OR"}]] {
state " " as 2aca13bd0cdd10008872916a68aaf9df_entry  <<entryPoint>>
state "(sure_password) 值为空(Nil)" as af10a6d1afe0eaa6f4d51ef898820bed [[$./password#aaf10a6d1afe0eaa6f4d51ef898820bed {"[常规条件] 值为空(Nil)"}]]
state "(new_password) 值为空(Nil)" as 46ba9d815a3860a8e94a3afa7320ceb0 [[$./password#a46ba9d815a3860a8e94a3afa7320ceb0 {"[常规条件] 值为空(Nil)"}]]
state "(sure_password) 等于(=) 数据对象属性 (new_password)" as 5f410af0e683bf4356d6f9d48419a8ee [[$./password#a5f410af0e683bf4356d6f9d48419a8ee {"[常规条件] 等于(=) 数据对象属性 (new_password)"}]]
state " " as 2aca13bd0cdd10008872916a68aaf9df_exit  <<exitPoint>>
}


start --> 2aca13bd0cdd10008872916a68aaf9df_entry 
2aca13bd0cdd10008872916a68aaf9df_entry --> af10a6d1afe0eaa6f4d51ef898820bed 
af10a6d1afe0eaa6f4d51ef898820bed --> 2aca13bd0cdd10008872916a68aaf9df_exit  : yes
af10a6d1afe0eaa6f4d51ef898820bed -[#red]-> 46ba9d815a3860a8e94a3afa7320ceb0  : no

46ba9d815a3860a8e94a3afa7320ceb0 --> 2aca13bd0cdd10008872916a68aaf9df_exit  : yes
46ba9d815a3860a8e94a3afa7320ceb0 -[#red]-> 5f410af0e683bf4356d6f9d48419a8ee  : no

5f410af0e683bf4356d6f9d48419a8ee --> 2aca13bd0cdd10008872916a68aaf9df_exit  : yes
5f410af0e683bf4356d6f9d48419a8ee -[#red]-> end  : no
2aca13bd0cdd10008872916a68aaf9df_exit --> end 


@enduml
```

#### 条件说明

##### (sure_password) 值为空(Nil) :id=aaf10a6d1afe0eaa6f4d51ef898820bed



`sure_password` ISNULL 

##### (sure_password) 等于(=) 数据对象属性 (new_password) :id=a5f410af0e683bf4356d6f9d48419a8ee



`sure_password` EQ  `new_password`

> [!ATTENTION|label:规则信息|icon:fa fa-warning]
> 两次输入的密码不一致


##### (new_password) 值为空(Nil) :id=a46ba9d815a3860a8e94a3afa7320ceb0



`new_password` ISNULL 


### 默认规则 :id=Default

```plantuml
@startuml
hide empty description
<style>
root {
  HyperlinkColor #42b983
}
</style>

state "start" as start  <<start>>
state "end" as end <<end>>
state "默认字符串长度" as 993c4cf6749c233ad568ebae98cd0696 [[$./password#a993c4cf6749c233ad568ebae98cd0696 {"默认字符串长度"}]]


start --> 993c4cf6749c233ad568ebae98cd0696 
993c4cf6749c233ad568ebae98cd0696 --> end 


@enduml
```

#### 条件说明

##### 默认字符串长度 :id=a993c4cf6749c233ad568ebae98cd0696


*关键条件*


`PASSWORD(密码)` 属性长度在区间 `(0 , 200]` 内

> [!ATTENTION|label:规则信息|icon:fa fa-warning]
> 内容长度必须小于等于[200]







