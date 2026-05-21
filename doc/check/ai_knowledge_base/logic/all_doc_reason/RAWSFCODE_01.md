<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
def _all_reason_content = logic.param("all_reason_content").getReal();
def _doc_reason_list = logic.param("doc_reason_list").getReal();
      
//def dataList = new groovy.json.JsonSlurper().parseText(_doc_reason_list)
//def allContent = _doc_reason_list.collect { it.content ?: '' }.join('\n')

def allContent = _doc_reason_list.collect { item ->
    def docname = item.name ?: 'unknown'
    def content = item.content ?: ''
"""\
# 分段资料：${docname}
```
${item.content}
```
---\
"""
}.join('\n')

_all_reason_content.set('fullcontent',allContent)

println "------------------------allContent：" + allContent

```
