## 结束时间(END_AT) <!-- {docsify-ignore-all} -->

   

### 结束时间 :id=END_AT

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
state "[条件组]OR" as e1aed87f79bfa4d0b2db03310f04c4b5 [[$./end_at#ae1aed87f79bfa4d0b2db03310f04c4b5 {"[条件组]OR"}]] {
state " " as e1aed87f79bfa4d0b2db03310f04c4b5_entry  <<entryPoint>>
state "(END_AT) 值为空(Nil)" as 91d545fdd58982e284dd1d63792d575c [[$./end_at#a91d545fdd58982e284dd1d63792d575c {"[常规条件] 值为空(Nil)"}]]
state "[条件组]OR" as ab53ab6c86933abfbfb19a6af534b334 [[$./end_at#aab53ab6c86933abfbfb19a6af534b334 {"[条件组]OR"}]] {
state " " as ab53ab6c86933abfbfb19a6af534b334_entry  <<entryPoint>>
state "(START_AT) 值为空(Nil)" as a86f995ce2fc547c412bd681a3dd18cf [[$./end_at#aa86f995ce2fc547c412bd681a3dd18cf {"[常规条件] 值为空(Nil)"}]]
state "(END_AT) 大于等于(>=) 数据对象属性 (START_AT)" as 2e0e1a38e58013075e2efcfa42e0452d [[$./end_at#a2e0e1a38e58013075e2efcfa42e0452d {"[常规条件] 大于等于(>=) 数据对象属性 (START_AT)"}]]
state " " as ab53ab6c86933abfbfb19a6af534b334_exit  <<exitPoint>>
}
state " " as e1aed87f79bfa4d0b2db03310f04c4b5_exit  <<exitPoint>>
}


start --> e1aed87f79bfa4d0b2db03310f04c4b5_entry 
e1aed87f79bfa4d0b2db03310f04c4b5_entry --> 91d545fdd58982e284dd1d63792d575c 
91d545fdd58982e284dd1d63792d575c --> e1aed87f79bfa4d0b2db03310f04c4b5_exit  : yes
91d545fdd58982e284dd1d63792d575c -[#red]-> ab53ab6c86933abfbfb19a6af534b334_entry  : no

ab53ab6c86933abfbfb19a6af534b334_entry --> a86f995ce2fc547c412bd681a3dd18cf 
a86f995ce2fc547c412bd681a3dd18cf --> ab53ab6c86933abfbfb19a6af534b334_exit  : yes
a86f995ce2fc547c412bd681a3dd18cf -[#red]-> 2e0e1a38e58013075e2efcfa42e0452d  : no

2e0e1a38e58013075e2efcfa42e0452d --> ab53ab6c86933abfbfb19a6af534b334_exit  : yes
2e0e1a38e58013075e2efcfa42e0452d -[#red]-> end  : no
ab53ab6c86933abfbfb19a6af534b334_exit --> e1aed87f79bfa4d0b2db03310f04c4b5_exit 
e1aed87f79bfa4d0b2db03310f04c4b5_exit --> end 


@enduml
```

#### 条件说明

##### (END_AT) 值为空(Nil) :id=a91d545fdd58982e284dd1d63792d575c



`END_AT(结束时间)` ISNULL 

##### (START_AT) 值为空(Nil) :id=aa86f995ce2fc547c412bd681a3dd18cf



`START_AT(开始时间)` ISNULL 

##### (END_AT) 大于等于(>=) 数据对象属性 (START_AT) :id=a2e0e1a38e58013075e2efcfa42e0452d



`END_AT(结束时间)` GTANDEQ  `START_AT`

> [!ATTENTION|label:规则信息|icon:fa fa-warning]
> 结束时间必须大于等于开始时间







