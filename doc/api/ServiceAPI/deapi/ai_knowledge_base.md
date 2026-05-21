# 知识库(ai_knowledge_base) :id=ai_knowledge_base
## 创建知识库

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`CREATE`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库名称|
|<el-row justify="space-between"><el-col :span="20">visibility</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|可见范围|
|<el-row justify="space-between"><el-col :span="20">is_archived</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已归档|
|<el-row justify="space-between"><el-col :span="20">is_deleted</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已删除|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">is_favorite</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|是否星标|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">scope_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|引导提示词|
|<el-row justify="space-between"><el-col :span="20">scope_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属对象|
|<el-row justify="space-between"><el-col :span="20">chat_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型|
|<el-row justify="space-between"><el-col :span="20">rerank_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型|
|<el-row justify="space-between"><el-col :span="20">description_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|描述向量|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|引导词向量|
|<el-row justify="space-between"><el-col :span="20">similarity_threshold</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|召回相似度阈值|
|<el-row justify="space-between"><el-col :span="20">vector_similarity_weight</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|向量相似度权重|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">resource_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">top_k</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最大召回数量|
|<el-row justify="space-between"><el-col :span="20">rerank</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|召回重排|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务键值|
|<el-row justify="space-between"><el-col :span="20">use_kg</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|使用知识图谱|
|<el-row justify="space-between"><el-col :span="20">pageindex</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|智能目录索引|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源类型|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">matched_documents</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|命中文档|
|<el-row justify="space-between"><el-col :span="20">parsed_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|解析文档数|
|<el-row justify="space-between"><el-col :span="20">document_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|文档数|
|<el-row justify="space-between"><el-col :span="20">category_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录标识|
|<el-row justify="space-between"><el-col :span="20">category_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">chat_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">code_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|代码标识|
|<el-row justify="space-between"><el-col :span="20">description</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|描述|
|<el-row justify="space-between"><el-col :span="20">embedding_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|embedding模型|
|<el-row justify="space-between"><el-col :span="20">embedding_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">record_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据记录标识|
|<el-row justify="space-between"><el-col :span="20">record_title</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">rerank_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源标识|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">source_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "is_archived" : null,
  "is_deleted" : null,
  "meta_data" : null,
  "status" : null,
  "is_favorite" : null,
  "tag_sets" : null,
  "scope_type" : null,
  "guidance_prompt" : null,
  "scope_id" : null,
  "chat_model" : null,
  "rerank_model" : null,
  "description_vector" : null,
  "guidance_prompt_vector" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "key" : null,
  "use_kg" : null,
  "pageindex" : null,
  "page_index_info" : null,
  "source_type" : null,
  "summary" : null,
  "matched_documents" : null,
  "parsed_cnt" : null,
  "document_cnt" : null,
  "category_id" : null,
  "category_name" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "code_name" : null,
  "description" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "parser_config" : null,
  "record_id" : null,
  "record_title" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
}
```


##### 响应示例： {docsify-ignore}
```json

{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "is_archived" : null,
  "is_deleted" : null,
  "meta_data" : null,
  "status" : null,
  "is_favorite" : null,
  "tag_sets" : null,
  "scope_type" : null,
  "guidance_prompt" : null,
  "scope_id" : null,
  "chat_model" : null,
  "rerank_model" : null,
  "description_vector" : null,
  "guidance_prompt_vector" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "key" : null,
  "use_kg" : null,
  "pageindex" : null,
  "page_index_info" : null,
  "source_type" : null,
  "summary" : null,
  "matched_documents" : null,
  "parsed_cnt" : null,
  "document_cnt" : null,
  "category_id" : null,
  "category_name" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "code_name" : null,
  "description" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "parser_config" : null,
  "record_id" : null,
  "record_title" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
}

```

## 获取知识库

<el-row>
<div style="width: 80px">
<el-alert center title="GET" type="success" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{key}" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库标识|




##### 响应示例： {docsify-ignore}
```json

{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "is_archived" : null,
  "is_deleted" : null,
  "meta_data" : null,
  "status" : null,
  "is_favorite" : null,
  "tag_sets" : null,
  "scope_type" : null,
  "guidance_prompt" : null,
  "scope_id" : null,
  "chat_model" : null,
  "rerank_model" : null,
  "description_vector" : null,
  "guidance_prompt_vector" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "key" : null,
  "use_kg" : null,
  "pageindex" : null,
  "page_index_info" : null,
  "source_type" : null,
  "summary" : null,
  "matched_documents" : null,
  "parsed_cnt" : null,
  "document_cnt" : null,
  "category_id" : null,
  "category_name" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "code_name" : null,
  "description" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "parser_config" : null,
  "record_id" : null,
  "record_title" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
}

```

## 删除知识库

<el-row>
<div style="width: 80px">
<el-alert center title="DELETE" type="error" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{key}" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`DELETE`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库标识|





## 更新知识库

<el-row>
<div style="width: 80px">
<el-alert center title="PUT" type="warning" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{key}" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`UPDATE`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库标识|



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库名称|
|<el-row justify="space-between"><el-col :span="20">visibility</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|可见范围|
|<el-row justify="space-between"><el-col :span="20">is_archived</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已归档|
|<el-row justify="space-between"><el-col :span="20">is_deleted</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已删除|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">is_favorite</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|是否星标|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">scope_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|引导提示词|
|<el-row justify="space-between"><el-col :span="20">scope_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属对象|
|<el-row justify="space-between"><el-col :span="20">chat_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型|
|<el-row justify="space-between"><el-col :span="20">rerank_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型|
|<el-row justify="space-between"><el-col :span="20">description_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|描述向量|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|引导词向量|
|<el-row justify="space-between"><el-col :span="20">similarity_threshold</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|召回相似度阈值|
|<el-row justify="space-between"><el-col :span="20">vector_similarity_weight</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|向量相似度权重|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">resource_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">top_k</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最大召回数量|
|<el-row justify="space-between"><el-col :span="20">rerank</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|召回重排|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务键值|
|<el-row justify="space-between"><el-col :span="20">use_kg</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|使用知识图谱|
|<el-row justify="space-between"><el-col :span="20">pageindex</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|智能目录索引|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源类型|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">matched_documents</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|命中文档|
|<el-row justify="space-between"><el-col :span="20">parsed_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|解析文档数|
|<el-row justify="space-between"><el-col :span="20">document_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|文档数|
|<el-row justify="space-between"><el-col :span="20">category_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录标识|
|<el-row justify="space-between"><el-col :span="20">category_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">chat_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">code_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|代码标识|
|<el-row justify="space-between"><el-col :span="20">description</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|描述|
|<el-row justify="space-between"><el-col :span="20">embedding_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|embedding模型|
|<el-row justify="space-between"><el-col :span="20">embedding_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">record_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据记录标识|
|<el-row justify="space-between"><el-col :span="20">record_title</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">rerank_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源标识|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">source_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "is_archived" : null,
  "is_deleted" : null,
  "meta_data" : null,
  "status" : null,
  "is_favorite" : null,
  "tag_sets" : null,
  "scope_type" : null,
  "guidance_prompt" : null,
  "scope_id" : null,
  "chat_model" : null,
  "rerank_model" : null,
  "description_vector" : null,
  "guidance_prompt_vector" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "key" : null,
  "use_kg" : null,
  "pageindex" : null,
  "page_index_info" : null,
  "source_type" : null,
  "summary" : null,
  "matched_documents" : null,
  "parsed_cnt" : null,
  "document_cnt" : null,
  "category_id" : null,
  "category_name" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "code_name" : null,
  "description" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "parser_config" : null,
  "record_id" : null,
  "record_title" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
}
```


##### 响应示例： {docsify-ignore}
```json

{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "is_archived" : null,
  "is_deleted" : null,
  "meta_data" : null,
  "status" : null,
  "is_favorite" : null,
  "tag_sets" : null,
  "scope_type" : null,
  "guidance_prompt" : null,
  "scope_id" : null,
  "chat_model" : null,
  "rerank_model" : null,
  "description_vector" : null,
  "guidance_prompt_vector" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "key" : null,
  "use_kg" : null,
  "pageindex" : null,
  "page_index_info" : null,
  "source_type" : null,
  "summary" : null,
  "matched_documents" : null,
  "parsed_cnt" : null,
  "document_cnt" : null,
  "category_id" : null,
  "category_name" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "code_name" : null,
  "description" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "parser_config" : null,
  "record_id" : null,
  "record_title" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
}

```

## 知识库全盘推理

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{key}/all_doc_reason" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库标识|



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库名称|
|<el-row justify="space-between"><el-col :span="20">visibility</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|可见范围|
|<el-row justify="space-between"><el-col :span="20">is_archived</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已归档|
|<el-row justify="space-between"><el-col :span="20">is_deleted</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已删除|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">is_favorite</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|是否星标|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">scope_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|引导提示词|
|<el-row justify="space-between"><el-col :span="20">scope_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属对象|
|<el-row justify="space-between"><el-col :span="20">chat_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型|
|<el-row justify="space-between"><el-col :span="20">rerank_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型|
|<el-row justify="space-between"><el-col :span="20">description_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|描述向量|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|引导词向量|
|<el-row justify="space-between"><el-col :span="20">similarity_threshold</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|召回相似度阈值|
|<el-row justify="space-between"><el-col :span="20">vector_similarity_weight</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|向量相似度权重|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">resource_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">top_k</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最大召回数量|
|<el-row justify="space-between"><el-col :span="20">rerank</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|召回重排|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务键值|
|<el-row justify="space-between"><el-col :span="20">use_kg</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|使用知识图谱|
|<el-row justify="space-between"><el-col :span="20">pageindex</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|智能目录索引|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源类型|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">matched_documents</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|命中文档|
|<el-row justify="space-between"><el-col :span="20">parsed_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|解析文档数|
|<el-row justify="space-between"><el-col :span="20">document_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|文档数|
|<el-row justify="space-between"><el-col :span="20">category_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录标识|
|<el-row justify="space-between"><el-col :span="20">category_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">chat_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">code_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|代码标识|
|<el-row justify="space-between"><el-col :span="20">description</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|描述|
|<el-row justify="space-between"><el-col :span="20">embedding_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|embedding模型|
|<el-row justify="space-between"><el-col :span="20">embedding_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">record_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据记录标识|
|<el-row justify="space-between"><el-col :span="20">record_title</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">rerank_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源标识|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">source_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "is_archived" : null,
  "is_deleted" : null,
  "meta_data" : null,
  "status" : null,
  "is_favorite" : null,
  "tag_sets" : null,
  "scope_type" : null,
  "guidance_prompt" : null,
  "scope_id" : null,
  "chat_model" : null,
  "rerank_model" : null,
  "description_vector" : null,
  "guidance_prompt_vector" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "key" : null,
  "use_kg" : null,
  "pageindex" : null,
  "page_index_info" : null,
  "source_type" : null,
  "summary" : null,
  "matched_documents" : null,
  "parsed_cnt" : null,
  "document_cnt" : null,
  "category_id" : null,
  "category_name" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "code_name" : null,
  "description" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "parser_config" : null,
  "record_id" : null,
  "record_title" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
}
```



## 变更管理员角色

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{key}/change_admin_role" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`UPDATE`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库标识|



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库名称|
|<el-row justify="space-between"><el-col :span="20">visibility</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|可见范围|
|<el-row justify="space-between"><el-col :span="20">is_archived</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已归档|
|<el-row justify="space-between"><el-col :span="20">is_deleted</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已删除|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">is_favorite</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|是否星标|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">scope_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|引导提示词|
|<el-row justify="space-between"><el-col :span="20">scope_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属对象|
|<el-row justify="space-between"><el-col :span="20">chat_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型|
|<el-row justify="space-between"><el-col :span="20">rerank_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型|
|<el-row justify="space-between"><el-col :span="20">description_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|描述向量|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|引导词向量|
|<el-row justify="space-between"><el-col :span="20">similarity_threshold</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|召回相似度阈值|
|<el-row justify="space-between"><el-col :span="20">vector_similarity_weight</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|向量相似度权重|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">resource_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">top_k</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最大召回数量|
|<el-row justify="space-between"><el-col :span="20">rerank</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|召回重排|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务键值|
|<el-row justify="space-between"><el-col :span="20">use_kg</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|使用知识图谱|
|<el-row justify="space-between"><el-col :span="20">pageindex</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|智能目录索引|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源类型|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">matched_documents</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|命中文档|
|<el-row justify="space-between"><el-col :span="20">parsed_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|解析文档数|
|<el-row justify="space-between"><el-col :span="20">document_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|文档数|
|<el-row justify="space-between"><el-col :span="20">category_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录标识|
|<el-row justify="space-between"><el-col :span="20">category_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">chat_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">code_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|代码标识|
|<el-row justify="space-between"><el-col :span="20">description</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|描述|
|<el-row justify="space-between"><el-col :span="20">embedding_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|embedding模型|
|<el-row justify="space-between"><el-col :span="20">embedding_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">record_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据记录标识|
|<el-row justify="space-between"><el-col :span="20">record_title</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">rerank_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源标识|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">source_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "is_archived" : null,
  "is_deleted" : null,
  "meta_data" : null,
  "status" : null,
  "is_favorite" : null,
  "tag_sets" : null,
  "scope_type" : null,
  "guidance_prompt" : null,
  "scope_id" : null,
  "chat_model" : null,
  "rerank_model" : null,
  "description_vector" : null,
  "guidance_prompt_vector" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "key" : null,
  "use_kg" : null,
  "pageindex" : null,
  "page_index_info" : null,
  "source_type" : null,
  "summary" : null,
  "matched_documents" : null,
  "parsed_cnt" : null,
  "document_cnt" : null,
  "category_id" : null,
  "category_name" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "code_name" : null,
  "description" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "parser_config" : null,
  "record_id" : null,
  "record_title" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
}
```



