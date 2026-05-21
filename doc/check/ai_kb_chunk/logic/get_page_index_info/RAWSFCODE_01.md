<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
def chunk = logic.param("default").getReal();
try{


        def sb = new StringBuilder()

        def doc = new groovy.json.JsonSlurper().parseText(chunk.get("content"))
        def processDetails
        processDetails = { items, parentPath, docTitle, row_num ->
            def detailText = ""
            items.each { item ->
                def currentPath = parentPath ? "${parentPath} > ${item.title}" : "${docTitle} > ${item.title}"
                def level = currentPath.split(" > ").size() 
                def range = item.location ? "${item.location.start} - ${item.location.end}" : "N/A"

                detailText += "${'#' * level} ${item.id} ${item.title}\n"
                detailText += "- 【位置】: ${range}\n"
                if (item.summary) detailText += "- 【摘要】: ${item.summary}\n"


                if (item.children) detailText += processDetails(item.children, currentPath, docTitle, row_num)
            }
            return detailText
        }

        def range = doc.page_range ? "${doc.page_range.start} - ${doc.page_range.end}" : "N/A"

        sb.append("#  ${doc.document_title}\n")
        sb.append("- 【位置】: ${range}\n")

        // 插入详细层级内容
        sb.append(processDetails(doc.index, "", doc.document_title, doc.row_num))
        chunk.set("page_index_info", sb.toString())

}catch(Exception ex) {
    
}
```
