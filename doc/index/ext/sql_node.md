
## 存在直接SQL调用的处理逻辑节点<sup class="footnote-symbol"> <font color=orange>[43]</font></sup>

#### [智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context)的处理逻辑[get_by_code](module/ai/ai_agent_context/logic/get_by_code)

节点：直接SQL调用
<p class="panel-title"><b>执行sql语句</b></p>

```sql
select max(id) as id from ai_agent_context where code_name=? or code_name like concat(?,'@%')
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).CODE_NAME(代码标识)`
2. `Default(传入变量).CODE_NAME(代码标识)`

将执行sql结果赋值给参数`Default(传入变量)`
#### [智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context)的处理逻辑[创建之前(beforefile)](module/ai/ai_agent_context/logic/beforefile)

节点：直接SQL调用
<p class="panel-title"><b>执行sql语句</b></p>

```sql
select id as ai_agent_id from ai_agent where id = ?
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).template_id`

重置参数`Default(传入变量)`，并将执行sql结果赋值给参数`Default(传入变量)`
#### [智能体会话(AI_AGENT_CONVERSATION)](module/ai/ai_agent_conversation)的处理逻辑[清空消息(clear_message)](module/ai/ai_agent_conversation/logic/clear_message)

节点：直接SQL调用
<p class="panel-title"><b>执行sql语句</b></p>

```sql
DELETE FROM AI_AGENT_MESSAGE WHERE CONVERSATION_ID IN (SELECT ID FROM AI_AGENT_CONVERSATION WHERE SESSION_ID = ?);
DELETE  FROM AI_AGENT_FEEDBACK WHERE CONVERSATION_ID = ? ;

```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).SESSION_ID(外部会话ID)`
2. `Default(传入变量).ID(标识)`

#### [智能体会话(AI_AGENT_CONVERSATION)](module/ai/ai_agent_conversation)的处理逻辑[除指定外清空会话(clear_all_except)](module/ai/ai_agent_conversation/logic/clear_all_except)

节点：直接SQL调用
<p class="panel-title"><b>执行sql语句</b></p>

```sql
UPDATE AI_AGENT_CONVERSATION  SET STATUS= 'ended' WHERE SESSION_ID <> ? AND  USER_ID = ?
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).SESSION_ID(外部会话ID)`
2. `用户全局对象.srfpersonid`

#### [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document)的处理逻辑[ai_kb_document_type_counters](module/ai/ai_kb_document/logic/ai_kb_document_type_counters)

节点：统计知识库分类数量
<p class="panel-title"><b>执行sql语句</b></p>

```sql
SELECT COUNT(*) AS total FROM ai_kb_document WHERE kb_id = ?
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).kb_id(知识库标识)`

重置参数`Default(传入变量)`，并将执行sql结果赋值给参数`Default(传入变量)`
#### [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document)的处理逻辑[构建切片(build_chunk)](module/ai/ai_kb_document/logic/build_chunk)

节点：准备状态
<p class="panel-title"><b>执行sql语句</b></p>

```sql
update ai_kb_document t set status =  case when t.status = '4' or t.status='99' then '99' else '1' end where id = ?
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).ID(知识库文档标识)`

#### [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document)的处理逻辑[构建索引(build_index)](module/ai/ai_kb_document/logic/build_index)

节点：准备状态
<p class="panel-title"><b>执行sql语句</b></p>

```sql
update ai_kb_document t set status =  case when t.status = '4' or t.status='99' then '99' else '1' end where id = ?
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).ID(知识库文档标识)`

#### [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document)的处理逻辑[统计文档类型并更新知识库(cal_source_type)](module/ai/ai_kb_document/logic/cal_source_type)

节点：查询类型并更新知识库
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

#### [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document)的处理逻辑[统计评论数(comment_counters)](module/ai/ai_kb_document/logic/comment_counters)

节点：统计知识库文档评论数
<p class="panel-title"><b>执行sql语句</b></p>

```sql
SELECT COUNT(*) AS total FROM comment WHERE PRINCIPAL_TYPE = 'AI_KB_DOCUMENT' AND CONTENT <> '<p><del>该评论已删除</del></p>' AND PRINCIPAL_ID = ?
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).ai_kb_document`

将执行sql结果赋值给参数`comment_num(评论数)`
#### [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document)的处理逻辑[获取关联信息(retrieve_ref_info)](module/ai/ai_kb_document/logic/retrieve_ref_info)

节点：查询智能分析
<p class="panel-title"><b>执行sql语句</b></p>

```sql
select content as intelligent_analysis from AI_KB_CHUNK where document_id = ? and pid is null and type='cluster'
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).ID(知识库文档标识)`

重置参数`Default(传入变量)`，并将执行sql结果赋值给参数`Default(传入变量)`
#### [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document)的处理逻辑[获取关联信息(retrieve_ref_info)](module/ai/ai_kb_document/logic/retrieve_ref_info)

节点：查询关键字和问题
<p class="panel-title"><b>执行sql语句</b></p>

```sql
SELECT keywords,key_questions FROM AI_KB_CHUNK where key_questions is NOT null and document_id = ? ORDER BY RANDOM() LIMIT 1;
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).ID(知识库文档标识)`

重置参数`Default(传入变量)`，并将执行sql结果赋值给参数`Default(传入变量)`
#### [知识库文档同步(AI_KB_DOCUMENT_SYNC)](module/ai/ai_kb_document_sync)的处理逻辑[同步删除文档和分块(sync_remove_doc_chunk)](module/ai/ai_kb_document_sync/logic/sync_remove_doc_chunk)

节点：删除文档分块
<p class="panel-title"><b>执行sql语句</b></p>

```sql
DELETE   FROM ai_kb_chunk  c WHERE  exists (select 1 from ai_kb_document doc where doc.id=c.document_id and doc.SYNC_ID= ? )
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).ID(标识)`

#### [知识库文档同步(AI_KB_DOCUMENT_SYNC)](module/ai/ai_kb_document_sync)的处理逻辑[同步删除文档和分块(sync_remove_doc_chunk)](module/ai/ai_kb_document_sync/logic/sync_remove_doc_chunk)

节点：删除文档
<p class="panel-title"><b>执行sql语句</b></p>

```sql
DELETE  FROM ai_kb_document doc WHERE doc.sync_id = ?
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).ID(标识)`

#### [知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base)的处理逻辑[取消星标(un_favorite)](module/ai/ai_knowledge_base/logic/un_favorite)

节点：删除收藏数据
<p class="panel-title"><b>执行sql语句</b></p>

```sql
delete from favorite where create_man = ? and owner_id = ?
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `用户全局对象.srfuserid`
2. `Default(传入变量).owner_id`

