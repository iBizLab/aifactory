<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
def defaultEntity = logic.param("default").getReal()
if(!defaultEntity.get("page_index")) {
    defaultEntity.set("page_index",0)
}
def context_content = "\n---\n\n* **执行智能体**: "+defaultEntity.get("name") +"\n"
if(defaultEntity.get("description")){
    context_content = context_content+"* **智能体描述**: " + defaultEntity.get("description") +"\n"
}
context_content = context_content +"\n---\n"
defaultEntity.set("context_content",context_content)
```
