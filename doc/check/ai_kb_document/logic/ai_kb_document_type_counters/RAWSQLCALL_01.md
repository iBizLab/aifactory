<p class="panel-title"><b>执行sql语句</b></p>

```sql
SELECT COUNT(*) AS total FROM ai_kb_document WHERE kb_id = ?
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).kb_id(知识库标识)`

重置参数`Default(传入变量)`，并将执行sql结果赋值给参数`Default(传入变量)`