#### [知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base)的处理逻辑[生成引导提示词(generate_guided_prompts)](module/ai/ai_knowledge_base/logic/generate_guided_prompts)

节点：更新引导提示词
<p class="panel-title"><b>执行sql语句</b></p>

```sql
UPDATE AI_KNOWLEDGE_BASE set GUIDANCE_PROMPT=? where ID = ?
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).GUIDANCE_PROMPT(引导提示词)`
2. `Default(传入变量).ID(知识库标识)`

#### [知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base)的处理逻辑[计算解析数完成知识库状态处理(calc_parsed_cnt)](module/ai/ai_knowledge_base/logic/calc_parsed_cnt)

节点：AI_KB_DOCUMENT数量
<p class="panel-title"><b>执行sql语句</b></p>

```sql
select count(1) as document_cnt, count(1) FILTER (WHERE status = '1') AS parsed_cnt  from AI_KB_DOCUMENT where kb_id = ?
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).ID(知识库标识)`

重置参数`Default(传入变量)`，并将执行sql结果赋值给参数`Default(传入变量)`
#### [知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base)的处理逻辑[重置分片索引数据(reset_all_chunk)](module/ai/ai_knowledge_base/logic/reset_all_chunk)

节点：直接SQL调用
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

#### [类别(CATEGORY)](module/Base/category)的处理逻辑[删除类别及子类别(delete_child_category)](module/Base/category/logic/delete_child_category)

节点：修改需求信息
<p class="panel-title"><b>执行sql语句</b></p>

```sql
UPDATE idea t 
INNER JOIN category t21 ON t.category_id = t21.ID 
SET t.category_id = NULL
WHERE (t.category_id = ? OR t21.categories LIKE CONCAT('%',?,'%'))
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).ID(标识)`
2. `Default(传入变量).ID(标识)`

