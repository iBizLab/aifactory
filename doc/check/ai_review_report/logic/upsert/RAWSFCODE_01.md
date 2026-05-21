<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
def defaultEntity = logic.param("default").getReal();

String unionId=""
if (defaultEntity.get("kb_id"))
    unionId+=defaultEntity.getString("kb_id","")
if (defaultEntity.get("document_id"))
    unionId+=("||"+defaultEntity.getString("document_id",""))
if (defaultEntity.get("record_id"))
    unionId+=("||"+defaultEntity.getString("record_id",""))
if(!unionId)
    org.springframework.util.Assert.hasLength(unionId,"未传入审查对象");
if (defaultEntity.get("agent_tag"))
    unionId+=("||"+defaultEntity.getString("agent_tag",""))
defaultEntity.set("id",net.ibizsys.runtime.util.KeyValueUtils.genUniqueId(unionId))

```
