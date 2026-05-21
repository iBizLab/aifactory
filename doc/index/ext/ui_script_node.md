
## 使用脚本的界面逻辑节点<sup class="footnote-symbol"> <font color=orange>[95]</font></sup>

#### [智能体分配(AI_AGENT_ASSIGNMENT)](module/ai/ai_agent_assignment)的处理逻辑[run分配智能体逻辑(run)](module/ai/ai_agent_assignment/uilogic/run)

节点：注入脚本代码
<p class="panel-title"><b>执行代码</b></p>

```javascript
console.log("执行智能体");
 Object.assign(uiLogic.aicontext, uiLogic.default);
uiLogic.aicontext._name=uiLogic.aicontext.name;
uiLogic.aicontext.agent_name=uiLogic.aicontext.name;
uiLogic.aicontext.agent_description=uiLogic.aicontext.description;
uiLogic.aicontext.srfmajortext = uiLogic.aicontext.agent_name;
uiLogic.aicontext.name = null;
uiLogic.aicontext.description = null;

var context_content = "\n---\n\n* **执行智能体**: "+uiLogic.aicontext.agent_name +"\n";
if(uiLogic.aicontext.agent_description) {
    context_content = context_content+"* **智能体描述**: " + uiLogic.aicontext.agent_description+"\n";
}
context_content = context_content +"\n---\n";
uiLogic.aicontext.context_content=context_content;
// if(!uiLogic.aicontext.page_index) {
//     uiLogic.aicontext.page_index=0;
// }
const screenshot = uiLogic.aicontext.agent_description && uiLogic.aicontext.agent_description.indexOf("截图")>=0
uiLogic.context.ai_agent_context=uiLogic.aicontext.context_id;
if(view && view.parentView) {
    
    const appDataEntityId=view.parentView.model.appDataEntityId;
    if(appDataEntityId && appDataEntityId.indexOf(".")>0) {
        uiLogic.aicontext._entity_tag=appDataEntityId.split(".")[1];
        uiLogic.context._entity_tag=uiLogic.aicontext._entity_tag;
    }
    var contextObj = view.parentView.state.srfactiveviewdata;
    if((!contextObj) && view.parentData && view.parentData.length > 0) {
        if (view.parentData.length == 1) {
            contextObj = view.parentData[0];
        }
        else {
            contextObj = view.parentData;
        }
    }
    else if((!contextObj) && view.parentView.getController("form")) {
        contextObj = view.parentView.getController("form").data;
    }
    if(contextObj) {
        // 使用Object.assign进行浅合并
        if (!Array.isArray(contextObj)) {
            Object.assign(uiLogic.aicontext, contextObj);
        }
        else {
            uiLogic.aicontext.list = contextObj;
        }
    }
     
    if(screenshot) {
        try{

            const viewDom = document.getElementById(view.parentView.id);
            if (viewDom) {
                const fileName = view.parentView.model.caption || view.parentView.model.codeName;
                const screenshotElement = document.querySelector('.priority-screenshot') || 
                          document.querySelector('.ibiz-bi-report-panel-content>.el-collapse') || 
                          document.querySelector('.ibiz-custom-dashboard-container') || 
                          viewDom;
                
                const canvas = await ibiz.util.html2canvas.getCanvas(screenshotElement, { fileName });

                const blob = await new Promise((resolve) => {
                    canvas.toBlob((b) => {
                        if (b) {
                             const file = new File([b], fileName + '.png', {
                                type: 'image/png',
                                lastModified: new Date().getTime()
                            });
                            resolve(file);
                        } else {
                            resolve(null);
                        }
                    }, 'image/png', 0.7);
                });

                const fileUrlObj = ibiz.util.file.calcFileUpDownUrl(view.parentView.context,view.parentView.params);
                const fileobj = await ibiz.util.file.fileUpload(fileUrlObj.uploadUrl,blob,ibiz.util.file.getUploadHeaders());

                uiLogic.aicontext.screenshot="![img]("+fileUrlObj.downloadUrl.replace("%fileId%",fileobj.id)+")";
                
                
            }

         } catch (error) {
        }
        
    }
}
```
#### [智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context)的处理逻辑[prompt_feedback](module/ai/ai_agent_context/uilogic/prompt_feedback)

节点：注入脚本代码
<p class="panel-title"><b>执行代码</b></p>

```javascript
console.info("ai default_system_prompt");
var answer = null;
var realView = view;
var _entity_tag = view.context._entity_tag;
if (realView.model.appDataEntityId && realView.model.appDataEntityId.endsWith("ai_agent_assignment")) {
    realView = view.parentView;
}
if (!_entity_tag) {
    _entity_tag = realView.model.appDataEntityId ? realView.model.appDataEntityId.split('.').at(-1) : "";
}
if (_entity_tag) {
    uiLogic.default._entity_tag = _entity_tag;
}
var formController = realView.getController("form");

if (uiLogic.default.data && uiLogic.default.data.messages && uiLogic.default.data.messages.length > 0) {
    const lastAns = uiLogic.default.data.messages[uiLogic.default.data.messages.length - 1];
    answer = lastAns.realcontent;
}
else if (uiLogic.default.msg) {
    answer = uiLogic.default.msg.realcontent;
}

if (answer && typeof answer == 'string') {
    if (formController){
        var targetFormItem = formController.getFormDetail("FORMITEM","default_system_prompt");
		if(targetFormItem){
           try {
                var newvalue = answer;
                var oldvalue = formController.data["default_system_prompt"];
                
                if(oldvalue) {
                    newvalue = oldvalue + "\n---------\n" + answer;
                }
                formController.setDataValue("default_system_prompt", newvalue);

            } catch (error) {
            }
        }
         
    }

}
uiLogic.result = {content: "已完成"};


```
#### [智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context)的处理逻辑[run智能体逻辑(run)](module/ai/ai_agent_context/uilogic/run)

节点：注入脚本代码
<p class="panel-title"><b>执行代码</b></p>

```javascript
console.log("执行智能体");
 Object.assign(uiLogic.aicontext, uiLogic.default);
uiLogic.aicontext._name=uiLogic.aicontext.name;
uiLogic.aicontext.agent_name=uiLogic.aicontext.name;
uiLogic.aicontext.agent_description=uiLogic.aicontext.description;
uiLogic.aicontext.context_code_name = uiLogic.aicontext.code_name;
uiLogic.aicontext.context_namee = uiLogic.aicontext.name;
uiLogic.aicontext.context_id = uiLogic.aicontext.id;
uiLogic.aicontext.srfmajortext = uiLogic.aicontext.agent_name;
uiLogic.aicontext.name = null;
uiLogic.aicontext.description = null;

var context_content = "\n---\n\n* **执行智能体**: "+uiLogic.aicontext.agent_name +"\n";
if(uiLogic.aicontext.agent_description) {
    context_content = context_content+"* **智能体描述**: " + uiLogic.aicontext.agent_description+"\n";
}
context_content = context_content +"\n---\n";
uiLogic.aicontext.context_content=context_content;
// if(!uiLogic.aicontext.page_index) {
//     uiLogic.aicontext.page_index=0;
// }
const screenshot = uiLogic.aicontext.agent_description && uiLogic.aicontext.agent_description.indexOf("截图")>=0
uiLogic.context.ai_agent_context=uiLogic.aicontext.context_id;
uiLogic.context.ai_knowledge_base=uiLogic.aicontext.kb_id;
if(view && view.parentView) {
    
    var appDataEntityId=view.parentView.model.appDataEntityId;
    if(uiLogic.aicontext.kb_id && appDataEntityId === "ai.ai_agent_context") {
        appDataEntityId="ai.ai_knowledge_base";
    }
    else {
        var contextObj = view.parentView.state.srfactiveviewdata;
            if((!contextObj) && view.parentData && view.parentData.length > 0) {
                if (view.parentData.length == 1) {
                    contextObj = view.parentData[0];
                }
                else {
                    contextObj = view.parentData;
                }
            }
            else if((!contextObj) && view.parentView.getController("form")) {
                contextObj = view.parentView.getController("form").data;
            }
            if(contextObj) {
                // 使用Object.assign进行浅合并
                if (!Array.isArray(contextObj)) {
                    Object.assign(uiLogic.aicontext, contextObj);
                }
                else {
                    uiLogic.aicontext.list = contextObj;
                }
            }
    }


    if(appDataEntityId && appDataEntityId.indexOf(".")>0) {
        uiLogic.aicontext._entity_tag=appDataEntityId.split(".")[1];
        uiLogic.context._entity_tag=uiLogic.aicontext._entity_tag;
    }
     
    if(screenshot) {
        try{

            const viewDom = document.getElementById(view.parentView.id);
            if (viewDom) {
                const fileName = view.parentView.model.caption || view.parentView.model.codeName;
                const screenshotElement = document.querySelector('.priority-screenshot') || 
                          document.querySelector('.ibiz-bi-report-panel-content>.el-collapse') || 
                          document.querySelector('.ibiz-custom-dashboard-container') || 
                          viewDom;
                
                const canvas = await ibiz.util.html2canvas.getCanvas(screenshotElement, { fileName });

                const blob = await new Promise((resolve) => {
                    canvas.toBlob((b) => {
                        if (b) {
                             const file = new File([b], fileName + '.png', {
                                type: 'image/png',
                                lastModified: new Date().getTime()
                            });
                            resolve(file);
                        } else {
                            resolve(null);
                        }
                    }, 'image/png', 0.7);
                });

                const fileUrlObj = ibiz.util.file.calcFileUpDownUrl(view.parentView.context,view.parentView.params);
                const fileobj = await ibiz.util.file.fileUpload(fileUrlObj.uploadUrl,blob,ibiz.util.file.getUploadHeaders());

                uiLogic.aicontext.screenshot="![img]("+fileUrlObj.downloadUrl.replace("%fileId%",fileobj.id)+")";
                
                
            }

         } catch (error) {
        }
        
    }
}
```
#### [智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context)的处理逻辑[template_feedback](module/ai/ai_agent_context/uilogic/template_feedback)