#### [类别(CATEGORY)](module/Base/category)的处理逻辑[设置默认分组(set_section)](module/Base/category/logic/set_section)

节点：批更新子节点分组
<p class="panel-title"><b>执行sql语句</b></p>

```sql
update category set section_id=? where INSTR(categories,?)>0
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).SECTION_ID(分组标识)`
2. `Default(传入变量).ID(标识)`

#### [动态数据看板(DYNADASHBOARD)](module/Base/dyna_dashboard)的处理逻辑[仅获取(only_get)](module/Base/dyna_dashboard/logic/only_get)

节点：直接SQL调用
<p class="panel-title"><b>执行sql语句</b></p>

```sql
SELECT
t1.`APPID`,
t1.`CREATEDATE`,
t1.`CREATEMAN`,
t1.`DYNADASHBOARDID`,
t1.`DYNADASHBOARDNAME`,
t1.`EXAMPLE_CHART`,
t1.`IS_SYSTEM`,
t1.`MODELID`,
t1.`OWNER_ID`,
t1.`OWNER_TYPE`,
t1.`SEQUENCES`,
t1.`TYPE`,
t1.`UPDATE_MAN`,
t1.`UPDATE_TIME`,
t1.`USERID`
FROM `DYNADASHBOARD` t1 
WHERE t1.DYNADASHBOARDID = ?

```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).DYNADASHBOARDID(动态数据看板标识)`

重置参数`Default(传入变量)`，并将执行sql结果赋值给参数`Default(传入变量)`
#### [效能报表(INSIGHT_REPORT)](module/Insight/insight_report)的处理逻辑[删除类别(delete_categories)](module/Insight/insight_report/logic/delete_categories)

节点：直接SQL调用当类别删除时修改发布的类别属性
<p class="panel-title"><b>执行sql语句</b></p>

```sql
UPDATE insight_report
SET categories = TRIM(BOTH ',' FROM REPLACE(CONCAT(',', categories, ','), CONCAT(',', ?, ','), ','))
WHERE FIND_IN_SET(?, categories) > 0 ;
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).ID(标识)`
2. `Default(传入变量).ID(标识)`

#### [效能视图(INSIGHT_VIEW)](module/Insight/insight_view)的处理逻辑[取消星标(un_favorite)](module/Insight/insight_view/logic/un_favorite)

节点：直接SQL调用
<p class="panel-title"><b>执行sql语句</b></p>

```sql
delete from `favorite` where create_man = ? and owner_id = ?
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `用户全局对象.srfuserid`
2. `Default(传入变量).owner_id`

#### [页面(PAGE)](module/Wiki/article_page)的处理逻辑[关闭共享(closed_shared)](module/Wiki/article_page/logic/closed_shared)

节点：直接SQL调用
<p class="panel-title"><b>执行sql语句</b></p>

```sql
delete from `member` where owner_id = ? and owner_type = 'PAGE' and OWNER_SUBTYPE = 'SHARED'
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).ID(标识)`

#### [页面(PAGE)](module/Wiki/article_page)的处理逻辑[删除(delete)](module/Wiki/article_page/logic/delete)

节点：删除最近访问
<p class="panel-title"><b>执行sql语句</b></p>

```sql
update recent set IS_DELETED=1 where owner_id=? and owner_subtype='page'
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).ID(标识)`

#### [页面(PAGE)](module/Wiki/article_page)的处理逻辑[发布页面（测试）(publish_page_test)](module/Wiki/article_page/logic/publish_page_test)

节点：删除草稿版本
<p class="panel-title"><b>执行sql语句</b></p>

```sql
DELETE
FROM version  where OWNER_ID = ?  and JSON_EXTRACT(data, '$.is_published') = 0  and OWNER_TYPE = 'PAGE' ORDER BY name desc;
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).ID(标识)`

#### [页面(PAGE)](module/Wiki/article_page)的处理逻辑[取消星标(un_favorite)](module/Wiki/article_page/logic/un_favorite)

节点：删除收藏数据
<p class="panel-title"><b>执行sql语句</b></p>

