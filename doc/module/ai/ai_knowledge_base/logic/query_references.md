## 获取参考资料 <!-- {docsify-ignore-all} -->

   

### 处理过程

```plantuml
@startuml
hide empty description
<style>
root {
  HyperlinkColor #42b983
}
</style>

hide empty description
state "开始" as Begin <<start>> [[$./query_references#begin {"开始"}]]
state "绑定chunk_list参数" as BINDPARAM_01  [[$./query_references#bindparam_01 {"绑定chunk_list参数"}]]
state "准备查询知识库参数" as PREPAREPARAM_02  [[$./query_references#prepareparam_02 {"准备查询知识库参数"}]]
state "附加聊天请求" as SYSAICHATAGENT_APPENDCHATREQUEST_02  [[$./query_references#sysaichatagent_appendchatrequest_02 {"附加聊天请求"}]]
state "附加聊天请求" as SYSAICHATAGENT_APPENDCHATREQUEST_01  [[$./query_references#sysaichatagent_appendchatrequest_01 {"附加聊天请求"}]]
state "交谈输出" as SYSAICHATAGENT_CHATOUTPUT_02  [[$./query_references#sysaichatagent_chatoutput_02 {"交谈输出"}]]
state "准备聊天请求参数" as PREPAREPARAM_03  [[$./query_references#prepareparam_03 {"准备聊天请求参数"}]]
state "交谈输出" as SYSAICHATAGENT_CHATOUTPUT_01  [[$./query_references#sysaichatagent_chatoutput_01 {"交谈输出"}]]
state "设置聊天返回" as PREPAREPARAM_01  [[$./query_references#prepareparam_01 {"设置聊天返回"}]]
state "结束" as END_01 <<end>> [[$./query_references#end_01 {"结束"}]]
state "准备聊天请求参数" as PREPAREPARAM_04  [[$./query_references#prepareparam_04 {"准备聊天请求参数"}]]
state "知识检索" as SYSAICHATAGENT_FETCHCHUNKS_01  [[$./query_references#sysaichatagent_fetchchunks_01 {"知识检索"}]]


Begin --> PREPAREPARAM_04
PREPAREPARAM_04 --> SYSAICHATAGENT_APPENDCHATREQUEST_02
SYSAICHATAGENT_APPENDCHATREQUEST_02 --> SYSAICHATAGENT_CHATOUTPUT_02
SYSAICHATAGENT_CHATOUTPUT_02 --> PREPAREPARAM_01
PREPAREPARAM_01 --> END_01


@enduml
```


### 处理步骤说明

#### 准备查询知识库参数 :id=PREPAREPARAM_02<sup class="footnote-symbol"> <font color=gray size=1>[准备参数]</font></sup>



1. 将`Default(传入变量).id(知识库标识)` 设置给  `chunk_query.n_kbid_eq`
2. 将`Default(传入变量).query` 设置给  `chunk_query.query`
3. 将`0.7` 设置给  `chunk_query.n_vector_similarity_gtandeq`
4. 将`2` 设置给  `chunk_query.n_rerank_eq`
5. 将`10` 设置给  `chunk_query.size`
6. 将`0.2` 设置给  `chunk_query.n_similarity_gtandeq`
7. 将`片段A` 设置给  `chunk_query.chunksnprefix`
8. 将`chunkview://{id}` 设置给  `chunk_query.chunkviewurl`
9. 将`2` 设置给  `chunk_query.n_pageindex_eq`

#### 开始 :id=Begin<sup class="footnote-symbol"> <font color=gray size=1>[开始]</font></sup>



*- N/A*
#### 知识检索 :id=SYSAICHATAGENT_FETCHCHUNKS_01<sup class="footnote-symbol"> <font color=gray size=1>[SYSAICHATAGENT_FETCHCHUNKS]</font></sup>




#### 准备聊天请求参数 :id=PREPAREPARAM_04<sup class="footnote-symbol"> <font color=gray size=1>[准备参数]</font></sup>



1. 将`Default(传入变量).id(知识库标识)` 设置给  `chat_request.knowledgebases`
2. 将`Default(传入变量).query` 设置给  `chat_request.chunkqueries`

#### 绑定chunk_list参数 :id=BINDPARAM_01<sup class="footnote-symbol"> <font color=gray size=1>[绑定参数]</font></sup>



绑定参数`chunk_page` 到 `chunk_list`
#### 附加聊天请求 :id=SYSAICHATAGENT_APPENDCHATREQUEST_02<sup class="footnote-symbol"> <font color=gray size=1>[SYSAICHATAGENT_APPENDCHATREQUEST]</font></sup>




#### 附加聊天请求 :id=SYSAICHATAGENT_APPENDCHATREQUEST_01<sup class="footnote-symbol"> <font color=gray size=1>[SYSAICHATAGENT_APPENDCHATREQUEST]</font></sup>




#### 交谈输出 :id=SYSAICHATAGENT_CHATOUTPUT_02<sup class="footnote-symbol"> <font color=gray size=1>[SYSAICHATAGENT_CHATOUTPUT]</font></sup>




#### 准备聊天请求参数 :id=PREPAREPARAM_03<sup class="footnote-symbol"> <font color=gray size=1>[准备参数]</font></sup>



1. 将`no` 设置给  `chat_request.chunksection`
2. 将`no` 设置给  `chat_request.chunkprompt`
3. 将`chunk_list` 设置给  `chat_request.chunks`

#### 交谈输出 :id=SYSAICHATAGENT_CHATOUTPUT_01<sup class="footnote-symbol"> <font color=gray size=1>[SYSAICHATAGENT_CHATOUTPUT]</font></sup>




#### 设置聊天返回 :id=PREPAREPARAM_01<sup class="footnote-symbol"> <font color=gray size=1>[准备参数]</font></sup>



1. 将`chat_response.content` 设置给  `Default(传入变量).result`

#### 结束 :id=END_01<sup class="footnote-symbol"> <font color=gray size=1>[结束]</font></sup>



返回 `Default(传入变量)`



### 实体逻辑参数

|    中文名   |    代码名    |  数据类型    |  实体   |备注 |
| --------| --------| -------- | -------- | --------   |
|传入变量(<i class="fa fa-check"/></i>)|Default|数据对象|[知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base.md)||
|chat_request|chat_request||||
|chat_response|chat_response||||
|chunk_list|chunk_list|数据对象列表|[知识库文档分块(AI_KB_CHUNK)](module/ai/ai_kb_chunk.md)||
|chunk_page|chunk_page|分页查询|||
|chunk_query|chunk_query|过滤器|||
