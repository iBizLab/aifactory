# 类别设置(category_settings) :id=category_settings
## 创建类别设置

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/category_settings" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`CREATE`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">category_id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|标识|
|<el-row justify="space-between"><el-col :span="20">category_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|名称|
|<el-row justify="space-between"><el-col :span="20">enable</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|逻辑有效标识|
|<el-row justify="space-between"><el-col :span="20">visibility</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|可见范围|
|<el-row justify="space-between"><el-col :span="20">guided_prompt_agent_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|引导提示词智能体标识|
|<el-row justify="space-between"><el-col :span="20">chat_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型|
|<el-row justify="space-between"><el-col :span="20">flash_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|快速交谈模型|
|<el-row justify="space-between"><el-col :span="20">intent_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|快速交谈模型|
|<el-row justify="space-between"><el-col :span="20">rerank_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型|
|<el-row justify="space-between"><el-col :span="20">vl_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|多模态模型|
|<el-row justify="space-between"><el-col :span="20">auto_gen_kb</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|自动创建资源知识库|
|<el-row justify="space-between"><el-col :span="20">configs</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|configs|
|<el-row justify="space-between"><el-col :span="20">similarity_threshold</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|召回相似度阈值|
|<el-row justify="space-between"><el-col :span="20">vector_similarity_weight</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|向量相似度权重|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">resource_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">top_k</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最大召回数量|
|<el-row justify="space-between"><el-col :span="20">rerank</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|召回重排|
|<el-row justify="space-between"><el-col :span="20">use_kg</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|使用知识图谱|
|<el-row justify="space-between"><el-col :span="20">chat_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">embedding_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|embedding模型|
|<el-row justify="space-between"><el-col :span="20">embedding_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">flash_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|快速交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">intent_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|模型标识|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">rerank_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标识|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">source_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|
|<el-row justify="space-between"><el-col :span="20">vl_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|多模态模型标识|



##### 请求示例： {docsify-ignore}
```json
{
  "category_id" : null,
  "category_name" : null,
  "enable" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "guided_prompt_agent_id" : null,
  "chat_model" : null,
  "flash_model" : null,
  "intent_model" : null,
  "rerank_model" : null,
  "vl_model" : null,
  "auto_gen_kb" : null,
  "configs" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "use_kg" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "flash_model_id" : null,
  "intent_model_id" : null,
  "parser_config" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
  "vl_model_id" : null,
}
```


##### 响应示例： {docsify-ignore}
```json

{
  "category_id" : null,
  "category_name" : null,
  "enable" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "guided_prompt_agent_id" : null,
  "chat_model" : null,
  "flash_model" : null,
  "intent_model" : null,
  "rerank_model" : null,
  "vl_model" : null,
  "auto_gen_kb" : null,
  "configs" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "use_kg" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "flash_model_id" : null,
  "intent_model_id" : null,
  "parser_config" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
  "vl_model_id" : null,
}

```

## 获取类别设置

<el-row>
<div style="width: 80px">
<el-alert center title="GET" type="success" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/category_settings/{key}" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|标识|




##### 响应示例： {docsify-ignore}
```json

{
  "category_id" : null,
  "category_name" : null,
  "enable" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "guided_prompt_agent_id" : null,
  "chat_model" : null,
  "flash_model" : null,
  "intent_model" : null,
  "rerank_model" : null,
  "vl_model" : null,
  "auto_gen_kb" : null,
  "configs" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "use_kg" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "flash_model_id" : null,
  "intent_model_id" : null,
  "parser_config" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
  "vl_model_id" : null,
}

```

## 删除类别设置

<el-row>
<div style="width: 80px">
<el-alert center title="DELETE" type="error" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/category_settings/{key}" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`DELETE`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|标识|





## 更新类别设置

