<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
def chat_response = logic.param('chat_response').getReal()
def lastcontent = logic.param('lastcontent').getReal()

if (chat_response?.choices) {
    lastcontent = chat_response.choices.last().content
}
```
