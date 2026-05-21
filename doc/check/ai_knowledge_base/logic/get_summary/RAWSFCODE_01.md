<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
    def defaultEntity = logic.param("default").getReal();
        def chunks = logic.param("chunks").getReal();
        def clusters = logic.param("cluster").getReal();
        List docs = new ArrayList()
        def sb = new StringBuilder()
        def header = new StringBuilder()
        def paragraph = new StringBuilder()
        def sbTOC = new StringBuilder()
        def summary = new StringBuilder()
        def cluster = new StringBuilder()
        def footer = new StringBuilder()
        boolean summarized = false

        if(defaultEntity.get("name")) {
            sb.append("# ${defaultEntity.name}\n")
            if (defaultEntity.get("description")) {
                sb.append("## 摘要\n${defaultEntity.description}\n")
                sb.append("\n---\n\n")
            }
            header.append(sb.toString())
        }
        if(clusters) {
            clusters.forEach { item ->
                if (item.get("document_name")) {
                    sb.append("## ${item.document_name}\n")
                    if (item.get("categories"))
                        sb.append("* **目录**: ${item.categories}\n")
                    sb.append("* **文档ID**: ${item.document_id}\n")

                    if (item.get("content")) {
                        sb.append("### 摘要\n${item.content}\n")
                    }
                    sb.append("\n---\n\n")
                }

            }
            if(sb.length()<12288) {
                header = new StringBuilder()
                header.append(sb.toString())
            }
        }
        if(chunks) {
            chunks.forEach { chunk ->
                if(chunk.get("content")) {
                    try{
                        def doc = new groovy.json.JsonSlurper().parseText(chunk.get("content"))
                        doc["document_id"] = chunk.get("document_id")
                        doc['document_name'] = chunk.get("document_name")
                        doc['categories'] = chunk.get("categories")
                        docs.add(doc)

                    }catch (Exception ex) {}
                }
            }

            def lastDocId = ""

            docs.eachWithIndex { doc, index ->
                if(!lastDocId.equalsIgnoreCase(doc.document_id)) {
                    paragraph.append("\n---\n\n")
                    paragraph.append("## ${doc.document_name}\n")
                    paragraph.append("\n* **文档ID**: ${doc.document_id}\n\n")
                    if (doc.get("categories"))
                        paragraph.append("* **目录**: ${doc.categories}\n\n")

                    paragraph.append("| 章节名称 | 页码范围 |\n")
                    paragraph.append("| :--- | :--- |\n")
                    lastDocId = doc.document_id

                }

                def range = doc.page_range ? "${doc.page_range.start} - ${doc.page_range.end}" : "N/A"
                doc.row_num = index + 1
                doc.range = range
                paragraph.append("| ${doc.document_title} | ${doc.range} |\n")
            }


            if(!summarized && paragraph.length()>16384) {
                summarized = true
                summary.append(header.toString())
                summary.append(paragraph.toString())
            }




            // --- 2. 内部递归辅助闭包 ---
            // 闭包 A: 生成树状小目录
            def generateTOC
            generateTOC = { items, depth, row_num, maxDepth ->
                def tocText = ""
                items.each { item ->
                    def range = item.location ? "${item.location.start} - ${item.location.end}" : "N/A"
                    item.range = range
                    tocText += "  " * depth + "- ${row_num}.${item.id} ${item.title} (${item.range})\n"
                    if (item.children && depth<maxDepth) tocText += generateTOC(item.children, depth + 1, row_num, maxDepth)
                }
                return tocText
            }

            // 闭包 B: 生成详细内容块
            def processDetails
            processDetails = { items, parentPath, docTitle, row_num ->
                def detailText = ""
                items.each { item ->
                    def currentPath = parentPath ? "${parentPath} > ${item.title}" : "${docTitle} > ${item.title}"
                    def level = currentPath.split(" > ").size() + 1

                    detailText += "#${'#' * level} ${row_num}.${item.id} ${item.title}\n"
                    detailText += "- **位置**: ${item.range}\n"
                    if (item.summary) detailText += "- **摘要**: ${item.summary}\n"


                    if (item.children) detailText += processDetails(item.children, currentPath, docTitle, row_num)
                }
                return detailText
            }



            lastDocId = ""
            // --- 3. 遍历文档构建全文 ---
            docs.each { doc ->
                if(!lastDocId.equalsIgnoreCase(doc.document_id)) {
                    sbTOC.append("\n---\n\n")
                    sbTOC.append("## ${doc.document_name} 目录清单\n")
                    sbTOC.append("\n* **文档ID**: ${doc.document_id}\n\n")
                    if (doc.get("categories"))
                        sbTOC.append("* **目录**: ${doc.categories}\n\n")
                    lastDocId = doc.document_id
                }
                // 插入局部小目录
                sbTOC.append("- ${doc.row_num} ${doc.document_title} (${doc.range})\n")
                sbTOC.append(generateTOC(doc.index, 1, doc.row_num, 4))

            }



            lastDocId = ""
            // --- 3. 遍历文档构建全文 ---
            docs.each { doc ->

                if(!lastDocId.equalsIgnoreCase(doc.document_id)) {
                    footer.append("\n---\n\n")
                    footer.append("## ${doc.document_name} 章节简介\n")
                    footer.append("\n* **文档ID**: ${doc.document_id}\n\n")
                    if (doc.get("categories"))
                        footer.append("* **目录**: ${doc.categories}\n\n")
                    lastDocId = doc.document_id
                }

                footer.append("### ${doc.row_num} ${doc.document_title}\n")

                footer.append("- **位置**: ${doc.range}\n")

                // 插入详细层级内容
                footer.append(processDetails(doc.index, "", doc.document_title, doc.row_num))


                footer.append("\n---\n\n")

            }

            if(!summarized && footer.length()<16384) {
                summarized = true
                summary.append(header.toString())
                summary.append(footer.toString())
            }

            sb.append(footer.toString())


            if(!summarized) {
                summarized = true
                if(sbTOC.length()>16384) {
                    sbTOC = new StringBuilder()
                    lastDocId = ""
                    docs.each { doc ->
                        if(!lastDocId.equalsIgnoreCase(doc.document_id)) {
                            sbTOC.append("\n---\n\n")
                            sbTOC.append("## ${doc.document_name} 目录清单\n")
                            sbTOC.append("\n* **文档ID**: ${doc.document_id}\n\n")
                            if (doc.get("categories"))
                                sbTOC.append("* **目录**: ${doc.categories}\n\n")
                            lastDocId = doc.document_id
                        }
                        // 插入局部小目录
                        sbTOC.append("- ${doc.row_num} ${doc.document_title} (${doc.range})\n")
                        sbTOC.append(generateTOC(doc.index, 1, doc.row_num, 2))
                    }
                }
                if(sbTOC.length()>16384) {
                    sbTOC = new StringBuilder()
                    lastDocId = ""
                    docs.each { doc ->
                        if(!lastDocId.equalsIgnoreCase(doc.document_id)) {
                            sbTOC.append("\n---\n\n")
                            sbTOC.append("## ${doc.document_name} 目录清单\n")
                            sbTOC.append("\n* **文档ID**: ${doc.document_id}\n\n")
                            if (doc.get("categories"))
                                sbTOC.append("* **目录**: ${doc.categories}\n\n")
                            lastDocId = doc.document_id
                        }
                        // 插入局部小目录
                        sbTOC.append("- ${doc.row_num} ${doc.document_title} (${doc.range})\n")
                        sbTOC.append(generateTOC(doc.index, 1, doc.row_num, 1))
                    }
                }
                if(sbTOC.length()>16384) {
                    sbTOC = new StringBuilder()
                    sbTOC.append(paragraph.toString())
                }
                summary.append(header.toString())
                summary.append(sbTOC.toString())
            }




            defaultEntity.set("page_index_info", sb.toString())
        }
        if(!summarized) {
            summary.append(sb.toString())
        }
        defaultEntity.set("summary", summary.toString())
```