<el-row>
<div style="width: 80px">
<el-alert center title="PUT" type="warning" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/category_settings/{key}" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`UPDATE`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|标识|



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">category_id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|标识|
|<el-row justify="space-between"><el-col :span="20">category_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|名称|
|<el-row justify="space-between"><el-col :span="20">enable</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|逻辑有效标识|
|<el-row justify="space-between"><el-col :span="20">visibility</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|可见范围|
|<el-row justify="space-between"><el-col :span="20">guided_prompt_agent_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|引导提示词智能体标识|
|<el-row justify="space-between"><el-col :span="20">chat_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型|
|<el-row justify="space-between"><el-col :span="20">flash_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|快速交谈模型|
|<el-row justify="space-between"><el-col :span="20">intent_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|快速交谈模型|
|<el-row justify="space-between"><el-col :span="20">rerank_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型|
|<el-row justify="space-between"><el-col :span="20">vl_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|多模态模型|
|<el-row justify="space-between"><el-col :span="20">auto_gen_kb</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|自动创建资源知识库|
|<el-row justify="space-between"><el-col :span="20">configs</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|configs|
|<el-row justify="space-between"><el-col :span="20">similarity_threshold</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|召回相似度阈值|
|<el-row justify="space-between"><el-col :span="20">vector_similarity_weight</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|向量相似度权重|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">resource_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">top_k</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最大召回数量|
|<el-row justify="space-between"><el-col :span="20">rerank</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|召回重排|
|<el-row justify="space-between"><el-col :span="20">use_kg</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|使用知识图谱|
|<el-row justify="space-between"><el-col :span="20">chat_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">embedding_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|embedding模型|
|<el-row justify="space-between"><el-col :span="20">embedding_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">flash_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|快速交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">intent_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|模型标识|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">rerank_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标识|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">source_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|
|<el-row justify="space-between"><el-col :span="20">vl_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|多模态模型标识|



##### 请求示例： {docsify-ignore}
```json
{
  "category_id" : null,
  "category_name" : null,
  "enable" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "guided_prompt_agent_id" : null,
  "chat_model" : null,
  "flash_model" : null,
  "intent_model" : null,
  "rerank_model" : null,
  "vl_model" : null,
  "auto_gen_kb" : null,
  "configs" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "use_kg" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "flash_model_id" : null,
  "intent_model_id" : null,
  "parser_config" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
  "vl_model_id" : null,
}
```


##### 响应示例： {docsify-ignore}
```json

{
  "category_id" : null,
  "category_name" : null,
  "enable" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "guided_prompt_agent_id" : null,
  "chat_model" : null,
  "flash_model" : null,
  "intent_model" : null,
  "rerank_model" : null,
  "vl_model" : null,
  "auto_gen_kb" : null,
  "configs" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "use_kg" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "flash_model_id" : null,
  "intent_model_id" : null,
  "parser_config" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
  "vl_model_id" : null,
}

```

## 检查类别设置主键

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/category_settings/check_key" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`CREATE`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">category_id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|标识|
|<el-row justify="space-between"><el-col :span="20">category_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|名称|
|<el-row justify="space-between"><el-col :span="20">enable</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|逻辑有效标识|
|<el-row justify="space-between"><el-col :span="20">visibility</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|可见范围|
|<el-row justify="space-between"><el-col :span="20">guided_prompt_agent_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|引导提示词智能体标识|
|<el-row justify="space-between"><el-col :span="20">chat_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型|
|<el-row justify="space-between"><el-col :span="20">flash_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|快速交谈模型|
|<el-row justify="space-between"><el-col :span="20">intent_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|快速交谈模型|
|<el-row justify="space-between"><el-col :span="20">rerank_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型|
|<el-row justify="space-between"><el-col :span="20">vl_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|多模态模型|
|<el-row justify="space-between"><el-col :span="20">auto_gen_kb</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|自动创建资源知识库|
|<el-row justify="space-between"><el-col :span="20">configs</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|configs|
|<el-row justify="space-between"><el-col :span="20">similarity_threshold</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|召回相似度阈值|
|<el-row justify="space-between"><el-col :span="20">vector_similarity_weight</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|向量相似度权重|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">resource_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">top_k</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最大召回数量|
|<el-row justify="space-between"><el-col :span="20">rerank</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|召回重排|
|<el-row justify="space-between"><el-col :span="20">use_kg</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|使用知识图谱|
|<el-row justify="space-between"><el-col :span="20">chat_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">embedding_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|embedding模型|
|<el-row justify="space-between"><el-col :span="20">embedding_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">flash_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|快速交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">intent_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|模型标识|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">rerank_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标识|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">source_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|
|<el-row justify="space-between"><el-col :span="20">vl_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|多模态模型标识|



