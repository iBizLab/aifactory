<p class="panel-title"><b>执行sql语句</b></p>

```sql
delete from ai_kb_chunk where document_id in (select id from ai_kb_document where kb_id=?) ;
delete from ai_kb_graph_entity_chunk where ai_kb_graph_entity_chunk.entity_id in (select id from ai_kb_graph_entity where kb_id=?) ;
delete from ai_kb_graph_entity where  kb_id=? ;
delete from ai_kb_graph_relation_chunk where ai_kb_graph_relation_chunk.relation_id in (select id from ai_kb_graph_relation where kb_id=?) ;
delete from ai_kb_graph_relation where   kb_id=?  ;
update ai_kb_document set chunk_method=(select chunk_method from ai_knowledge_base where ai_knowledge_base.id=ai_kb_document.kb_id),status='3',parsed_content = null where kb_id = '785219b0c35d9739f271d5cba07df681';

```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).ID(知识库标识)`
2. `Default(传入变量).ID(知识库标识)`
3. `Default(传入变量).ID(知识库标识)`
4. `Default(传入变量).ID(知识库标识)`
5. `Default(传入变量).ID(知识库标识)`
6. `Default(传入变量).ID(知识库标识)`