## 检查知识库主键

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/check_key" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`CREATE`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库名称|
|<el-row justify="space-between"><el-col :span="20">visibility</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|可见范围|
|<el-row justify="space-between"><el-col :span="20">is_archived</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已归档|
|<el-row justify="space-between"><el-col :span="20">is_deleted</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已删除|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">is_favorite</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|是否星标|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">scope_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|引导提示词|
|<el-row justify="space-between"><el-col :span="20">scope_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属对象|
|<el-row justify="space-between"><el-col :span="20">chat_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型|
|<el-row justify="space-between"><el-col :span="20">rerank_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型|
|<el-row justify="space-between"><el-col :span="20">description_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|描述向量|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|引导词向量|
|<el-row justify="space-between"><el-col :span="20">similarity_threshold</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|召回相似度阈值|
|<el-row justify="space-between"><el-col :span="20">vector_similarity_weight</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|向量相似度权重|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">resource_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">top_k</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最大召回数量|
|<el-row justify="space-between"><el-col :span="20">rerank</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|召回重排|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务键值|
|<el-row justify="space-between"><el-col :span="20">use_kg</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|使用知识图谱|
|<el-row justify="space-between"><el-col :span="20">pageindex</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|智能目录索引|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源类型|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">matched_documents</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|命中文档|
|<el-row justify="space-between"><el-col :span="20">parsed_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|解析文档数|
|<el-row justify="space-between"><el-col :span="20">document_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|文档数|
|<el-row justify="space-between"><el-col :span="20">category_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录标识|
|<el-row justify="space-between"><el-col :span="20">category_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">chat_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">code_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|代码标识|
|<el-row justify="space-between"><el-col :span="20">description</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|描述|
|<el-row justify="space-between"><el-col :span="20">embedding_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|embedding模型|
|<el-row justify="space-between"><el-col :span="20">embedding_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">record_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据记录标识|
|<el-row justify="space-between"><el-col :span="20">record_title</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">rerank_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源标识|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">source_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "is_archived" : null,
  "is_deleted" : null,
  "meta_data" : null,
  "status" : null,
  "is_favorite" : null,
  "tag_sets" : null,
  "scope_type" : null,
  "guidance_prompt" : null,
  "scope_id" : null,
  "chat_model" : null,
  "rerank_model" : null,
  "description_vector" : null,
  "guidance_prompt_vector" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "key" : null,
  "use_kg" : null,
  "pageindex" : null,
  "page_index_info" : null,
  "source_type" : null,
  "summary" : null,
  "matched_documents" : null,
  "parsed_cnt" : null,
  "document_cnt" : null,
  "category_id" : null,
  "category_name" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "code_name" : null,
  "description" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "parser_config" : null,
  "record_id" : null,
  "record_title" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
}
```


##### 响应示例： {docsify-ignore}
```json
Integer
```

## 深度研究

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{key}/deep_research" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库标识|



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库名称|
|<el-row justify="space-between"><el-col :span="20">visibility</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|可见范围|
|<el-row justify="space-between"><el-col :span="20">is_archived</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已归档|
|<el-row justify="space-between"><el-col :span="20">is_deleted</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已删除|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">is_favorite</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|是否星标|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">scope_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|引导提示词|
|<el-row justify="space-between"><el-col :span="20">scope_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属对象|
|<el-row justify="space-between"><el-col :span="20">chat_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型|
|<el-row justify="space-between"><el-col :span="20">rerank_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型|
|<el-row justify="space-between"><el-col :span="20">description_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|描述向量|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|引导词向量|
|<el-row justify="space-between"><el-col :span="20">similarity_threshold</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|召回相似度阈值|
|<el-row justify="space-between"><el-col :span="20">vector_similarity_weight</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|向量相似度权重|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">resource_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">top_k</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最大召回数量|
|<el-row justify="space-between"><el-col :span="20">rerank</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|召回重排|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务键值|
|<el-row justify="space-between"><el-col :span="20">use_kg</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|使用知识图谱|
|<el-row justify="space-between"><el-col :span="20">pageindex</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|智能目录索引|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源类型|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">matched_documents</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|命中文档|
|<el-row justify="space-between"><el-col :span="20">parsed_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|解析文档数|
|<el-row justify="space-between"><el-col :span="20">document_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|文档数|
|<el-row justify="space-between"><el-col :span="20">category_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录标识|
|<el-row justify="space-between"><el-col :span="20">category_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">chat_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">code_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|代码标识|
|<el-row justify="space-between"><el-col :span="20">description</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|描述|
|<el-row justify="space-between"><el-col :span="20">embedding_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|embedding模型|
|<el-row justify="space-between"><el-col :span="20">embedding_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">record_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据记录标识|
|<el-row justify="space-between"><el-col :span="20">record_title</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">rerank_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源标识|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">source_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "is_archived" : null,
  "is_deleted" : null,
  "meta_data" : null,
  "status" : null,
  "is_favorite" : null,
  "tag_sets" : null,
  "scope_type" : null,
  "guidance_prompt" : null,
  "scope_id" : null,
  "chat_model" : null,
  "rerank_model" : null,
  "description_vector" : null,
  "guidance_prompt_vector" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "key" : null,
  "use_kg" : null,
  "pageindex" : null,
  "page_index_info" : null,
  "source_type" : null,
  "summary" : null,
  "matched_documents" : null,
  "parsed_cnt" : null,
  "document_cnt" : null,
  "category_id" : null,
  "category_name" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "code_name" : null,
  "description" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "parser_config" : null,
  "record_id" : null,
  "record_title" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
}
```



## 删除

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{key}/delete" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库标识|



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库名称|
|<el-row justify="space-between"><el-col :span="20">visibility</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|可见范围|
|<el-row justify="space-between"><el-col :span="20">is_archived</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已归档|
|<el-row justify="space-between"><el-col :span="20">is_deleted</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已删除|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">is_favorite</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|是否星标|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">scope_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|引导提示词|
|<el-row justify="space-between"><el-col :span="20">scope_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属对象|
|<el-row justify="space-between"><el-col :span="20">chat_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型|
|<el-row justify="space-between"><el-col :span="20">rerank_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型|
|<el-row justify="space-between"><el-col :span="20">description_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|描述向量|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|引导词向量|
|<el-row justify="space-between"><el-col :span="20">similarity_threshold</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|召回相似度阈值|
|<el-row justify="space-between"><el-col :span="20">vector_similarity_weight</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|向量相似度权重|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">resource_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">top_k</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最大召回数量|
|<el-row justify="space-between"><el-col :span="20">rerank</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|召回重排|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务键值|
|<el-row justify="space-between"><el-col :span="20">use_kg</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|使用知识图谱|
|<el-row justify="space-between"><el-col :span="20">pageindex</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|智能目录索引|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源类型|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">matched_documents</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|命中文档|
|<el-row justify="space-between"><el-col :span="20">parsed_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|解析文档数|
|<el-row justify="space-between"><el-col :span="20">document_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|文档数|
|<el-row justify="space-between"><el-col :span="20">category_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录标识|
|<el-row justify="space-between"><el-col :span="20">category_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">chat_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">code_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|代码标识|
|<el-row justify="space-between"><el-col :span="20">description</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|描述|
|<el-row justify="space-between"><el-col :span="20">embedding_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|embedding模型|
|<el-row justify="space-between"><el-col :span="20">embedding_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">record_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据记录标识|
|<el-row justify="space-between"><el-col :span="20">record_title</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">rerank_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源标识|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">source_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "is_archived" : null,
  "is_deleted" : null,
  "meta_data" : null,
  "status" : null,
  "is_favorite" : null,
  "tag_sets" : null,
  "scope_type" : null,
  "guidance_prompt" : null,
  "scope_id" : null,
  "chat_model" : null,
  "rerank_model" : null,
  "description_vector" : null,
  "guidance_prompt_vector" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "key" : null,
  "use_kg" : null,
  "pageindex" : null,
  "page_index_info" : null,
  "source_type" : null,
  "summary" : null,
  "matched_documents" : null,
  "parsed_cnt" : null,
  "document_cnt" : null,
  "category_id" : null,
  "category_name" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "code_name" : null,
  "description" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "parser_config" : null,
  "record_id" : null,
  "record_title" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
}
```



## 设置星标

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{key}/favorite" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库标识|



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库名称|
|<el-row justify="space-between"><el-col :span="20">visibility</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|可见范围|
|<el-row justify="space-between"><el-col :span="20">is_archived</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已归档|
|<el-row justify="space-between"><el-col :span="20">is_deleted</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已删除|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">is_favorite</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|是否星标|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">scope_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|引导提示词|
|<el-row justify="space-between"><el-col :span="20">scope_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属对象|
|<el-row justify="space-between"><el-col :span="20">chat_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型|
|<el-row justify="space-between"><el-col :span="20">rerank_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型|
|<el-row justify="space-between"><el-col :span="20">description_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|描述向量|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|引导词向量|
|<el-row justify="space-between"><el-col :span="20">similarity_threshold</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|召回相似度阈值|
|<el-row justify="space-between"><el-col :span="20">vector_similarity_weight</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|向量相似度权重|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">resource_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">top_k</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最大召回数量|
|<el-row justify="space-between"><el-col :span="20">rerank</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|召回重排|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务键值|
|<el-row justify="space-between"><el-col :span="20">use_kg</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|使用知识图谱|
|<el-row justify="space-between"><el-col :span="20">pageindex</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|智能目录索引|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源类型|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">matched_documents</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|命中文档|
|<el-row justify="space-between"><el-col :span="20">parsed_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|解析文档数|
|<el-row justify="space-between"><el-col :span="20">document_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|文档数|
|<el-row justify="space-between"><el-col :span="20">category_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录标识|
|<el-row justify="space-between"><el-col :span="20">category_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">chat_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">code_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|代码标识|
|<el-row justify="space-between"><el-col :span="20">description</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|描述|
|<el-row justify="space-between"><el-col :span="20">embedding_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|embedding模型|
|<el-row justify="space-between"><el-col :span="20">embedding_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">record_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据记录标识|
|<el-row justify="space-between"><el-col :span="20">record_title</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">rerank_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源标识|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">source_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "is_archived" : null,
  "is_deleted" : null,
  "meta_data" : null,
  "status" : null,
  "is_favorite" : null,
  "tag_sets" : null,
  "scope_type" : null,
  "guidance_prompt" : null,
  "scope_id" : null,
  "chat_model" : null,
  "rerank_model" : null,
  "description_vector" : null,
  "guidance_prompt_vector" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "key" : null,
  "use_kg" : null,
  "pageindex" : null,
  "page_index_info" : null,
  "source_type" : null,
  "summary" : null,
  "matched_documents" : null,
  "parsed_cnt" : null,
  "document_cnt" : null,
  "category_id" : null,
  "category_name" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "code_name" : null,
  "description" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "parser_config" : null,
  "record_id" : null,
  "record_title" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
}
```