节点：注入脚本代码
<p class="panel-title"><b>执行代码</b></p>

```javascript
console.info("ai default_system_prompt");
var answer = null;
var realView = view;
var _entity_tag = view.context._entity_tag;
if (realView.model.appDataEntityId && realView.model.appDataEntityId.endsWith("ai_agent_assignment")) {
    realView = view.parentView;
}
if (!_entity_tag) {
    _entity_tag = realView.model.appDataEntityId ? realView.model.appDataEntityId.split('.').at(-1) : "";
}
if (_entity_tag) {
    uiLogic.default._entity_tag = _entity_tag;
}
var formController = realView.getController("form");

if (uiLogic.default.data && uiLogic.default.data.messages && uiLogic.default.data.messages.length > 0) {
    const lastAns = uiLogic.default.data.messages[uiLogic.default.data.messages.length - 1];
    answer = lastAns.realcontent;
}
else if (uiLogic.default.msg) {
    answer = uiLogic.default.msg.realcontent;
}

if (answer && typeof answer == 'string') {
    if (formController){
        var targetFormItem = formController.getFormDetail("FORMITEM","default_system_prompt");
		if(targetFormItem){
           try {
                var newvalue = '<user>\n'+answer+"\n</user>";
                
                formController.setDataValue("welcome_message", newvalue);

            } catch (error) {
            }
        }
         
    }

}
uiLogic.result = {content: "已完成"};


```
#### [智能体会话(AI_AGENT_SESSION)](module/ai/ai_agent_session)的处理逻辑[jenkins_build](module/ai/ai_agent_session/uilogic/jenkins_build)

节点：注入脚本代码
<p class="panel-title"><b>执行代码</b></p>

```javascript
var answer = null;
if(uiLogic.default.data && uiLogic.default.data.messages && uiLogic.default.data.messages.length>0) {
    const lastAns = uiLogic.default.data.messages[uiLogic.default.data.messages.length-1];
    answer = lastAns.realcontent;
}
else if(uiLogic.default.msg) {
    answer = uiLogic.default.msg.realcontent;
}
 if(answer) {
     if (answer && typeof answer == 'string') {
        var ret =ibiz.util.jsonUtil.parseJson(answer);
        ret.project = view.parentView.context.project;
        if(ret.success && ret.data) {
            if(ret.data_type == 'jsonobject' ) {
                // API配置
                const apiUrl = 'http://172.16.240.30:8000';
                
                console.log('原始ret.data:', ret.data);

                // 直接使用ret.data作为参数
                // 确保有task_type字段
                if (!ret.data.task_type) {
                    throw new Error('参数中缺少task_type字段');
                }

                // 构建请求数据 - 直接传递ret.data
                const requestData = {
                    task_type: ret.data.task_type,
                    params: {},
                    timeout: ret.data.timeout || 300,
                    callback_url: ret.data.callback_url || null
                };

                // 将所有其他参数复制到params中
                Object.entries(ret.data).forEach(([key, value]) => {
                    if (key !== 'task_type' && key !== 'timeout' && key !== 'callback_url') {
                        requestData.params[key] = value;
                    }
                });

                console.log('API请求数据:', requestData);

                // 调用API
                const response = await fetch(`${apiUrl}/api/v1/jobs`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json'
                    },
                    body: JSON.stringify(requestData)
                });

                if (!response.ok) {
                    const errorText = await response.text();
                    throw new Error(`API请求失败: ${response.status} - ${errorText}`);
                }

                const result = await response.json();
                
                console.log('API返回结果:', result);
                // 设置节点返回对象
                uiLogic.result = {
                    content: result.message
                };
                ibiz.message.success(`任务已提交到调度系统，任务ID: ${result.task_id}`);
            }
        }
    }
}
```
#### [智能体会话(AI_AGENT_SESSION)](module/ai/ai_agent_session)的处理逻辑[remark_feedback](module/ai/ai_agent_session/uilogic/remark_feedback)

节点：注入脚本代码
<p class="panel-title"><b>执行代码</b></p>

```javascript
console.info("ai remark");
var answer = null;
var realView = view;
var _entity_tag = view.context._entity_tag;
if (realView.model.appDataEntityId && realView.model.appDataEntityId.endsWith("ai_agent_assignment")) {
    realView = view.parentView;
}
if (!_entity_tag) {
    _entity_tag = realView.model.appDataEntityId ? realView.model.appDataEntityId.split('.').at(-1) : "";
}
if (_entity_tag) {
    uiLogic.default._entity_tag = _entity_tag;
}
var formController = realView.getController("form");

if (uiLogic.default.data && uiLogic.default.data.messages && uiLogic.default.data.messages.length > 0) {
    const lastAns = uiLogic.default.data.messages[uiLogic.default.data.messages.length - 1];
    answer = lastAns.realcontent;
}
else if (uiLogic.default.msg) {
    answer = uiLogic.default.msg.realcontent;
}

if (answer && typeof answer == 'string') {
    if (formController){
           try {
                var newvalue = answer;
                var oldvalue = formController.data["description"];
                if(oldvalue) {
                    newvalue = oldvalue + "\n---------\n" + answer;
                }
                if(_entity_tag=='work_item' || _entity_tag=='idea') {
                    formController.setDataValue('formitem1', newvalue);
                }
                formController.setDataValue("description", newvalue);

            } catch (error) {
            }
            try {
                var newvalue = answer;
                var oldvalue = formController.data["content"];
                if(oldvalue) {
                    newvalue = oldvalue + "\n---------\n" + answer;
                }
                formController.setDataValue("content", newvalue);

            } catch (error) {
            }
    }

}
uiLogic.result = {content: "已完成"};


```
#### [智能体会话(AI_AGENT_SESSION)](module/ai/ai_agent_session)的处理逻辑[debug_context](module/ai/ai_agent_session/uilogic/debug_context)

节点：注入脚本代码
<p class="panel-title"><b>执行代码</b></p>

```javascript
console.log(uiLogic.default);

const target = uiLogic.default;

// 检查context_data是否存在且为字符串
if (target.context_debug_data && typeof target.context_debug_data === 'string') {
    try {
        // 将JSON字符串解析为对象
        const contextObj = JSON.parse(target.context_debug_data);
        console.log('解析后的context_data对象:', contextObj);
        //const _id = uiLogic.default.id;

        // 将解析后的对象合并到uiLogic.default中
        // 使用Object.assign进行浅合并
        if (!Array.isArray(contextObj)) {
            Object.assign(uiLogic.default, contextObj);
        }
    } catch (parseError) {
        console.error('JSON解析错误:', parseError);
        console.error('无效的JSON字符串:', target.context_debug_data);
    }

}       
 //uiLogic.default.id = _id; 
uiLogic.default._id = uiLogic.default.context_id + '-' + uiLogic.context.srfnavctrlid + '-' + (target?.id || (Date.now().toString(36) + Math.random().toString(36).substr(2, 5)));
console.log('合并后的uiLogic.default:', uiLogic.default);

```
#### [智能体会话(AI_AGENT_SESSION)](module/ai/ai_agent_session)的处理逻辑[accept_feedback](module/ai/ai_agent_session/uilogic/accept_feedback)

节点：注入脚本代码
<p class="panel-title"><b>执行代码</b></p>

```javascript
console.info("ai callback");
var answer = null;
var realView = view;
var _entity_tag = view.context._entity_tag;
if (realView.model.appDataEntityId && realView.model.appDataEntityId.endsWith("ai_agent_assignment")) {
    realView = view.parentView;
}
if (!_entity_tag) {
    _entity_tag = realView.model.appDataEntityId ? realView.model.appDataEntityId.split('.').at(-1) : "";
}
if (_entity_tag) {
    uiLogic.default._entity_tag = _entity_tag;
}
var formController = realView.getController("form");

if (uiLogic.default.data && uiLogic.default.data.messages && uiLogic.default.data.messages.length > 0) {
    const lastAns = uiLogic.default.data.messages[uiLogic.default.data.messages.length - 1];
    answer = lastAns.realcontent;
}
else if (uiLogic.default.msg) {
    answer = uiLogic.default.msg.realcontent;
}

if (answer && typeof answer == 'string') {
    var ret = ibiz.util.jsonUtil.parseJson(answer);
    if (ret.success && ret.data) {
        if (ret.data_type == 'jsonobject' && formController) {
            Object.entries(ret.data).forEach(([key, value]) => {
                try {
                    if(value) {
                        var newvalue = value;
                        if(key === 'description' || key === 'content') {
                            var oldvalue = formController.data[key];
                            if(oldvalue) {
                                newvalue = oldvalue + "\n---------\n" + value;
                            }
                            if(key ==='description' &&  (_entity_tag=='work_item' || _entity_tag=='idea')) {
                                formController.setDataValue('formitem1', newvalue);
                            }
                        }
                        formController.setDataValue(key, newvalue);
                        console.log(`已设置表单字段: ${key} =`, newvalue);
                    }
                } catch (error) {
                }
            });
        }

        if (formController && formController.model.codeName === "debug") {
            try {
                formController.setDataValue("debug_callback_2", ret.data);

            } catch (error) {
            }
        }
    }
    else if (formController){
            try {
                var newvalue = answer;
                var oldvalue = formController.data["description"];
                if(oldvalue) {
                    newvalue = oldvalue + "\n---------\n" + answer;
                }
                if(_entity_tag=='work_item' || _entity_tag=='idea') {
                    formController.setDataValue('formitem1', newvalue);
                }
                formController.setDataValue("description", newvalue);

            } catch (error) {
            }
            try {
                var newvalue = answer;
                var oldvalue = formController.data["content"];
                if(oldvalue) {
                    newvalue = oldvalue + "\n---------\n" + answer;
                }
                formController.setDataValue("content", newvalue);

            } catch (error) {
            }
    }

}

if (formController && formController.model.codeName === "debug") {
    try {
        formController.setDataValue("debug_callback_1", answer);
    } catch (error) {
    }
}

uiLogic.result = {content: "已完成"};

```
#### [智能体会话(AI_AGENT_SESSION)](module/ai/ai_agent_session)的处理逻辑[dyna_context](module/ai/ai_agent_session/uilogic/dyna_context)

