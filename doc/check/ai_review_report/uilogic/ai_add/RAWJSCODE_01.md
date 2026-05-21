<p class="panel-title"><b>执行代码</b></p>

```javascript
console.info("ai callback");
//var formController = realView.getController("form");
var report_id = "";
var kb_id = "";
var kb_name = "";
var agent_code = "";
//var agent_name = "";
var report = "";
if(uiLogic.default.topic.aiChat && 
    uiLogic.default.topic.aiChat.appendCurData &&
    uiLogic.default.topic.aiChat.appendCurData.context_code_name) {
    agent_code = uiLogic.default.topic.aiChat.appendCurData.context_code_name;
    if(uiLogic.default.topic.aiChat.appendCurData.kb_id &&
    uiLogic.default.topic.aiChat.appendCurData.kb_name)
    {
        kb_id = uiLogic.default.topic.aiChat.appendCurData.kb_id;
        kb_name = uiLogic.default.topic.aiChat.appendCurData.kb_name;
    }
}
if(uiLogic.default.topic.aiChat && 
    uiLogic.default.topic.aiChat.params &&
    uiLogic.default.topic.aiChat.params.knowledgebases) {
    kb_id = uiLogic.default.topic.aiChat.params.knowledgebases;
}
if(uiLogic.default.msg &&
    uiLogic.default.msg.realcontent){
    report = uiLogic.default.msg.realcontent;
}
if(kb_id && agent_code){
    report_id = agent_code+kb_id;
}

uiLogic.kb = {};
uiLogic.kb.id = kb_id;

uiLogic.aireport = {};
uiLogic.aireport.id= report_id;
uiLogic.aireport.name= kb_name;
uiLogic.aireport.kb_id= kb_id;
uiLogic.aireport.agent_tag= agent_code;
uiLogic.aireport.review_report = report;

```
