<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
def _defualt = logic.param('Default').getReal()
def kb_list = logic.param('kb_list').getReal()
def kb_ids = _defualt.get('kb_ids')
if(kb_ids) {
    def kb_runtime = sys.dataentity('AI_KNOWLEDGE_BASE')
    groovy.json.JsonSlurper jsonParser = new groovy.json.JsonSlurper()
    def kbs = jsonParser.parseText(kb_ids)
    if (kbs.size() > 0) {
        kbs.each { it ->
            def kb = kb_runtime.entity()
            kb.set('id', it.get('id'))
            kb.set('agenttag', _defualt.get('code_name'))
            kb_list.add(kb)
        }
    }    
}

```
