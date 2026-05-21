<p class="panel-title"><b>执行sql语句</b></p>

```sql
update ai_kb_document t set status =  case when t.status = '4' or t.status='99' then '99' else '1' end where id = ?
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).ID(知识库文档标识)`