```sql
delete from favorite where create_man = ? and owner_id = ?
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `用户全局对象.srfuserid`
2. `Default(传入变量).owner_id`

#### [页面(PAGE)](module/Wiki/article_page)的处理逻辑[恢复(recover)](module/Wiki/article_page/logic/recover)

节点：恢复最近访问
<p class="panel-title"><b>执行sql语句</b></p>

```sql
update recent set IS_DELETED=0 where owner_id=? and owner_subtype='page'
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).ID(标识)`

#### [页面(PAGE)](module/Wiki/article_page)的处理逻辑[统计页面评论数(count_comment)](module/Wiki/article_page/logic/count_comment)

节点：统计页面评论数
<p class="panel-title"><b>执行sql语句</b></p>

```sql
SELECT COUNT(*) AS total FROM comment WHERE PRINCIPAL_TYPE = 'PAGE' AND CONTENT <> '<p><del>该评论已删除</del></p>' AND PRINCIPAL_ID = ?
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).article_page`

将执行sql结果赋值给参数`comment_num(评论数)`
#### [页面(PAGE)](module/Wiki/article_page)的处理逻辑[获取共享信息(get_shared_info)](module/Wiki/article_page/logic/get_shared_info)

节点：获取访问密码
<p class="panel-title"><b>执行sql语句</b></p>

```sql
SELECT access_password FROM page WHERE id = ?
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).ID(标识)`

重置参数`Default(传入变量)`，并将执行sql结果赋值给参数`Default(传入变量)`
#### [页面(PAGE)](module/Wiki/article_page)的处理逻辑[获取草稿页面(get_draft_pages)](module/Wiki/article_page/logic/get_draft_pages)

节点：查询草稿数据
<p class="panel-title"><b>执行sql语句</b></p>

```sql
select * from page where page.SPACE_ID = ? and page.IS_PUBLISHED = 0;
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).space_id(空间标识)`

重置参数`page_list(页面列表)`，并将执行sql结果赋值给参数`page_list(页面列表)`
#### [文件夹(PORTFOLIO)](module/Base/portfolio)的处理逻辑[从项目集中移除(remove_from_project_set)](module/Base/portfolio/logic/remove_from_project_set)

节点：从项目集中移除
<p class="panel-title"><b>执行sql语句</b></p>

```sql
delete from `work` where PORTFOLIO_ID = ? and PRINCIPAL_ID = ?
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).portfolio_id`
2. `Default(传入变量).ID(标识)`

#### [文件夹(PORTFOLIO)](module/Base/portfolio)的处理逻辑[取消星标(un_favorite)](module/Base/portfolio/logic/un_favorite)

节点：删除收藏数据
<p class="panel-title"><b>执行sql语句</b></p>

```sql
delete from `favorite` where create_man = ? and owner_id = ?
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `用户全局对象.srfuserid`
2. `Default(传入变量).owner_id`

#### [分组(SECTION)](module/Base/section)的处理逻辑[删除分组及其下类别(delete_section)](module/Base/section/logic/delete_section)

节点：修改需求信息
<p class="panel-title"><b>执行sql语句</b></p>

```sql
UPDATE idea t 
INNER JOIN category t21 ON t.category_id = t21.ID 
INNER JOIN section t31 on t21.SECTION_ID = t31.id
SET t.category_id = NULL
WHERE (t21.SECTION_ID = ? )
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).ID(标识)`

#### [共享空间(SHARED_SPACE)](module/Wiki/shared_space)的处理逻辑[校验共享访问密码(access_password)](module/Wiki/shared_space/logic/access_password)

节点：查询共享空间密码信息
<p class="panel-title"><b>执行sql语句</b></p>

```sql
select `ACCESS_PASSWORD` from `space` where id = ?
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).ID(标识)`

重置参数`check_space(校验空间)`，并将执行sql结果赋值给参数`check_space(校验空间)`
#### [共享空间(SHARED_SPACE)](module/Wiki/shared_space)的处理逻辑[检验共享页面(check_shared)](module/Wiki/shared_space/logic/check_shared)

节点：查询共享空间密码信息
<p class="panel-title"><b>执行sql语句</b></p>

```sql
select `ACCESS_PASSWORD` from `space` where id = ?
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).id(标识)`

重置参数`Default(传入变量)`，并将执行sql结果赋值给参数`Default(传入变量)`
#### [共享空间(SHARED_SPACE)](module/Wiki/shared_space)的处理逻辑[获取共享空间信息(shared_page_info)](module/Wiki/shared_space/logic/shared_page_info)

