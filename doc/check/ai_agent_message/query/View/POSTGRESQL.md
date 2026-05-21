```sql
SELECT
t1."content",
t1."content_type",
t1."conversation_id",
t11."name" AS "conversation_name",
t11."title" AS "conversation_title",
t1."create_man",
t1."create_time",
t1."id",
(select count(1) from ai_agent_feedback t where t.user_id=#{ctx.sessioncontext.srfuserid} and t.message_id=t1."id" and t.feedback_type='dislike') AS "is_dislike",
(select count(1) from ai_agent_feedback t where t.user_id=#{ctx.sessioncontext.srfuserid} and t.message_id=t1."id" and t.feedback_type='like') AS "is_like",
t1."metadata",
t1."name",
t1."sender_type",
t1."sequence",
t11."session_id",
t1."status",
t1."update_man",
t1."update_time",
t11."user_id"
FROM "ai_agent_message" t1 
LEFT JOIN "ai_agent_conversation" t11 ON t1."conversation_id" = t11."id" 


```