节点：注入脚本代码
<p class="panel-title"><b>执行代码</b></p>

```javascript
console.log(uiLogic.default);

const target = uiLogic.default;

// 检查context_data是否存在且为字符串
if (target.context_debug_data && typeof target.context_debug_data === 'string') {
    try {
        // 将JSON字符串解析为对象
        const contextObj = JSON.parse(target.context_debug_data);
        console.log('解析后的context_data对象:', contextObj);
        //const _id = uiLogic.default.id;

        // 将解析后的对象合并到uiLogic.default中
        // 使用Object.assign进行浅合并
        if (!Array.isArray(contextObj)) {
            Object.assign(uiLogic.default, contextObj);
        }
    } catch (parseError) {
        console.error('JSON解析错误:', parseError);
        console.error('无效的JSON字符串:', target.context_debug_data);
    }

}       
 //uiLogic.default.id = _id; 
uiLogic.default._id =uiLogic.default.context_id + '-' + uiLogic.context.srfviewid + '-' + (target?.id || (Date.now().toString(36) + Math.random().toString(36).substr(2, 5)))+'-'+uiLogic.default._entity_tag;
console.log('合并后的uiLogic.default:', uiLogic.default);
uiLogic.view.closeView();


```
#### [AI客户端凭证(AI_CLIENT_CREDENTIAL)](module/ai/ai_client_credential)的处理逻辑[复制密钥(copy_access_key)](module/ai/ai_client_credential/uilogic/copy_access_key)

节点： 复制密钥
<p class="panel-title"><b>执行代码</b></p>

```javascript
var _default = uiLogic.default;
var access_key = _default.access_key;

if(access_key !== null && access_key !== undefined){
    var textArea = document.createElement("textarea");
    // 在 textarea 中放入需要复制的文本
    textArea.value = access_key;
    // 将 textarea 添加到 DOM 中
    document.body.appendChild(textArea);
    // 选中 textarea 中的文本
    textArea.select();
    // 执行复制命令
    var successful = document.execCommand('copy');
    var msg = successful ? '' : '复制密钥失败!';
    if(successful){
        util.message.success('复制密钥成功!');
    } else {
        util.message.error('复制密钥失败!');
    }
} else {
    util.message.error('复制密钥失败!');
}

```
#### [知识库文档分块(AI_KB_CHUNK)](module/ai/ai_kb_chunk)的处理逻辑[打开所属文档(open_doc)](module/ai/ai_kb_chunk/uilogic/open_doc)

节点：打开所属文档
<p class="panel-title"><b>执行代码</b></p>

```javascript
var _default = uiLogic.default;
const ai_knowledge_base = context.ai_knowledge_base
const ai_kb_document = context.ai_kb_document? context.ai_kb_document:_default.docid;
const document_type =_default.document_type
// window.location.hash=`/-/index/ai_knowledge_base=${ai_knowledge_base}/ai_knowledge_base_index_view/srfnavctx={"srfnavctrlid":"aifactoryweb.ai_knowledge_base_grid_view@aifactoryweb.ai_knowledge_base.main"};srfnav=index_view/ai_kb_document_tree_exp_view/srfnavctx={"srfdefaulttoroutedepth":3};srfnav=root:doc_type@${document_type}:ai_kb_doc@${ai_kb_document}/ai_kb_chunk_card_view/n_document_id_eq=${ai_kb_document};doc_type=${document_type};srfnavctx={"ai_kb_document":"${ai_kb_document}","srfnavctrlid":"aifactoryweb.ai_kb_document_tree_exp_view@aifactoryweb.ai_kb_document.tree_exp_view_tree_view"}`
window.location.hash=`/-/index/ai_knowledge_base=${ai_knowledge_base}/ai_knowledge_base_index_view/srfnavctx={"srfnavctrlid":"aifactoryweb.ai_knowledge_base_grid_view@aifactoryweb.ai_knowledge_base.main"};srfnav=index_view/ai_kb_document_main_list_exp_view/srfnavctx={"srfnavctrlid":"aifactoryweb.ai_kb_document_main_grid_view@aifactoryweb.ai_kb_document.main2","ai_kb_document":"${ai_kb_document}","selected_data":"${ai_kb_document}"};srfnav=${ai_kb_document}/ai_kb_document_main_show_view/srfnavctx={"srfnavctrlid":"aifactoryweb.ai_kb_document_main_list_exp_view@aifactoryweb.ai_kb_document.main_list_exp_view_list","ai_kb_document":"${ai_kb_document}"}`

```
#### [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document)的处理逻辑[显示基本信息(show_info)](module/ai/ai_kb_document/uilogic/show_info)

节点：通知刷新
<p class="panel-title"><b>执行代码</b></p>

```javascript
ibiz.mc.command.create.send({ srfdecodename: 'ai_kb_document'});
```
#### [知识库文档同步(AI_KB_DOCUMENT_SYNC)](module/ai/ai_kb_document_sync)的处理逻辑[刷新文档同步表格(refresh_doc_sync_grid)](module/ai/ai_kb_document_sync/uilogic/refresh_doc_sync_grid)

节点：刷新表格
<p class="panel-title"><b>执行代码</b></p>

```javascript
if (uiLogic.grid) {
    uiLogic.grid.refresh();
}
```
#### [知识库文档向导(AI_KB_DOCUMENT_WIZARD)](module/ai/ai_kb_document_wizard)的处理逻辑[通知刷新(notify_refresh)](module/ai/ai_kb_document_wizard/uilogic/notify_refresh)

节点：注入脚本代码
<p class="panel-title"><b>执行代码</b></p>

```javascript
ibiz.mc.command.create.send({ srfdecodename: 'ai_kb_document'});
```
#### [知识库成员(AI_KB_MEMBER)](module/ai/ai_kb_member)的处理逻辑[新建知识库默认临时成员(create_default_temp_members)](module/ai/ai_kb_member/uilogic/create_default_temp_members)

节点：创建临时数据
<p class="panel-title"><b>执行代码</b></p>

```javascript
ibiz.hub.getApp(context.srfappid).deService.exec(
    'aifactoryweb.ai_kb_member',
    'Create',
    context,
    uiLogic.user,
);
```
#### [知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base)的处理逻辑[计算表格列行为状态(ai_knowledge_base)(calc_column_action_state)](module/ai/ai_knowledge_base/uilogic/calc_column_action_state)

节点：计算表格列行为状态
<p class="panel-title"><b>执行代码</b></p>

```javascript
	const rows = uiLogic.grid.state.rows;
	if (rows && rows.length > 0) {
		rows.forEach(row => {
			const titleColumn = row.uiActionGroupStates.name;
			const is_favorite = row.data.is_favorite;
			if (titleColumn && Object.values(titleColumn).length > 0) {
				Object.values(titleColumn).forEach(action => {
					// 收藏
					if (action.uiActionId === 'add_favorite@ai_knowledge_base') {
						action.visible = is_favorite == 0;
					} else if (action.uiActionId === 'cancel_favorite@ai_knowledge_base') {
						// 取消收藏
						action.visible = is_favorite != 0;
					}
				})
			}
		})
	}

```
#### [知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base)的处理逻辑[查找知识库首页模版(find_template)](module/ai/ai_knowledge_base/uilogic/find_template)

节点：注入脚本代码
<p class="panel-title"><b>执行代码</b></p>

```javascript
var _kb_entity = uiLogic.kb_entity;
console.log('正在设置知识库首页动态看板');
if(_kb_entity){
    const c = view.ctx.controllersMap.get('drbar');
    if(c){
        c.context.dyna_dashboard = _kb_entity.dyna_dashboard_id;
        c.context.srfdynadashboardid = _kb_entity.dyna_dashboard_id;
    }
}
```
#### [知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base)的处理逻辑[提示词填充(prompt_feedback)](module/ai/ai_knowledge_base/uilogic/prompt_feedback)

节点：注入脚本代码
<p class="panel-title"><b>执行代码</b></p>

```javascript
console.info("ai default_guidance_prompt");
var answer = null;
var realView = view;
var _entity_tag = view.context._entity_tag;
if (realView.model.appDataEntityId && realView.model.appDataEntityId.endsWith("ai_agent_assignment")) {
    realView = view.parentView;
}
if (!_entity_tag) {
    _entity_tag = realView.model.appDataEntityId ? realView.model.appDataEntityId.split('.').at(-1) : "";
}
if (_entity_tag) {
    uiLogic.default._entity_tag = _entity_tag;
}
var formController = realView.getController("form");

if (uiLogic.default.data && uiLogic.default.data.messages && uiLogic.default.data.messages.length > 0) {
    const lastAns = uiLogic.default.data.messages[uiLogic.default.data.messages.length - 1];
    answer = lastAns.realcontent;
}
else if (uiLogic.default.msg) {
    answer = uiLogic.default.msg.realcontent;
}

if (answer && typeof answer == 'string') {
    if (formController){
        var targetFormItem = formController.getFormDetail("FORMITEM","guidance_prompt");
		if(targetFormItem){
           try {
                var newvalue = answer;
                var oldvalue = formController.data["guidance_prompt"];
                
                if(oldvalue) {
                    newvalue = oldvalue + "\n---------\n" + answer;
                }
                formController.setDataValue("guidance_prompt", newvalue);

            } catch (error) {
            }
        }
         
    }

}
uiLogic.result = {content: "已完成填充"};


```
#### [知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base)的处理逻辑[刷新当前表格(refresh_current_grid)](module/ai/ai_knowledge_base/uilogic/refresh_current_grid)

