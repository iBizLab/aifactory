<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
        def _doc_list = logic.param("doc_list").getReal();
        def kb_doc_runtime = sys.dataentity('ai_kb_document')
        def _doc_fulltext = logic.param("doc_fulltext").getReal();

        _doc_fulltext.clear()
        
        _doc_list.each { doc ->
            def text = kb_doc_runtime.executeAction("get_full_text", null, doc)
            _doc_fulltext.add( [
                    name: (doc.get("categories") ? (doc.get("categories") + "/") : "") + doc.get("name"),
                    content: text ?: ""
            ]
            )
        }


```
