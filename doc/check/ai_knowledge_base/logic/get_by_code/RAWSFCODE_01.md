<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
def defaultEntity = logic.param("default").getReal();
def filter = logic.param("filter").getReal();

def kbtags=defaultEntity.get("kb_tag")
if(!kbtags)
    kbtags=defaultEntity.get("id")

def ids =[kbtags].flatten().findAll().collectMany { it.toString().replaceAll(/[\[\]\"]/, "").split(',')*.trim() }.findAll { it }.collect { it.split("-kb--")[-1] }


//def knowledge_base_runtime = sys.dataentity('ai_knowledge_base')
//knowledge_base = knowledge_base_runtime.get(kbids[0])
if(ids) {
    defaultEntity.set("id",ids[0])
    if(ids.size()>1)  {
        filter.set("n_id_in",ids)
    }
}

```
