<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
def values = []
//doc_id为知识库标识||业务范围标识||用户标识合成
def _default = logic.param('default').getReal()
def kb_tag = _default.get("kb_tag")
def mode = _default.get("memory_isolation_mode")
if(kb_tag){
    values.add(kb_tag)
    def user_id = _default.get("user_id")?_default.get("user_id"):"undefined"
    def scope = _default.get("scope")?_default.get("scope"):"undefined"
    if (!mode || mode == "NONE") {
        values.add("__global__")
        values.add("__global__")
        _default.set("doc_path", "/__global__/__global__/")
    } 
    else if (mode == "BUSINESS_SCOPE") {
        values.add(scope)
        values.add("__global__")
        _default.set("doc_path", "/${scope}/__global__/")
    } 
    else if (mode == "USER_SCOPE") {
        values.add("__global__")
        values.add(user_id)
        _default.set("doc_path", "/__global__/${user_id}/")
    } 
    else if (mode == "BUSINESS_USER_SCOPE") {
        values.add(scope)
        values.add(user_id)
        _default.set("doc_path", "/${scope}/${user_id}/")
    }  else {
        //未识别按默认处理
        values.add("__global__")
        values.add("__global__")
        _default.set("doc_path", "/__global__/__global__/")
    }
    _default.set("doc_id",net.ibizsys.runtime.util.KeyValueUtils.genUniqueId(values.toArray()))
    }
```