## 填充分类配置

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/fill_category_config" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库名称|
|<el-row justify="space-between"><el-col :span="20">visibility</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|可见范围|
|<el-row justify="space-between"><el-col :span="20">is_archived</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已归档|
|<el-row justify="space-between"><el-col :span="20">is_deleted</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已删除|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">is_favorite</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|是否星标|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">scope_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|引导提示词|
|<el-row justify="space-between"><el-col :span="20">scope_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属对象|
|<el-row justify="space-between"><el-col :span="20">chat_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型|
|<el-row justify="space-between"><el-col :span="20">rerank_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型|
|<el-row justify="space-between"><el-col :span="20">description_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|描述向量|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|引导词向量|
|<el-row justify="space-between"><el-col :span="20">similarity_threshold</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|召回相似度阈值|
|<el-row justify="space-between"><el-col :span="20">vector_similarity_weight</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|向量相似度权重|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">resource_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">top_k</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最大召回数量|
|<el-row justify="space-between"><el-col :span="20">rerank</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|召回重排|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务键值|
|<el-row justify="space-between"><el-col :span="20">use_kg</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|使用知识图谱|
|<el-row justify="space-between"><el-col :span="20">pageindex</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|智能目录索引|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源类型|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">matched_documents</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|命中文档|
|<el-row justify="space-between"><el-col :span="20">parsed_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|解析文档数|
|<el-row justify="space-between"><el-col :span="20">document_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|文档数|
|<el-row justify="space-between"><el-col :span="20">category_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录标识|
|<el-row justify="space-between"><el-col :span="20">category_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">chat_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">code_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|代码标识|
|<el-row justify="space-between"><el-col :span="20">description</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|描述|
|<el-row justify="space-between"><el-col :span="20">embedding_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|embedding模型|
|<el-row justify="space-between"><el-col :span="20">embedding_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">record_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据记录标识|
|<el-row justify="space-between"><el-col :span="20">record_title</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">rerank_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源标识|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">source_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "is_archived" : null,
  "is_deleted" : null,
  "meta_data" : null,
  "status" : null,
  "is_favorite" : null,
  "tag_sets" : null,
  "scope_type" : null,
  "guidance_prompt" : null,
  "scope_id" : null,
  "chat_model" : null,
  "rerank_model" : null,
  "description_vector" : null,
  "guidance_prompt_vector" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "key" : null,
  "use_kg" : null,
  "pageindex" : null,
  "page_index_info" : null,
  "source_type" : null,
  "summary" : null,
  "matched_documents" : null,
  "parsed_cnt" : null,
  "document_cnt" : null,
  "category_id" : null,
  "category_name" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "code_name" : null,
  "description" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "parser_config" : null,
  "record_id" : null,
  "record_title" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
}
```


##### 响应示例： {docsify-ignore}
```json

{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "is_archived" : null,
  "is_deleted" : null,
  "meta_data" : null,
  "status" : null,
  "is_favorite" : null,
  "tag_sets" : null,
  "scope_type" : null,
  "guidance_prompt" : null,
  "scope_id" : null,
  "chat_model" : null,
  "rerank_model" : null,
  "description_vector" : null,
  "guidance_prompt_vector" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "key" : null,
  "use_kg" : null,
  "pageindex" : null,
  "page_index_info" : null,
  "source_type" : null,
  "summary" : null,
  "matched_documents" : null,
  "parsed_cnt" : null,
  "document_cnt" : null,
  "category_id" : null,
  "category_name" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "code_name" : null,
  "description" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "parser_config" : null,
  "record_id" : null,
  "record_title" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
}

```

## find_by_code

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/find_by_code" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库名称|
|<el-row justify="space-between"><el-col :span="20">visibility</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|可见范围|
|<el-row justify="space-between"><el-col :span="20">is_archived</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已归档|
|<el-row justify="space-between"><el-col :span="20">is_deleted</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已删除|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">is_favorite</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|是否星标|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">scope_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|引导提示词|
|<el-row justify="space-between"><el-col :span="20">scope_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属对象|
|<el-row justify="space-between"><el-col :span="20">chat_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型|
|<el-row justify="space-between"><el-col :span="20">rerank_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型|
|<el-row justify="space-between"><el-col :span="20">description_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|描述向量|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|引导词向量|
|<el-row justify="space-between"><el-col :span="20">similarity_threshold</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|召回相似度阈值|
|<el-row justify="space-between"><el-col :span="20">vector_similarity_weight</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|向量相似度权重|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">resource_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">top_k</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最大召回数量|
|<el-row justify="space-between"><el-col :span="20">rerank</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|召回重排|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务键值|
|<el-row justify="space-between"><el-col :span="20">use_kg</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|使用知识图谱|
|<el-row justify="space-between"><el-col :span="20">pageindex</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|智能目录索引|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源类型|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">matched_documents</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|命中文档|
|<el-row justify="space-between"><el-col :span="20">parsed_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|解析文档数|
|<el-row justify="space-between"><el-col :span="20">document_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|文档数|
|<el-row justify="space-between"><el-col :span="20">category_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录标识|
|<el-row justify="space-between"><el-col :span="20">category_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">chat_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">code_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|代码标识|
|<el-row justify="space-between"><el-col :span="20">description</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|描述|
|<el-row justify="space-between"><el-col :span="20">embedding_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|embedding模型|
|<el-row justify="space-between"><el-col :span="20">embedding_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">record_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据记录标识|
|<el-row justify="space-between"><el-col :span="20">record_title</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">rerank_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源标识|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">source_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "is_archived" : null,
  "is_deleted" : null,
  "meta_data" : null,
  "status" : null,
  "is_favorite" : null,
  "tag_sets" : null,
  "scope_type" : null,
  "guidance_prompt" : null,
  "scope_id" : null,
  "chat_model" : null,
  "rerank_model" : null,
  "description_vector" : null,
  "guidance_prompt_vector" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "key" : null,
  "use_kg" : null,
  "pageindex" : null,
  "page_index_info" : null,
  "source_type" : null,
  "summary" : null,
  "matched_documents" : null,
  "parsed_cnt" : null,
  "document_cnt" : null,
  "category_id" : null,
  "category_name" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "code_name" : null,
  "description" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "parser_config" : null,
  "record_id" : null,
  "record_title" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
}
```



## 查找知识库首页模版

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{key}/find_template" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库标识|



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库名称|
|<el-row justify="space-between"><el-col :span="20">visibility</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|可见范围|
|<el-row justify="space-between"><el-col :span="20">is_archived</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已归档|
|<el-row justify="space-between"><el-col :span="20">is_deleted</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已删除|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">is_favorite</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|是否星标|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">scope_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|引导提示词|
|<el-row justify="space-between"><el-col :span="20">scope_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属对象|
|<el-row justify="space-between"><el-col :span="20">chat_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型|
|<el-row justify="space-between"><el-col :span="20">rerank_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型|
|<el-row justify="space-between"><el-col :span="20">description_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|描述向量|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|引导词向量|
|<el-row justify="space-between"><el-col :span="20">similarity_threshold</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|召回相似度阈值|
|<el-row justify="space-between"><el-col :span="20">vector_similarity_weight</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|向量相似度权重|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">resource_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">top_k</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最大召回数量|
|<el-row justify="space-between"><el-col :span="20">rerank</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|召回重排|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务键值|
|<el-row justify="space-between"><el-col :span="20">use_kg</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|使用知识图谱|
|<el-row justify="space-between"><el-col :span="20">pageindex</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|智能目录索引|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源类型|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">matched_documents</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|命中文档|
|<el-row justify="space-between"><el-col :span="20">parsed_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|解析文档数|
|<el-row justify="space-between"><el-col :span="20">document_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|文档数|
|<el-row justify="space-between"><el-col :span="20">category_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录标识|
|<el-row justify="space-between"><el-col :span="20">category_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">chat_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">code_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|代码标识|
|<el-row justify="space-between"><el-col :span="20">description</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|描述|
|<el-row justify="space-between"><el-col :span="20">embedding_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|embedding模型|
|<el-row justify="space-between"><el-col :span="20">embedding_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">record_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据记录标识|
|<el-row justify="space-between"><el-col :span="20">record_title</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">rerank_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源标识|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">source_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "is_archived" : null,
  "is_deleted" : null,
  "meta_data" : null,
  "status" : null,
  "is_favorite" : null,
  "tag_sets" : null,
  "scope_type" : null,
  "guidance_prompt" : null,
  "scope_id" : null,
  "chat_model" : null,
  "rerank_model" : null,
  "description_vector" : null,
  "guidance_prompt_vector" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "key" : null,
  "use_kg" : null,
  "pageindex" : null,
  "page_index_info" : null,
  "source_type" : null,
  "summary" : null,
  "matched_documents" : null,
  "parsed_cnt" : null,
  "document_cnt" : null,
  "category_id" : null,
  "category_name" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "code_name" : null,
  "description" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "parser_config" : null,
  "record_id" : null,
  "record_title" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
}
```



## 全文内容推理

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{key}/fulltext_reason" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`
查询知识库下文档，将多文档内容合并后以字数为分割进行逐一推理，最后再总结为整个知识库的报告

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库标识|



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库名称|
|<el-row justify="space-between"><el-col :span="20">visibility</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|可见范围|
|<el-row justify="space-between"><el-col :span="20">is_archived</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已归档|
|<el-row justify="space-between"><el-col :span="20">is_deleted</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已删除|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">is_favorite</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|是否星标|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">scope_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|引导提示词|
|<el-row justify="space-between"><el-col :span="20">scope_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属对象|
|<el-row justify="space-between"><el-col :span="20">chat_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型|
|<el-row justify="space-between"><el-col :span="20">rerank_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型|
|<el-row justify="space-between"><el-col :span="20">description_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|描述向量|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|引导词向量|
|<el-row justify="space-between"><el-col :span="20">similarity_threshold</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|召回相似度阈值|
|<el-row justify="space-between"><el-col :span="20">vector_similarity_weight</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|向量相似度权重|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">resource_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">top_k</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最大召回数量|
|<el-row justify="space-between"><el-col :span="20">rerank</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|召回重排|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务键值|
|<el-row justify="space-between"><el-col :span="20">use_kg</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|使用知识图谱|
|<el-row justify="space-between"><el-col :span="20">pageindex</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|智能目录索引|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源类型|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">matched_documents</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|命中文档|
|<el-row justify="space-between"><el-col :span="20">parsed_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|解析文档数|
|<el-row justify="space-between"><el-col :span="20">document_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|文档数|
|<el-row justify="space-between"><el-col :span="20">category_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录标识|
|<el-row justify="space-between"><el-col :span="20">category_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">chat_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">code_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|代码标识|
|<el-row justify="space-between"><el-col :span="20">description</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|描述|
|<el-row justify="space-between"><el-col :span="20">embedding_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|embedding模型|
|<el-row justify="space-between"><el-col :span="20">embedding_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">record_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据记录标识|
|<el-row justify="space-between"><el-col :span="20">record_title</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">rerank_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源标识|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">source_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "is_archived" : null,
  "is_deleted" : null,
  "meta_data" : null,
  "status" : null,
  "is_favorite" : null,
  "tag_sets" : null,
  "scope_type" : null,
  "guidance_prompt" : null,
  "scope_id" : null,
  "chat_model" : null,
  "rerank_model" : null,
  "description_vector" : null,
  "guidance_prompt_vector" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "key" : null,
  "use_kg" : null,
  "pageindex" : null,
  "page_index_info" : null,
  "source_type" : null,
  "summary" : null,
  "matched_documents" : null,
  "parsed_cnt" : null,
  "document_cnt" : null,
  "category_id" : null,
  "category_name" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "code_name" : null,
  "description" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "parser_config" : null,
  "record_id" : null,
  "record_title" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
}
```



## 生成引导提示词

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{key}/generate_guided_prompts" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`UPDATE`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库标识|



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库名称|
|<el-row justify="space-between"><el-col :span="20">visibility</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|可见范围|
|<el-row justify="space-between"><el-col :span="20">is_archived</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已归档|
|<el-row justify="space-between"><el-col :span="20">is_deleted</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已删除|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">is_favorite</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|是否星标|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">scope_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|引导提示词|
|<el-row justify="space-between"><el-col :span="20">scope_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属对象|
|<el-row justify="space-between"><el-col :span="20">chat_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型|
|<el-row justify="space-between"><el-col :span="20">rerank_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型|
|<el-row justify="space-between"><el-col :span="20">description_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|描述向量|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|引导词向量|
|<el-row justify="space-between"><el-col :span="20">similarity_threshold</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|召回相似度阈值|
|<el-row justify="space-between"><el-col :span="20">vector_similarity_weight</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|向量相似度权重|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">resource_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">top_k</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最大召回数量|
|<el-row justify="space-between"><el-col :span="20">rerank</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|召回重排|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务键值|
|<el-row justify="space-between"><el-col :span="20">use_kg</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|使用知识图谱|
|<el-row justify="space-between"><el-col :span="20">pageindex</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|智能目录索引|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源类型|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">matched_documents</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|命中文档|
|<el-row justify="space-between"><el-col :span="20">parsed_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|解析文档数|
|<el-row justify="space-between"><el-col :span="20">document_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|文档数|
|<el-row justify="space-between"><el-col :span="20">category_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录标识|
|<el-row justify="space-between"><el-col :span="20">category_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">chat_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">code_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|代码标识|
|<el-row justify="space-between"><el-col :span="20">description</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|描述|
|<el-row justify="space-between"><el-col :span="20">embedding_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|embedding模型|
|<el-row justify="space-between"><el-col :span="20">embedding_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">record_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据记录标识|
|<el-row justify="space-between"><el-col :span="20">record_title</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">rerank_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源标识|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">source_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "is_archived" : null,
  "is_deleted" : null,
  "meta_data" : null,
  "status" : null,
  "is_favorite" : null,
  "tag_sets" : null,
  "scope_type" : null,
  "guidance_prompt" : null,
  "scope_id" : null,
  "chat_model" : null,
  "rerank_model" : null,
  "description_vector" : null,
  "guidance_prompt_vector" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "key" : null,
  "use_kg" : null,
  "pageindex" : null,
  "page_index_info" : null,
  "source_type" : null,
  "summary" : null,
  "matched_documents" : null,
  "parsed_cnt" : null,
  "document_cnt" : null,
  "category_id" : null,
  "category_name" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "code_name" : null,
  "description" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "parser_config" : null,
  "record_id" : null,
  "record_title" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
}
```



