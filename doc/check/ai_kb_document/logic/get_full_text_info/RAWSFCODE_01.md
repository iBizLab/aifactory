<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
        def defaultEntity = logic.param("default").getReal();
        def fullText = logic.param("fulltext").getReal()?logic.param("fulltext").getReal().toString():"";
        def summary = defaultEntity.get("summary")?defaultEntity.get("summary").toString():""
        def sb = ""

        if(defaultEntity.get("name")  && fullText) {
            sb += "# ${defaultEntity.name}\n"
            if (defaultEntity.get("kb_name")) {
                sb += "<details><summary>所属: ${defaultEntity.kb_name}"
                if (defaultEntity.get("categories")) {
                    sb += "/${defaultEntity.categories}"
                }
                sb += "</summary>【文档ID】: ${defaultEntity.id}"
                sb += "</details>\n\n"
            }
            sb += "## 正文\n${fullText}\n"

            defaultEntity.set("full_text", sb)
            if(fullText.length() > 28672 ){
                if(summary && summary.length() < 28672){
                    defaultEntity.set("analysis_content", summary + "\n---\n\n## 部分正文\n" + fullText.substring(0,28672-summary.length()) + "\n\n更多内容，略……")
                }
                else {
                    defaultEntity.set("analysis_content", defaultEntity.get("full_text").substring(0,28672-10)  + "\n\n更多内容，略……")
                }

            }
            else {
                defaultEntity.set("analysis_content", defaultEntity.get("full_text"))
            }
        }
        else if(summary){
            defaultEntity.set("full_text", summary)
            defaultEntity.set("analysis_content", summary)
        }
    
        
```
