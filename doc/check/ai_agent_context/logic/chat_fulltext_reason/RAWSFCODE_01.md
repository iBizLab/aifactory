<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
def _all_reason_content = logic.param("all_reason_content").getReal();
def _doc_reason_list = logic.param("chunk_reason_list").getReal();

def _fullcontent_reason_report = logic.param("fullcontent_reason_report").getReal();
_all_reason_content.set('fullcontent',null)


if(_doc_reason_list.size()==1) {
    _fullcontent_reason_report.set("review_report", _doc_reason_list.get(0).content)
}
      
def allContent = _doc_reason_list.collect { item ->
    def content = item.content ?: ''
"""\
# 分段结果：
```
${item.content}
```
---\
"""
}.join('\n\n')

int retry = 0
if(_all_reason_content.get("retry"))
    retry = _all_reason_content.get("retry")

if(allContent.length()<25600)  {
    _all_reason_content.set('fullcontent',allContent)
    println "------------------------allContent：" + allContent
}
else if(retry<3){
        def _doc_fulltext = logic.param("doc_fulltext").getReal();
        retry = retry +1
        _all_reason_content.set("retry", retry)
        println "------------------------allContent 过大再次分段审查：" + allContent

        _doc_fulltext.clear()
        
        _doc_reason_list.each { item ->
            
            _doc_fulltext.add( [
                    name: "分段结果",
                    content: item.content ?: ''
            ]
            )
        }
    
}
else {
        _fullcontent_reason_report.set("review_report", allContent)
        println "------------------------重试分段审查3次 allContent 仍过大，直接保存报告：" + allContent
}



```