## 获取知识库草稿

<el-row>
<div style="width: 80px">
<el-alert center title="GET" type="success" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/get_draft" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`CREATE`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库名称|
|<el-row justify="space-between"><el-col :span="20">visibility</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|可见范围|
|<el-row justify="space-between"><el-col :span="20">is_archived</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已归档|
|<el-row justify="space-between"><el-col :span="20">is_deleted</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已删除|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">is_favorite</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|是否星标|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">scope_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|引导提示词|
|<el-row justify="space-between"><el-col :span="20">scope_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属对象|
|<el-row justify="space-between"><el-col :span="20">chat_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型|
|<el-row justify="space-between"><el-col :span="20">rerank_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型|
|<el-row justify="space-between"><el-col :span="20">description_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|描述向量|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|引导词向量|
|<el-row justify="space-between"><el-col :span="20">similarity_threshold</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|召回相似度阈值|
|<el-row justify="space-between"><el-col :span="20">vector_similarity_weight</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|向量相似度权重|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">resource_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">top_k</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最大召回数量|
|<el-row justify="space-between"><el-col :span="20">rerank</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|召回重排|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务键值|
|<el-row justify="space-between"><el-col :span="20">use_kg</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|使用知识图谱|
|<el-row justify="space-between"><el-col :span="20">pageindex</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|智能目录索引|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源类型|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">matched_documents</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|命中文档|
|<el-row justify="space-between"><el-col :span="20">parsed_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|解析文档数|
|<el-row justify="space-between"><el-col :span="20">document_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|文档数|
|<el-row justify="space-between"><el-col :span="20">category_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录标识|
|<el-row justify="space-between"><el-col :span="20">category_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">chat_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">code_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|代码标识|
|<el-row justify="space-between"><el-col :span="20">description</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|描述|
|<el-row justify="space-between"><el-col :span="20">embedding_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|embedding模型|
|<el-row justify="space-between"><el-col :span="20">embedding_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">record_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据记录标识|
|<el-row justify="space-between"><el-col :span="20">record_title</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">rerank_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源标识|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">source_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "is_archived" : null,
  "is_deleted" : null,
  "meta_data" : null,
  "status" : null,
  "is_favorite" : null,
  "tag_sets" : null,
  "scope_type" : null,
  "guidance_prompt" : null,
  "scope_id" : null,
  "chat_model" : null,
  "rerank_model" : null,
  "description_vector" : null,
  "guidance_prompt_vector" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "key" : null,
  "use_kg" : null,
  "pageindex" : null,
  "page_index_info" : null,
  "source_type" : null,
  "summary" : null,
  "matched_documents" : null,
  "parsed_cnt" : null,
  "document_cnt" : null,
  "category_id" : null,
  "category_name" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "code_name" : null,
  "description" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "parser_config" : null,
  "record_id" : null,
  "record_title" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
}
```


##### 响应示例： {docsify-ignore}
```json

{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "is_archived" : null,
  "is_deleted" : null,
  "meta_data" : null,
  "status" : null,
  "is_favorite" : null,
  "tag_sets" : null,
  "scope_type" : null,
  "guidance_prompt" : null,
  "scope_id" : null,
  "chat_model" : null,
  "rerank_model" : null,
  "description_vector" : null,
  "guidance_prompt_vector" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "key" : null,
  "use_kg" : null,
  "pageindex" : null,
  "page_index_info" : null,
  "source_type" : null,
  "summary" : null,
  "matched_documents" : null,
  "parsed_cnt" : null,
  "document_cnt" : null,
  "category_id" : null,
  "category_name" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "code_name" : null,
  "description" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "parser_config" : null,
  "record_id" : null,
  "record_title" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
}

```

## GetFullData

<el-row>
<div style="width: 80px">
<el-alert center title="GET" type="success" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{key}/get_full_data" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库标识|




##### 响应示例： {docsify-ignore}
```json

{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "is_archived" : null,
  "is_deleted" : null,
  "meta_data" : null,
  "status" : null,
  "is_favorite" : null,
  "tag_sets" : null,
  "scope_type" : null,
  "guidance_prompt" : null,
  "scope_id" : null,
  "chat_model" : null,
  "rerank_model" : null,
  "description_vector" : null,
  "guidance_prompt_vector" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "key" : null,
  "use_kg" : null,
  "pageindex" : null,
  "page_index_info" : null,
  "source_type" : null,
  "summary" : null,
  "matched_documents" : null,
  "parsed_cnt" : null,
  "document_cnt" : null,
  "category_id" : null,
  "category_name" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "code_name" : null,
  "description" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "parser_config" : null,
  "record_id" : null,
  "record_title" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
}

```

## ls

<el-row>
<div style="width: 80px">
<el-alert center title="GET" type="success" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{key}/ls" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库标识|




##### 响应示例： {docsify-ignore}
```json

{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "is_archived" : null,
  "is_deleted" : null,
  "meta_data" : null,
  "status" : null,
  "is_favorite" : null,
  "tag_sets" : null,
  "scope_type" : null,
  "guidance_prompt" : null,
  "scope_id" : null,
  "chat_model" : null,
  "rerank_model" : null,
  "description_vector" : null,
  "guidance_prompt_vector" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "key" : null,
  "use_kg" : null,
  "pageindex" : null,
  "page_index_info" : null,
  "source_type" : null,
  "summary" : null,
  "matched_documents" : null,
  "parsed_cnt" : null,
  "document_cnt" : null,
  "category_id" : null,
  "category_name" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "code_name" : null,
  "description" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "parser_config" : null,
  "record_id" : null,
  "record_title" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
}

```

## 获取参考资料

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{key}/query_references" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库标识|



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库名称|
|<el-row justify="space-between"><el-col :span="20">visibility</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|可见范围|
|<el-row justify="space-between"><el-col :span="20">is_archived</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已归档|
|<el-row justify="space-between"><el-col :span="20">is_deleted</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已删除|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">is_favorite</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|是否星标|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">scope_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|引导提示词|
|<el-row justify="space-between"><el-col :span="20">scope_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属对象|
|<el-row justify="space-between"><el-col :span="20">chat_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型|
|<el-row justify="space-between"><el-col :span="20">rerank_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型|
|<el-row justify="space-between"><el-col :span="20">description_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|描述向量|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|引导词向量|
|<el-row justify="space-between"><el-col :span="20">similarity_threshold</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|召回相似度阈值|
|<el-row justify="space-between"><el-col :span="20">vector_similarity_weight</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|向量相似度权重|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">resource_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">top_k</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最大召回数量|
|<el-row justify="space-between"><el-col :span="20">rerank</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|召回重排|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务键值|
|<el-row justify="space-between"><el-col :span="20">use_kg</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|使用知识图谱|
|<el-row justify="space-between"><el-col :span="20">pageindex</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|智能目录索引|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源类型|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">matched_documents</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|命中文档|
|<el-row justify="space-between"><el-col :span="20">parsed_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|解析文档数|
|<el-row justify="space-between"><el-col :span="20">document_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|文档数|
|<el-row justify="space-between"><el-col :span="20">category_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录标识|
|<el-row justify="space-between"><el-col :span="20">category_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">chat_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">code_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|代码标识|
|<el-row justify="space-between"><el-col :span="20">description</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|描述|
|<el-row justify="space-between"><el-col :span="20">embedding_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|embedding模型|
|<el-row justify="space-between"><el-col :span="20">embedding_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">record_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据记录标识|
|<el-row justify="space-between"><el-col :span="20">record_title</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">rerank_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源标识|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">source_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "is_archived" : null,
  "is_deleted" : null,
  "meta_data" : null,
  "status" : null,
  "is_favorite" : null,
  "tag_sets" : null,
  "scope_type" : null,
  "guidance_prompt" : null,
  "scope_id" : null,
  "chat_model" : null,
  "rerank_model" : null,
  "description_vector" : null,
  "guidance_prompt_vector" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "key" : null,
  "use_kg" : null,
  "pageindex" : null,
  "page_index_info" : null,
  "source_type" : null,
  "summary" : null,
  "matched_documents" : null,
  "parsed_cnt" : null,
  "document_cnt" : null,
  "category_id" : null,
  "category_name" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "code_name" : null,
  "description" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "parser_config" : null,
  "record_id" : null,
  "record_title" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
}
```



## 推理

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{key}/reason" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库标识|



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库名称|
|<el-row justify="space-between"><el-col :span="20">visibility</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|可见范围|
|<el-row justify="space-between"><el-col :span="20">is_archived</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已归档|
|<el-row justify="space-between"><el-col :span="20">is_deleted</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已删除|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">is_favorite</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|是否星标|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">scope_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|引导提示词|
|<el-row justify="space-between"><el-col :span="20">scope_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属对象|
|<el-row justify="space-between"><el-col :span="20">chat_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型|
|<el-row justify="space-between"><el-col :span="20">rerank_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型|
|<el-row justify="space-between"><el-col :span="20">description_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|描述向量|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|引导词向量|
|<el-row justify="space-between"><el-col :span="20">similarity_threshold</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|召回相似度阈值|
|<el-row justify="space-between"><el-col :span="20">vector_similarity_weight</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|向量相似度权重|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">resource_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">top_k</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最大召回数量|
|<el-row justify="space-between"><el-col :span="20">rerank</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|召回重排|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务键值|
|<el-row justify="space-between"><el-col :span="20">use_kg</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|使用知识图谱|
|<el-row justify="space-between"><el-col :span="20">pageindex</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|智能目录索引|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源类型|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">matched_documents</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|命中文档|
|<el-row justify="space-between"><el-col :span="20">parsed_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|解析文档数|
|<el-row justify="space-between"><el-col :span="20">document_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|文档数|
|<el-row justify="space-between"><el-col :span="20">category_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录标识|
|<el-row justify="space-between"><el-col :span="20">category_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">chat_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">code_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|代码标识|
|<el-row justify="space-between"><el-col :span="20">description</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|描述|
|<el-row justify="space-between"><el-col :span="20">embedding_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|embedding模型|
|<el-row justify="space-between"><el-col :span="20">embedding_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">record_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据记录标识|
|<el-row justify="space-between"><el-col :span="20">record_title</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">rerank_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源标识|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">source_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "is_archived" : null,
  "is_deleted" : null,
  "meta_data" : null,
  "status" : null,
  "is_favorite" : null,
  "tag_sets" : null,
  "scope_type" : null,
  "guidance_prompt" : null,
  "scope_id" : null,
  "chat_model" : null,
  "rerank_model" : null,
  "description_vector" : null,
  "guidance_prompt_vector" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "key" : null,
  "use_kg" : null,
  "pageindex" : null,
  "page_index_info" : null,
  "source_type" : null,
  "summary" : null,
  "matched_documents" : null,
  "parsed_cnt" : null,
  "document_cnt" : null,
  "category_id" : null,
  "category_name" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "code_name" : null,
  "description" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "parser_config" : null,
  "record_id" : null,
  "record_title" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
}
```



## 恢复

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{key}/recover" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库标识|



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库名称|
|<el-row justify="space-between"><el-col :span="20">visibility</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|可见范围|
|<el-row justify="space-between"><el-col :span="20">is_archived</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已归档|
|<el-row justify="space-between"><el-col :span="20">is_deleted</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已删除|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">is_favorite</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|是否星标|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">scope_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|引导提示词|
|<el-row justify="space-between"><el-col :span="20">scope_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属对象|
|<el-row justify="space-between"><el-col :span="20">chat_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型|
|<el-row justify="space-between"><el-col :span="20">rerank_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型|
|<el-row justify="space-between"><el-col :span="20">description_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|描述向量|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|引导词向量|
|<el-row justify="space-between"><el-col :span="20">similarity_threshold</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|召回相似度阈值|
|<el-row justify="space-between"><el-col :span="20">vector_similarity_weight</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|向量相似度权重|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">resource_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">top_k</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最大召回数量|
|<el-row justify="space-between"><el-col :span="20">rerank</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|召回重排|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务键值|
|<el-row justify="space-between"><el-col :span="20">use_kg</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|使用知识图谱|
|<el-row justify="space-between"><el-col :span="20">pageindex</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|智能目录索引|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源类型|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">matched_documents</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|命中文档|
|<el-row justify="space-between"><el-col :span="20">parsed_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|解析文档数|
|<el-row justify="space-between"><el-col :span="20">document_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|文档数|
|<el-row justify="space-between"><el-col :span="20">category_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录标识|
|<el-row justify="space-between"><el-col :span="20">category_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">chat_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">code_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|代码标识|
|<el-row justify="space-between"><el-col :span="20">description</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|描述|
|<el-row justify="space-between"><el-col :span="20">embedding_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|embedding模型|
|<el-row justify="space-between"><el-col :span="20">embedding_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">record_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据记录标识|
|<el-row justify="space-between"><el-col :span="20">record_title</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">rerank_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源标识|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">source_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "is_archived" : null,
  "is_deleted" : null,
  "meta_data" : null,
  "status" : null,
  "is_favorite" : null,
  "tag_sets" : null,
  "scope_type" : null,
  "guidance_prompt" : null,
  "scope_id" : null,
  "chat_model" : null,
  "rerank_model" : null,
  "description_vector" : null,
  "guidance_prompt_vector" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "key" : null,
  "use_kg" : null,
  "pageindex" : null,
  "page_index_info" : null,
  "source_type" : null,
  "summary" : null,
  "matched_documents" : null,
  "parsed_cnt" : null,
  "document_cnt" : null,
  "category_id" : null,
  "category_name" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "code_name" : null,
  "description" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "parser_config" : null,
  "record_id" : null,
  "record_title" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
}
```