节点：通过实体刷新表格、树
<p class="panel-title"><b>执行代码</b></p>

```javascript
ibiz.mc.command.update.send({ srfdecodename: 'ai_knowledge_base', srfkey: params.owner_id})
```
#### [知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base)的处理逻辑[刷新当前表格(refresh_current_grid)](module/ai/ai_knowledge_base/uilogic/refresh_current_grid)

节点：刷新视图
<p class="panel-title"><b>执行代码</b></p>

```javascript
view.call('Refresh');
setTimeout(() => {
    if (view.layoutPanel.panelItems.nav_pos && view.layoutPanel.panelItems.nav_pos.curNavViewMsg) {
        // 找到当前的右侧视图
        const viewId = view.layoutPanel.panelItems.nav_pos.curNavViewMsg.viewId;
        if (viewId) {
            const key = viewId.split('.').pop();
            const viewPos = view.getController(key);
            if (viewPos) {
                viewPos.call('Refresh');
            }
        }
    }
}, 300)
```
#### [智能审查报告(AI_REVIEW_REPORT)](module/ai/ai_review_report)的处理逻辑[AI添加审查报告(ai_add)](module/ai/ai_review_report/uilogic/ai_add)

节点：注入脚本代码
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
#### [智能审查报告(AI_REVIEW_REPORT)](module/ai/ai_review_report)的处理逻辑[AI添加审查报告(ai_add)](module/ai/ai_review_report/uilogic/ai_add)

节点：完成提示
<p class="panel-title"><b>执行代码</b></p>

```javascript
ibiz.message.success('添加到审查报告成功');
uiLogic.result={content: "已添加到审查报告"};
```
#### [附件(ATTACHMENT)](module/Base/attachment)的处理逻辑[附件删除(remove_attachment)](module/Base/attachment/uilogic/remove_attachment)

节点：注入脚本代码
<p class="panel-title"><b>执行代码</b></p>

```javascript
del = await ibiz.confirm.error({
    title: ibiz.i18n.t('runtime.controller.common.control.dataDeletion'),
    desc: ibiz.i18n.t(
    '确认删除文件？',
    ),
});

if (del) {
    uiLogic.default.is_delete = true;
}
```
#### [附件(ATTACHMENT)](module/Base/attachment)的处理逻辑[附件删除(remove_attachment)](module/Base/attachment/uilogic/remove_attachment)

节点：设置附件数据
<p class="panel-title"><b>执行代码</b></p>

```javascript
uiLogic.attach = { data: uiLogic.default, silent: true };
```
#### [附件(ATTACHMENT)](module/Base/attachment)的处理逻辑[附件预览(attachment_preview)](module/Base/attachment/uilogic/attachment_preview)

节点：注入脚本代码
<p class="panel-title"><b>执行代码</b></p>

```javascript
const url = window.location;
var file_name = uiLogic.default.name;
var file_id = uiLogic.default.file_id;
var file_preview_address = ibiz.env.customParams.file_preview_address;

if (file_preview_address !== null && file_preview_address !== undefined && file_preview_address !== '') {
    const windowInfo = getCurrentWindowInfo(url);

    let uploadUrl = `${ibiz.env.baseUrl}/${ibiz.env.appId}${ibiz.env.downloadFileUrl}`;
    const app = ibiz.hub.getApp(context.srfappid);
    const OSSCat = app.model.userParam?.DefaultOSSCat;
    uploadUrl = uploadUrl.replace('/{cat}', OSSCat ? `/${OSSCat}` : '');

    var filedownloadurl = windowInfo + uploadUrl + '/'+file_id+'?fullfilename='+file_name;

    var b64Encoded = ibiz.util.base64.encode(filedownloadurl);
    var previewUrl = file_preview_address + '/onlinePreview?url='+encodeURIComponent(b64Encoded);

    window.open(previewUrl);
} else {
  util.message.error('无附件预览服务，请联系管理员添加!');
}

function getCurrentWindowInfo(url) {
    const protocol = url.protocol;
    const host = url.hostname; 
    const port = url.port || (protocol === "https:" ? "443" : "80"); 
    const isIPAddress = /^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/.test(host);
    if (isIPAddress) {
        return  protocol +"//" + host + ":" + port ;
    } else {
        return  protocol +"//" + host + ":" + port ;
    }
}
```
#### [附件(ATTACHMENT)](module/Base/attachment)的处理逻辑[计算附件是否隐藏逻辑(calc_attachment_hidden)](module/Base/attachment/uilogic/calc_attachment_hidden)

节点：设置表格隐藏
<p class="panel-title"><b>执行代码</b></p>

```javascript
uiLogic.grid.state.keepAlive = true;
uiLogic.grid.state.visible = false;
```
#### [附件(ATTACHMENT)](module/Base/attachment)的处理逻辑[计算附件是否隐藏逻辑(calc_attachment_hidden)](module/Base/attachment/uilogic/calc_attachment_hidden)

节点：设置表格显示
<p class="panel-title"><b>执行代码</b></p>

```javascript
uiLogic.grid.state.keepAlive = true;
uiLogic.grid.state.visible = true;
```
#### [附件(ATTACHMENT)](module/Base/attachment)的处理逻辑[计算附件是否隐藏逻辑(calc_attachment_hidden)](module/Base/attachment/uilogic/calc_attachment_hidden)

节点：上下文中srfreadonly禁用删除附件行为
<p class="panel-title"><b>执行代码</b></p>

```javascript
const rows = uiLogic.grid.mdController.state.rows;
const srfreadonly = context.srfreadonly;
if (rows && rows.length > 0) {
	rows.forEach(row => {
        // 删除附件行为禁用
		const uiActionId = row.uaColStates.uagridcolumn1.u44d00e2;
        if(srfreadonly == true && uiActionId.hasOwnProperty('disabled')){
            uiActionId.disabled = true;
        }    
	})
}	

```
#### [评论(COMMENT)](module/Base/comment)的处理逻辑[控制评论按钮显示（知识库）(comment_icon_show_wiki)](module/Base/comment/uilogic/comment_icon_show_wiki)

节点：控制评论按钮显示（知识库）
<p class="panel-title"><b>执行代码</b></p>

```javascript
uiLogic.send = uiLogic.view.layoutPanel.panelItems.container_singledata.panelItems.comment_send.state;
uiLogic.reset = uiLogic.view.layoutPanel.panelItems.container_singledata.panelItems.comment_cancel.state;
uiLogic.icon = uiLogic.view.layoutPanel.panelItems.container_singledata.panelItems.comment_icon.state;
uiLogic.icon.visible = false;
uiLogic.send.visible = uiLogic.context.srfreadonly !== true;
uiLogic.reset.visible = uiLogic.context.srfreadonly !== true;
```
#### [评论(COMMENT)](module/Base/comment)的处理逻辑[ai添加评论(ai_comment)](module/Base/comment/uilogic/ai_comment)

节点：注入脚本代码
<p class="panel-title"><b>执行代码</b></p>

```javascript

console.info("ai callback");
var answer = null;
var realView = view;
var _entity_tag = view.context._entity_tag;
if (realView.model.appDataEntityId && realView.model.appDataEntityId.endsWith("ai_agent_assignment")) {
    realView = view.parentView;
}
if (!_entity_tag) {
    _entity_tag = realView.model.appDataEntityId ? realView.model.appDataEntityId.split('.').at(-1) : "";
}
if (_entity_tag) {
    uiLogic.default._entity_tag = _entity_tag;
}
//var formController = realView.getController("form");
var from = "from: AI智能体\n";
if (uiLogic.default.data && uiLogic.default.data.messages && uiLogic.default.data.messages.length > 0) {
    const lastAns = uiLogic.default.data.messages[uiLogic.default.data.messages.length - 1];
    answer = lastAns.realcontent;
    if(uiLogic.default.data.caption) {
        from = "from: "+uiLogic.default.data.caption+"\n";
    }
}
else if (uiLogic.default.msg) {
    answer = uiLogic.default.msg.realcontent;
    if(uiLogic.default.topic && uiLogic.default.topic.caption) {
        from = "from: "+uiLogic.default.topic.caption+"\n";
    }
}

uiLogic.entity = {};

if (answer && typeof answer == 'string') {

    uiLogic.entity.principal_id = realView.context[_entity_tag];
    var principal_type = _entity_tag.toUpperCase();
    if(principal_type === 'ARTICLE_PAGE' ) {
        principal_type = 'PAGE';
    }
    uiLogic.entity.principal_type= principal_type;
    uiLogic.entity.owner_type= principal_type;
    var html_content = from + answer; 

    uiLogic.entity.content = html_content;
            
}

```
#### [评论(COMMENT)](module/Base/comment)的处理逻辑[ai添加评论(ai_comment)](module/Base/comment/uilogic/ai_comment)

节点：注入脚本代码
<p class="panel-title"><b>执行代码</b></p>

