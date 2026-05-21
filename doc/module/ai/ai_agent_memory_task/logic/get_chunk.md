## 获取记忆分块 <!-- {docsify-ignore-all} -->

   

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
state "开始" as Begin <<start>> [[$./get_chunk#begin {"开始"}]]
state "获取记忆分块" as RAWSFCODE_01  [[$./get_chunk#rawsfcode_01 {"获取记忆分块"}]]
state "结束" as END_01 <<end>> [[$./get_chunk#end_01 {"结束"}]]


Begin --> RAWSFCODE_01 : [[$./get_chunk#begin-rawsfcode_01{连接名称} 连接名称]]
RAWSFCODE_01 --> END_01


@enduml
```


### 处理步骤说明

#### 开始 :id=Begin<sup class="footnote-symbol"> <font color=gray size=1>[开始]</font></sup>



*- N/A*
#### 获取记忆分块 :id=RAWSFCODE_01<sup class="footnote-symbol"> <font color=gray size=1>[直接后台代码]</font></sup>



<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
def _default = logic.param('default').getReal()
def _chunk= logic.param('chunk').getReal()
def log = org.apache.commons.logging.LogFactory.getLog("cn.ibizlab.central.core.dataentity.logic.DELogicRuntimeBase")
def kb_tag = _default.get("kb_tag")
def doc_id = _default.get("doc_id")
def chunk_id = _default.get("chunk_id")
if (!kb_tag || !doc_id|| !chunk_id ) {
    log.debug("缺少记忆知识库、文档标识或分块标识，忽略获取记忆分块")
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
def kb_chunk = sys.getSysKBUtilRuntime(false).getChunk(kb_config, doc_id,chunk_id)
kb_chunk.copyTo(_chunk)

```

#### 结束 :id=END_01<sup class="footnote-symbol"> <font color=gray size=1>[结束]</font></sup>



返回 `chunk(记忆分块)`


### 连接条件说明
#### 连接名称 :id=Begin-RAWSFCODE_01

`Default(传入变量).chunk_id` ISNOTNULL


### 实体逻辑参数

|    中文名   |    代码名    |  数据类型    |  实体   |备注 |
| --------| --------| -------- | -------- | --------   |
|传入变量(<i class="fa fa-check"/></i>)|Default|数据对象|[智能体记忆任务实例(AI_AGENT_MEMORY_TASK)](module/ai/ai_agent_memory_task.md)||
|记忆分块|chunk|数据对象|||
