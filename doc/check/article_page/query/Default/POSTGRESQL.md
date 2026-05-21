```sql
SELECT
t1."categories",
t1."create_man",
t1."create_time",
t1."cur_version_id",
t1."cur_version_name",
t1."format_type",
t1."icon",
t1."id",
t1."identifier",
t1."is_archived",
t1."is_deleted",
(select count(1) from favorite where create_man=#{ctx.sessioncontext.srfpersonid} and OWNER_ID=t1."id" ) AS "is_favorite",
t1."is_leaf",
t1."is_lock",
t1."is_published",
t1."is_shared",
t1."is_shared_subset",
t1."name",
t1."parent_id",
t1."published",
t1."publish_man",
t1."publish_name",
t1."publish_time",
CURRENT_DATE - t1."create_time"::date AS "recent_create_days",
t1."review_result_state",
t1."sequence",
concat(t11."identifier",'-',t1."identifier") AS "show_identifier",
t1."space_id",
t11."identifier" AS "space_identifier",
t11."name" AS "space_name",
t1."type",
t1."update_man",
t1."update_time",
t1."user_tag",
t1."user_tag2"
FROM "page" t1 
LEFT JOIN "space" t11 ON t1."space_id" = t11."id" 


```