```javascript
view.parentView.call("Refresh");
ibiz.message.success('评论成功');
uiLogic.result={content: "已添加到评论"};
```
#### [评论(COMMENT)](module/Base/comment)的处理逻辑[发送评论(知识库)(send_comment_wiki)](module/Base/comment/uilogic/send_comment_wiki)

节点：获取评论框内容和编辑器对象
<p class="panel-title"><b>执行代码</b></p>

```javascript
uiLogic.comment.content = uiLogic.view.layoutPanel.panelItems.container_singledata.panelItems.field_textbox.value;
uiLogic.editor = uiLogic.view.layoutPanel.panelItems.container_singledata.panelItems.field_textbox.editor
```
#### [评论(COMMENT)](module/Base/comment)的处理逻辑[发送评论(知识库)(send_comment_wiki)](module/Base/comment/uilogic/send_comment_wiki)

节点：清空评论框与评论id
<p class="panel-title"><b>执行代码</b></p>

```javascript
uiLogic.view.layoutPanel.panelItems.container_singledata.panelItems.field_textbox.value = '';
uiLogic.view.layoutPanel.panelItems.container_singledata.panelItems.field_textbox.data.field_textbox = '';
uiLogic.view.edit_comment_id = null;
uiLogic.view.reply_comment_id = null;
uiLogic.editor.reply.value = null;
uiLogic.editor.toggleCollapse(false);
```
#### [评论(COMMENT)](module/Base/comment)的处理逻辑[发送评论(知识库)(send_comment_wiki)](module/Base/comment/uilogic/send_comment_wiki)

节点：刷新评论列表
<p class="panel-title"><b>执行代码</b></p>

```javascript
ibiz.mc.command.send({ srfdecodename: 'comment' }, 'OBJECTUPDATED');
```
#### [评论(COMMENT)](module/Base/comment)的处理逻辑[清空评论（知识库）(clear_comment_wiki)](module/Base/comment/uilogic/clear_comment_wiki)

节点：清空评论（知识库）
<p class="panel-title"><b>执行代码</b></p>

```javascript
uiLogic.view.layoutPanel.panelItems.container_singledata.panelItems.field_textbox.editor.clear();
uiLogic.view.edit_comment_id = null;
uiLogic.view.reply_comment_id = null;
```
#### [评论(COMMENT)](module/Base/comment)的处理逻辑[控制评论按钮隐藏（知识库）(comment_icon_hidden_wiki)](module/Base/comment/uilogic/comment_icon_hidden_wiki)

节点：控制评论按钮隐藏（知识库）
<p class="panel-title"><b>执行代码</b></p>

```javascript
uiLogic.send = uiLogic.view.layoutPanel.panelItems.container_singledata.panelItems.comment_send.state;
uiLogic.reset = uiLogic.view.layoutPanel.panelItems.container_singledata.panelItems.comment_cancel.state;
uiLogic.icon = uiLogic.view.layoutPanel.panelItems.container_singledata.panelItems.comment_icon.state;
const text_box = uiLogic.view.layoutPanel.panelItems.container_singledata.panelItems.field_textbox;


uiLogic.send.visible = uiLogic.context.srfreadonly !== true && text_box.value ? true : false;
uiLogic.reset.visible = uiLogic.context.srfreadonly !== true && text_box.value ? true : false;
uiLogic.icon.visible = text_box.value ? false : true;
```
#### [评论(COMMENT)](module/Base/comment)的处理逻辑[回复评论（知识库）(reply_comment_wiki)](module/Base/comment/uilogic/reply_comment_wiki)

节点：展开评论输入框并设值回复
<p class="panel-title"><b>执行代码</b></p>

```javascript
uiLogic.comment = uiLogic.view.layoutPanel.panelItems.container_singledata.panelItems.field_textbox.editor;
const _app = ibiz.hub.getApp(context.srfappid);
_app.codeList.get('SysOperator', context, params).then(items => {
	const create_man = uiLogic.default.create_man;
	const findItem = items.find(item => item.value == create_man);
	const name = findItem ? findItem.text : create_man;
	const content = uiLogic.default.content;
	uiLogic.comment.setReply({name, content});
	uiLogic.comment.toggleCollapse(true);
})
uiLogic.view.edit_comment_id='';
uiLogic.view.reply_comment_id=uiLogic.default.id;
```
#### [评论(COMMENT)](module/Base/comment)的处理逻辑[编辑评论（知识库）(edit_comment_wiki)](module/Base/comment/uilogic/edit_comment_wiki)

节点：展开评论输入框并设值
<p class="panel-title"><b>执行代码</b></p>

```javascript
uiLogic.comment = uiLogic.view.layoutPanel.panelItems.container_singledata.panelItems.field_textbox.editor;
uiLogic.comment.toggleCollapse(true);
uiLogic.comment.setValue(uiLogic.default.content);
uiLogic.comment.reply.value = null;
```
#### [动态数据看板(DYNADASHBOARD)](module/Base/dyna_dashboard)的处理逻辑[仪表盘操作列(control_del)](module/Base/dyna_dashboard/uilogic/control_del)

节点：剩余一个仪表盘禁止删除
<p class="panel-title"><b>执行代码</b></p>

```javascript
  const rows = uiLogic.grid.state.rows;
//   console.log(rows);
  if (rows && rows.length === 1) {
    rows.forEach(row => {
        row.uaColStates.uagridcolumn1.u36f5de4.disabled = true
    })
  }
```
#### [动态数据看板(DYNADASHBOARD)](module/Base/dyna_dashboard)的处理逻辑[通知刷新(notify_refresh)](module/Base/dyna_dashboard/uilogic/notify_refresh)

节点：注入脚本代码
<p class="panel-title"><b>执行代码</b></p>

```javascript
ibiz.mc.command.update.send({ srfdecodename: 'dynadashboard'})
```
#### [动态数据看板(DYNADASHBOARD)](module/Base/dyna_dashboard)的处理逻辑[使用此模板(禁止关闭)(use_cur_template_no_closed)](module/Base/dyna_dashboard/uilogic/use_cur_template_no_closed)

节点：通知刷新
<p class="panel-title"><b>执行代码</b></p>

```javascript
ibiz.mc.command.update.send({ srfdecodename: 'insight_view', srfkey: context.insight_view})
```
#### [动态数据看板(DYNADASHBOARD)](module/Base/dyna_dashboard)的处理逻辑[使用此模板(禁止关闭)(use_cur_template_no_closed)](module/Base/dyna_dashboard/uilogic/use_cur_template_no_closed)

节点：设置上下文
<p class="panel-title"><b>执行代码</b></p>

```javascript
if(uiLogic.selecteddata && uiLogic.selecteddata.length >0){
    uiLogic.ctx.dynadashboard = uiLogic.selecteddata[0].dynadashboardid;
    uiLogic.dyna_dashboard_info = uiLogic.selecteddata[0];
    uiLogic.dyna_dashboard_info.owner_id = uiLogic.ctx.insight_view_id;
}
```
#### [动态数据看板(DYNADASHBOARD)](module/Base/dyna_dashboard)的处理逻辑[使用此模板(禁止关闭)(use_cur_template_no_closed)](module/Base/dyna_dashboard/uilogic/use_cur_template_no_closed)

节点：打开视图
<p class="panel-title"><b>执行代码</b></p>

```javascript
const new_dynadashboard = uiLogic.new_dynadashboard;
const insight_view_id = context.insight_view_id;
const dyna_dashboard_id = new_dynadashboard.dyna_dashboard_id;
 window.location.hash= `/-/index/insight_view=${insight_view_id}/insight_view_index_view/srfnavctx=%257B%2522srfnavctrlid%2522%253A%2522plmweb.insight_view_all_grid_view%2540plmweb.insight_view.all_grid_view_grid%2522%257D;srfnav=usrdrgroup0517936766/insight_view_custom_view/srfnavctx=%257B%2522srfdefaulttoroutedepth%2522%253A3%252C%2522dyna_dashboard%2522%253A%2522${dyna_dashboard_id}%2522%257D`


```
#### [动态数据看板(DYNADASHBOARD)](module/Base/dyna_dashboard)的处理逻辑[使用此模板(禁止关闭)(use_cur_template_no_closed)](module/Base/dyna_dashboard/uilogic/use_cur_template_no_closed)

节点：关闭当前视图
<p class="panel-title"><b>执行代码</b></p>

```javascript
view.state.isLoading = false;
view.closeView();
```
#### [动态数据看板(DYNADASHBOARD)](module/Base/dyna_dashboard)的处理逻辑[使用此模板(禁止关闭)(use_cur_template_no_closed)](module/Base/dyna_dashboard/uilogic/use_cur_template_no_closed)

节点：注入脚本代码
<p class="panel-title"><b>执行代码</b></p>

```javascript
ibiz.mc.command.update.send({ srfdecodename: 'dynadashboard'})
```
#### [动态数据看板(DYNADASHBOARD)](module/Base/dyna_dashboard)的处理逻辑[列表加载完成(list_load_success)](module/Base/dyna_dashboard/uilogic/list_load_success)

节点：设置默认仪盘表标题
<p class="panel-title"><b>执行代码</b></p>

```javascript
const selectData = uiLogic.ctrl.state.selectedData;
if(selectData != null &&  selectData.length > 0){
    const firstObject = selectData[0];
    if(firstObject.dyna_dashboard_name != null && firstObject.dyna_dashboard_name != undefined){
        view.layoutPanel.panelItems.board_title.setDataValue(firstObject.dyna_dashboard_name);
    }  
}
```
#### [动态数据看板(DYNADASHBOARD)](module/Base/dyna_dashboard)的处理逻辑[获取选中模板名称(fill_choosed_board_name)](module/Base/dyna_dashboard/uilogic/fill_choosed_board_name)

节点：设置仪表盘标题
<p class="panel-title"><b>执行代码</b></p>