##### 请求示例： {docsify-ignore}
```json
{
  "category_id" : null,
  "category_name" : null,
  "enable" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "guided_prompt_agent_id" : null,
  "chat_model" : null,
  "flash_model" : null,
  "intent_model" : null,
  "rerank_model" : null,
  "vl_model" : null,
  "auto_gen_kb" : null,
  "configs" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "use_kg" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "flash_model_id" : null,
  "intent_model_id" : null,
  "parser_config" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
  "vl_model_id" : null,
}
```


##### 响应示例： {docsify-ignore}
```json
Integer
```

## find_aifactory_sys_env

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/category_settings/{key}/find_aifactory_sys_env" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|标识|



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">category_id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|标识|
|<el-row justify="space-between"><el-col :span="20">category_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|名称|
|<el-row justify="space-between"><el-col :span="20">enable</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|逻辑有效标识|
|<el-row justify="space-between"><el-col :span="20">visibility</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|可见范围|
|<el-row justify="space-between"><el-col :span="20">guided_prompt_agent_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|引导提示词智能体标识|
|<el-row justify="space-between"><el-col :span="20">chat_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型|
|<el-row justify="space-between"><el-col :span="20">flash_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|快速交谈模型|
|<el-row justify="space-between"><el-col :span="20">intent_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|快速交谈模型|
|<el-row justify="space-between"><el-col :span="20">rerank_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型|
|<el-row justify="space-between"><el-col :span="20">vl_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|多模态模型|
|<el-row justify="space-between"><el-col :span="20">auto_gen_kb</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|自动创建资源知识库|
|<el-row justify="space-between"><el-col :span="20">configs</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|configs|
|<el-row justify="space-between"><el-col :span="20">similarity_threshold</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|召回相似度阈值|
|<el-row justify="space-between"><el-col :span="20">vector_similarity_weight</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|向量相似度权重|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">resource_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">top_k</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最大召回数量|
|<el-row justify="space-between"><el-col :span="20">rerank</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|召回重排|
|<el-row justify="space-between"><el-col :span="20">use_kg</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|使用知识图谱|
|<el-row justify="space-between"><el-col :span="20">chat_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">embedding_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|embedding模型|
|<el-row justify="space-between"><el-col :span="20">embedding_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">flash_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|快速交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">intent_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|模型标识|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">rerank_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标识|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">source_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|
|<el-row justify="space-between"><el-col :span="20">vl_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|多模态模型标识|



##### 请求示例： {docsify-ignore}
```json
{
  "category_id" : null,
  "category_name" : null,
  "enable" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "guided_prompt_agent_id" : null,
  "chat_model" : null,
  "flash_model" : null,
  "intent_model" : null,
  "rerank_model" : null,
  "vl_model" : null,
  "auto_gen_kb" : null,
  "configs" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "use_kg" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "flash_model_id" : null,
  "intent_model_id" : null,
  "parser_config" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
  "vl_model_id" : null,
}
```



## 获取类别设置草稿