## 保存知识库

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/save" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`CREATE`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库名称|
|<el-row justify="space-between"><el-col :span="20">visibility</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|可见范围|
|<el-row justify="space-between"><el-col :span="20">is_archived</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已归档|
|<el-row justify="space-between"><el-col :span="20">is_deleted</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已删除|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">is_favorite</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|是否星标|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">scope_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|引导提示词|
|<el-row justify="space-between"><el-col :span="20">scope_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属对象|
|<el-row justify="space-between"><el-col :span="20">chat_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型|
|<el-row justify="space-between"><el-col :span="20">rerank_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型|
|<el-row justify="space-between"><el-col :span="20">description_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|描述向量|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|引导词向量|
|<el-row justify="space-between"><el-col :span="20">similarity_threshold</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|召回相似度阈值|
|<el-row justify="space-between"><el-col :span="20">vector_similarity_weight</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|向量相似度权重|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">resource_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">top_k</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最大召回数量|
|<el-row justify="space-between"><el-col :span="20">rerank</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|召回重排|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务键值|
|<el-row justify="space-between"><el-col :span="20">use_kg</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|使用知识图谱|
|<el-row justify="space-between"><el-col :span="20">pageindex</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|智能目录索引|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源类型|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">matched_documents</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|命中文档|
|<el-row justify="space-between"><el-col :span="20">parsed_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|解析文档数|
|<el-row justify="space-between"><el-col :span="20">document_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|文档数|
|<el-row justify="space-between"><el-col :span="20">category_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录标识|
|<el-row justify="space-between"><el-col :span="20">category_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">chat_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">code_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|代码标识|
|<el-row justify="space-between"><el-col :span="20">description</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|描述|
|<el-row justify="space-between"><el-col :span="20">embedding_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|embedding模型|
|<el-row justify="space-between"><el-col :span="20">embedding_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">record_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据记录标识|
|<el-row justify="space-between"><el-col :span="20">record_title</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">rerank_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源标识|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">source_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "is_archived" : null,
  "is_deleted" : null,
  "meta_data" : null,
  "status" : null,
  "is_favorite" : null,
  "tag_sets" : null,
  "scope_type" : null,
  "guidance_prompt" : null,
  "scope_id" : null,
  "chat_model" : null,
  "rerank_model" : null,
  "description_vector" : null,
  "guidance_prompt_vector" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "key" : null,
  "use_kg" : null,
  "pageindex" : null,
  "page_index_info" : null,
  "source_type" : null,
  "summary" : null,
  "matched_documents" : null,
  "parsed_cnt" : null,
  "document_cnt" : null,
  "category_id" : null,
  "category_name" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "code_name" : null,
  "description" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "parser_config" : null,
  "record_id" : null,
  "record_title" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
}
```


##### 响应示例： {docsify-ignore}
```json

{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "is_archived" : null,
  "is_deleted" : null,
  "meta_data" : null,
  "status" : null,
  "is_favorite" : null,
  "tag_sets" : null,
  "scope_type" : null,
  "guidance_prompt" : null,
  "scope_id" : null,
  "chat_model" : null,
  "rerank_model" : null,
  "description_vector" : null,
  "guidance_prompt_vector" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "key" : null,
  "use_kg" : null,
  "pageindex" : null,
  "page_index_info" : null,
  "source_type" : null,
  "summary" : null,
  "matched_documents" : null,
  "parsed_cnt" : null,
  "document_cnt" : null,
  "category_id" : null,
  "category_name" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "code_name" : null,
  "description" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "parser_config" : null,
  "record_id" : null,
  "record_title" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
}

```

## 取消星标

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{key}/un_favorite" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库标识|



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库名称|
|<el-row justify="space-between"><el-col :span="20">visibility</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|可见范围|
|<el-row justify="space-between"><el-col :span="20">is_archived</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已归档|
|<el-row justify="space-between"><el-col :span="20">is_deleted</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|是否已删除|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">is_favorite</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|是否星标|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">scope_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|引导提示词|
|<el-row justify="space-between"><el-col :span="20">scope_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属对象|
|<el-row justify="space-between"><el-col :span="20">chat_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型|
|<el-row justify="space-between"><el-col :span="20">rerank_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型|
|<el-row justify="space-between"><el-col :span="20">description_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|描述向量|
|<el-row justify="space-between"><el-col :span="20">guidance_prompt_vector</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|引导词向量|
|<el-row justify="space-between"><el-col :span="20">similarity_threshold</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|召回相似度阈值|
|<el-row justify="space-between"><el-col :span="20">vector_similarity_weight</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|向量相似度权重|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">resource_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">top_k</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最大召回数量|
|<el-row justify="space-between"><el-col :span="20">rerank</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|召回重排|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务键值|
|<el-row justify="space-between"><el-col :span="20">use_kg</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|使用知识图谱|
|<el-row justify="space-between"><el-col :span="20">pageindex</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|智能目录索引|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源类型|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">matched_documents</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|命中文档|
|<el-row justify="space-between"><el-col :span="20">parsed_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|解析文档数|
|<el-row justify="space-between"><el-col :span="20">document_cnt</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|文档数|
|<el-row justify="space-between"><el-col :span="20">category_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录标识|
|<el-row justify="space-between"><el-col :span="20">category_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">chat_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">code_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|代码标识|
|<el-row justify="space-between"><el-col :span="20">description</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|描述|
|<el-row justify="space-between"><el-col :span="20">embedding_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|embedding模型|
|<el-row justify="space-between"><el-col :span="20">embedding_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">record_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据记录标识|
|<el-row justify="space-between"><el-col :span="20">record_title</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">rerank_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源标识|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">source_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "is_archived" : null,
  "is_deleted" : null,
  "meta_data" : null,
  "status" : null,
  "is_favorite" : null,
  "tag_sets" : null,
  "scope_type" : null,
  "guidance_prompt" : null,
  "scope_id" : null,
  "chat_model" : null,
  "rerank_model" : null,
  "description_vector" : null,
  "guidance_prompt_vector" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "key" : null,
  "use_kg" : null,
  "pageindex" : null,
  "page_index_info" : null,
  "source_type" : null,
  "summary" : null,
  "matched_documents" : null,
  "parsed_cnt" : null,
  "document_cnt" : null,
  "category_id" : null,
  "category_name" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "code_name" : null,
  "description" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "parser_config" : null,
  "record_id" : null,
  "record_title" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
}
```



## 管理员

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/fetch_admin" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_category_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录标识|
|<el-row justify="space-between"><el-col :span="20">n_category_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">n_category_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">n_chat_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">n_embedding_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">n_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_id_noteq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库名称|
|<el-row justify="space-between"><el-col :span="20">n_record_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据记录标识|
|<el-row justify="space-between"><el-col :span="20">n_record_title_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">n_record_title_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">n_rerank_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">n_resource_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">n_resource_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源标识|
|<el-row justify="space-between"><el-col :span="20">n_resource_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">n_scope_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属|
|<el-row justify="space-between"><el-col :span="20">n_source_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">n_source_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|
|<el-row justify="space-between"><el-col :span="20">n_source_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|



##### 请求示例： {docsify-ignore}
```json
{
  "page" : 0,
  "size" : 20,
  "sort" : null,
  "n_category_id_eq" : null,
  "n_category_name_eq" : null,
  "n_category_name_like" : null,
  "n_chat_model_id_eq" : null,
  "n_embedding_model_id_eq" : null,
  "n_id_eq" : null,
  "n_id_noteq" : null,
  "n_name_like" : null,
  "n_record_id_eq" : null,
  "n_record_title_eq" : null,
  "n_record_title_like" : null,
  "n_rerank_model_id_eq" : null,
  "n_resource_eq" : null,
  "n_resource_id_eq" : null,
  "n_resource_like" : null,
  "n_scope_type_eq" : null,
  "n_source_id_eq" : null,
  "n_source_name_eq" : null,
  "n_source_name_like" : null,
}
```


##### 响应示例： {docsify-ignore}
```json
[
  {
    "id" : null,
    "name" : null,
    "create_man" : null,
    "create_time" : null,
    "update_man" : null,
    "update_time" : null,
    "visibility" : null,
    "is_archived" : null,
    "is_deleted" : null,
    "meta_data" : null,
    "status" : null,
    "is_favorite" : null,
    "tag_sets" : null,
    "scope_type" : null,
    "guidance_prompt" : null,
    "scope_id" : null,
    "chat_model" : null,
    "rerank_model" : null,
    "description_vector" : null,
    "guidance_prompt_vector" : null,
    "similarity_threshold" : null,
    "vector_similarity_weight" : null,
    "resource" : null,
    "resource_code" : null,
    "top_k" : null,
    "rerank" : null,
    "key" : null,
    "use_kg" : null,
    "pageindex" : null,
    "page_index_info" : null,
    "source_type" : null,
    "summary" : null,
    "matched_documents" : null,
    "parsed_cnt" : null,
    "document_cnt" : null,
    "category_id" : null,
    "category_name" : null,
    "chat_model_id" : null,
    "chunk_method" : null,
    "code_name" : null,
    "description" : null,
    "embedding_model" : null,
    "embedding_model_id" : null,
    "parser_config" : null,
    "record_id" : null,
    "record_title" : null,
    "rerank_model_id" : null,
    "resource_id" : null,
    "source_id" : null,
    "source_name" : null,
  }
]
```

## AI知识库目录查询

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/fetch_ai_docs_by_kb" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_category_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录标识|
|<el-row justify="space-between"><el-col :span="20">n_category_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">n_category_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">n_chat_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">n_embedding_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">n_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_id_noteq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库名称|
|<el-row justify="space-between"><el-col :span="20">n_record_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据记录标识|
|<el-row justify="space-between"><el-col :span="20">n_record_title_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">n_record_title_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">n_rerank_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">n_resource_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">n_resource_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源标识|
|<el-row justify="space-between"><el-col :span="20">n_resource_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">n_scope_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属|
|<el-row justify="space-between"><el-col :span="20">n_source_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">n_source_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|
|<el-row justify="space-between"><el-col :span="20">n_source_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|



##### 请求示例： {docsify-ignore}
```json
{
  "page" : 0,
  "size" : 20,
  "sort" : null,
  "n_category_id_eq" : null,
  "n_category_name_eq" : null,
  "n_category_name_like" : null,
  "n_chat_model_id_eq" : null,
  "n_embedding_model_id_eq" : null,
  "n_id_eq" : null,
  "n_id_noteq" : null,
  "n_name_like" : null,
  "n_record_id_eq" : null,
  "n_record_title_eq" : null,
  "n_record_title_like" : null,
  "n_rerank_model_id_eq" : null,
  "n_resource_eq" : null,
  "n_resource_id_eq" : null,
  "n_resource_like" : null,
  "n_scope_type_eq" : null,
  "n_source_id_eq" : null,
  "n_source_name_eq" : null,
  "n_source_name_like" : null,
}
```


