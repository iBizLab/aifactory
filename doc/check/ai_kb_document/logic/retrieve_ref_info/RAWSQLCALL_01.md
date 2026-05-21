<p class="panel-title"><b>执行sql语句</b></p>

```sql
select content as intelligent_analysis from AI_KB_CHUNK where document_id = ? and pid is null and type='cluster'
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).ID(知识库文档标识)`

重置参数`Default(传入变量)`，并将执行sql结果赋值给参数`Default(传入变量)`
