<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
def _default = logic.param('default').getReal()
def _chunk= logic.param('chunk').getReal()
def log = org.apache.commons.logging.LogFactory.getLog("cn.ibizlab.central.core.dataentity.logic.DELogicRuntimeBase")
def chunk_id = _default.get("id")
def _name = _default.get("name")
def kb_tag =  _default.get("kbid")
def doc_id = _default.get("docid")
def content = _default.get("content")

println "\n--- 保存记忆分块传入数据 ---\n${_default}"
if (!kb_tag || !doc_id|| !chunk_id ) {
    log.debug("缺少记忆知识库、文档标识或分块标识，忽略保存记忆分块")
    return 
}
_chunk = new net.ibizsys.central.cloud.core.util.domain.Chunk()
_chunk.set("id",chunk_id)
_chunk.set("name",_name)
_chunk.set("type","MANUAL")
_chunk.set("kbid",kb_tag)
_chunk.set("docid",doc_id)
_chunk.set("content",content)
def system_id = sys.getDeploySystemId()
if(sys instanceof net.ibizsys.central.cloud.core.IServiceSystemRuntime) {
    def iServiceSystemRuntime = (net.ibizsys.central.cloud.core.IServiceSystemRuntime)sys
    if(iServiceSystemRuntime.getMainSystemId()) {
        system_id = iServiceSystemRuntime.getMainSystemId();
    }
}
def kb_config = "${system_id}-kb--${kb_tag}"
def kb_chunk = sys.getSysKBUtilRuntime(false).saveChunk(kb_config, doc_id,chunk_id,_chunk)
kb_chunk.copyTo(_chunk)
```
