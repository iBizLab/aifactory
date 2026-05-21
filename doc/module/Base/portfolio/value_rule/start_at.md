## 开始时间(START_AT) <!-- {docsify-ignore-all} -->

   

### 开始时间 :id=START_AT

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
state "[条件组]OR" as 976d16116e8b7742ce0ef479d82a4809 [[$./start_at#a976d16116e8b7742ce0ef479d82a4809 {"[条件组]OR"}]] {
state " " as 976d16116e8b7742ce0ef479d82a4809_entry  <<entryPoint>>
state "(START_AT) 值为空(Nil)" as 445a4613d8c2d80fbb7959dd1eec3b4f [[$./start_at#a445a4613d8c2d80fbb7959dd1eec3b4f {"[常规条件] 值为空(Nil)"}]]
state "[条件组]OR" as df36e2799a8ae1babf47d75e8c6eaeec [[$./start_at#adf36e2799a8ae1babf47d75e8c6eaeec {"[条件组]OR"}]] {
state " " as df36e2799a8ae1babf47d75e8c6eaeec_entry  <<entryPoint>>
state "(END_AT) 值为空(Nil)" as 57ef74a0960811354d578d1996054417 [[$./start_at#a57ef74a0960811354d578d1996054417 {"[常规条件] 值为空(Nil)"}]]
state "(START_AT) 小于等于(<=) 数据对象属性 (END_AT)" as 121847da24caff37501429ed0f67480e [[$./start_at#a121847da24caff37501429ed0f67480e {"[常规条件] 小于等于(<=) 数据对象属性 (END_AT)"}]]
state " " as df36e2799a8ae1babf47d75e8c6eaeec_exit  <<exitPoint>>
}
state " " as 976d16116e8b7742ce0ef479d82a4809_exit  <<exitPoint>>
}


start --> 976d16116e8b7742ce0ef479d82a4809_entry 
976d16116e8b7742ce0ef479d82a4809_entry --> 445a4613d8c2d80fbb7959dd1eec3b4f 
445a4613d8c2d80fbb7959dd1eec3b4f --> 976d16116e8b7742ce0ef479d82a4809_exit  : yes
445a4613d8c2d80fbb7959dd1eec3b4f -[#red]-> df36e2799a8ae1babf47d75e8c6eaeec_entry  : no

df36e2799a8ae1babf47d75e8c6eaeec_entry --> 57ef74a0960811354d578d1996054417 
57ef74a0960811354d578d1996054417 --> df36e2799a8ae1babf47d75e8c6eaeec_exit  : yes
57ef74a0960811354d578d1996054417 -[#red]-> 121847da24caff37501429ed0f67480e  : no

121847da24caff37501429ed0f67480e --> df36e2799a8ae1babf47d75e8c6eaeec_exit  : yes
121847da24caff37501429ed0f67480e -[#red]-> end  : no
df36e2799a8ae1babf47d75e8c6eaeec_exit --> 976d16116e8b7742ce0ef479d82a4809_exit 
976d16116e8b7742ce0ef479d82a4809_exit --> end 


@enduml
```

#### 条件说明

##### (START_AT) 小于等于(<=) 数据对象属性 (END_AT) :id=a121847da24caff37501429ed0f67480e



`START_AT(开始时间)` LTANDEQ  `END_AT`

> [!ATTENTION|label:规则信息|icon:fa fa-warning]
> 开始时间必须小于等于结束时间


##### (START_AT) 值为空(Nil) :id=a445a4613d8c2d80fbb7959dd1eec3b4f



`START_AT(开始时间)` ISNULL 

##### (END_AT) 值为空(Nil) :id=a57ef74a0960811354d578d1996054417



`END_AT(结束时间)` ISNULL 