##### 响应示例： {docsify-ignore}
```json
[
  {
    "id" : null,
    "name" : null,
    "create_man" : null,
    "create_time" : null,
    "update_man" : null,
    "update_time" : null,
    "visibility" : null,
    "is_archived" : null,
    "is_deleted" : null,
    "meta_data" : null,
    "status" : null,
    "is_favorite" : null,
    "tag_sets" : null,
    "scope_type" : null,
    "guidance_prompt" : null,
    "scope_id" : null,
    "chat_model" : null,
    "rerank_model" : null,
    "description_vector" : null,
    "guidance_prompt_vector" : null,
    "similarity_threshold" : null,
    "vector_similarity_weight" : null,
    "resource" : null,
    "resource_code" : null,
    "top_k" : null,
    "rerank" : null,
    "key" : null,
    "use_kg" : null,
    "pageindex" : null,
    "page_index_info" : null,
    "source_type" : null,
    "summary" : null,
    "matched_documents" : null,
    "parsed_cnt" : null,
    "document_cnt" : null,
    "category_id" : null,
    "category_name" : null,
    "chat_model_id" : null,
    "chunk_method" : null,
    "code_name" : null,
    "description" : null,
    "embedding_model" : null,
    "embedding_model_id" : null,
    "parser_config" : null,
    "record_id" : null,
    "record_title" : null,
    "rerank_model_id" : null,
    "resource_id" : null,
    "source_id" : null,
    "source_name" : null,
  }
]
```

## AI知识库清单查询

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/fetch_ai_kb_query" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_category_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录标识|
|<el-row justify="space-between"><el-col :span="20">n_category_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">n_category_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">n_chat_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">n_embedding_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">n_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_id_noteq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库名称|
|<el-row justify="space-between"><el-col :span="20">n_record_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据记录标识|
|<el-row justify="space-between"><el-col :span="20">n_record_title_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">n_record_title_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">n_rerank_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">n_resource_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">n_resource_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源标识|
|<el-row justify="space-between"><el-col :span="20">n_resource_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">n_scope_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属|
|<el-row justify="space-between"><el-col :span="20">n_source_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">n_source_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|
|<el-row justify="space-between"><el-col :span="20">n_source_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|



##### 请求示例： {docsify-ignore}
```json
{
  "page" : 0,
  "size" : 20,
  "sort" : null,
  "n_category_id_eq" : null,
  "n_category_name_eq" : null,
  "n_category_name_like" : null,
  "n_chat_model_id_eq" : null,
  "n_embedding_model_id_eq" : null,
  "n_id_eq" : null,
  "n_id_noteq" : null,
  "n_name_like" : null,
  "n_record_id_eq" : null,
  "n_record_title_eq" : null,
  "n_record_title_like" : null,
  "n_rerank_model_id_eq" : null,
  "n_resource_eq" : null,
  "n_resource_id_eq" : null,
  "n_resource_like" : null,
  "n_scope_type_eq" : null,
  "n_source_id_eq" : null,
  "n_source_name_eq" : null,
  "n_source_name_like" : null,
}
```


##### 响应示例： {docsify-ignore}
```json
[
  {
    "id" : null,
    "name" : null,
    "create_man" : null,
    "create_time" : null,
    "update_man" : null,
    "update_time" : null,
    "visibility" : null,
    "is_archived" : null,
    "is_deleted" : null,
    "meta_data" : null,
    "status" : null,
    "is_favorite" : null,
    "tag_sets" : null,
    "scope_type" : null,
    "guidance_prompt" : null,
    "scope_id" : null,
    "chat_model" : null,
    "rerank_model" : null,
    "description_vector" : null,
    "guidance_prompt_vector" : null,
    "similarity_threshold" : null,
    "vector_similarity_weight" : null,
    "resource" : null,
    "resource_code" : null,
    "top_k" : null,
    "rerank" : null,
    "key" : null,
    "use_kg" : null,
    "pageindex" : null,
    "page_index_info" : null,
    "source_type" : null,
    "summary" : null,
    "matched_documents" : null,
    "parsed_cnt" : null,
    "document_cnt" : null,
    "category_id" : null,
    "category_name" : null,
    "chat_model_id" : null,
    "chunk_method" : null,
    "code_name" : null,
    "description" : null,
    "embedding_model" : null,
    "embedding_model_id" : null,
    "parser_config" : null,
    "record_id" : null,
    "record_title" : null,
    "rerank_model_id" : null,
    "resource_id" : null,
    "source_id" : null,
    "source_name" : null,
  }
]
```

## 目录下的知识库

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/fetch_category_ai_kb" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_category_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录标识|
|<el-row justify="space-between"><el-col :span="20">n_category_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">n_category_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">n_chat_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">n_embedding_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">n_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_id_noteq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库名称|
|<el-row justify="space-between"><el-col :span="20">n_record_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据记录标识|
|<el-row justify="space-between"><el-col :span="20">n_record_title_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">n_record_title_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">n_rerank_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">n_resource_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">n_resource_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源标识|
|<el-row justify="space-between"><el-col :span="20">n_resource_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">n_scope_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属|
|<el-row justify="space-between"><el-col :span="20">n_source_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">n_source_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|
|<el-row justify="space-between"><el-col :span="20">n_source_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|



##### 请求示例： {docsify-ignore}
```json
{
  "page" : 0,
  "size" : 20,
  "sort" : null,
  "n_category_id_eq" : null,
  "n_category_name_eq" : null,
  "n_category_name_like" : null,
  "n_chat_model_id_eq" : null,
  "n_embedding_model_id_eq" : null,
  "n_id_eq" : null,
  "n_id_noteq" : null,
  "n_name_like" : null,
  "n_record_id_eq" : null,
  "n_record_title_eq" : null,
  "n_record_title_like" : null,
  "n_rerank_model_id_eq" : null,
  "n_resource_eq" : null,
  "n_resource_id_eq" : null,
  "n_resource_like" : null,
  "n_scope_type_eq" : null,
  "n_source_id_eq" : null,
  "n_source_name_eq" : null,
  "n_source_name_like" : null,
}
```


##### 响应示例： {docsify-ignore}
```json
[
  {
    "id" : null,
    "name" : null,
    "create_man" : null,
    "create_time" : null,
    "update_man" : null,
    "update_time" : null,
    "visibility" : null,
    "is_archived" : null,
    "is_deleted" : null,
    "meta_data" : null,
    "status" : null,
    "is_favorite" : null,
    "tag_sets" : null,
    "scope_type" : null,
    "guidance_prompt" : null,
    "scope_id" : null,
    "chat_model" : null,
    "rerank_model" : null,
    "description_vector" : null,
    "guidance_prompt_vector" : null,
    "similarity_threshold" : null,
    "vector_similarity_weight" : null,
    "resource" : null,
    "resource_code" : null,
    "top_k" : null,
    "rerank" : null,
    "key" : null,
    "use_kg" : null,
    "pageindex" : null,
    "page_index_info" : null,
    "source_type" : null,
    "summary" : null,
    "matched_documents" : null,
    "parsed_cnt" : null,
    "document_cnt" : null,
    "category_id" : null,
    "category_name" : null,
    "chat_model_id" : null,
    "chunk_method" : null,
    "code_name" : null,
    "description" : null,
    "embedding_model" : null,
    "embedding_model_id" : null,
    "parser_config" : null,
    "record_id" : null,
    "record_title" : null,
    "rerank_model_id" : null,
    "resource_id" : null,
    "source_id" : null,
    "source_name" : null,
  }
]
```

## DEFAULT

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/fetch_default" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_category_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录标识|
|<el-row justify="space-between"><el-col :span="20">n_category_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">n_category_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">n_chat_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">n_embedding_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">n_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_id_noteq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库名称|
|<el-row justify="space-between"><el-col :span="20">n_record_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据记录标识|
|<el-row justify="space-between"><el-col :span="20">n_record_title_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">n_record_title_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">n_rerank_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">n_resource_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">n_resource_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源标识|
|<el-row justify="space-between"><el-col :span="20">n_resource_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">n_scope_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属|
|<el-row justify="space-between"><el-col :span="20">n_source_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">n_source_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|
|<el-row justify="space-between"><el-col :span="20">n_source_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|



##### 请求示例： {docsify-ignore}
```json
{
  "page" : 0,
  "size" : 20,
  "sort" : null,
  "n_category_id_eq" : null,
  "n_category_name_eq" : null,
  "n_category_name_like" : null,
  "n_chat_model_id_eq" : null,
  "n_embedding_model_id_eq" : null,
  "n_id_eq" : null,
  "n_id_noteq" : null,
  "n_name_like" : null,
  "n_record_id_eq" : null,
  "n_record_title_eq" : null,
  "n_record_title_like" : null,
  "n_rerank_model_id_eq" : null,
  "n_resource_eq" : null,
  "n_resource_id_eq" : null,
  "n_resource_like" : null,
  "n_scope_type_eq" : null,
  "n_source_id_eq" : null,
  "n_source_name_eq" : null,
  "n_source_name_like" : null,
}
```


##### 响应示例： {docsify-ignore}
```json
[
  {
    "id" : null,
    "name" : null,
    "create_man" : null,
    "create_time" : null,
    "update_man" : null,
    "update_time" : null,
    "visibility" : null,
    "is_archived" : null,
    "is_deleted" : null,
    "meta_data" : null,
    "status" : null,
    "is_favorite" : null,
    "tag_sets" : null,
    "scope_type" : null,
    "guidance_prompt" : null,
    "scope_id" : null,
    "chat_model" : null,
    "rerank_model" : null,
    "description_vector" : null,
    "guidance_prompt_vector" : null,
    "similarity_threshold" : null,
    "vector_similarity_weight" : null,
    "resource" : null,
    "resource_code" : null,
    "top_k" : null,
    "rerank" : null,
    "key" : null,
    "use_kg" : null,
    "pageindex" : null,
    "page_index_info" : null,
    "source_type" : null,
    "summary" : null,
    "matched_documents" : null,
    "parsed_cnt" : null,
    "document_cnt" : null,
    "category_id" : null,
    "category_name" : null,
    "chat_model_id" : null,
    "chunk_method" : null,
    "code_name" : null,
    "description" : null,
    "embedding_model" : null,
    "embedding_model_id" : null,
    "parser_config" : null,
    "record_id" : null,
    "record_title" : null,
    "rerank_model_id" : null,
    "resource_id" : null,
    "source_id" : null,
    "source_name" : null,
  }
]
```

## 已删除

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/fetch_deleted" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_category_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录标识|
|<el-row justify="space-between"><el-col :span="20">n_category_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">n_category_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">n_chat_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">n_embedding_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">n_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_id_noteq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库名称|
|<el-row justify="space-between"><el-col :span="20">n_record_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据记录标识|
|<el-row justify="space-between"><el-col :span="20">n_record_title_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">n_record_title_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">n_rerank_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">n_resource_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">n_resource_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源标识|
|<el-row justify="space-between"><el-col :span="20">n_resource_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">n_scope_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属|
|<el-row justify="space-between"><el-col :span="20">n_source_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">n_source_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|
|<el-row justify="space-between"><el-col :span="20">n_source_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|



##### 请求示例： {docsify-ignore}
```json
{
  "page" : 0,
  "size" : 20,
  "sort" : null,
  "n_category_id_eq" : null,
  "n_category_name_eq" : null,
  "n_category_name_like" : null,
  "n_chat_model_id_eq" : null,
  "n_embedding_model_id_eq" : null,
  "n_id_eq" : null,
  "n_id_noteq" : null,
  "n_name_like" : null,
  "n_record_id_eq" : null,
  "n_record_title_eq" : null,
  "n_record_title_like" : null,
  "n_rerank_model_id_eq" : null,
  "n_resource_eq" : null,
  "n_resource_id_eq" : null,
  "n_resource_like" : null,
  "n_scope_type_eq" : null,
  "n_source_id_eq" : null,
  "n_source_name_eq" : null,
  "n_source_name_like" : null,
}
```


##### 响应示例： {docsify-ignore}
```json
[
  {
    "id" : null,
    "name" : null,
    "create_man" : null,
    "create_time" : null,
    "update_man" : null,
    "update_time" : null,
    "visibility" : null,
    "is_archived" : null,
    "is_deleted" : null,
    "meta_data" : null,
    "status" : null,
    "is_favorite" : null,
    "tag_sets" : null,
    "scope_type" : null,
    "guidance_prompt" : null,
    "scope_id" : null,
    "chat_model" : null,
    "rerank_model" : null,
    "description_vector" : null,
    "guidance_prompt_vector" : null,
    "similarity_threshold" : null,
    "vector_similarity_weight" : null,
    "resource" : null,
    "resource_code" : null,
    "top_k" : null,
    "rerank" : null,
    "key" : null,
    "use_kg" : null,
    "pageindex" : null,
    "page_index_info" : null,
    "source_type" : null,
    "summary" : null,
    "matched_documents" : null,
    "parsed_cnt" : null,
    "document_cnt" : null,
    "category_id" : null,
    "category_name" : null,
    "chat_model_id" : null,
    "chunk_method" : null,
    "code_name" : null,
    "description" : null,
    "embedding_model" : null,
    "embedding_model_id" : null,
    "parser_config" : null,
    "record_id" : null,
    "record_title" : null,
    "rerank_model_id" : null,
    "resource_id" : null,
    "source_id" : null,
    "source_name" : null,
  }
]
```

