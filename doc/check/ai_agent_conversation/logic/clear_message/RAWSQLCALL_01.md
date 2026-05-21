<p class="panel-title"><b>执行sql语句</b></p>

```sql
DELETE FROM AI_AGENT_MESSAGE WHERE CONVERSATION_ID IN (SELECT ID FROM AI_AGENT_CONVERSATION WHERE SESSION_ID = ?);
DELETE  FROM AI_AGENT_FEEDBACK WHERE CONVERSATION_ID = ? ;

```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).SESSION_ID(外部会话ID)`
2. `Default(传入变量).ID(标识)`

