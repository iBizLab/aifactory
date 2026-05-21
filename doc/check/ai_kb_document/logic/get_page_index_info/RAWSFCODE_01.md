<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
        def defaultEntity = logic.param("default").getReal();
        def chunks = logic.param("chunks").getReal();
        List docs = new ArrayList()
        def sb = new StringBuilder()
        def header = new StringBuilder()
        def paragraph = new StringBuilder()
        def sbTOC = new StringBuilder()
        def summary = new StringBuilder()
        def footer = new StringBuilder()
        boolean summarized = false

        if(defaultEntity.get("name")) {
            sb.append("# ${defaultEntity.name}\n")
            if (defaultEntity.get("kb_name")) {
                sb.append("<details><summary>所属: ${defaultEntity.kb_name}")
                if (defaultEntity.get("categories"))
                    sb.append("/${defaultEntity.categories}")
                sb.append("</summary>【文档ID】: ${defaultEntity.id}")
                sb.append("</details>\n\n")

                if (defaultEntity.get("intelligent_analysis")) {
                    sb.append("## 摘要\n${defaultEntity.intelligent_analysis}\n")
                }
                sb.append("\n---\n\n")
            }
            header.append(sb.toString())
        }
        if(chunks) {
            chunks.forEach { chunk ->
                if(chunk.get("content")) {
                    try{
                        def doc = new groovy.json.JsonSlurper().parseText(chunk.get("content"))
                        doc["document_id"] = chunk.get("document_id")
                        doc['document_name'] = chunk.get("document_name")
                        docs.add(doc)

                    }catch (Exception ex) {}
                }
            }

            paragraph.append("## 章节索引\n")
            paragraph.append("| 章节名称 | 页码范围 |\n")
            paragraph.append("| :--- | :--- |\n")
            docs.eachWithIndex { doc, index ->
                def range = doc.page_range ? "${doc.page_range.start} - ${doc.page_range.end}" : "N/A"
                doc.row_num = index + 1
                doc.range = range
                paragraph.append("| ${doc.row_num} ${doc.document_title} | ${doc.range} |\n")
            }


            if(!summarized && header.length()+paragraph.length()>16384) {
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


            sbTOC.append("## 目录清单\n")
            // --- 3. 遍历文档构建全文 ---
            docs.each { doc ->
                // 插入局部小目录
                sbTOC.append("- ${doc.row_num} ${doc.document_title} (${doc.range})\n")
                sbTOC.append(generateTOC(doc.index, 1, doc.row_num, 4))

            }



            footer.append("## 章节简介\n")
            // --- 3. 遍历文档构建全文 ---
            docs.each { doc ->

                footer.append("### ${doc.row_num} ${doc.document_title}\n")

                footer.append("- **位置**: ${doc.range}\n")

                // 插入详细层级内容
                footer.append(processDetails(doc.index, "", doc.document_title, doc.row_num))


                footer.append("\n---\n\n")

            }

            if(!summarized && header.length()+footer.length()<16384) {
                summarized = true
                summary.append(header.toString())
                summary.append(footer.toString())
            }

            sb.append(footer.toString())


            if(!summarized) {
                summarized = true
                if(header.length()+sbTOC.length()>16384) {
                    sbTOC = new StringBuilder()
                    sbTOC.append("## 目录清单\n")
                    docs.each { doc ->
                        // 插入局部小目录
                        sbTOC.append("- ${doc.row_num} ${doc.document_title} (${doc.range})\n")
                        sbTOC.append(generateTOC(doc.index, 1, doc.row_num, 2))
                    }
                }
                if(header.length()+sbTOC.length()>16384) {
                    sbTOC = new StringBuilder()
                    sbTOC.append("## 目录清单\n")
                    docs.each { doc ->
                        // 插入局部小目录
                        sbTOC.append("- ${doc.row_num} ${doc.document_title} (${doc.range})\n")
                        sbTOC.append(generateTOC(doc.index, 1, doc.row_num, 1))
                    }
                }
                if(header.length()+sbTOC.length()>16384) {
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
