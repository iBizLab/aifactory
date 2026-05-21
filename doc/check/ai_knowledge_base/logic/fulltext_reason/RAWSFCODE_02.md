<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
def _full_doc_list = logic.param("full_doc_list").getReal();
def _doc_fulltext = logic.param("doc_fulltext").getReal();

def mergedDocument  = _full_doc_list.collect { doc ->
    def header = "---${doc.name}---"
    "$header\n${doc.analysis_content}"
}.join('\n\n')  // 用两个换行分隔不同文档

_doc_fulltext = mergedDocument

println "------------------------doc_fulltext：" + _doc_fulltext
```
