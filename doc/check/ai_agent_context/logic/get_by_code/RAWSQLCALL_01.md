<p class="panel-title"><b>执行sql语句</b></p>

```sql
select max(id) as id from ai_agent_context where code_name=? or code_name like concat(?,'@%')
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).CODE_NAME(代码标识)`
2. `Default(传入变量).CODE_NAME(代码标识)`

将执行sql结果赋值给参数`Default(传入变量)`