节点：获取密码信息
<p class="panel-title"><b>执行sql语句</b></p>

```sql
select `ACCESS_PASSWORD` from `space` where id = ?
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).ID(标识)`

重置参数`Default(传入变量)`，并将执行sql结果赋值给参数`Default(传入变量)`
#### [空间(SPACE)](module/Wiki/space)的处理逻辑[删除(delete)](module/Wiki/space/logic/delete)

节点：删除最近访问
<p class="panel-title"><b>执行sql语句</b></p>

```sql
update recent set IS_DELETED=1 where owner_id=? and owner_subtype='space'
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).ID(标识)`

#### [空间(SPACE)](module/Wiki/space)的处理逻辑[取消星标(un_favorite)](module/Wiki/space/logic/un_favorite)

节点：删除收藏数据
<p class="panel-title"><b>执行sql语句</b></p>

```sql
delete from favorite where create_man = ? and owner_id = ?
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `用户全局对象.srfuserid`
2. `Default(传入变量).owner_id`

#### [空间(SPACE)](module/Wiki/space)的处理逻辑[恢复(recover)](module/Wiki/space/logic/recover)

节点：恢复最近访问
<p class="panel-title"><b>执行sql语句</b></p>

```sql
update recent set IS_DELETED=0 where owner_id=? and owner_subtype='space'
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).ID(标识)`

#### [空间(SPACE)](module/Wiki/space)的处理逻辑[标记主空间(mark_main_space)](module/Wiki/space/logic/mark_main_space)

节点：清除主标记
<p class="panel-title"><b>执行sql语句</b></p>

```sql
UPDATE relation
SET RELATION_TYPE = NULL
WHERE PRINCIPAL_ID = ? AND (PRINCIPAL_TYPE = 'project' OR PRINCIPAL_TYPE = 'product') AND TARGET_TYPE = 'space';
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).principal_id`

#### [空间(SPACE)](module/Wiki/space)的处理逻辑[标记主空间(mark_main_space)](module/Wiki/space/logic/mark_main_space)

节点：标记主知识库
<p class="panel-title"><b>执行sql语句</b></p>

```sql
UPDATE relation
SET RELATION_TYPE = 'main_space'
WHERE PRINCIPAL_ID = ? AND TARGET_ID = ? AND (PRINCIPAL_TYPE = 'project' OR PRINCIPAL_TYPE = 'product') AND TARGET_TYPE = 'space';
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).principal_id`
2. `Default(传入变量).ID(标识)`

#### [空间(SPACE)](module/Wiki/space)的处理逻辑[获取关联的空间(get_re_space)](module/Wiki/space/logic/get_re_space)

节点：获取关联数据
<p class="panel-title"><b>执行sql语句</b></p>

```sql
SELECT
	t1.ID,
	t1.`NAME`,
	t2.RELATION_TYPE 
FROM
	space t1
	JOIN relation t2 ON t2.TARGET_ID = t1.ID 
WHERE
	t1.IS_DELETED = 0 
	AND t1.IS_ARCHIVED = 0 
	AND t2.PRINCIPAL_TYPE = ? 
	AND t2.TARGET_TYPE = ? 
	AND t2.PRINCIPAL_ID = ?;
```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).principal_type`
2. `Default(传入变量).target_type`
3. `Default(传入变量).principal_id`

重置参数`page(page)`，并将执行sql结果赋值给参数`page(page)`
#### [版本(VERSION)](module/Base/version)的处理逻辑[新建版本时填充默认版本名称(fill_default_name)](module/Base/version/logic/fill_default_name)

节点：获取当前版本
<p class="panel-title"><b>执行sql语句</b></p>

```sql
select IDENTIFIER, `NAME` from `version`
where owner_id = ? and owner_type = ?
order by IDENTIFIER desc
limit 1

```

<p class="panel-title"><b>执行sql参数</b></p>

1. `Default(传入变量).OWNER_ID(所属数据标识)`
2. `Default(传入变量).OWNER_TYPE(所属数据对象)`

重置参数`cur_version(当前版本)`，并将执行sql结果赋值给参数`cur_version(当前版本)`