<el-row>
<div style="width: 80px">
<el-alert center title="GET" type="success" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/category_settings/get_draft" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`CREATE`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">category_id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|标识|
|<el-row justify="space-between"><el-col :span="20">category_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|名称|
|<el-row justify="space-between"><el-col :span="20">enable</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|逻辑有效标识|
|<el-row justify="space-between"><el-col :span="20">visibility</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|可见范围|
|<el-row justify="space-between"><el-col :span="20">guided_prompt_agent_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|引导提示词智能体标识|
|<el-row justify="space-between"><el-col :span="20">chat_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型|
|<el-row justify="space-between"><el-col :span="20">flash_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|快速交谈模型|
|<el-row justify="space-between"><el-col :span="20">intent_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|快速交谈模型|
|<el-row justify="space-between"><el-col :span="20">rerank_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型|
|<el-row justify="space-between"><el-col :span="20">vl_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|多模态模型|
|<el-row justify="space-between"><el-col :span="20">auto_gen_kb</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|自动创建资源知识库|
|<el-row justify="space-between"><el-col :span="20">configs</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|configs|
|<el-row justify="space-between"><el-col :span="20">similarity_threshold</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|召回相似度阈值|
|<el-row justify="space-between"><el-col :span="20">vector_similarity_weight</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|向量相似度权重|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">resource_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">top_k</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最大召回数量|
|<el-row justify="space-between"><el-col :span="20">rerank</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|召回重排|
|<el-row justify="space-between"><el-col :span="20">use_kg</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|使用知识图谱|
|<el-row justify="space-between"><el-col :span="20">chat_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">embedding_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|embedding模型|
|<el-row justify="space-between"><el-col :span="20">embedding_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">flash_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|快速交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">intent_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|模型标识|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">rerank_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标识|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">source_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|
|<el-row justify="space-between"><el-col :span="20">vl_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|多模态模型标识|



##### 请求示例： {docsify-ignore}
```json
{
  "category_id" : null,
  "category_name" : null,
  "enable" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "guided_prompt_agent_id" : null,
  "chat_model" : null,
  "flash_model" : null,
  "intent_model" : null,
  "rerank_model" : null,
  "vl_model" : null,
  "auto_gen_kb" : null,
  "configs" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "use_kg" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "flash_model_id" : null,
  "intent_model_id" : null,
  "parser_config" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
  "vl_model_id" : null,
}
```


##### 响应示例： {docsify-ignore}
```json

{
  "category_id" : null,
  "category_name" : null,
  "enable" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "guided_prompt_agent_id" : null,
  "chat_model" : null,
  "flash_model" : null,
  "intent_model" : null,
  "rerank_model" : null,
  "vl_model" : null,
  "auto_gen_kb" : null,
  "configs" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "use_kg" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "flash_model_id" : null,
  "intent_model_id" : null,
  "parser_config" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
  "vl_model_id" : null,
}

```

## 保存类别设置

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/category_settings/save" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`CREATE`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">category_id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|标识|
|<el-row justify="space-between"><el-col :span="20">category_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|名称|
|<el-row justify="space-between"><el-col :span="20">enable</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|逻辑有效标识|
|<el-row justify="space-between"><el-col :span="20">visibility</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|可见范围|
|<el-row justify="space-between"><el-col :span="20">guided_prompt_agent_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|引导提示词智能体标识|
|<el-row justify="space-between"><el-col :span="20">chat_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型|
|<el-row justify="space-between"><el-col :span="20">flash_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|快速交谈模型|
|<el-row justify="space-between"><el-col :span="20">intent_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|快速交谈模型|
|<el-row justify="space-between"><el-col :span="20">rerank_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型|
|<el-row justify="space-between"><el-col :span="20">vl_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|多模态模型|
|<el-row justify="space-between"><el-col :span="20">auto_gen_kb</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|自动创建资源知识库|
|<el-row justify="space-between"><el-col :span="20">configs</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|configs|
|<el-row justify="space-between"><el-col :span="20">similarity_threshold</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|召回相似度阈值|
|<el-row justify="space-between"><el-col :span="20">vector_similarity_weight</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|向量相似度权重|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">resource_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">top_k</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最大召回数量|
|<el-row justify="space-between"><el-col :span="20">rerank</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|召回重排|
|<el-row justify="space-between"><el-col :span="20">use_kg</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|使用知识图谱|
|<el-row justify="space-between"><el-col :span="20">chat_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">embedding_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|embedding模型|
|<el-row justify="space-between"><el-col :span="20">embedding_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">flash_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|快速交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">intent_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|模型标识|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">rerank_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标识|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">source_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|
|<el-row justify="space-between"><el-col :span="20">vl_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|多模态模型标识|



