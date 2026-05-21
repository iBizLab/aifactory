<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
/*Groovy*/
def _refrence_chat_request = logic.param('refrence_chat_request').getReal()
def _kb = logic.param('default').getReal()
def _agententity = logic.param('agent').getReal()

String chunkqueries = "我需要执行如下任务，请帮我查询相关信息，精简输出为引用参考资料。"
if(_agententity.get('context_content')){
  chunkqueries += "\n" + _agententity.get('context_content')
}

chunkqueries += "\n任务目标数据情况如下："

if(_kb.get('guidance_prompt')){
  chunkqueries += _kb.get('guidance_prompt')
}else if(_kb.get('description')){
  chunkqueries += _kb.get('description')
}

_refrence_chat_request.set('chunkqueries',chunkqueries)
```
