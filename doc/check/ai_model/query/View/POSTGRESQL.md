```sql
SELECT
t21."bearer_token" AS "access_token",
t1."active",
t1."ai_credential_id",
t21."name" AS "ai_credential_name",
t1."api_base_url",
t1."code_name",
t1."create_man",
t1."create_time",
t1."desc_oss_image",
t1."extra_params",
t1."id",
t1."max_context_tokens",
t1."max_output_tokens",
t1."model_capability",
t1."model_category",
t1."name",
t1."oss_image_vl_prompt",
t1."provider",
t11."name" AS "provider_name",
t1."update_man",
t1."update_time"
FROM "ai_model" t1 
LEFT JOIN "ai_model_provider" t11 ON t1."provider" = t11."id" 
LEFT JOIN "ai_credential" t21 ON t1."ai_credential_id" = t21."id" 


```