##### 请求示例： {docsify-ignore}
```json
{
  "category_id" : null,
  "category_name" : null,
  "enable" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "guided_prompt_agent_id" : null,
  "chat_model" : null,
  "flash_model" : null,
  "intent_model" : null,
  "rerank_model" : null,
  "vl_model" : null,
  "auto_gen_kb" : null,
  "configs" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "use_kg" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "flash_model_id" : null,
  "intent_model_id" : null,
  "parser_config" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
  "vl_model_id" : null,
}
```


##### 响应示例： {docsify-ignore}
```json

{
  "category_id" : null,
  "category_name" : null,
  "enable" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "guided_prompt_agent_id" : null,
  "chat_model" : null,
  "flash_model" : null,
  "intent_model" : null,
  "rerank_model" : null,
  "vl_model" : null,
  "auto_gen_kb" : null,
  "configs" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "use_kg" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "flash_model_id" : null,
  "intent_model_id" : null,
  "parser_config" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
  "vl_model_id" : null,
}

```

## save_aifactory_sys_env

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/category_settings/{key}/save_aifactory_sys_env" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`ENV`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|标识|



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">category_id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|标识|
|<el-row justify="space-between"><el-col :span="20">category_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|名称|
|<el-row justify="space-between"><el-col :span="20">enable</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|逻辑有效标识|
|<el-row justify="space-between"><el-col :span="20">visibility</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|可见范围|
|<el-row justify="space-between"><el-col :span="20">guided_prompt_agent_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|引导提示词智能体标识|
|<el-row justify="space-between"><el-col :span="20">chat_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型|
|<el-row justify="space-between"><el-col :span="20">flash_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|快速交谈模型|
|<el-row justify="space-between"><el-col :span="20">intent_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|快速交谈模型|
|<el-row justify="space-between"><el-col :span="20">rerank_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型|
|<el-row justify="space-between"><el-col :span="20">vl_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|多模态模型|
|<el-row justify="space-between"><el-col :span="20">auto_gen_kb</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|自动创建资源知识库|
|<el-row justify="space-between"><el-col :span="20">configs</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|configs|
|<el-row justify="space-between"><el-col :span="20">similarity_threshold</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|召回相似度阈值|
|<el-row justify="space-between"><el-col :span="20">vector_similarity_weight</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|向量相似度权重|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">resource_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|数据资源|
|<el-row justify="space-between"><el-col :span="20">top_k</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最大召回数量|
|<el-row justify="space-between"><el-col :span="20">rerank</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|召回重排|
|<el-row justify="space-between"><el-col :span="20">use_kg</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|使用知识图谱|
|<el-row justify="space-between"><el-col :span="20">chat_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">embedding_model</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|embedding模型|
|<el-row justify="space-between"><el-col :span="20">embedding_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">flash_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|快速交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">intent_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|模型标识|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">rerank_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标识|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">source_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源名称|
|<el-row justify="space-between"><el-col :span="20">vl_model_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|多模态模型标识|