```javascript
view.layoutPanel.panelItems.board_title.setDataValue(uiLogic.ctrl.inputData.dyna_dashboard_name);


```
#### [效能成员(INSIGHT_MEMBER)](module/Insight/insight_member)的处理逻辑[新建视图默认临时成员(create_default_temp_members)](module/Insight/insight_member/uilogic/create_default_temp_members)

节点：创建临时数据
<p class="panel-title"><b>执行代码</b></p>

```javascript
ibiz.hub.getApp(context.srfappid).deService.exec(
    'plmweb.insight_member',
    'Create',
    context,
    uiLogic.user,
);
```
#### [效能报表(INSIGHT_REPORT)](module/Insight/insight_report)的处理逻辑[导出表格(export_excel)](module/Insight/insight_report/uilogic/export_excel)

节点：整合表格数据并导出
<p class="panel-title"><b>执行代码</b></p>

```javascript
if (uiLogic.grid) {
    uiLogic.grid.exportData({params: {}});
}
```
#### [效能报表(INSIGHT_REPORT)](module/Insight/insight_report)的处理逻辑[使用此模板(use_cur_template)](module/Insight/insight_report/uilogic/use_cur_template)

节点：获取卡片视图选中数据
<p class="panel-title"><b>执行代码</b></p>

```javascript
const controllersMap = view.ctx.controllersMap;
const card_view = controllersMap.get("insight_reportcustom_card_view");
const selectdata = card_view.layoutPanel.panelItems.dataview.control.state.selectedData;
uiLogic.selecteddata = selectdata;
console.log(selectdata);

```
#### [效能报表(INSIGHT_REPORT)](module/Insight/insight_report)的处理逻辑[使用此模板(use_cur_template)](module/Insight/insight_report/uilogic/use_cur_template)

节点：设置上下文
<p class="panel-title"><b>执行代码</b></p>

```javascript
if(uiLogic.selecteddata && uiLogic.selecteddata.length >0){
    uiLogic.ctx.dynadashboard = uiLogic.selecteddata[0].dynadashboardid;
    uiLogic.dyna_dashboard_info = uiLogic.selecteddata[0];
    uiLogic.dyna_dashboard_info.insight_view_id = uiLogic.ctx.insight_view_id;
}
```
#### [效能报表(INSIGHT_REPORT)](module/Insight/insight_report)的处理逻辑[使用此模板(use_cur_template)](module/Insight/insight_report/uilogic/use_cur_template)

节点：关闭当前视图
<p class="panel-title"><b>执行代码</b></p>

```javascript
view.state.isLoading = false;
view.closeView();
```
#### [效能报表(INSIGHT_REPORT)](module/Insight/insight_report)的处理逻辑[使用此模板(use_cur_template)](module/Insight/insight_report/uilogic/use_cur_template)

节点：通知刷新
<p class="panel-title"><b>执行代码</b></p>

```javascript
ibiz.mc.command.create.send({ srfdecodename: 'insight_report'})
```
#### [效能报表(INSIGHT_REPORT)](module/Insight/insight_report)的处理逻辑[导出为pdf(export_pdf)](module/Insight/insight_report/uilogic/export_pdf)

节点：导出图片脚本
<p class="panel-title"><b>执行代码</b></p>

```javascript
const viewDom = document.getElementById(view.id);
if (viewDom) {
    const content = viewDom.querySelector('.ibiz-bi-report-panel-content>.el-collapse');
    const fileName = view.model.caption;
    ibiz.util.html2canvas.exportCanvas(content, { fileName });
}
```
#### [效能视图(INSIGHT_VIEW)](module/Insight/insight_view)的处理逻辑[计算表格列行为状态(insight)(calc_column_action_state)](module/Insight/insight_view/uilogic/calc_column_action_state)

节点：依据is_favorite显示星标按钮
<p class="panel-title"><b>执行代码</b></p>

```javascript
	const rows = uiLogic.grid.state.rows;
	if (rows && rows.length > 0) {
		rows.forEach(row => {
			const titleColumn = row.uiActionGroupStates.name;
			const is_favorite = row.data.is_favorite;
			if (titleColumn && Object.values(titleColumn).length > 0) {
				Object.values(titleColumn).forEach(action => {
					// 星标
					if (action.uiActionId === 'add_favorite@insight_view') {
						action.visible = is_favorite == 0;
					} else if (action.uiActionId === 'cancel_favorite@insight_view') {
						// 取消星标
						action.visible = is_favorite != 0;
					}
				})
			}
		})
	}

```
#### [效能视图(INSIGHT_VIEW)](module/Insight/insight_view)的处理逻辑[通知刷新(notify_refresh)](module/Insight/insight_view/uilogic/notify_refresh)

节点：通知刷新
<p class="panel-title"><b>执行代码</b></p>

```javascript
ibiz.mc.command.update.send({ srfdecodename: 'insight_view', srfkey: params.owner_id})
```
#### [效能视图(INSIGHT_VIEW)](module/Insight/insight_view)的处理逻辑[批量删除视图成员临时数据(remove_batch_temp)](module/Insight/insight_view/uilogic/remove_batch_temp)

节点：批量删除临时数据（临时）
<p class="panel-title"><b>执行代码</b></p>

```javascript
return (async function() { 
    // 获取所有临时数据
    const serviceUtil = ibiz.hub.getApp(context.srfappid).deService;
    const service = await serviceUtil.getService(context, 'web.insight_member');
    const list = service.local.getList();
    // 遍历临时数据删除
    list.forEach(item => {
        service.local.delete(context, item.id);
    })
    } 
)();

```
#### [成员(MEMBER)](module/Base/member)的处理逻辑[添加页面共享成员(add_shared_member)](module/Base/member/uilogic/add_shared_member)

节点：添加页面共享成员
<p class="panel-title"><b>执行代码</b></p>

```javascript
view.layoutPanel.panelItems.choose_member.setDataValue(null);
```
#### [通知事件(NOTIFY_EVENT)](module/extension/notify_event)的处理逻辑[保存列表多数据部件(save_list_mdctrl)](module/extension/notify_event/uilogic/save_list_mdctrl)

节点：更新列表数据
<p class="panel-title"><b>执行代码</b></p>

```javascript
const list = uiLogic.setting_model_list;
const items = list.getAllData() || [];
if (uiLogic.listservice) {
    uiLogic.listservice.updateBatch(list.context, items).then((res) => {
        if (res.data) {
            list.setData(res.data);
        }
        list.evt.emit('onSaveSuccess', undefined);
    })
}
```
#### [页面(PAGE)](module/Wiki/article_page)的处理逻辑[关闭评论区(close_comment)](module/Wiki/article_page/uilogic/close_comment)

节点：记录评论状态
<p class="panel-title"><b>执行代码</b></p>

```javascript
const operator = context.loginname;

localStorage.removeItem(operator);
```
#### [页面(PAGE)](module/Wiki/article_page)的处理逻辑[关闭评论区(close_comment)](module/Wiki/article_page/uilogic/close_comment)

节点：通知刷新
<p class="panel-title"><b>执行代码</b></p>

```javascript
ibiz.mc.command.create.send({ srfdecodename: 'article_page'})
```
#### [页面(PAGE)](module/Wiki/article_page)的处理逻辑[ai添加page(ai_add_page)](module/Wiki/article_page/uilogic/ai_add_page)

节点：注入脚本代码
<p class="panel-title"><b>执行代码</b></p>

```javascript

console.info("ai callback");
var answer = null;
var realView = view;
var _entity_tag = view.context._entity_tag;
if (realView.model.appDataEntityId && realView.model.appDataEntityId.endsWith("ai_agent_assignment")) {
    realView = view.parentView;
}
if (!_entity_tag) {
    _entity_tag = realView.model.appDataEntityId ? realView.model.appDataEntityId.split('.').at(-1) : "";
}
if (_entity_tag) {
    uiLogic.default._entity_tag = _entity_tag;
}
//var formController = realView.getController("form");
var curData = {};
var from = "from: AI智能体\n";
if (uiLogic.default.data && uiLogic.default.data.messages && uiLogic.default.data.messages.length > 0) {
    const lastAns = uiLogic.default.data.messages[uiLogic.default.data.messages.length - 1];
    answer = lastAns.realcontent;
    if(uiLogic.default.data.aiChat && 
        uiLogic.default.data.aiChat.appendCurData ) {
        curData = uiLogic.default.data.aiChat.appendCurData;
    }
      if(uiLogic.default.data.caption) {
        from = "from: "+uiLogic.default.data.caption+"\n";
    }
}
else if (uiLogic.default.msg) {
    answer = uiLogic.default.msg.realcontent;
    if(uiLogic.default.topic && uiLogic.default.topic.aiChat && 
        uiLogic.default.topic.aiChat.appendCurData ) {
        curData = uiLogic.default.topic.aiChat.appendCurData;
    }
    if(uiLogic.default.topic && uiLogic.default.topic.caption) {
        from = "from: "+uiLogic.default.topic.caption +"\n";
    }
}

uiLogic.entity = {};

var project  = realView.context.project ? realView.context.project : realView.context.product;
if (!project) {
     project = curData.project_id || curData.product_id;
}
if (!project) {
    ibiz.message.error('未找到关联的知识空间');
}
else  if (answer && typeof answer == 'string') {
    uiLogic.entity.name = curData.title || curData.name; 
    uiLogic.entity.content = from+answer;
    uiLogic.entity.project = project; 
}

```
#### [页面(PAGE)](module/Wiki/article_page)的处理逻辑[ai添加page(ai_add_page)](module/Wiki/article_page/uilogic/ai_add_page)

