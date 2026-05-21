## 创建智能体 <!-- {docsify-ignore-all} -->

   

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
state "开始" as Begin <<start>> [[$./create_ai_agent_context#begin {"开始"}]]
state "输出default参数" as DEBUGPARAM_01  [[$./create_ai_agent_context#debugparam_01 {"输出default参数"}]]
state "附加聊天请求" as SYSAICHATAGENT_APPENDCHATREQUEST_01  [[$./create_ai_agent_context#sysaichatagent_appendchatrequest_01 {"附加聊天请求"}]]
state "交谈输出" as SYSAICHATAGENT_CHATOUTPUT_01  [[$./create_ai_agent_context#sysaichatagent_chatoutput_01 {"交谈输出"}]]
state "步骤消息" as SYSAICHATAGENT_CHATSTEP_01  [[$./create_ai_agent_context#sysaichatagent_chatstep_01 {"步骤消息"}]]
state "准备参数" as PREPAREPARAM_04  [[$./create_ai_agent_context#prepareparam_04 {"准备参数"}]]
state "交谈输出" as SYSAICHATAGENT_CHATOUTPUT_03  [[$./create_ai_agent_context#sysaichatagent_chatoutput_03 {"交谈输出"}]]
state "交谈输出" as SYSAICHATAGENT_CHATOUTPUT_02  [[$./create_ai_agent_context#sysaichatagent_chatoutput_02 {"交谈输出"}]]
state "问题分类" as SYSAICHATAGENT_CHATCATEGORY_03  [[$./create_ai_agent_context#sysaichatagent_chatcategory_03 {"问题分类"}]]
state "提取json" as PREPAREPARAM_01  [[$./create_ai_agent_context#prepareparam_01 {"提取json"}]]
state "路径选择" as SYSAICHATAGENT_CHATDECISION_01  [[$./create_ai_agent_context#sysaichatagent_chatdecision_01 {"路径选择"}]]
state "界面行为反馈" as SYSAICHATAGENT_CHATUIACTION_02  [[$./create_ai_agent_context#sysaichatagent_chatuiaction_02 {"界面行为反馈"}]]
state "附加聊天请求" as SYSAICHATAGENT_APPENDCHATREQUEST_02  [[$./create_ai_agent_context#sysaichatagent_appendchatrequest_02 {"附加聊天请求"}]]
state "获取智能体默认参数" as DEACTION_01  [[$./create_ai_agent_context#deaction_01 {"获取智能体默认参数"}]]
state "准备参数" as PREPAREPARAM_03  [[$./create_ai_agent_context#prepareparam_03 {"准备参数"}]]
state "步骤消息" as SYSAICHATAGENT_CHATSTEP_02  [[$./create_ai_agent_context#sysaichatagent_chatstep_02 {"步骤消息"}]]
state "创建异常" as SYSAICHATAGENT_CHATSTEP_03  [[$./create_ai_agent_context#sysaichatagent_chatstep_03 {"创建异常"}]]
state "建立智能体" as DEACTION_03  [[$./create_ai_agent_context#deaction_03 {"建立智能体"}]]
state "下一步或重新生成" as SYSAICHATAGENT_CHATINPUT_02  [[$./create_ai_agent_context#sysaichatagent_chatinput_02 {"下一步或重新生成"}]]
state "回写查看建立数据的按钮" as SYSAICHATAGENT_CHATUIACTION_01  [[$./create_ai_agent_context#sysaichatagent_chatuiaction_01 {"回写查看建立数据的按钮"}]]
state "写入错误信息" as PREPAREPARAM_02  [[$./create_ai_agent_context#prepareparam_02 {"写入错误信息"}]]
state "问题分类" as SYSAICHATAGENT_CHATCATEGORY_05  [[$./create_ai_agent_context#sysaichatagent_chatcategory_05 {"问题分类"}]]
state "等待输入" as SYSAICHATAGENT_CHATINPUT_04  [[$./create_ai_agent_context#sysaichatagent_chatinput_04 {"等待输入"}]]
state "步骤消息" as SYSAICHATAGENT_CHATSTEP_04  [[$./create_ai_agent_context#sysaichatagent_chatstep_04 {"步骤消息"}]]
state "结束" as END_01 <<end>> [[$./create_ai_agent_context#end_01 {"结束"}]]


Begin --> DEBUGPARAM_01
DEBUGPARAM_01 --> PREPAREPARAM_04
PREPAREPARAM_04 --> SYSAICHATAGENT_CHATOUTPUT_02
SYSAICHATAGENT_CHATOUTPUT_02 --> SYSAICHATAGENT_CHATUIACTION_02
SYSAICHATAGENT_CHATUIACTION_02 --> PREPAREPARAM_03
PREPAREPARAM_03 --> SYSAICHATAGENT_CHATDECISION_01
SYSAICHATAGENT_CHATDECISION_01 --> SYSAICHATAGENT_APPENDCHATREQUEST_01
SYSAICHATAGENT_APPENDCHATREQUEST_01 --> SYSAICHATAGENT_CHATOUTPUT_01
SYSAICHATAGENT_CHATOUTPUT_01 --> PREPAREPARAM_01
PREPAREPARAM_01 --> DEACTION_01
DEACTION_01 --> DEACTION_03
DEACTION_03 --> SYSAICHATAGENT_CHATUIACTION_01
SYSAICHATAGENT_CHATUIACTION_01 --> END_01
DEACTION_03 -[#red]-> PREPAREPARAM_02
PREPAREPARAM_02 --> SYSAICHATAGENT_CHATSTEP_03
SYSAICHATAGENT_CHATSTEP_03 --> SYSAICHATAGENT_APPENDCHATREQUEST_02
SYSAICHATAGENT_APPENDCHATREQUEST_02 --> SYSAICHATAGENT_CHATOUTPUT_03
SYSAICHATAGENT_CHATOUTPUT_03 --> PREPAREPARAM_01
SYSAICHATAGENT_CHATSTEP_03 -[#red]-> SYSAICHATAGENT_CHATSTEP_04
SYSAICHATAGENT_CHATSTEP_04 --> END_01
SYSAICHATAGENT_CHATDECISION_01 --> SYSAICHATAGENT_CHATOUTPUT_02


@enduml
```


### 处理步骤说明

#### 开始 :id=Begin<sup class="footnote-symbol"> <font color=gray size=1>[开始]</font></sup>



*- N/A*
#### 输出default参数 :id=DEBUGPARAM_01<sup class="footnote-symbol"> <font color=gray size=1>[调试逻辑参数]</font></sup>



> [!NOTE|label:调试信息|icon:fa fa-bug]
> 调试输出参数`Default(传入变量)`的详细信息


#### 附加聊天请求 :id=SYSAICHATAGENT_APPENDCHATREQUEST_01<sup class="footnote-symbol"> <font color=gray size=1>[SYSAICHATAGENT_APPENDCHATREQUEST]</font></sup>




#### 交谈输出 :id=SYSAICHATAGENT_CHATOUTPUT_01<sup class="footnote-symbol"> <font color=gray size=1>[SYSAICHATAGENT_CHATOUTPUT]</font></sup>




#### 步骤消息 :id=SYSAICHATAGENT_CHATSTEP_01<sup class="footnote-symbol"> <font color=gray size=1>[SYSAICHATAGENT_CHATSTEP]</font></sup>




#### 准备参数 :id=PREPAREPARAM_04<sup class="footnote-symbol"> <font color=gray size=1>[准备参数]</font></sup>



1. 将`Default(传入变量).srfextparams` 绑定给  `srfextparams`

#### 交谈输出 :id=SYSAICHATAGENT_CHATOUTPUT_03<sup class="footnote-symbol"> <font color=gray size=1>[SYSAICHATAGENT_CHATOUTPUT]</font></sup>




#### 交谈输出 :id=SYSAICHATAGENT_CHATOUTPUT_02<sup class="footnote-symbol"> <font color=gray size=1>[SYSAICHATAGENT_CHATOUTPUT]</font></sup>




#### 问题分类 :id=SYSAICHATAGENT_CHATCATEGORY_03<sup class="footnote-symbol"> <font color=gray size=1>[SYSAICHATAGENT_CHATCATEGORY]</font></sup>




#### 提取json :id=PREPAREPARAM_01<sup class="footnote-symbol"> <font color=gray size=1>[准备参数]</font></sup>



1. 将`chat_response(AI反馈).json` 绑定给  `ai_agent_context(智能体)`
2. 将`srfextparams.AI_AGENT_ID(智能体标识)` 设置给  `ai_agent_context(智能体).AI_AGENT_ID(智能体标识)`

#### 界面行为反馈 :id=SYSAICHATAGENT_CHATUIACTION_02<sup class="footnote-symbol"> <font color=gray size=1>[SYSAICHATAGENT_CHATUIACTION]</font></sup>

[{
"type": "raw",
  "data": {
    "content": "确认生成"
  },
  "metadata": {
   "content_name": "确认生成",
   "language": "zh-CN"
  }
}]


#### 路径选择 :id=SYSAICHATAGENT_CHATDECISION_01<sup class="footnote-symbol"> <font color=gray size=1>[SYSAICHATAGENT_CHATDECISION]</font></sup>




#### 附加聊天请求 :id=SYSAICHATAGENT_APPENDCHATREQUEST_02<sup class="footnote-symbol"> <font color=gray size=1>[SYSAICHATAGENT_APPENDCHATREQUEST]</font></sup>




#### 准备参数 :id=PREPAREPARAM_03<sup class="footnote-symbol"> <font color=gray size=1>[准备参数]</font></sup>




    无

#### 获取智能体默认参数 :id=DEACTION_01<sup class="footnote-symbol"> <font color=gray size=1>[实体行为]</font></sup>



调用实体 [智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context.md) 行为 [GetDraft](module/ai/ai_agent_context#行为) ，行为参数为`ai_agent_context(智能体)`

将执行结果返回给参数`ai_agent_context(智能体)`

#### 步骤消息 :id=SYSAICHATAGENT_CHATSTEP_02<sup class="footnote-symbol"> <font color=gray size=1>[SYSAICHATAGENT_CHATSTEP]</font></sup>




#### 创建异常 :id=SYSAICHATAGENT_CHATSTEP_03<sup class="footnote-symbol"> <font color=gray size=1>[SYSAICHATAGENT_CHATSTEP]</font></sup>




#### 建立智能体 :id=DEACTION_03<sup class="footnote-symbol"> <font color=gray size=1>[实体行为]</font></sup>



调用实体 [智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context.md) 行为 [Create](module/ai/ai_agent_context#行为) ，行为参数为`ai_agent_context(智能体)`

将执行结果返回给参数`ai_agent_context(智能体)`

#### 下一步或重新生成 :id=SYSAICHATAGENT_CHATINPUT_02<sup class="footnote-symbol"> <font color=gray size=1>[SYSAICHATAGENT_CHATINPUT]</font></sup>




#### 回写查看建立数据的按钮 :id=SYSAICHATAGENT_CHATUIACTION_01<sup class="footnote-symbol"> <font color=gray size=1>[SYSAICHATAGENT_CHATUIACTION]</font></sup>

[{
  "id": "open_edit_view",
  "type": "uiaction",
  "data": {
    "id": "open_edit_view",
    "uiaction_id": "open_edit_view@ai_agent_context",
    "de_name": "ai_agent_context"
  },
  "metadata": {
   "name": "打开建立的智能体",
   "actionContext": "ai_agent_context:${params.ai_agent_context.id}",
   "uiaction_id": "open_edit_view@ai_agent_context"
  }
}]


#### 写入错误信息 :id=PREPAREPARAM_02<sup class="footnote-symbol"> <font color=gray size=1>[准备参数]</font></sup>



1. 将`last_return` 设置给  `temp.error`

#### 问题分类 :id=SYSAICHATAGENT_CHATCATEGORY_05<sup class="footnote-symbol"> <font color=gray size=1>[SYSAICHATAGENT_CHATCATEGORY]</font></sup>




#### 等待输入 :id=SYSAICHATAGENT_CHATINPUT_04<sup class="footnote-symbol"> <font color=gray size=1>[SYSAICHATAGENT_CHATINPUT]</font></sup>




#### 步骤消息 :id=SYSAICHATAGENT_CHATSTEP_04<sup class="footnote-symbol"> <font color=gray size=1>[SYSAICHATAGENT_CHATSTEP]</font></sup>




#### 结束 :id=END_01<sup class="footnote-symbol"> <font color=gray size=1>[结束]</font></sup>



返回 `chat_response(AI反馈)`



### 实体逻辑参数

|    中文名   |    代码名    |  数据类型    |  实体   |备注 |
| --------| --------| -------- | -------- | --------   |
|传入变量(<i class="fa fa-check"/></i>)|Default||||
|智能体|ai_agent_context|数据对象|[智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context.md)||
|AI反馈|chat_response||||
|last_return|last_return|上一次调用返回|||
|srfextparams|srfextparams|数据对象|[智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context.md)||
|temp|temp|数据对象|||
