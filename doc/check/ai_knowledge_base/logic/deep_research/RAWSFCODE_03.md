<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
def report = logic.param('report').getReal()
def review = report.get("review_report")
if (review) {
    try {
        def jsonContent = net.ibizsys.central.cloud.core.ai.util.AIChatUtils.getJsonContent(review)
        def json = new groovy.json.JsonSlurper().parseText(jsonContent)
        
        // 只处理Map类型
        if (json && json instanceof Map) {
            def result = json.get("result")
            def check = json.get("check_info")
            
            if (result != null) {
                report.set("review_result", result)
            }
            if (check != null) {
                report.set("check_info", check)
            }
        } 
    } catch (Exception e) {
        println("处理报告时发生错误: " + e.message)
    }
}
```