节点：注入脚本代码
<p class="panel-title"><b>执行代码</b></p>

```javascript
view.parentView.call("Refresh");
ibiz.message.success('已添加到知识空间');
uiLogic.result={content: "已添加到知识空间"};
```
#### [页面(PAGE)](module/Wiki/article_page)的处理逻辑[恢复历史版本并通知刷新(page_refresh)](module/Wiki/article_page/uilogic/page_refresh)

节点：通知刷新
<p class="panel-title"><b>执行代码</b></p>

```javascript
view.parentView.state.isLoading = false;
view.parentView.closeView();
ibiz.mc.command.send({srfdecodename: 'article_page',srfkey:uiLogic.context.article_page}, 'OBJECTUPDATED',uiLogic.form.triggerKey);
```
#### [页面(PAGE)](module/Wiki/article_page)的处理逻辑[复制共享链接(copy_shared_url)](module/Wiki/article_page/uilogic/copy_shared_url)

节点：复制共享链接
<p class="panel-title"><b>执行代码</b></p>

```javascript
var _default = uiLogic.default;
var shared_url = _default.shared_page_url;
if(shared_url !== null && shared_url !== undefined){
    var textArea = document.createElement("textarea");
    // 在 textarea 中放入需要复制的文本
    textArea.readOnly = true;
    textArea.value = shared_url;
    // 将 textarea 添加到 DOM 中
    document.body.appendChild(textArea);
    // 选中 textarea 中的文本
    textArea.select();
    // 执行复制命令
    var successful = document.execCommand('copy');
    var msg = successful ? '' : '复制失败';
    if(successful){
        util.message.success('复制共享链接成功');
    } else {
        util.message.error('复制共享链接失败!');
    }
} else {
    util.message.error('复制共享链接失败!');
}

```
#### [页面(PAGE)](module/Wiki/article_page)的处理逻辑[后续刷新(refresh)](module/Wiki/article_page/uilogic/refresh)

节点：注入脚本代码
<p class="panel-title"><b>执行代码</b></p>

```javascript
ibiz.mc.command.update.send({ srfdecodename: 'space', srfkey: uiLogic.default.id});
```
#### [页面(PAGE)](module/Wiki/article_page)的处理逻辑[添加附件数据(add_attachment)](module/Wiki/article_page/uilogic/add_attachment)

节点：设置附件参数
<p class="panel-title"><b>执行代码</b></p>

```javascript
// 计算新建默认值
const defaultData = uiLogic.grid.calcDefaultValue({}, true);
uiLogic.attach = uiLogic.files.map(item => 
    {
        return {
            name: item.name,
            file_id: item.id,
            id: item.uuid,
            ...defaultData,
        }
    }
)
```
#### [页面(PAGE)](module/Wiki/article_page)的处理逻辑[新建发布并通知刷新(save_notify_refresh)](module/Wiki/article_page/uilogic/save_notify_refresh)

节点：注入脚本代码
<p class="panel-title"><b>执行代码</b></p>

```javascript
//uiLogic.page_info = view.layoutPanel.panelItems.form.control.getReal();

const page_info = uiLogic.page_info;

console.info(page_info);

if(page_info.format_type === "HTML"  &&  page_info.html_description !== undefined){
    page_info.content = page_info.html_description;
}
if(page_info.format_type === "MD"  &&  page_info.md_description !== undefined){
    page_info.content = page_info.md_description;
}
if(page_info.format_type === "EXCEL" &&  page_info.excel_description !== undefined){
    page_info.content = page_info.excel_description;
}




```
#### [页面(PAGE)](module/Wiki/article_page)的处理逻辑[新建发布并通知刷新(save_notify_refresh)](module/Wiki/article_page/uilogic/save_notify_refresh)

节点：设置表单是否变更
<p class="panel-title"><b>执行代码</b></p>

```javascript
if (uiLogic.form) {
    uiLogic.form.state.modified = false;
}
```
#### [页面(PAGE)](module/Wiki/article_page)的处理逻辑[新建发布并通知刷新(save_notify_refresh)](module/Wiki/article_page/uilogic/save_notify_refresh)

节点：通知刷新
<p class="panel-title"><b>执行代码</b></p>

```javascript
ibiz.mc.command.send({srfdecodename: 'article_page'}, 'OBJECTCREATED');
```
#### [页面(PAGE)](module/Wiki/article_page)的处理逻辑[共享设置表单加载数据(shared_form_data)](module/Wiki/article_page/uilogic/shared_form_data)

节点：设置共享页面默认参数
<p class="panel-title"><b>执行代码</b></p>

```javascript

var form = view.layoutPanel.panelItems.form.control.details
var shared_scope = form.shared_scope;
var enable_password = form.enable_password;
var enable_expiration = form.enable_expiration;
var access_password = form.access_password;
var expiration_date = form.expiration_date;
var _url = uiLogic.default.shared_page_url;
if(_url !== null && _url !== undefined) {
    var shared_url = form.shared_page_url;
    shared_url.setDataValue(_url);
}
if(expiration_date.value !== null && expiration_date.value !== undefined) {
    enable_expiration.setDataValue(1);
} else {
    enable_expiration.setDataValue(0);
    var today = new Date();  // 获取当前日期
    // 获取 30 天后的日期
    var nextDate = new Date();
    nextDate.setDate(today.getDate() + 30);

    // 获取年、月、日
    var nextYear = nextDate.getFullYear();
    var nextMonth = ('0' + (nextDate.getMonth() + 1)).slice(-2);
    var nextDay = ('0' + nextDate.getDate()).slice(-2);
    // 格式化成 YYYY-MM-DD 的字符串
    var _date = nextYear + '-' + nextMonth + '-' + nextDay;
    expiration_date.setDataValue(_date);
}
if(access_password.value !== null && access_password.value !== undefined) {
    enable_password.setDataValue(1);
} else {
    enable_password.setDataValue(0);
    // 生成4位随机数
    var randomNumber = Math.floor(Math.random() * 9000) + 1000;
    access_password.setDataValue(randomNumber);
}

```
#### [页面(PAGE)](module/Wiki/article_page)的处理逻辑[显示评论区(show_commnet)](module/Wiki/article_page/uilogic/show_commnet)

节点：记录评论状态
<p class="panel-title"><b>执行代码</b></p>

```javascript
const operator = context.loginname;

localStorage.setItem(operator, 'true');
```
#### [核心产品功能(PSCOREPRDFUNC)](module/extension/PSCorePrdFunc)的处理逻辑[跳转设置页面(skip_setting)](module/extension/PSCorePrdFunc/uilogic/skip_setting)

节点：跳转
<p class="panel-title"><b>执行代码</b></p>

```javascript
const { settingurl } = uiLogic.default;

window.open(settingurl, '_self');

```
#### [核心产品功能(PSCOREPRDFUNC)](module/extension/PSCorePrdFunc)的处理逻辑[clone此应用(clone_git)](module/extension/PSCorePrdFunc/uilogic/clone_git)

节点：注入脚本代码
<p class="panel-title"><b>执行代码</b></p>

```javascript
var { httpurltorepo } = uiLogic.default;

var aux = document.createElement("textarea");
// aux.setAttribute("value", info); 
aux.value='git clone ' + httpurltorepo;
document.body.appendChild(aux); 
aux.select(); 
document.execCommand("copy"); 
document.body.removeChild(aux); 

util.message.success('复制成功!');
```
#### [核心产品功能(PSCOREPRDFUNC)](module/extension/PSCorePrdFunc)的处理逻辑[自定义版本安装(custom_version_info)](module/extension/PSCorePrdFunc/uilogic/custom_version_info)

节点：注入脚本代码
<p class="panel-title"><b>执行代码</b></p>

```javascript
console.log("custom version execed");
// ibiz.mc.command.create.send({ srfdecodename: 'PSCorePrdFunc'}, { triggerKey: 'specinstallbtn' });
if(view && view.parentView ){
    await view.parentView.callUIAction('Refresh');
}
```
#### [核心产品功能(PSCOREPRDFUNC)](module/extension/PSCorePrdFunc)的处理逻辑[准备版本数据(prepare_version_info)](module/extension/PSCorePrdFunc/uilogic/prepare_version_info)

节点：注入脚本代码
<p class="panel-title"><b>执行代码</b></p>

```javascript
console.log("prepare version data");
Object.assign(uiLogic.spec, uiLogic.view.state.srfactiveviewdata);
Object.assign(uiLogic.spec, uiLogic.default);
```
#### [核心产品功能(PSCOREPRDFUNC)](module/extension/PSCorePrdFunc)的处理逻辑[准备版本数据(prepare_version_info)](module/extension/PSCorePrdFunc/uilogic/prepare_version_info)

节点：注入脚本代码
<p class="panel-title"><b>执行代码</b></p>

```javascript
console.log("spec version execed");
// ibiz.mc.command.create.send({ srfdecodename: 'PSCorePrdFunc'}, { triggerKey: 'specinstallbtn' });
if(view && view.parentView ){
    await view.parentView.callUIAction('Refresh');
}
```
#### [核心产品功能(PSCOREPRDFUNC)](module/extension/PSCorePrdFunc)的处理逻辑[初始化插件信息(init_plugin_info)](module/extension/PSCorePrdFunc/uilogic/init_plugin_info)

节点：初始化
<p class="panel-title"><b>执行代码</b></p>

```javascript
var data = uiLogic.form.state.data;
var setting_json = JSON.parse(data.settings, null, 4);
data.rt_object_repo = setting_json.rTObjectRepo || "";
data.plugin_code = setting_json.pluginCode || "";
```
#### [核心产品功能(PSCOREPRDFUNC)](module/extension/PSCorePrdFunc)的处理逻辑[跳转gitlab(skip_gitlab)](module/extension/PSCorePrdFunc/uilogic/skip_gitlab)

