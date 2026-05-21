<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
def kb = logic.param("Default").getReal();
def prompt_before = kb.get("GUIDANCE_PROMPT")
def prompt_after = prompt_before?.take(2000) ?: kb.get("description")

kb.set("GUIDANCE_PROMPT",prompt_after)
```
