<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
def document = logic.param("Default").getReal();
String input = document.get("key_questions");
// def questions = input.split(/\n?\d+\.\s+/).findAll { it.trim() }
def lines = input.split('\n')
// def key_questions_list = questions.eachWithIndex { q, i -> println "${i + 1}: [${q}]" }

document.set("key_questions",lines);
```