## 查询星标

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/fetch_favorite" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_category_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录标识|
|<el-row justify="space-between"><el-col :span="20">n_category_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">n_category_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">n_chat_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">n_embedding_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">n_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_id_noteq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库名称|
|<el-row justify="space-between"><el-col :span="20">n_record_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据记录标识|
|<el-row justify="space-between"><el-col :span="20">n_record_title_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">n_record_title_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">n_rerank_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">n_resource_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">n_resource_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源标识|
|<el-row justify="space-between"><el-col :span="20">n_resource_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">n_scope_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属|
|<el-row justify="space-between"><el-col :span="20">n_source_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">n_source_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|
|<el-row justify="space-between"><el-col :span="20">n_source_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|



##### 请求示例： {docsify-ignore}
```json
{
  "page" : 0,
  "size" : 20,
  "sort" : null,
  "n_category_id_eq" : null,
  "n_category_name_eq" : null,
  "n_category_name_like" : null,
  "n_chat_model_id_eq" : null,
  "n_embedding_model_id_eq" : null,
  "n_id_eq" : null,
  "n_id_noteq" : null,
  "n_name_like" : null,
  "n_record_id_eq" : null,
  "n_record_title_eq" : null,
  "n_record_title_like" : null,
  "n_rerank_model_id_eq" : null,
  "n_resource_eq" : null,
  "n_resource_id_eq" : null,
  "n_resource_like" : null,
  "n_scope_type_eq" : null,
  "n_source_id_eq" : null,
  "n_source_name_eq" : null,
  "n_source_name_like" : null,
}
```


##### 响应示例： {docsify-ignore}
```json
[
  {
    "id" : null,
    "name" : null,
    "create_man" : null,
    "create_time" : null,
    "update_man" : null,
    "update_time" : null,
    "visibility" : null,
    "is_archived" : null,
    "is_deleted" : null,
    "meta_data" : null,
    "status" : null,
    "is_favorite" : null,
    "tag_sets" : null,
    "scope_type" : null,
    "guidance_prompt" : null,
    "scope_id" : null,
    "chat_model" : null,
    "rerank_model" : null,
    "description_vector" : null,
    "guidance_prompt_vector" : null,
    "similarity_threshold" : null,
    "vector_similarity_weight" : null,
    "resource" : null,
    "resource_code" : null,
    "top_k" : null,
    "rerank" : null,
    "key" : null,
    "use_kg" : null,
    "pageindex" : null,
    "page_index_info" : null,
    "source_type" : null,
    "summary" : null,
    "matched_documents" : null,
    "parsed_cnt" : null,
    "document_cnt" : null,
    "category_id" : null,
    "category_name" : null,
    "chat_model_id" : null,
    "chunk_method" : null,
    "code_name" : null,
    "description" : null,
    "embedding_model" : null,
    "embedding_model_id" : null,
    "parser_config" : null,
    "record_id" : null,
    "record_title" : null,
    "rerank_model_id" : null,
    "resource_id" : null,
    "source_id" : null,
    "source_name" : null,
  }
]
```

## 全文检索

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/fetch_full_text" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`
根据keyword参数搜索，keyword可以是一组词以空格分割，命中多着靠前



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_category_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录标识|
|<el-row justify="space-between"><el-col :span="20">n_category_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">n_category_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">n_chat_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">n_embedding_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">n_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_id_noteq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库名称|
|<el-row justify="space-between"><el-col :span="20">n_record_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据记录标识|
|<el-row justify="space-between"><el-col :span="20">n_record_title_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">n_record_title_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">n_rerank_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">n_resource_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">n_resource_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源标识|
|<el-row justify="space-between"><el-col :span="20">n_resource_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">n_scope_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属|
|<el-row justify="space-between"><el-col :span="20">n_source_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">n_source_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|
|<el-row justify="space-between"><el-col :span="20">n_source_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|



##### 请求示例： {docsify-ignore}
```json
{
  "page" : 0,
  "size" : 20,
  "sort" : null,
  "n_category_id_eq" : null,
  "n_category_name_eq" : null,
  "n_category_name_like" : null,
  "n_chat_model_id_eq" : null,
  "n_embedding_model_id_eq" : null,
  "n_id_eq" : null,
  "n_id_noteq" : null,
  "n_name_like" : null,
  "n_record_id_eq" : null,
  "n_record_title_eq" : null,
  "n_record_title_like" : null,
  "n_rerank_model_id_eq" : null,
  "n_resource_eq" : null,
  "n_resource_id_eq" : null,
  "n_resource_like" : null,
  "n_scope_type_eq" : null,
  "n_source_id_eq" : null,
  "n_source_name_eq" : null,
  "n_source_name_like" : null,
}
```


##### 响应示例： {docsify-ignore}
```json
[
  {
    "id" : null,
    "name" : null,
    "update_time" : null,
    "guidance_prompt" : null,
    "resource" : null,
    "matched_documents" : null,
    "category_name" : null,
    "description" : null,
    "source_name" : null,
  }
]
```

## 主表格查询

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/fetch_main" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_category_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录标识|
|<el-row justify="space-between"><el-col :span="20">n_category_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">n_category_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">n_chat_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">n_embedding_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">n_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_id_noteq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库名称|
|<el-row justify="space-between"><el-col :span="20">n_record_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据记录标识|
|<el-row justify="space-between"><el-col :span="20">n_record_title_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">n_record_title_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">n_rerank_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">n_resource_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">n_resource_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源标识|
|<el-row justify="space-between"><el-col :span="20">n_resource_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">n_scope_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属|
|<el-row justify="space-between"><el-col :span="20">n_source_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">n_source_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|
|<el-row justify="space-between"><el-col :span="20">n_source_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|



##### 请求示例： {docsify-ignore}
```json
{
  "page" : 0,
  "size" : 20,
  "sort" : null,
  "n_category_id_eq" : null,
  "n_category_name_eq" : null,
  "n_category_name_like" : null,
  "n_chat_model_id_eq" : null,
  "n_embedding_model_id_eq" : null,
  "n_id_eq" : null,
  "n_id_noteq" : null,
  "n_name_like" : null,
  "n_record_id_eq" : null,
  "n_record_title_eq" : null,
  "n_record_title_like" : null,
  "n_rerank_model_id_eq" : null,
  "n_resource_eq" : null,
  "n_resource_id_eq" : null,
  "n_resource_like" : null,
  "n_scope_type_eq" : null,
  "n_source_id_eq" : null,
  "n_source_name_eq" : null,
  "n_source_name_like" : null,
}
```


##### 响应示例： {docsify-ignore}
```json
[
  {
    "id" : null,
    "name" : null,
    "create_man" : null,
    "create_time" : null,
    "update_man" : null,
    "update_time" : null,
    "visibility" : null,
    "is_archived" : null,
    "is_deleted" : null,
    "meta_data" : null,
    "status" : null,
    "is_favorite" : null,
    "tag_sets" : null,
    "scope_type" : null,
    "guidance_prompt" : null,
    "scope_id" : null,
    "chat_model" : null,
    "rerank_model" : null,
    "description_vector" : null,
    "guidance_prompt_vector" : null,
    "similarity_threshold" : null,
    "vector_similarity_weight" : null,
    "resource" : null,
    "resource_code" : null,
    "top_k" : null,
    "rerank" : null,
    "key" : null,
    "use_kg" : null,
    "pageindex" : null,
    "page_index_info" : null,
    "source_type" : null,
    "summary" : null,
    "matched_documents" : null,
    "parsed_cnt" : null,
    "document_cnt" : null,
    "category_id" : null,
    "category_name" : null,
    "chat_model_id" : null,
    "chunk_method" : null,
    "code_name" : null,
    "description" : null,
    "embedding_model" : null,
    "embedding_model_id" : null,
    "parser_config" : null,
    "record_id" : null,
    "record_title" : null,
    "rerank_model_id" : null,
    "resource_id" : null,
    "source_id" : null,
    "source_name" : null,
  }
]
```

## 只读用户

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/fetch_reader" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_category_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录标识|
|<el-row justify="space-between"><el-col :span="20">n_category_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">n_category_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">n_chat_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">n_embedding_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">n_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_id_noteq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库名称|
|<el-row justify="space-between"><el-col :span="20">n_record_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据记录标识|
|<el-row justify="space-between"><el-col :span="20">n_record_title_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">n_record_title_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">n_rerank_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">n_resource_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">n_resource_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源标识|
|<el-row justify="space-between"><el-col :span="20">n_resource_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">n_scope_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属|
|<el-row justify="space-between"><el-col :span="20">n_source_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">n_source_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|
|<el-row justify="space-between"><el-col :span="20">n_source_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|



##### 请求示例： {docsify-ignore}
```json
{
  "page" : 0,
  "size" : 20,
  "sort" : null,
  "n_category_id_eq" : null,
  "n_category_name_eq" : null,
  "n_category_name_like" : null,
  "n_chat_model_id_eq" : null,
  "n_embedding_model_id_eq" : null,
  "n_id_eq" : null,
  "n_id_noteq" : null,
  "n_name_like" : null,
  "n_record_id_eq" : null,
  "n_record_title_eq" : null,
  "n_record_title_like" : null,
  "n_rerank_model_id_eq" : null,
  "n_resource_eq" : null,
  "n_resource_id_eq" : null,
  "n_resource_like" : null,
  "n_scope_type_eq" : null,
  "n_source_id_eq" : null,
  "n_source_name_eq" : null,
  "n_source_name_like" : null,
}
```


##### 响应示例： {docsify-ignore}
```json
[
  {
    "id" : null,
    "name" : null,
    "create_man" : null,
    "create_time" : null,
    "update_man" : null,
    "update_time" : null,
    "visibility" : null,
    "is_archived" : null,
    "is_deleted" : null,
    "meta_data" : null,
    "status" : null,
    "is_favorite" : null,
    "tag_sets" : null,
    "scope_type" : null,
    "guidance_prompt" : null,
    "scope_id" : null,
    "chat_model" : null,
    "rerank_model" : null,
    "description_vector" : null,
    "guidance_prompt_vector" : null,
    "similarity_threshold" : null,
    "vector_similarity_weight" : null,
    "resource" : null,
    "resource_code" : null,
    "top_k" : null,
    "rerank" : null,
    "key" : null,
    "use_kg" : null,
    "pageindex" : null,
    "page_index_info" : null,
    "source_type" : null,
    "summary" : null,
    "matched_documents" : null,
    "parsed_cnt" : null,
    "document_cnt" : null,
    "category_id" : null,
    "category_name" : null,
    "chat_model_id" : null,
    "chunk_method" : null,
    "code_name" : null,
    "description" : null,
    "embedding_model" : null,
    "embedding_model_id" : null,
    "parser_config" : null,
    "record_id" : null,
    "record_title" : null,
    "rerank_model_id" : null,
    "resource_id" : null,
    "source_id" : null,
    "source_name" : null,
  }
]
```

## 数据集

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/fetch_switch" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_category_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录标识|
|<el-row justify="space-between"><el-col :span="20">n_category_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">n_category_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">n_chat_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">n_embedding_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">n_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_id_noteq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库名称|
|<el-row justify="space-between"><el-col :span="20">n_record_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据记录标识|
|<el-row justify="space-between"><el-col :span="20">n_record_title_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">n_record_title_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">n_rerank_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">n_resource_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">n_resource_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源标识|
|<el-row justify="space-between"><el-col :span="20">n_resource_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">n_scope_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属|
|<el-row justify="space-between"><el-col :span="20">n_source_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">n_source_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|
|<el-row justify="space-between"><el-col :span="20">n_source_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|



##### 请求示例： {docsify-ignore}
```json
{
  "page" : 0,
  "size" : 20,
  "sort" : null,
  "n_category_id_eq" : null,
  "n_category_name_eq" : null,
  "n_category_name_like" : null,
  "n_chat_model_id_eq" : null,
  "n_embedding_model_id_eq" : null,
  "n_id_eq" : null,
  "n_id_noteq" : null,
  "n_name_like" : null,
  "n_record_id_eq" : null,
  "n_record_title_eq" : null,
  "n_record_title_like" : null,
  "n_rerank_model_id_eq" : null,
  "n_resource_eq" : null,
  "n_resource_id_eq" : null,
  "n_resource_like" : null,
  "n_scope_type_eq" : null,
  "n_source_id_eq" : null,
  "n_source_name_eq" : null,
  "n_source_name_like" : null,
}
```


