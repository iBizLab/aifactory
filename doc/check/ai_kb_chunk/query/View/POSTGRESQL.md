```sql
SELECT
t1."active",
t11."categories",
t1."chunk_type",
t1."content",
t1."content_preview",
t1."create_man",
t1."create_time",
t1."document_id",
t11."name" AS "document_name",
t11."sequence" AS "document_sequence",
t11."type" AS "document_type",
t11."file" AS "doc_file",
t11."name" AS "doc_name",
t11."parsed_content" AS "doc_parsed_content",
t1."id",
t11."kb_id",
t21."name" AS "kb_name",
t1."keywords",
t1."key_questions",
t1."meta_data",
t1."name",
t1."path",
t1."pid",
t1."positions",
t1."sequence",
t1."source_count",
t1."source_indices",
t1."tags",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "ai_kb_chunk" t1 
LEFT JOIN "ai_kb_document" t11 ON t1."document_id" = t11."id" 
LEFT JOIN "ai_knowledge_base" t21 ON t11."kb_id" = t21."id" 


```