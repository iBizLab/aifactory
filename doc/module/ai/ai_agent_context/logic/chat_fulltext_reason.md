## 交谈全文内容推理 <!-- {docsify-ignore-all} -->

   

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
state "开始" as Begin <<start>> [[$./chat_fulltext_reason#begin {"开始"}]]
state "绑定参数" as BINDPARAM_01  [[$./chat_fulltext_reason#bindparam_01 {"绑定参数"}]]
state "查询智能体" as DELOGIC_02  [[$./chat_fulltext_reason#delogic_02 {"查询智能体"}]]
state "设置筛选条件" as PREPAREPARAM_01  [[$./chat_fulltext_reason#prepareparam_01 {"设置筛选条件"}]]
state "查询知识库文档" as SYSAICHATAGENT_CHATSTEP_01  [[$./chat_fulltext_reason#sysaichatagent_chatstep_01 {"查询知识库文档"}]]
state "准备知识库标识" as PREPAREPARAM_06  [[$./chat_fulltext_reason#prepareparam_06 {"准备知识库标识"}]]
state "设置智能体代码标识" as PREPAREPARAM_07  [[$./chat_fulltext_reason#prepareparam_07 {"设置智能体代码标识"}]]
state "输出合并后大内容" as DEBUGPARAM_03  [[$./chat_fulltext_reason#debugparam_03 {"输出合并后大内容"}]]
state "查询知识库下文档" as DEDATASET_01  [[$./chat_fulltext_reason#dedataset_01 {"查询知识库下文档"}]]
state "准备文档正文" as RAWSFCODE_03  [[$./chat_fulltext_reason#rawsfcode_03 {"准备文档正文"}]]
state "输出大内容拆分集合" as DEBUGPARAM_04  [[$./chat_fulltext_reason#debugparam_04 {"输出大内容拆分集合"}]]
state "查询知识库详情" as DELOGIC_01  [[$./chat_fulltext_reason#delogic_01 {"查询知识库详情"}]]
state "将大内容拆分" as RAWSFCODE_05  [[$./chat_fulltext_reason#rawsfcode_05 {"将大内容拆分"}]]
state "重新建立参数" as RENEWPARAM_04  [[$./chat_fulltext_reason#renewparam_04 {"重新建立参数"}]]
state "逐一开始审查" as SYSAICHATAGENT_CHATSTEP_02  [[$./chat_fulltext_reason#sysaichatagent_chatstep_02 {"逐一开始审查"}]]
state "结果过多再次分段审查" as DEBUGPARAM_05  [[$./chat_fulltext_reason#debugparam_05 {"结果过多再次分段审查"}]]
state "重新建立交谈请求" as RENEWPARAM_01  [[$./chat_fulltext_reason#renewparam_01 {"重新建立交谈请求"}]]
state "内容总结" as SYSAICHATAGENT_CHATSTEP_04  [[$./chat_fulltext_reason#sysaichatagent_chatstep_04 {"内容总结"}]]
state "重新建立交谈输出" as RENEWPARAM_02  [[$./chat_fulltext_reason#renewparam_02 {"重新建立交谈输出"}]]
state "置空知识库标识" as PREPAREPARAM_03  [[$./chat_fulltext_reason#prepareparam_03 {"置空知识库标识"}]]
state "获取知识库文档推理结果" as RAWSFCODE_01  [[$./chat_fulltext_reason#rawsfcode_01 {"获取知识库文档推理结果"}]]
state "只有一条无需总结" as DEBUGPARAM_06  [[$./chat_fulltext_reason#debugparam_06 {"只有一条无需总结"}]]
state "重新建立参数" as RENEWPARAM_03  [[$./chat_fulltext_reason#renewparam_03 {"重新建立参数"}]]
state "待总结片段" as DEBUGPARAM_07  [[$./chat_fulltext_reason#debugparam_07 {"待总结片段"}]]
state "设置全文推理结果审查报告" as PREPAREPARAM_05  [[$./chat_fulltext_reason#prepareparam_05 {"设置全文推理结果审查报告"}]]
state "附加聊天请求" as SYSAICHATAGENT_APPENDCHATREQUEST_01  [[$./chat_fulltext_reason#sysaichatagent_appendchatrequest_01 {"附加聊天请求"}]]
state "交谈输出" as SYSAICHATAGENT_CHATOUTPUT_01  [[$./chat_fulltext_reason#sysaichatagent_chatoutput_01 {"交谈输出"}]]
state "创建审查报告" as DEACTION_03  [[$./chat_fulltext_reason#deaction_03 {"创建审查报告"}]]
state "准备参数总结智能体" as PREPAREPARAM_010  [[$./chat_fulltext_reason#prepareparam_010 {"准备参数总结智能体"}]]
state "全文推理完成" as SYSAICHATAGENT_CHATSTEP_03  [[$./chat_fulltext_reason#sysaichatagent_chatstep_03 {"全文推理完成"}]]
state "交谈输出" as SYSAICHATAGENT_CHATOUTPUT_03  [[$./chat_fulltext_reason#sysaichatagent_chatoutput_03 {"交谈输出"}]]
state "准备参数" as PREPAREPARAM_011  [[$./chat_fulltext_reason#prepareparam_011 {"准备参数"}]]
state "查询知识库详情" as DEACTION_04  [[$./chat_fulltext_reason#deaction_04 {"查询知识库详情"}]]
state "结束" as END_01 <<end>> [[$./chat_fulltext_reason#end_01 {"结束"}]]
state "循环子调用" as LOOPSUBCALL_02  [[$./chat_fulltext_reason#loopsubcall_02 {"循环子调用"}]] #green {
state "调试逻辑参数" as DEBUGPARAM_01  [[$./chat_fulltext_reason#debugparam_01 {"调试逻辑参数"}]]
state "设置交谈参数" as PREPAREPARAM_09  [[$./chat_fulltext_reason#prepareparam_09 {"设置交谈参数"}]]
state "附加聊天请求" as SYSAICHATAGENT_APPENDCHATREQUEST_02  [[$./chat_fulltext_reason#sysaichatagent_appendchatrequest_02 {"附加聊天请求"}]]
state "交谈输出" as SYSAICHATAGENT_CHATOUTPUT_02  [[$./chat_fulltext_reason#sysaichatagent_chatoutput_02 {"交谈输出"}]]
state "回填交谈结果" as PREPAREPARAM_08  [[$./chat_fulltext_reason#prepareparam_08 {"回填交谈结果"}]]
state "将交谈结果附加到数组" as APPENDPARAM_03  [[$./chat_fulltext_reason#appendparam_03 {"将交谈结果附加到数组"}]]
}


Begin --> BINDPARAM_01
BINDPARAM_01 --> SYSAICHATAGENT_CHATSTEP_01
SYSAICHATAGENT_CHATSTEP_01 --> PREPAREPARAM_06
PREPAREPARAM_06 --> DELOGIC_01
DELOGIC_01 --> PREPAREPARAM_07
PREPAREPARAM_07 --> DELOGIC_02
DELOGIC_02 --> PREPAREPARAM_01
PREPAREPARAM_01 --> DEDATASET_01
DEDATASET_01 --> RAWSFCODE_03
RAWSFCODE_03 --> DEBUGPARAM_03
DEBUGPARAM_03 --> RAWSFCODE_05
RAWSFCODE_05 --> DEBUGPARAM_04
DEBUGPARAM_04 --> SYSAICHATAGENT_CHATSTEP_02
SYSAICHATAGENT_CHATSTEP_02 --> RENEWPARAM_04
RENEWPARAM_04 --> LOOPSUBCALL_02
LOOPSUBCALL_02 --> DEBUGPARAM_01
DEBUGPARAM_01 --> PREPAREPARAM_09
PREPAREPARAM_09 --> SYSAICHATAGENT_APPENDCHATREQUEST_02
SYSAICHATAGENT_APPENDCHATREQUEST_02 --> SYSAICHATAGENT_CHATOUTPUT_02
SYSAICHATAGENT_CHATOUTPUT_02 --> PREPAREPARAM_08
PREPAREPARAM_08 --> APPENDPARAM_03
LOOPSUBCALL_02 --> SYSAICHATAGENT_CHATSTEP_04
SYSAICHATAGENT_CHATSTEP_04 --> RAWSFCODE_01
RAWSFCODE_01 --> PREPAREPARAM_03 : [[$./chat_fulltext_reason#rawsfcode_01-prepareparam_03{连接名称} 连接名称]]
PREPAREPARAM_03 --> DEBUGPARAM_07
DEBUGPARAM_07 --> SYSAICHATAGENT_APPENDCHATREQUEST_01
SYSAICHATAGENT_APPENDCHATREQUEST_01 --> SYSAICHATAGENT_CHATOUTPUT_01 : [[$./chat_fulltext_reason#sysaichatagent_appendchatrequest_01-sysaichatagent_chatoutput_01{连接名称} 连接名称]]
SYSAICHATAGENT_CHATOUTPUT_01 --> PREPAREPARAM_011
SYSAICHATAGENT_APPENDCHATREQUEST_01 --> PREPAREPARAM_010 : [[$./chat_fulltext_reason#sysaichatagent_appendchatrequest_01-prepareparam_010{连接名称} 连接名称]]
PREPAREPARAM_010 --> SYSAICHATAGENT_CHATOUTPUT_03
SYSAICHATAGENT_CHATOUTPUT_03 --> PREPAREPARAM_011
RAWSFCODE_01 --> DEBUGPARAM_06 : [[$./chat_fulltext_reason#rawsfcode_01-debugparam_06{连接名称} 连接名称]]
DEBUGPARAM_06 --> PREPAREPARAM_05
PREPAREPARAM_05 --> DEACTION_03
DEACTION_03 --> SYSAICHATAGENT_CHATSTEP_03
SYSAICHATAGENT_CHATSTEP_03 --> END_01
RAWSFCODE_01 --> DEBUGPARAM_05 : [[$./chat_fulltext_reason#rawsfcode_01-debugparam_05{连接名称} 连接名称]]
DEBUGPARAM_05 --> RAWSFCODE_05


@enduml
```


### 处理步骤说明

#### 开始 :id=Begin<sup class="footnote-symbol"> <font color=gray size=1>[开始]</font></sup>



*- N/A*
#### 查询知识库文档 :id=SYSAICHATAGENT_CHATSTEP_01<sup class="footnote-symbol"> <font color=gray size=1>[SYSAICHATAGENT_CHATSTEP]</font></sup>




#### 绑定参数 :id=BINDPARAM_01<sup class="footnote-symbol"> <font color=gray size=1>[绑定参数]</font></sup>



绑定参数`Default(传入变量)` 到 `default_temp`
#### 查询知识库详情 :id=DELOGIC_01<sup class="footnote-symbol"> <font color=gray size=1>[实体逻辑]</font></sup>



调用实体 [知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base.md) 处理逻辑 [get_by_code]((module/ai/ai_knowledge_base/logic/get_by_code.md)) ，行为参数为`kb(kb)`
将执行结果返回给参数`kb(kb)`

#### 查询知识库详情 :id=DEACTION_04<sup class="footnote-symbol"> <font color=gray size=1>[实体行为]</font></sup>



调用实体 [知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base.md) 行为 [Get](module/ai/ai_knowledge_base#行为) ，行为参数为`kb`

将执行结果返回给参数`kb`

#### 准备知识库标识 :id=PREPAREPARAM_06<sup class="footnote-symbol"> <font color=gray size=1>[准备参数]</font></sup>



1. 将`default_temp.knowledgebases` 设置给  `kb.ID(智能体业务上下文标识)`

#### 设置筛选条件 :id=PREPAREPARAM_01<sup class="footnote-symbol"> <font color=gray size=1>[准备参数]</font></sup>



1. 将`kb.ID(智能体业务上下文标识)` 设置给  `doc_filter(文档筛选条件).n_kb_id_eq`
2. 将`1000` 设置给  `doc_filter(文档筛选条件).size(内容大小)`

#### 查询智能体 :id=DELOGIC_02<sup class="footnote-symbol"> <font color=gray size=1>[实体逻辑]</font></sup>



调用实体 [智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context.md) 处理逻辑 [get_by_code]((module/ai/ai_agent_context/logic/get_by_code.md)) ，行为参数为`agent(agent)`
将执行结果返回给参数`agent(agent)`

#### 设置智能体代码标识 :id=PREPAREPARAM_07<sup class="footnote-symbol"> <font color=gray size=1>[准备参数]</font></sup>



1. 将`default_temp.srfaiagenttag` 设置给  `agent.CODE_NAME(代码标识)`

#### 查询知识库下文档 :id=DEDATASET_01<sup class="footnote-symbol"> <font color=gray size=1>[实体数据集]</font></sup>



调用实体 [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document.md) 数据集合 [DEFAULT](module/ai/ai_kb_document#数据集合) ，查询参数为`doc_filter(文档筛选条件)`

将执行结果返回给参数`doc_list(文档查询列表)`

#### 准备文档正文 :id=RAWSFCODE_03<sup class="footnote-symbol"> <font color=gray size=1>[直接后台代码]</font></sup>



<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
        def _doc_list = logic.param("doc_list").getReal();
        def kb_doc_runtime = sys.dataentity('ai_kb_document')
        def _doc_fulltext = logic.param("doc_fulltext").getReal();

        _doc_fulltext.clear()
        
        _doc_list.each { doc ->
            def text = kb_doc_runtime.executeAction("get_full_text", null, doc)
            _doc_fulltext.add( [
                    name: (doc.get("categories") ? (doc.get("categories") + "/") : "") + doc.get("name"),
                    content: text ?: ""
            ]
            )
        }


```

#### 输出合并后大内容 :id=DEBUGPARAM_03<sup class="footnote-symbol"> <font color=gray size=1>[调试逻辑参数]</font></sup>



> [!NOTE|label:调试信息|icon:fa fa-bug]
> 调试输出参数`doc_fulltext`的详细信息


#### 重新建立参数 :id=RENEWPARAM_04<sup class="footnote-symbol"> <font color=gray size=1>[重新建立参数]</font></sup>



重建参数```chunk_reason_list(chunk_reason_list)```
#### 逐一开始审查 :id=SYSAICHATAGENT_CHATSTEP_02<sup class="footnote-symbol"> <font color=gray size=1>[SYSAICHATAGENT_CHATSTEP]</font></sup>




#### 输出大内容拆分集合 :id=DEBUGPARAM_04<sup class="footnote-symbol"> <font color=gray size=1>[调试逻辑参数]</font></sup>



> [!NOTE|label:调试信息|icon:fa fa-bug]
> 调试输出参数`fulltext_chunk_list`的详细信息


#### 将大内容拆分 :id=RAWSFCODE_05<sup class="footnote-symbol"> <font color=gray size=1>[直接后台代码]</font></sup>



<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
        def processedDocs = logic.param("doc_fulltext").getReal();
        
        def splitContent
        splitContent = { String text, int limit ->
            def res = []
            def start = 0
            while (start < text.length()) {
                int end = Math.min(start + limit, text.length())
                // 尽量找换行符切分，避免切断句子
                if (end < text.length()) {
                    int lastNewline = text.lastIndexOf("\n", end)
                    if (lastNewline > start) end = lastNewline
                }
                res << text.substring(start, end).trim()
                start = end
            }
            return res
        }


        def MAX_CHARS = 25600
        def allGroups = []
        def currentGroup = []
        def currentGroupSize = 0

        def flatFragments = []

        processedDocs.each { doc ->

            def content = doc.content
            def docName = doc.name

            if (content.length() > MAX_CHARS) {
                // 超大文档：切分成多个虚拟片段对象
                def parts = splitContent(content, MAX_CHARS)
                parts.eachWithIndex { text, index ->
                    flatFragments << [name: docName, content: text, part: index + 1]
                }
            } else {
                // 普通文档
                flatFragments << [name: docName, content: content, part: null]
            }
        }

        flatFragments.each { frag ->
            if (currentGroupSize + frag.content.length() > MAX_CHARS) {
                if (currentGroup) {
                    allGroups << currentGroup
                }
                currentGroup = [frag]
                currentGroupSize = frag.content.length()
            } else {
                currentGroup << frag
                currentGroupSize += frag.content.length()
            }
        }
        if (currentGroup) allGroups << currentGroup

        def chunks = logic.param("fulltext_chunk_list").getReal();

        chunks.clear()

        int sn = 1
        allGroups.each { group ->
            chunks << [sn: sn++, content:
                group.collect { item ->
                    def partAttr = item.part ? " part=\"${item.part}\"" : ""
                    "<doc name=\"${item.name}\"${partAttr}>\n${item.content}\n</doc>"
                }.join("\n\n")
            ]
        }

        processedDocs.clear()
```

#### 结果过多再次分段审查 :id=DEBUGPARAM_05<sup class="footnote-symbol"> <font color=gray size=1>[调试逻辑参数]</font></sup>



> [!NOTE|label:调试信息|icon:fa fa-bug]
> 调试输出参数`doc_fulltext`的详细信息


#### 重新建立交谈请求 :id=RENEWPARAM_01<sup class="footnote-symbol"> <font color=gray size=1>[重新建立参数]</font></sup>



重建参数```chat_request(chat_request)```
#### 设置交谈参数 :id=PREPAREPARAM_09<sup class="footnote-symbol"> <font color=gray size=1>[准备参数]</font></sup>



1. 将`null` 重新建立为  `chat_request`
2. 将`null` 重新建立为  `chat_response`
3. 将`null` 重新建立为  `chunk_reason`
4. 将`空值（NULL）` 设置给  `chat_request.knowledgebases`
5. 将`agent.CODE_NAME(代码标识)` 设置给  `chat_request.srfaiagenttag`

#### 调试逻辑参数 :id=DEBUGPARAM_01<sup class="footnote-symbol"> <font color=gray size=1>[调试逻辑参数]</font></sup>



> [!NOTE|label:调试信息|icon:fa fa-bug]
> 调试输出参数`text_chunk`的详细信息


#### 循环子调用 :id=LOOPSUBCALL_02<sup class="footnote-symbol"> <font color=gray size=1>[循环子调用]</font></sup>



循环参数`fulltext_chunk_list`，子循环参数使用`text_chunk`
#### 内容总结 :id=SYSAICHATAGENT_CHATSTEP_04<sup class="footnote-symbol"> <font color=gray size=1>[SYSAICHATAGENT_CHATSTEP]</font></sup>




#### 重新建立交谈输出 :id=RENEWPARAM_02<sup class="footnote-symbol"> <font color=gray size=1>[重新建立参数]</font></sup>



重建参数```chat_response(chat_response)```
#### 置空知识库标识 :id=PREPAREPARAM_03<sup class="footnote-symbol"> <font color=gray size=1>[准备参数]</font></sup>



1. 将`空值（NULL）` 设置给  `textreason_chat_request.knowledgebases`
2. 将`null` 重新建立为  `textreason_chat_request`
3. 将`null` 重新建立为  `textreason_chat_response`

#### 获取知识库文档推理结果 :id=RAWSFCODE_01<sup class="footnote-symbol"> <font color=gray size=1>[直接后台代码]</font></sup>



<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
def _all_reason_content = logic.param("all_reason_content").getReal();
def _doc_reason_list = logic.param("chunk_reason_list").getReal();

def _fullcontent_reason_report = logic.param("fullcontent_reason_report").getReal();
_all_reason_content.set('fullcontent',null)


if(_doc_reason_list.size()==1) {
    _fullcontent_reason_report.set("review_report", _doc_reason_list.get(0).content)
}
      
def allContent = _doc_reason_list.collect { item ->
    def content = item.content ?: ''
"""\
# 分段结果：
```
${item.content}
```
---\
"""
}.join('\n\n')

int retry = 0
if(_all_reason_content.get("retry"))
    retry = _all_reason_content.get("retry")

if(allContent.length()<25600)  {
    _all_reason_content.set('fullcontent',allContent)
    println "------------------------allContent：" + allContent
}
else if(retry<3){
        def _doc_fulltext = logic.param("doc_fulltext").getReal();
        retry = retry +1
        _all_reason_content.set("retry", retry)
        println "------------------------allContent 过大再次分段审查：" + allContent

        _doc_fulltext.clear()
        
        _doc_reason_list.each { item ->
            
            _doc_fulltext.add( [
                    name: "分段结果",
                    content: item.content ?: ''
            ]
            )
        }
    
}
else {
        _fullcontent_reason_report.set("review_report", allContent)
        println "------------------------重试分段审查3次 allContent 仍过大，直接保存报告：" + allContent
}



```

#### 只有一条无需总结 :id=DEBUGPARAM_06<sup class="footnote-symbol"> <font color=gray size=1>[调试逻辑参数]</font></sup>



> [!NOTE|label:调试信息|icon:fa fa-bug]
> 调试输出参数`fullcontent_reason_report`的详细信息


#### 附加聊天请求 :id=SYSAICHATAGENT_APPENDCHATREQUEST_02<sup class="footnote-symbol"> <font color=gray size=1>[SYSAICHATAGENT_APPENDCHATREQUEST]</font></sup>




#### 重新建立参数 :id=RENEWPARAM_03<sup class="footnote-symbol"> <font color=gray size=1>[重新建立参数]</font></sup>



重建参数```chunk_reason(chunk_reason)```
#### 待总结片段 :id=DEBUGPARAM_07<sup class="footnote-symbol"> <font color=gray size=1>[调试逻辑参数]</font></sup>



> [!NOTE|label:调试信息|icon:fa fa-bug]
> 调试输出参数`chunk_reason_list`的详细信息


#### 交谈输出 :id=SYSAICHATAGENT_CHATOUTPUT_02<sup class="footnote-symbol"> <font color=gray size=1>[SYSAICHATAGENT_CHATOUTPUT]</font></sup>




#### 设置全文推理结果审查报告 :id=PREPAREPARAM_05<sup class="footnote-symbol"> <font color=gray size=1>[准备参数]</font></sup>



1. 将`kb.ID(智能体业务上下文标识)` 设置给  `fullcontent_reason_report.KB_ID(知识库标识)`
2. 将`Default(传入变量).srfaiagenttag` 设置给  `fullcontent_reason_report.AGENT_TAG(智能体标记)`
3. 将`kb.NAME(名称)` 设置给  `fullcontent_reason_report.NAME(审查对象)`
4. 将`all_reason_content.fullcontent` 设置给  `fullcontent_reason_report.CHECK_INFO(校验信息)`
5. 将`all_reason_content.retry` 设置给  `fullcontent_reason_report.REVIEW_RESULT(审查结果)`

#### 附加聊天请求 :id=SYSAICHATAGENT_APPENDCHATREQUEST_01<sup class="footnote-symbol"> <font color=gray size=1>[SYSAICHATAGENT_APPENDCHATREQUEST]</font></sup>




#### 交谈输出 :id=SYSAICHATAGENT_CHATOUTPUT_01<sup class="footnote-symbol"> <font color=gray size=1>[SYSAICHATAGENT_CHATOUTPUT]</font></sup>




#### 回填交谈结果 :id=PREPAREPARAM_08<sup class="footnote-symbol"> <font color=gray size=1>[准备参数]</font></sup>



1. 将`chat_response.content` 设置给  `chunk_reason.content`
2. 将`chat_response` 拷贝到  `final_chat_response`

#### 创建审查报告 :id=DEACTION_03<sup class="footnote-symbol"> <font color=gray size=1>[实体行为]</font></sup>



调用实体 [智能审查报告(AI_REVIEW_REPORT)](module/ai/ai_review_report.md) 行为 [upsert](module/ai/ai_review_report#行为) ，行为参数为`fullcontent_reason_report`

将执行结果返回给参数`fullcontent_reason_report`

#### 准备参数总结智能体 :id=PREPAREPARAM_010<sup class="footnote-symbol"> <font color=gray size=1>[准备参数]</font></sup>



1. 将`agent.SYNTHESIZER(总结智能体)` 设置给  `textreason_chat_request.srfaiagenttag`

#### 将交谈结果附加到数组 :id=APPENDPARAM_03<sup class="footnote-symbol"> <font color=gray size=1>[附加到数组参数]</font></sup>



将参数`chunk_reason` 添加到数组参数`chunk_reason_list`
#### 全文推理完成 :id=SYSAICHATAGENT_CHATSTEP_03<sup class="footnote-symbol"> <font color=gray size=1>[SYSAICHATAGENT_CHATSTEP]</font></sup>




#### 交谈输出 :id=SYSAICHATAGENT_CHATOUTPUT_03<sup class="footnote-symbol"> <font color=gray size=1>[SYSAICHATAGENT_CHATOUTPUT]</font></sup>




#### 准备参数 :id=PREPAREPARAM_011<sup class="footnote-symbol"> <font color=gray size=1>[准备参数]</font></sup>



1. 将`textreason_chat_response.content` 设置给  `fullcontent_reason_report.REVIEW_REPORT(报告)`
2. 将`textreason_chat_response` 拷贝到  `final_chat_response`

#### 结束 :id=END_01<sup class="footnote-symbol"> <font color=gray size=1>[结束]</font></sup>



返回 `final_chat_response`


### 连接条件说明
#### 连接名称 :id=RAWSFCODE_01-PREPAREPARAM_03

`fullcontent_reason_report(fullcontent_reason_report).REVIEW_REPORT(报告)` ISNULL AND `all_reason_content(all_reason_content).fullcontent` ISNOTNULL
#### 连接名称 :id=SYSAICHATAGENT_APPENDCHATREQUEST_01-SYSAICHATAGENT_CHATOUTPUT_01

`agent(agent).SYNTHESIZER(总结智能体)` ISNULL
#### 连接名称 :id=SYSAICHATAGENT_APPENDCHATREQUEST_01-PREPAREPARAM_010

`agent(agent).SYNTHESIZER(总结智能体)` ISNOTNULL
#### 连接名称 :id=RAWSFCODE_01-DEBUGPARAM_06

`fullcontent_reason_report(fullcontent_reason_report).REVIEW_REPORT(报告)` ISNOTNULL
#### 连接名称 :id=RAWSFCODE_01-DEBUGPARAM_05

`doc_fulltext(doc_fulltext).size` GT `0` AND `all_reason_content(all_reason_content).fullcontent` ISNULL


### 实体逻辑参数

|    中文名   |    代码名    |  数据类型    |  实体   |备注 |
| --------| --------| -------- | -------- | --------   |
|传入变量(<i class="fa fa-check"/></i>)|Default||||
|agent|agent|数据对象|[智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context.md)||
|all_reason_content|all_reason_content|数据对象|||
|chat_request|chat_request||||
|chat_response|chat_response||||
|chunk_reason|chunk_reason|数据对象|||
|chunk_reason_list|chunk_reason_list|数据对象列表|||
|default_temp|default_temp|数据对象|[智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context.md)||
|doc|doc|数据对象|[知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document.md)||
|文档筛选条件|doc_filter|过滤器|||
|doc_fulltext|doc_fulltext|数据对象列表|||
|文档查询列表|doc_list|分页查询|||
|doc_reason_list|doc_reason_list|数据对象列表|[智能审查报告(AI_REVIEW_REPORT)](module/ai/ai_review_report.md)||
|final_chat_response|final_chat_response||||
|full_doc_list|full_doc_list|数据对象列表|[知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document.md)||
|fullcontent_reason_report|fullcontent_reason_report|数据对象|[智能审查报告(AI_REVIEW_REPORT)](module/ai/ai_review_report.md)||
|fulltext_chunk_list|fulltext_chunk_list|数据对象列表|||
|kb|kb|数据对象|[智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context.md)||
|obj|obj|数据对象|||
|refrence_chat_request|refrence_chat_request||||
|refrence_chat_response|refrence_chat_response||||
|report_doc|report_doc|数据对象|[智能审查报告(AI_REVIEW_REPORT)](module/ai/ai_review_report.md)||
|text_chunk|text_chunk|数据对象|||
|text_reason|text_reason|数据对象|[知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document.md)||
|textreason_chat_request|textreason_chat_request||||
|textreason_chat_response|textreason_chat_response||||
