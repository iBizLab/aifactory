<p class="panel-title"><b>执行sql语句</b></p>

```sql
update ai_knowledge_base a set source_type = (
    SELECT STRING_AGG(DISTINCT TYPE, ',' ORDER BY TYPE)
    FROM public.ai_kb_document b
    WHERE b.kb_id = a.id
)
where a.id =?
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).KB_ID(知识库标识)`

