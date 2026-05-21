<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
def _default = logic.param('default').getReal()
def log = org.apache.commons.logging.LogFactory.getLog("cn.ibizlab.central.core.dataentity.logic.DELogicRuntimeBase")
def kb_tag = _default.get("kb_tag")
def doc_id = _default.get("doc_id")
def doc_path = _default.get("doc_path")
def _document
if (!kb_tag || !doc_id) {
    log.debug("缺少记忆知识库或文档标识，忽略获取记忆文档")
    return 
}
def system_id = sys.getDeploySystemId()
if(sys instanceof net.ibizsys.central.cloud.core.IServiceSystemRuntime) {
    def iServiceSystemRuntime = (net.ibizsys.central.cloud.core.IServiceSystemRuntime)sys
    if(iServiceSystemRuntime.getMainSystemId()) {
        system_id = iServiceSystemRuntime.getMainSystemId();
    }
}
def kb_config = "${system_id}-kb--${kb_tag}"
try{
    _document = sys.getSysKBUtilRuntime(false).getDocument(kb_config, doc_id)
}catch(Exception e){
    log.debug("获取记忆知识库文档失败, ${doc_id}")
}
if(!_document){
   _document = new net.ibizsys.central.cloud.core.util.domain.Document()
   _document.set("id",doc_id)
   _document.set("name","Memory.md")
   _document.set("type","file")
   _document.set("kb_id",kb_tag)
   _document.set("categories",doc_path)
    sys.getSysKBUtilRuntime(false).saveDocument(kb_config, doc_id,_document)
}
```