##### 请求示例： {docsify-ignore}
```json
{
  "category_id" : null,
  "category_name" : null,
  "enable" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "visibility" : null,
  "guided_prompt_agent_id" : null,
  "chat_model" : null,
  "flash_model" : null,
  "intent_model" : null,
  "rerank_model" : null,
  "vl_model" : null,
  "auto_gen_kb" : null,
  "configs" : null,
  "similarity_threshold" : null,
  "vector_similarity_weight" : null,
  "resource" : null,
  "resource_code" : null,
  "top_k" : null,
  "rerank" : null,
  "use_kg" : null,
  "chat_model_id" : null,
  "chunk_method" : null,
  "embedding_model" : null,
  "embedding_model_id" : null,
  "flash_model_id" : null,
  "intent_model_id" : null,
  "parser_config" : null,
  "rerank_model_id" : null,
  "resource_id" : null,
  "source_id" : null,
  "source_name" : null,
  "vl_model_id" : null,
}
```



## DEFAULT

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/category_settings/fetch_default" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_chat_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">n_embedding_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|嵌入模型标识|
|<el-row justify="space-between"><el-col :span="20">n_flash_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|快速交谈模型标识|
|<el-row justify="space-between"><el-col :span="20">n_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标识|
|<el-row justify="space-between"><el-col :span="20">n_intent_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|模型标识|
|<el-row justify="space-between"><el-col :span="20">n_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|名称|
|<el-row justify="space-between"><el-col :span="20">n_rerank_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|召回重排模型标识|
|<el-row justify="space-between"><el-col :span="20">n_resource_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标识|
|<el-row justify="space-between"><el-col :span="20">n_source_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库源标识|
|<el-row justify="space-between"><el-col :span="20">n_vl_model_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|多模态模型标识|



##### 请求示例： {docsify-ignore}
```json
{
  "page" : 0,
  "size" : 20,
  "sort" : null,
  "n_chat_model_id_eq" : null,
  "n_embedding_model_id_eq" : null,
  "n_flash_model_id_eq" : null,
  "n_id_eq" : null,
  "n_intent_model_id_eq" : null,
  "n_name_like" : null,
  "n_rerank_model_id_eq" : null,
  "n_resource_id_eq" : null,
  "n_source_id_eq" : null,
  "n_vl_model_id_eq" : null,
}
```


##### 响应示例： {docsify-ignore}
```json
[
  {
    "category_id" : null,
    "category_name" : null,
    "enable" : null,
    "create_man" : null,
    "create_time" : null,
    "update_man" : null,
    "update_time" : null,
    "visibility" : null,
    "guided_prompt_agent_id" : null,
    "chat_model" : null,
    "flash_model" : null,
    "intent_model" : null,
    "rerank_model" : null,
    "vl_model" : null,
    "auto_gen_kb" : null,
    "configs" : null,
    "similarity_threshold" : null,
    "vector_similarity_weight" : null,
    "resource" : null,
    "resource_code" : null,
    "top_k" : null,
    "rerank" : null,
    "use_kg" : null,
    "chat_model_id" : null,
    "chunk_method" : null,
    "embedding_model" : null,
    "embedding_model_id" : null,
    "flash_model_id" : null,
    "intent_model_id" : null,
    "parser_config" : null,
    "rerank_model_id" : null,
    "resource_id" : null,
    "source_id" : null,
    "source_name" : null,
    "vl_model_id" : null,
  }
]
```



## 下载导入模板
<el-row>
<div style="width: 80px">
<el-alert center title="GET" type="success" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/category_settings/importtemplate" type="info" :closable="false" ></el-alert>
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
<el-alert title="/category_settings/exportdata/{param},/category_settings/exportdata/{param}/{key}" type="info" :closable="false" ></el-alert>
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
<el-alert title="/category_settings/importdata" type="info" :closable="false" ></el-alert>
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
<el-alert title="/category_settings/importdata2" type="info" :closable="false" ></el-alert>
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
<el-alert title="/category_settings/asyncimportdata2" type="info" :closable="false" ></el-alert>
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
<el-alert title="/category_settings/printdata/{key}" type="info" :closable="false" ></el-alert>
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
<el-alert title="/category_settings/report" type="info" :closable="false" ></el-alert>
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