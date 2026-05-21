<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
def document = logic.param("Default").getReal();
    String input = document.get("key_questions");
    if (!org.springframework.util.ObjectUtils.isEmpty(input)) {
        def lines = input.split('\n');
        List mapList = []
        if (lines.size() > 0) {
            for (String line : lines) {
                // Map<String, String> map = new HashMap<>();
                def map = sys.createEntity()
                map.set("name", line)
                mapList.add(map)
            }
            document.set("key_question_list", mapList)
        }
    }
```
