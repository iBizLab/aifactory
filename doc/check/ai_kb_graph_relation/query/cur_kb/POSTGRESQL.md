```sql
SELECT
t1."active",
t1."confidence",
t1."create_man",
t1."create_time",
t1."description",
t1."id",
t1."kb_id",
t31."name" AS "kb_name",
t1."name",
t1."object_id",
t21."name" AS "object_name",
t1."predicate",
t1."subject_id",
t11."name" AS "subject_name",
t1."update_man",
t1."update_time"
FROM "ai_kb_graph_relation" t1 
LEFT JOIN "ai_kb_graph_entity" t11 ON t1."subject_id" = t11."id" 
LEFT JOIN "ai_kb_graph_entity" t21 ON t1."object_id" = t21."id" 
LEFT JOIN "ai_knowledge_base" t31 ON t1."kb_id" = t31."id" 

WHERE ( <choose><when test="ctx.datacontext.ai_knowledge_base !=null ">  t1."kb_id" = #{ctx.datacontext.ai_knowledge_base}  </when><otherwise>1=1</otherwise></choose> )
```