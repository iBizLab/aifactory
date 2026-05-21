<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
        def processedDocs = logic.param("doc_fulltext").getReal();
        
        def splitContent
        splitContent = { String text, int limit ->
            def res = []
            def start = 0
            while (start < text.length()) {
                int end = Math.min(start + limit, text.length())
                // 尽量找换行符切分，避免切断句子
                if (end < text.length()) {
                    int lastNewline = text.lastIndexOf("\n", end)
                    if (lastNewline > start) end = lastNewline
                }
                res << text.substring(start, end).trim()
                start = end
            }
            return res
        }


        def MAX_CHARS = 25600
        def allGroups = []
        def currentGroup = []
        def currentGroupSize = 0

        def flatFragments = []

        processedDocs.each { doc ->

            def content = doc.content
            def docName = doc.name

            if (content.length() > MAX_CHARS) {
                // 超大文档：切分成多个虚拟片段对象
                def parts = splitContent(content, MAX_CHARS)
                parts.eachWithIndex { text, index ->
                    flatFragments << [name: docName, content: text, part: index + 1]
                }
            } else {
                // 普通文档
                flatFragments << [name: docName, content: content, part: null]
            }
        }

        flatFragments.each { frag ->
            if (currentGroupSize + frag.content.length() > MAX_CHARS) {
                if (currentGroup) {
                    allGroups << currentGroup
                }
                currentGroup = [frag]
                currentGroupSize = frag.content.length()
            } else {
                currentGroup << frag
                currentGroupSize += frag.content.length()
            }
        }
        if (currentGroup) allGroups << currentGroup

        def chunks = logic.param("fulltext_chunk_list").getReal();

        chunks.clear()

        int sn = 1
        allGroups.each { group ->
            chunks << [sn: sn++, content:
                group.collect { item ->
                    def partAttr = item.part ? " part=\"${item.part}\"" : ""
                    "<doc name=\"${item.name}\"${partAttr}>\n${item.content}\n</doc>"
                }.join("\n\n")
            ]
        }

        processedDocs.clear()
```