##### 响应示例： {docsify-ignore}
```json
[
  {
    "id" : null,
    "name" : null,
    "create_man" : null,
    "create_time" : null,
    "update_man" : null,
    "update_time" : null,
    "visibility" : null,
    "is_archived" : null,
    "is_deleted" : null,
    "meta_data" : null,
    "status" : null,
    "is_favorite" : null,
    "tag_sets" : null,
    "scope_type" : null,
    "guidance_prompt" : null,
    "scope_id" : null,
    "chat_model" : null,
    "rerank_model" : null,
    "description_vector" : null,
    "guidance_prompt_vector" : null,
    "similarity_threshold" : null,
    "vector_similarity_weight" : null,
    "resource" : null,
    "resource_code" : null,
    "top_k" : null,
    "rerank" : null,
    "key" : null,
    "use_kg" : null,
    "pageindex" : null,
    "page_index_info" : null,
    "source_type" : null,
    "summary" : null,
    "matched_documents" : null,
    "parsed_cnt" : null,
    "document_cnt" : null,
    "category_id" : null,
    "category_name" : null,
    "chat_model_id" : null,
    "chunk_method" : null,
    "code_name" : null,
    "description" : null,
    "embedding_model" : null,
    "embedding_model_id" : null,
    "parser_config" : null,
    "record_id" : null,
    "record_title" : null,
    "rerank_model_id" : null,
    "resource_id" : null,
    "source_id" : null,
    "source_name" : null,
  }
]
```

## 操作用户

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/fetch_user" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_category_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录标识|
|<el-row justify="space-between"><el-col :span="20">n_category_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">n_category_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">n_chat_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">n_embedding_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">n_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_id_noteq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库名称|
|<el-row justify="space-between"><el-col :span="20">n_record_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据记录标识|
|<el-row justify="space-between"><el-col :span="20">n_record_title_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">n_record_title_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">n_rerank_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">n_resource_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">n_resource_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源标识|
|<el-row justify="space-between"><el-col :span="20">n_resource_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">n_scope_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属|
|<el-row justify="space-between"><el-col :span="20">n_source_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">n_source_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|
|<el-row justify="space-between"><el-col :span="20">n_source_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|



##### 请求示例： {docsify-ignore}
```json
{
  "page" : 0,
  "size" : 20,
  "sort" : null,
  "n_category_id_eq" : null,
  "n_category_name_eq" : null,
  "n_category_name_like" : null,
  "n_chat_model_id_eq" : null,
  "n_embedding_model_id_eq" : null,
  "n_id_eq" : null,
  "n_id_noteq" : null,
  "n_name_like" : null,
  "n_record_id_eq" : null,
  "n_record_title_eq" : null,
  "n_record_title_like" : null,
  "n_rerank_model_id_eq" : null,
  "n_resource_eq" : null,
  "n_resource_id_eq" : null,
  "n_resource_like" : null,
  "n_scope_type_eq" : null,
  "n_source_id_eq" : null,
  "n_source_name_eq" : null,
  "n_source_name_like" : null,
}
```


##### 响应示例： {docsify-ignore}
```json
[
  {
    "id" : null,
    "name" : null,
    "create_man" : null,
    "create_time" : null,
    "update_man" : null,
    "update_time" : null,
    "visibility" : null,
    "is_archived" : null,
    "is_deleted" : null,
    "meta_data" : null,
    "status" : null,
    "is_favorite" : null,
    "tag_sets" : null,
    "scope_type" : null,
    "guidance_prompt" : null,
    "scope_id" : null,
    "chat_model" : null,
    "rerank_model" : null,
    "description_vector" : null,
    "guidance_prompt_vector" : null,
    "similarity_threshold" : null,
    "vector_similarity_weight" : null,
    "resource" : null,
    "resource_code" : null,
    "top_k" : null,
    "rerank" : null,
    "key" : null,
    "use_kg" : null,
    "pageindex" : null,
    "page_index_info" : null,
    "source_type" : null,
    "summary" : null,
    "matched_documents" : null,
    "parsed_cnt" : null,
    "document_cnt" : null,
    "category_id" : null,
    "category_name" : null,
    "chat_model_id" : null,
    "chunk_method" : null,
    "code_name" : null,
    "description" : null,
    "embedding_model" : null,
    "embedding_model_id" : null,
    "parser_config" : null,
    "record_id" : null,
    "record_title" : null,
    "rerank_model_id" : null,
    "resource_id" : null,
    "source_id" : null,
    "source_name" : null,
  }
]
```

## 启用数据集

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/fetch_valid" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_category_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录标识|
|<el-row justify="space-between"><el-col :span="20">n_category_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">n_category_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">n_chat_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">n_embedding_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">n_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_id_noteq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库名称|
|<el-row justify="space-between"><el-col :span="20">n_record_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据记录标识|
|<el-row justify="space-between"><el-col :span="20">n_record_title_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">n_record_title_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">n_rerank_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">n_resource_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">n_resource_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源标识|
|<el-row justify="space-between"><el-col :span="20">n_resource_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">n_scope_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属|
|<el-row justify="space-between"><el-col :span="20">n_source_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">n_source_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|
|<el-row justify="space-between"><el-col :span="20">n_source_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|



##### 请求示例： {docsify-ignore}
```json
{
  "page" : 0,
  "size" : 20,
  "sort" : null,
  "n_category_id_eq" : null,
  "n_category_name_eq" : null,
  "n_category_name_like" : null,
  "n_chat_model_id_eq" : null,
  "n_embedding_model_id_eq" : null,
  "n_id_eq" : null,
  "n_id_noteq" : null,
  "n_name_like" : null,
  "n_record_id_eq" : null,
  "n_record_title_eq" : null,
  "n_record_title_like" : null,
  "n_rerank_model_id_eq" : null,
  "n_resource_eq" : null,
  "n_resource_id_eq" : null,
  "n_resource_like" : null,
  "n_scope_type_eq" : null,
  "n_source_id_eq" : null,
  "n_source_name_eq" : null,
  "n_source_name_like" : null,
}
```


##### 响应示例： {docsify-ignore}
```json
[
  {
    "id" : null,
    "name" : null,
    "create_man" : null,
    "create_time" : null,
    "update_man" : null,
    "update_time" : null,
    "visibility" : null,
    "is_archived" : null,
    "is_deleted" : null,
    "meta_data" : null,
    "status" : null,
    "is_favorite" : null,
    "tag_sets" : null,
    "scope_type" : null,
    "guidance_prompt" : null,
    "scope_id" : null,
    "chat_model" : null,
    "rerank_model" : null,
    "description_vector" : null,
    "guidance_prompt_vector" : null,
    "similarity_threshold" : null,
    "vector_similarity_weight" : null,
    "resource" : null,
    "resource_code" : null,
    "top_k" : null,
    "rerank" : null,
    "key" : null,
    "use_kg" : null,
    "pageindex" : null,
    "page_index_info" : null,
    "source_type" : null,
    "summary" : null,
    "matched_documents" : null,
    "parsed_cnt" : null,
    "document_cnt" : null,
    "category_id" : null,
    "category_name" : null,
    "chat_model_id" : null,
    "chunk_method" : null,
    "code_name" : null,
    "description" : null,
    "embedding_model" : null,
    "embedding_model_id" : null,
    "parser_config" : null,
    "record_id" : null,
    "record_title" : null,
    "rerank_model_id" : null,
    "resource_id" : null,
    "source_id" : null,
    "source_name" : null,
  }
]
```

## with_record

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/fetch_with_record" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_category_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录标识|
|<el-row justify="space-between"><el-col :span="20">n_category_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">n_category_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">n_chat_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">n_embedding_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">n_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_id_noteq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库名称|
|<el-row justify="space-between"><el-col :span="20">n_record_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据记录标识|
|<el-row justify="space-between"><el-col :span="20">n_record_title_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">n_record_title_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标题|
|<el-row justify="space-between"><el-col :span="20">n_rerank_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">n_resource_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">n_resource_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源标识|
|<el-row justify="space-between"><el-col :span="20">n_resource_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">n_scope_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|所属|
|<el-row justify="space-between"><el-col :span="20">n_source_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">n_source_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|
|<el-row justify="space-between"><el-col :span="20">n_source_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|



##### 请求示例： {docsify-ignore}
```json
{
  "page" : 0,
  "size" : 20,
  "sort" : null,
  "n_category_id_eq" : null,
  "n_category_name_eq" : null,
  "n_category_name_like" : null,
  "n_chat_model_id_eq" : null,
  "n_embedding_model_id_eq" : null,
  "n_id_eq" : null,
  "n_id_noteq" : null,
  "n_name_like" : null,
  "n_record_id_eq" : null,
  "n_record_title_eq" : null,
  "n_record_title_like" : null,
  "n_rerank_model_id_eq" : null,
  "n_resource_eq" : null,
  "n_resource_id_eq" : null,
  "n_resource_like" : null,
  "n_scope_type_eq" : null,
  "n_source_id_eq" : null,
  "n_source_name_eq" : null,
  "n_source_name_like" : null,
}
```


##### 响应示例： {docsify-ignore}
```json
[
  {
    "id" : null,
    "name" : null,
    "create_man" : null,
    "create_time" : null,
    "update_man" : null,
    "update_time" : null,
    "visibility" : null,
    "is_archived" : null,
    "is_deleted" : null,
    "meta_data" : null,
    "status" : null,
    "is_favorite" : null,
    "tag_sets" : null,
    "scope_type" : null,
    "guidance_prompt" : null,
    "scope_id" : null,
    "chat_model" : null,
    "rerank_model" : null,
    "description_vector" : null,
    "guidance_prompt_vector" : null,
    "similarity_threshold" : null,
    "vector_similarity_weight" : null,
    "resource" : null,
    "resource_code" : null,
    "top_k" : null,
    "rerank" : null,
    "key" : null,
    "use_kg" : null,
    "pageindex" : null,
    "page_index_info" : null,
    "source_type" : null,
    "summary" : null,
    "matched_documents" : null,
    "parsed_cnt" : null,
    "document_cnt" : null,
    "category_id" : null,
    "category_name" : null,
    "chat_model_id" : null,
    "chunk_method" : null,
    "code_name" : null,
    "description" : null,
    "embedding_model" : null,
    "embedding_model_id" : null,
    "parser_config" : null,
    "record_id" : null,
    "record_title" : null,
    "rerank_model_id" : null,
    "resource_id" : null,
    "source_id" : null,
    "source_name" : null,
  }
]
```



## 下载导入模板
<el-row>
<div style="width: 80px">
<el-alert center title="GET" type="success" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/importtemplate" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 查询参数 {docsify-ignore}

|字段col300|类型col150|备注col400|
|---|---|----|
| srfimporttag | String | 导入标识 |



## 数据导出

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/exportdata/{param},/ai_knowledge_bases/exportdata/{param}/{key}" type="info" :closable="false" ></el-alert>
</div>
</el-row>

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|param|String|导出集合方法名称|
|key|String|数据主键|

##### 查询参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|srfexporttag|String|导出模板标识|

##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|page|Integer|page|
|size|Integer|分页大小|
|n_xxx_eq|String|过滤参数|


## 数据导入

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/importdata" type="info" :closable="false" ></el-alert>
</div>
</el-row>

##### 查询参数 {docsify-ignore}

|字段col300|类型col150|备注col400|
|---|---|----|
| srfimporttag | String | 导入标识 |

##### 请求参数 {docsify-ignore}

|字段col300|类型col150|备注col400|
|---|---|----|
| file | file | 导入数据文具 |

## 数据导入（返回错误excel）

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/importdata2" type="info" :closable="false" ></el-alert>
</div>
</el-row>

##### 查询参数 {docsify-ignore}

|字段col300|类型col150|备注col400|
|---|---|----|
| srfimporttag | String | 导入标识 |

##### 请求参数 {docsify-ignore}

|字段col300|类型col150|备注col400|
|---|---|----|
| file | file | 导入数据文具 |

## 自定义表头导入（异步）
<el-row>
<div style="width: 80px">
<el-alert center title="GET" type="success" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/asyncimportdata2" type="info" :closable="false" ></el-alert>
</div>
</el-row>

##### 查询参数 {docsify-ignore}

|字段col300|类型col150|备注col400|
|---|---|----|
| srfimporttag | String | 导入标识 |
| srfossfileid | String | 导入文件 |
| srfimportschemaid | String | 表头定义 |


## 数据打印
<el-row>
<div style="width: 80px">
<el-alert center title="GET" type="success" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/printdata/{key}" type="info" :closable="false" ></el-alert>
</div>
</el-row>

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|数据主键|

##### 查询参数 {docsify-ignore}

|字段col300|类型col150|备注col400|
|---|---|----|
| srfprinttag | String | 打印标识 |
| srfcontenttype | String | 打印类型 |



## 报表打印

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/report" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 查询参数 {docsify-ignore}

|字段col300|类型col150|备注col400|
|---|---|----|
| srfreporttag | String | 报表标识 |
| srfcontenttype | String | 报表类型 |




<script>
 const { createApp } = Vue
  createApp({
    data() {
      return {

      }
    },
    methods: {

    }
  }).use(ElementPlus).mount('#app')
</script>