节点：跳转
<p class="panel-title"><b>执行代码</b></p>

```javascript
const { httpurltorepo } = uiLogic.default;
window.open(httpurltorepo, '_blank');
```
#### [核心产品功能(PSCOREPRDFUNC)](module/extension/PSCorePrdFunc)的处理逻辑[更新插件设置(update_plugin_setting)](module/extension/PSCorePrdFunc/uilogic/update_plugin_setting)

节点：更新settings字段
<p class="panel-title"><b>执行代码</b></p>

```javascript
var rt_object_repo = uiLogic.default.rt_object_repo;
var data = uiLogic.form.state.data;
var setting_json = JSON.parse(data.settings);
setting_json.rTObjectRepo = rt_object_repo;
data.settings = JSON.stringify(setting_json, null, 4);
```
#### [实体处理逻辑(PSDELOGIC)](module/extension/PSDELogic)的处理逻辑[webhook调试(debug_webhook)](module/extension/PSDELogic/uilogic/debug_webhook)

节点：执行webhook调试
<p class="panel-title"><b>执行代码</b></p>

```javascript
var _default = uiLogic.default;
const webhookurl=_default.webhookurl;
const webhookdebugparams=_default.webhookdebugparams  || {} ;
const url = new URL(webhookurl);
const headers = {
    "Content-Type": "application/json"
};

fetch(url, {
    method: 'POST',
    headers: headers,
    body: webhookdebugparams
});

ibiz.message.success('执行指令已发出...');

```
#### [最近访问(RECENT)](module/Base/recent)的处理逻辑[最近访问跳转其他视图(recent_jump_other_view)](module/Base/recent/uilogic/recent_jump_other_view)

节点：获取选中数据详情
<p class="panel-title"><b>执行代码</b></p>

```javascript
let selecteddata=uiLogic.selecteddata;
if (selecteddata.length > 0) {
    uiLogic.selectobj = selecteddata[0];
}
```
#### [共享空间(SHARED_SPACE)](module/Wiki/shared_space)的处理逻辑[复制共享链接(copy_shared_url)](module/Wiki/shared_space/uilogic/copy_shared_url)

节点：复制共享链接
<p class="panel-title"><b>执行代码</b></p>

```javascript
var _default = uiLogic.default;
var shared_url = _default.shared_url;
if(shared_url !== null && shared_url !== undefined){
    var textArea = document.createElement("textarea");
    // 在 textarea 中放入需要复制的文本
    textArea.value = shared_url;
    // 将 textarea 添加到 DOM 中
    document.body.appendChild(textArea);
    // 选中 textarea 中的文本
    textArea.select();
    // 执行复制命令
    var successful = document.execCommand('copy');
    var msg = successful ? '' : '复制失败';
    if(successful){
        util.message.success('复制共享链接成功');
    } else {
        util.message.error('复制共享链接失败!');
    }
} else {
    util.message.error('复制共享链接失败!');
}

```
#### [共享空间(SHARED_SPACE)](module/Wiki/shared_space)的处理逻辑[后续刷新(refresh)](module/Wiki/shared_space/uilogic/refresh)

节点：注入脚本代码
<p class="panel-title"><b>执行代码</b></p>

```javascript
ibiz.mc.command.update.send({ srfdecodename: 'space', srfkey: uiLogic.default.id});
```
#### [空间(SPACE)](module/Wiki/space)的处理逻辑[计算表格列行为状态(space)(calc_column_action_state)](module/Wiki/space/uilogic/calc_column_action_state)

节点：计算表格列行为状态
<p class="panel-title"><b>执行代码</b></p>

```javascript
	const rows = uiLogic.grid.state.rows;
	if (rows && rows.length > 0) {
		rows.forEach(row => {
			const titleColumn = row.uiActionGroupStates.name;
			const is_favorite = row.data.is_favorite;
			if (titleColumn && Object.values(titleColumn).length > 0) {
				Object.values(titleColumn).forEach(action => {
					// 收藏
					if (action.uiActionId === 'add_favorite@space') {
						action.visible = is_favorite == 0;
					} else if (action.uiActionId === 'cancel_favorite@space') {
						// 取消收藏
						action.visible = is_favorite != 0;
					}
				})
			}
		})
	}

```
#### [空间(SPACE)](module/Wiki/space)的处理逻辑[批量删除空间成员临时数据(remove_batch_temp)](module/Wiki/space/uilogic/remove_batch_temp)

节点：批量删除临时数据（临时）
<p class="panel-title"><b>执行代码</b></p>

```javascript
return (async function() { 
    // 获取所有临时数据
    const serviceUtil = ibiz.hub.getApp(context.srfappid).deService;
    const service = await serviceUtil.getService(context, 'plmweb.space_member');
    const list = service.local.getList();
    // 遍历临时数据删除
    list.forEach(item => {
        service.local.delete(context, item.id);
    })
    } 
)();

```
#### [空间(SPACE)](module/Wiki/space)的处理逻辑[刷新当前表格(refresh_current_grid)](module/Wiki/space/uilogic/refresh_current_grid)

节点：通过实体刷新表格、树
<p class="panel-title"><b>执行代码</b></p>

```javascript
ibiz.mc.command.update.send({ srfdecodename: 'space', srfkey: params.owner_id})
```
#### [空间(SPACE)](module/Wiki/space)的处理逻辑[刷新当前表格(refresh_current_grid)](module/Wiki/space/uilogic/refresh_current_grid)

节点：刷新视图
<p class="panel-title"><b>执行代码</b></p>

```javascript
view.call('Refresh');
setTimeout(() => {
    if (view.layoutPanel.panelItems.nav_pos && view.layoutPanel.panelItems.nav_pos.curNavViewMsg) {
        // 找到当前的右侧视图
        const viewId = view.layoutPanel.panelItems.nav_pos.curNavViewMsg.viewId;
        if (viewId) {
            const key = viewId.split('.').pop();
            const viewPos = view.getController(key);
            if (viewPos) {
                viewPos.call('Refresh');
            }
        }
    }
}, 300)
```
#### [空间成员(SPACE_MEMBER)](module/Wiki/space_member)的处理逻辑[新建空间默认临时成员(create_default_temp_members)](module/Wiki/space_member/uilogic/create_default_temp_members)

节点：创建临时数据
<p class="panel-title"><b>执行代码</b></p>

```javascript
ibiz.hub.getApp(context.srfappid).deService.exec(
    'plmweb.space_member',
    'Create',
    context,
    uiLogic.user,
);
```
#### [页面模板(STENCIL)](module/Wiki/stencil)的处理逻辑[发布(release)](module/Wiki/stencil/uilogic/release)

节点：获取表单数据
<p class="panel-title"><b>执行代码</b></p>

```javascript
// uiLogic.stencil = view.layoutPanel.panelItems.form.control.getReal()[0];

const stencil = uiLogic.stencil;

console.info(stencil);

if(stencil.format_type === "HTML"  &&  stencil.html_description !== undefined){
    stencil.content = stencil.html_description;
}
if(stencil.format_type === "MD"  &&  stencil.md_description !== undefined){
    stencil.content = stencil.md_description;
}
if(stencil.format_type === "EXCEL" &&  stencil.excel_description !== undefined){
    stencil.content = stencil.excel_description;
}



```
#### [页面模板(STENCIL)](module/Wiki/stencil)的处理逻辑[打开新建页面并关闭模板中心(open_new_page)](module/Wiki/stencil/uilogic/open_new_page)

节点：设置上下文
<p class="panel-title"><b>执行代码</b></p>

```javascript
if(uiLogic.selecteddata && uiLogic.selecteddata.length >0){
    uiLogic.context.stencil_id = uiLogic.selecteddata[0].id;
    uiLogic.stencil_info = uiLogic.selecteddata[0];
    uiLogic.stencil_info.space_id = uiLogic.context.stencil_space;

}
```
#### [页面模板(STENCIL)](module/Wiki/stencil)的处理逻辑[打开新建页面并关闭模板中心(open_new_page)](module/Wiki/stencil/uilogic/open_new_page)

节点：关闭当前视图
<p class="panel-title"><b>执行代码</b></p>

```javascript
view.state.isLoading = false;
view.closeView();

```
#### [企业用户(USER)](module/Base/user)的处理逻辑[修改密码（表单）(change_pas)](module/Base/user/uilogic/change_pas)

节点：校验表单
<p class="panel-title"><b>执行代码</b></p>

```javascript
(async function() { 
const bol = await uiLogic.form.validate();
if (bol) {
    const {old_password,new_password,sure_password} = uiLogic.default;
    const result = await ibiz.appUtil.changePwd(old_password,new_password,{surePwd: sure_password})
    if (result && result.ok) {
      ibiz.message.success('修改密码成功');
    } else {
      ibiz.message.error(`修改密码失败`);
    }
} else {
    ibiz.message.error('请检查表单填写！');
}
} )();
```
#### [企业用户(USER)](module/Base/user)的处理逻辑[删除部门(trash_dept)](module/Base/user/uilogic/trash_dept)

节点：提示移除成员后才可删除
<p class="panel-title"><b>执行代码</b></p>

```javascript
const bol = await util.confirm.warning({
  title: '提示',
  desc: '请移除该部门下成员才可删除！',
});
```
#### [企业用户(USER)](module/Base/user)的处理逻辑[删除部门(trash_dept)](module/Base/user/uilogic/trash_dept)

节点：提示移除下级部门
<p class="panel-title"><b>执行代码</b></p>

```javascript
const bol = await util.confirm.warning({
  title: '提示',
  desc: '请先移除下级部门后才可删除！',
});
```




