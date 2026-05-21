## 清空消息 <!-- {docsify-ignore-all} -->

   

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
state "开始" as Begin <<start>> [[$./clear_message#begin {"开始"}]]
state "获取会话" as DEACTION_01  [[$./clear_message#deaction_01 {"获取会话"}]]
state "直接SQL调用" as RAWSQLCALL_01  [[$./clear_message#rawsqlcall_01 {"直接SQL调用"}]]
state "结束" as END_01 <<end>> [[$./clear_message#end_01 {"结束"}]]


Begin --> DEACTION_01
DEACTION_01 --> RAWSQLCALL_01
RAWSQLCALL_01 --> END_01


@enduml
```


### 处理步骤说明

#### 开始 :id=Begin<sup class="footnote-symbol"> <font color=gray size=1>[开始]</font></sup>



*- N/A*
#### 获取会话 :id=DEACTION_01<sup class="footnote-symbol"> <font color=gray size=1>[实体行为]</font></sup>



调用实体 [智能体会话(AI_AGENT_CONVERSATION)](module/ai/ai_agent_conversation.md) 行为 [Get](module/ai/ai_agent_conversation#行为) ，行为参数为`Default(传入变量)`

将执行结果返回给参数`Default(传入变量)`

#### 直接SQL调用 :id=RAWSQLCALL_01<sup class="footnote-symbol"> <font color=gray size=1>[直接SQL调用]</font></sup>



<p class="panel-title"><b>执行sql语句</b></p>

```sql
DELETE FROM AI_AGENT_MESSAGE WHERE CONVERSATION_ID IN (SELECT ID FROM AI_AGENT_CONVERSATION WHERE SESSION_ID = ?);
DELETE  FROM AI_AGENT_FEEDBACK WHERE CONVERSATION_ID = ? ;

```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).SESSION_ID(外部会话ID)`
2. `Default(传入变量).ID(标识)`


#### 结束 :id=END_01<sup class="footnote-symbol"> <font color=gray size=1>[结束]</font></sup>



*- N/A*



### 实体逻辑参数

|    中文名   |    代码名    |  数据类型    |  实体   |备注 |
| --------| --------| -------- | -------- | --------   |
|传入变量(<i class="fa fa-check"/></i>)|Default|数据对象|[智能体会话(AI_AGENT_CONVERSATION)](module/ai/ai_agent_conversation.md)||
