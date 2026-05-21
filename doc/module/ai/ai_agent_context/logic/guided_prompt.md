## 辅助生成引导提示词（停用） <!-- {docsify-ignore-all} -->

   

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
state "开始" as Begin <<start>> [[$./guided_prompt#begin {"开始"}]]
state "默认交谈" as SYSAICHATAGENT_CHATOUTPUT_02  [[$./guided_prompt#sysaichatagent_chatoutput_02 {"默认交谈"}]]
state "问题分类" as SYSAICHATAGENT_CHATCATEGORY_02  [[$./guided_prompt#sysaichatagent_chatcategory_02 {"问题分类"}]]
state "交谈回复" as DEBUGPARAM_01  [[$./guided_prompt#debugparam_01 {"交谈回复"}]]
state "问题分类" as SYSAICHATAGENT_CHATCATEGORY_01  [[$./guided_prompt#sysaichatagent_chatcategory_01 {"问题分类"}]]
state "等待输入" as SYSAICHATAGENT_CHATINPUT_02  [[$./guided_prompt#sysaichatagent_chatinput_02 {"等待输入"}]]
state "结束" as END_01 <<end>> [[$./guided_prompt#end_01 {"结束"}]]
state "获取AI反馈信息" as RAWSFCODE_01  [[$./guided_prompt#rawsfcode_01 {"获取AI反馈信息"}]]
state "填充提示词" as SYSAICHATAGENT_CHATUIACTION_01  [[$./guided_prompt#sysaichatagent_chatuiaction_01 {"填充提示词"}]]
state "继续细化或采用当前提示词" as SYSAICHATAGENT_CHATINPUT_01  [[$./guided_prompt#sysaichatagent_chatinput_01 {"继续细化或采用当前提示词"}]]


Begin --> SYSAICHATAGENT_CHATOUTPUT_02
SYSAICHATAGENT_CHATOUTPUT_02 --> RAWSFCODE_01
RAWSFCODE_01 --> SYSAICHATAGENT_CHATINPUT_01
SYSAICHATAGENT_CHATINPUT_01 --> SYSAICHATAGENT_CHATCATEGORY_01
SYSAICHATAGENT_CHATCATEGORY_01 --> SYSAICHATAGENT_CHATUIACTION_01
SYSAICHATAGENT_CHATUIACTION_01 --> SYSAICHATAGENT_CHATINPUT_02
SYSAICHATAGENT_CHATINPUT_02 --> SYSAICHATAGENT_CHATCATEGORY_02
SYSAICHATAGENT_CHATCATEGORY_02 --> END_01
SYSAICHATAGENT_CHATCATEGORY_02 --> SYSAICHATAGENT_CHATOUTPUT_02
SYSAICHATAGENT_CHATCATEGORY_01 --> SYSAICHATAGENT_CHATOUTPUT_02


@enduml
```


### 处理步骤说明

#### 开始 :id=Begin<sup class="footnote-symbol"> <font color=gray size=1>[开始]</font></sup>



*- N/A*
#### 默认交谈 :id=SYSAICHATAGENT_CHATOUTPUT_02<sup class="footnote-symbol"> <font color=gray size=1>[SYSAICHATAGENT_CHATOUTPUT]</font></sup>




#### 问题分类 :id=SYSAICHATAGENT_CHATCATEGORY_02<sup class="footnote-symbol"> <font color=gray size=1>[SYSAICHATAGENT_CHATCATEGORY]</font></sup>




#### 交谈回复 :id=DEBUGPARAM_01<sup class="footnote-symbol"> <font color=gray size=1>[调试逻辑参数]</font></sup>



> [!NOTE|label:调试信息|icon:fa fa-bug]
> 调试输出参数`chat_response(AI交谈反馈)`的详细信息


#### 问题分类 :id=SYSAICHATAGENT_CHATCATEGORY_01<sup class="footnote-symbol"> <font color=gray size=1>[SYSAICHATAGENT_CHATCATEGORY]</font></sup>




#### 等待输入 :id=SYSAICHATAGENT_CHATINPUT_02<sup class="footnote-symbol"> <font color=gray size=1>[SYSAICHATAGENT_CHATINPUT]</font></sup>




#### 结束 :id=END_01<sup class="footnote-symbol"> <font color=gray size=1>[结束]</font></sup>



返回 `chat_response(AI交谈反馈)`

#### 获取AI反馈信息 :id=RAWSFCODE_01<sup class="footnote-symbol"> <font color=gray size=1>[直接后台代码]</font></sup>



<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
def chat_response = logic.param('chat_response').getReal()
def lastcontent = logic.param('lastcontent').getReal()

if (chat_response?.choices) {
    lastcontent = chat_response.choices.last().content
}
```

#### 填充提示词 :id=SYSAICHATAGENT_CHATUIACTION_01<sup class="footnote-symbol"> <font color=gray size=1>[SYSAICHATAGENT_CHATUIACTION]</font></sup>




#### 继续细化或采用当前提示词 :id=SYSAICHATAGENT_CHATINPUT_01<sup class="footnote-symbol"> <font color=gray size=1>[SYSAICHATAGENT_CHATINPUT]</font></sup>






### 实体逻辑参数

|    中文名   |    代码名    |  数据类型    |  实体   |备注 |
| --------| --------| -------- | -------- | --------   |
|传入变量(<i class="fa fa-check"/></i>)|Default||||
|AI交谈反馈|chat_response||||
|lastcontent|lastcontent|简单数据|||
