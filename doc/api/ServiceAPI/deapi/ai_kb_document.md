# 知识库文档(ai_kb_document) :id=ai_kb_document
## 创建知识库文档

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_kb_documents" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`CREATE`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "active" : null,
  "kb_id" : null,
  "kb_name" : null,
  "sync_id" : null,
  "chunk_method" : null,
  "sync_frequency" : null,
  "source_type" : null,
  "source_id" : null,
  "type" : null,
  "file" : null,
  "meta_data" : null,
  "status" : null,
  "chunk_num" : null,
  "size" : null,
  "file_type" : null,
  "key_question_list" : null,
  "custom_chunk" : null,
  "parser_config" : null,
  "parsed_content" : null,
  "doc_create_time" : null,
  "parse_error" : null,
  "tag_sets" : null,
  "intelligent_analysis" : null,
  "references" : null,
  "key_questions" : null,
  "key" : null,
  "keywords" : null,
  "content" : null,
  "categories" : null,
  "resource" : null,
  "resource_count" : null,
  "resource_id" : null,
  "page_index_info" : null,
  "summary" : null,
  "digest_code" : null,
  "path" : null,
  "recent_create_days" : null,
  "sequence" : null,
  "user_tag" : null,
  "user_tag2" : null,
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
  "active" : null,
  "kb_id" : null,
  "kb_name" : null,
  "sync_id" : null,
  "chunk_method" : null,
  "sync_frequency" : null,
  "source_type" : null,
  "source_id" : null,
  "type" : null,
  "file" : null,
  "meta_data" : null,
  "status" : null,
  "chunk_num" : null,
  "size" : null,
  "file_type" : null,
  "key_question_list" : null,
  "custom_chunk" : null,
  "parser_config" : null,
  "parsed_content" : null,
  "doc_create_time" : null,
  "parse_error" : null,
  "tag_sets" : null,
  "intelligent_analysis" : null,
  "references" : null,
  "key_questions" : null,
  "key" : null,
  "keywords" : null,
  "content" : null,
  "categories" : null,
  "resource" : null,
  "resource_count" : null,
  "resource_id" : null,
  "page_index_info" : null,
  "summary" : null,
  "digest_code" : null,
  "path" : null,
  "recent_create_days" : null,
  "sequence" : null,
  "user_tag" : null,
  "user_tag2" : null,
}

```

## 获取知识库文档

<el-row>
<div style="width: 80px">
<el-alert center title="GET" type="success" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_kb_documents/{key}" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库文档标识|




##### 响应示例： {docsify-ignore}
```json

{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "active" : null,
  "kb_id" : null,
  "kb_name" : null,
  "sync_id" : null,
  "chunk_method" : null,
  "sync_frequency" : null,
  "source_type" : null,
  "source_id" : null,
  "type" : null,
  "file" : null,
  "meta_data" : null,
  "status" : null,
  "chunk_num" : null,
  "size" : null,
  "file_type" : null,
  "key_question_list" : null,
  "custom_chunk" : null,
  "parser_config" : null,
  "parsed_content" : null,
  "doc_create_time" : null,
  "parse_error" : null,
  "tag_sets" : null,
  "intelligent_analysis" : null,
  "references" : null,
  "key_questions" : null,
  "key" : null,
  "keywords" : null,
  "content" : null,
  "categories" : null,
  "resource" : null,
  "resource_count" : null,
  "resource_id" : null,
  "page_index_info" : null,
  "summary" : null,
  "digest_code" : null,
  "path" : null,
  "recent_create_days" : null,
  "sequence" : null,
  "user_tag" : null,
  "user_tag2" : null,
}

```

## 删除知识库文档

<el-row>
<div style="width: 80px">
<el-alert center title="DELETE" type="error" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_kb_documents/{key}" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`DELETE`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库文档标识|





## 更新知识库文档

<el-row>
<div style="width: 80px">
<el-alert center title="PUT" type="warning" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_kb_documents/{key}" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`UPDATE`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库文档标识|



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "active" : null,
  "kb_id" : null,
  "kb_name" : null,
  "sync_id" : null,
  "chunk_method" : null,
  "sync_frequency" : null,
  "source_type" : null,
  "source_id" : null,
  "type" : null,
  "file" : null,
  "meta_data" : null,
  "status" : null,
  "chunk_num" : null,
  "size" : null,
  "file_type" : null,
  "key_question_list" : null,
  "custom_chunk" : null,
  "parser_config" : null,
  "parsed_content" : null,
  "doc_create_time" : null,
  "parse_error" : null,
  "tag_sets" : null,
  "intelligent_analysis" : null,
  "references" : null,
  "key_questions" : null,
  "key" : null,
  "keywords" : null,
  "content" : null,
  "categories" : null,
  "resource" : null,
  "resource_count" : null,
  "resource_id" : null,
  "page_index_info" : null,
  "summary" : null,
  "digest_code" : null,
  "path" : null,
  "recent_create_days" : null,
  "sequence" : null,
  "user_tag" : null,
  "user_tag2" : null,
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
  "active" : null,
  "kb_id" : null,
  "kb_name" : null,
  "sync_id" : null,
  "chunk_method" : null,
  "sync_frequency" : null,
  "source_type" : null,
  "source_id" : null,
  "type" : null,
  "file" : null,
  "meta_data" : null,
  "status" : null,
  "chunk_num" : null,
  "size" : null,
  "file_type" : null,
  "key_question_list" : null,
  "custom_chunk" : null,
  "parser_config" : null,
  "parsed_content" : null,
  "doc_create_time" : null,
  "parse_error" : null,
  "tag_sets" : null,
  "intelligent_analysis" : null,
  "references" : null,
  "key_questions" : null,
  "key" : null,
  "keywords" : null,
  "content" : null,
  "categories" : null,
  "resource" : null,
  "resource_count" : null,
  "resource_id" : null,
  "page_index_info" : null,
  "summary" : null,
  "digest_code" : null,
  "path" : null,
  "recent_create_days" : null,
  "sequence" : null,
  "user_tag" : null,
  "user_tag2" : null,
}

```

## ai_kb_document_type_counters

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_kb_documents/ai_kb_document_type_counters" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "active" : null,
  "kb_id" : null,
  "kb_name" : null,
  "sync_id" : null,
  "chunk_method" : null,
  "sync_frequency" : null,
  "source_type" : null,
  "source_id" : null,
  "type" : null,
  "file" : null,
  "meta_data" : null,
  "status" : null,
  "chunk_num" : null,
  "size" : null,
  "file_type" : null,
  "key_question_list" : null,
  "custom_chunk" : null,
  "parser_config" : null,
  "parsed_content" : null,
  "doc_create_time" : null,
  "parse_error" : null,
  "tag_sets" : null,
  "intelligent_analysis" : null,
  "references" : null,
  "key_questions" : null,
  "key" : null,
  "keywords" : null,
  "content" : null,
  "categories" : null,
  "resource" : null,
  "resource_count" : null,
  "resource_id" : null,
  "page_index_info" : null,
  "summary" : null,
  "digest_code" : null,
  "path" : null,
  "recent_create_days" : null,
  "sequence" : null,
  "user_tag" : null,
  "user_tag2" : null,
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
  "active" : null,
  "kb_id" : null,
  "kb_name" : null,
  "sync_id" : null,
  "chunk_method" : null,
  "sync_frequency" : null,
  "source_type" : null,
  "source_id" : null,
  "type" : null,
  "file" : null,
  "meta_data" : null,
  "status" : null,
  "chunk_num" : null,
  "size" : null,
  "file_type" : null,
  "key_question_list" : null,
  "custom_chunk" : null,
  "parser_config" : null,
  "parsed_content" : null,
  "doc_create_time" : null,
  "parse_error" : null,
  "tag_sets" : null,
  "intelligent_analysis" : null,
  "references" : null,
  "key_questions" : null,
  "key" : null,
  "keywords" : null,
  "content" : null,
  "categories" : null,
  "resource" : null,
  "resource_count" : null,
  "resource_id" : null,
  "page_index_info" : null,
  "summary" : null,
  "digest_code" : null,
  "path" : null,
  "recent_create_days" : null,
  "sequence" : null,
  "user_tag" : null,
  "user_tag2" : null,
}

```

## 异步重新切片

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_kb_documents/{key}/async_build_chunk" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`UPDATE`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库文档标识|



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "active" : null,
  "kb_id" : null,
  "kb_name" : null,
  "sync_id" : null,
  "chunk_method" : null,
  "sync_frequency" : null,
  "source_type" : null,
  "source_id" : null,
  "type" : null,
  "file" : null,
  "meta_data" : null,
  "status" : null,
  "chunk_num" : null,
  "size" : null,
  "file_type" : null,
  "key_question_list" : null,
  "custom_chunk" : null,
  "parser_config" : null,
  "parsed_content" : null,
  "doc_create_time" : null,
  "parse_error" : null,
  "tag_sets" : null,
  "intelligent_analysis" : null,
  "references" : null,
  "key_questions" : null,
  "key" : null,
  "keywords" : null,
  "content" : null,
  "categories" : null,
  "resource" : null,
  "resource_count" : null,
  "resource_id" : null,
  "page_index_info" : null,
  "summary" : null,
  "digest_code" : null,
  "path" : null,
  "recent_create_days" : null,
  "sequence" : null,
  "user_tag" : null,
  "user_tag2" : null,
}
```


##### 响应示例： {docsify-ignore}
```json
```

## 异步重新索引

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_kb_documents/{key}/async_reindex" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`UPDATE`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库文档标识|



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "active" : null,
  "kb_id" : null,
  "kb_name" : null,
  "sync_id" : null,
  "chunk_method" : null,
  "sync_frequency" : null,
  "source_type" : null,
  "source_id" : null,
  "type" : null,
  "file" : null,
  "meta_data" : null,
  "status" : null,
  "chunk_num" : null,
  "size" : null,
  "file_type" : null,
  "key_question_list" : null,
  "custom_chunk" : null,
  "parser_config" : null,
  "parsed_content" : null,
  "doc_create_time" : null,
  "parse_error" : null,
  "tag_sets" : null,
  "intelligent_analysis" : null,
  "references" : null,
  "key_questions" : null,
  "key" : null,
  "keywords" : null,
  "content" : null,
  "categories" : null,
  "resource" : null,
  "resource_count" : null,
  "resource_id" : null,
  "page_index_info" : null,
  "summary" : null,
  "digest_code" : null,
  "path" : null,
  "recent_create_days" : null,
  "sequence" : null,
  "user_tag" : null,
  "user_tag2" : null,
}
```


##### 响应示例： {docsify-ignore}
```json
```

## 异步文档解析

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_kb_documents/{key}/async_reparse" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`UPDATE`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库文档标识|



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "active" : null,
  "kb_id" : null,
  "kb_name" : null,
  "sync_id" : null,
  "chunk_method" : null,
  "sync_frequency" : null,
  "source_type" : null,
  "source_id" : null,
  "type" : null,
  "file" : null,
  "meta_data" : null,
  "status" : null,
  "chunk_num" : null,
  "size" : null,
  "file_type" : null,
  "key_question_list" : null,
  "custom_chunk" : null,
  "parser_config" : null,
  "parsed_content" : null,
  "doc_create_time" : null,
  "parse_error" : null,
  "tag_sets" : null,
  "intelligent_analysis" : null,
  "references" : null,
  "key_questions" : null,
  "key" : null,
  "keywords" : null,
  "content" : null,
  "categories" : null,
  "resource" : null,
  "resource_count" : null,
  "resource_id" : null,
  "page_index_info" : null,
  "summary" : null,
  "digest_code" : null,
  "path" : null,
  "recent_create_days" : null,
  "sequence" : null,
  "user_tag" : null,
  "user_tag2" : null,
}
```


##### 响应示例： {docsify-ignore}
```json
```

## 批量解析

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_kb_documents/{key}/batch_parse" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`UPDATE`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库文档标识|



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "active" : null,
  "kb_id" : null,
  "kb_name" : null,
  "sync_id" : null,
  "chunk_method" : null,
  "sync_frequency" : null,
  "source_type" : null,
  "source_id" : null,
  "type" : null,
  "file" : null,
  "meta_data" : null,
  "status" : null,
  "chunk_num" : null,
  "size" : null,
  "file_type" : null,
  "key_question_list" : null,
  "custom_chunk" : null,
  "parser_config" : null,
  "parsed_content" : null,
  "doc_create_time" : null,
  "parse_error" : null,
  "tag_sets" : null,
  "intelligent_analysis" : null,
  "references" : null,
  "key_questions" : null,
  "key" : null,
  "keywords" : null,
  "content" : null,
  "categories" : null,
  "resource" : null,
  "resource_count" : null,
  "resource_id" : null,
  "page_index_info" : null,
  "summary" : null,
  "digest_code" : null,
  "path" : null,
  "recent_create_days" : null,
  "sequence" : null,
  "user_tag" : null,
  "user_tag2" : null,
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
  "active" : null,
  "kb_id" : null,
  "kb_name" : null,
  "sync_id" : null,
  "chunk_method" : null,
  "sync_frequency" : null,
  "source_type" : null,
  "source_id" : null,
  "type" : null,
  "file" : null,
  "meta_data" : null,
  "status" : null,
  "chunk_num" : null,
  "size" : null,
  "file_type" : null,
  "key_question_list" : null,
  "custom_chunk" : null,
  "parser_config" : null,
  "parsed_content" : null,
  "doc_create_time" : null,
  "parse_error" : null,
  "tag_sets" : null,
  "intelligent_analysis" : null,
  "references" : null,
  "key_questions" : null,
  "key" : null,
  "keywords" : null,
  "content" : null,
  "categories" : null,
  "resource" : null,
  "resource_count" : null,
  "resource_id" : null,
  "page_index_info" : null,
  "summary" : null,
  "digest_code" : null,
  "path" : null,
  "recent_create_days" : null,
  "sequence" : null,
  "user_tag" : null,
  "user_tag2" : null,
}

```

## 立即切片

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_kb_documents/{key}/build_chunk" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`UPDATE`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库文档标识|



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "active" : null,
  "kb_id" : null,
  "kb_name" : null,
  "sync_id" : null,
  "chunk_method" : null,
  "sync_frequency" : null,
  "source_type" : null,
  "source_id" : null,
  "type" : null,
  "file" : null,
  "meta_data" : null,
  "status" : null,
  "chunk_num" : null,
  "size" : null,
  "file_type" : null,
  "key_question_list" : null,
  "custom_chunk" : null,
  "parser_config" : null,
  "parsed_content" : null,
  "doc_create_time" : null,
  "parse_error" : null,
  "tag_sets" : null,
  "intelligent_analysis" : null,
  "references" : null,
  "key_questions" : null,
  "key" : null,
  "keywords" : null,
  "content" : null,
  "categories" : null,
  "resource" : null,
  "resource_count" : null,
  "resource_id" : null,
  "page_index_info" : null,
  "summary" : null,
  "digest_code" : null,
  "path" : null,
  "recent_create_days" : null,
  "sequence" : null,
  "user_tag" : null,
  "user_tag2" : null,
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
  "active" : null,
  "kb_id" : null,
  "kb_name" : null,
  "sync_id" : null,
  "chunk_method" : null,
  "sync_frequency" : null,
  "source_type" : null,
  "source_id" : null,
  "type" : null,
  "file" : null,
  "meta_data" : null,
  "status" : null,
  "chunk_num" : null,
  "size" : null,
  "file_type" : null,
  "key_question_list" : null,
  "custom_chunk" : null,
  "parser_config" : null,
  "parsed_content" : null,
  "doc_create_time" : null,
  "parse_error" : null,
  "tag_sets" : null,
  "intelligent_analysis" : null,
  "references" : null,
  "key_questions" : null,
  "key" : null,
  "keywords" : null,
  "content" : null,
  "categories" : null,
  "resource" : null,
  "resource_count" : null,
  "resource_id" : null,
  "page_index_info" : null,
  "summary" : null,
  "digest_code" : null,
  "path" : null,
  "recent_create_days" : null,
  "sequence" : null,
  "user_tag" : null,
  "user_tag2" : null,
}

```

## 立即索引

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_kb_documents/{key}/build_index" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`UPDATE`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库文档标识|



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "active" : null,
  "kb_id" : null,
  "kb_name" : null,
  "sync_id" : null,
  "chunk_method" : null,
  "sync_frequency" : null,
  "source_type" : null,
  "source_id" : null,
  "type" : null,
  "file" : null,
  "meta_data" : null,
  "status" : null,
  "chunk_num" : null,
  "size" : null,
  "file_type" : null,
  "key_question_list" : null,
  "custom_chunk" : null,
  "parser_config" : null,
  "parsed_content" : null,
  "doc_create_time" : null,
  "parse_error" : null,
  "tag_sets" : null,
  "intelligent_analysis" : null,
  "references" : null,
  "key_questions" : null,
  "key" : null,
  "keywords" : null,
  "content" : null,
  "categories" : null,
  "resource" : null,
  "resource_count" : null,
  "resource_id" : null,
  "page_index_info" : null,
  "summary" : null,
  "digest_code" : null,
  "path" : null,
  "recent_create_days" : null,
  "sequence" : null,
  "user_tag" : null,
  "user_tag2" : null,
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
  "active" : null,
  "kb_id" : null,
  "kb_name" : null,
  "sync_id" : null,
  "chunk_method" : null,
  "sync_frequency" : null,
  "source_type" : null,
  "source_id" : null,
  "type" : null,
  "file" : null,
  "meta_data" : null,
  "status" : null,
  "chunk_num" : null,
  "size" : null,
  "file_type" : null,
  "key_question_list" : null,
  "custom_chunk" : null,
  "parser_config" : null,
  "parsed_content" : null,
  "doc_create_time" : null,
  "parse_error" : null,
  "tag_sets" : null,
  "intelligent_analysis" : null,
  "references" : null,
  "key_questions" : null,
  "key" : null,
  "keywords" : null,
  "content" : null,
  "categories" : null,
  "resource" : null,
  "resource_count" : null,
  "resource_id" : null,
  "page_index_info" : null,
  "summary" : null,
  "digest_code" : null,
  "path" : null,
  "recent_create_days" : null,
  "sequence" : null,
  "user_tag" : null,
  "user_tag2" : null,
}

```

## 检查知识库文档主键

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_kb_documents/check_key" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`CREATE`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "active" : null,
  "kb_id" : null,
  "kb_name" : null,
  "sync_id" : null,
  "chunk_method" : null,
  "sync_frequency" : null,
  "source_type" : null,
  "source_id" : null,
  "type" : null,
  "file" : null,
  "meta_data" : null,
  "status" : null,
  "chunk_num" : null,
  "size" : null,
  "file_type" : null,
  "key_question_list" : null,
  "custom_chunk" : null,
  "parser_config" : null,
  "parsed_content" : null,
  "doc_create_time" : null,
  "parse_error" : null,
  "tag_sets" : null,
  "intelligent_analysis" : null,
  "references" : null,
  "key_questions" : null,
  "key" : null,
  "keywords" : null,
  "content" : null,
  "categories" : null,
  "resource" : null,
  "resource_count" : null,
  "resource_id" : null,
  "page_index_info" : null,
  "summary" : null,
  "digest_code" : null,
  "path" : null,
  "recent_create_days" : null,
  "sequence" : null,
  "user_tag" : null,
  "user_tag2" : null,
}
```


##### 响应示例： {docsify-ignore}
```json
Integer
```

## 切片

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_kb_documents/{key}/chunk" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`UPDATE`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库文档标识|



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "active" : null,
  "kb_id" : null,
  "kb_name" : null,
  "sync_id" : null,
  "chunk_method" : null,
  "sync_frequency" : null,
  "source_type" : null,
  "source_id" : null,
  "type" : null,
  "file" : null,
  "meta_data" : null,
  "status" : null,
  "chunk_num" : null,
  "size" : null,
  "file_type" : null,
  "key_question_list" : null,
  "custom_chunk" : null,
  "parser_config" : null,
  "parsed_content" : null,
  "doc_create_time" : null,
  "parse_error" : null,
  "tag_sets" : null,
  "intelligent_analysis" : null,
  "references" : null,
  "key_questions" : null,
  "key" : null,
  "keywords" : null,
  "content" : null,
  "categories" : null,
  "resource" : null,
  "resource_count" : null,
  "resource_id" : null,
  "page_index_info" : null,
  "summary" : null,
  "digest_code" : null,
  "path" : null,
  "recent_create_days" : null,
  "sequence" : null,
  "user_tag" : null,
  "user_tag2" : null,
}
```



## 统计评论数

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_kb_documents/{key}/comment_counters" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库文档标识|



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "active" : null,
  "kb_id" : null,
  "kb_name" : null,
  "sync_id" : null,
  "chunk_method" : null,
  "sync_frequency" : null,
  "source_type" : null,
  "source_id" : null,
  "type" : null,
  "file" : null,
  "meta_data" : null,
  "status" : null,
  "chunk_num" : null,
  "size" : null,
  "file_type" : null,
  "key_question_list" : null,
  "custom_chunk" : null,
  "parser_config" : null,
  "parsed_content" : null,
  "doc_create_time" : null,
  "parse_error" : null,
  "tag_sets" : null,
  "intelligent_analysis" : null,
  "references" : null,
  "key_questions" : null,
  "key" : null,
  "keywords" : null,
  "content" : null,
  "categories" : null,
  "resource" : null,
  "resource_count" : null,
  "resource_id" : null,
  "page_index_info" : null,
  "summary" : null,
  "digest_code" : null,
  "path" : null,
  "recent_create_days" : null,
  "sequence" : null,
  "user_tag" : null,
  "user_tag2" : null,
}
```



## 提取元数据

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_kb_documents/extract_meta_data" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "active" : null,
  "kb_id" : null,
  "kb_name" : null,
  "sync_id" : null,
  "chunk_method" : null,
  "sync_frequency" : null,
  "source_type" : null,
  "source_id" : null,
  "type" : null,
  "file" : null,
  "meta_data" : null,
  "status" : null,
  "chunk_num" : null,
  "size" : null,
  "file_type" : null,
  "key_question_list" : null,
  "custom_chunk" : null,
  "parser_config" : null,
  "parsed_content" : null,
  "doc_create_time" : null,
  "parse_error" : null,
  "tag_sets" : null,
  "intelligent_analysis" : null,
  "references" : null,
  "key_questions" : null,
  "key" : null,
  "keywords" : null,
  "content" : null,
  "categories" : null,
  "resource" : null,
  "resource_count" : null,
  "resource_id" : null,
  "page_index_info" : null,
  "summary" : null,
  "digest_code" : null,
  "path" : null,
  "recent_create_days" : null,
  "sequence" : null,
  "user_tag" : null,
  "user_tag2" : null,
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
  "active" : null,
  "kb_id" : null,
  "kb_name" : null,
  "sync_id" : null,
  "chunk_method" : null,
  "sync_frequency" : null,
  "source_type" : null,
  "source_id" : null,
  "type" : null,
  "file" : null,
  "meta_data" : null,
  "status" : null,
  "chunk_num" : null,
  "size" : null,
  "file_type" : null,
  "key_question_list" : null,
  "custom_chunk" : null,
  "parser_config" : null,
  "parsed_content" : null,
  "doc_create_time" : null,
  "parse_error" : null,
  "tag_sets" : null,
  "intelligent_analysis" : null,
  "references" : null,
  "key_questions" : null,
  "key" : null,
  "keywords" : null,
  "content" : null,
  "categories" : null,
  "resource" : null,
  "resource_count" : null,
  "resource_id" : null,
  "page_index_info" : null,
  "summary" : null,
  "digest_code" : null,
  "path" : null,
  "recent_create_days" : null,
  "sequence" : null,
  "user_tag" : null,
  "user_tag2" : null,
}

```

## 获取知识库文档草稿

<el-row>
<div style="width: 80px">
<el-alert center title="GET" type="success" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_kb_documents/get_draft" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`CREATE`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "active" : null,
  "kb_id" : null,
  "kb_name" : null,
  "sync_id" : null,
  "chunk_method" : null,
  "sync_frequency" : null,
  "source_type" : null,
  "source_id" : null,
  "type" : null,
  "file" : null,
  "meta_data" : null,
  "status" : null,
  "chunk_num" : null,
  "size" : null,
  "file_type" : null,
  "key_question_list" : null,
  "custom_chunk" : null,
  "parser_config" : null,
  "parsed_content" : null,
  "doc_create_time" : null,
  "parse_error" : null,
  "tag_sets" : null,
  "intelligent_analysis" : null,
  "references" : null,
  "key_questions" : null,
  "key" : null,
  "keywords" : null,
  "content" : null,
  "categories" : null,
  "resource" : null,
  "resource_count" : null,
  "resource_id" : null,
  "page_index_info" : null,
  "summary" : null,
  "digest_code" : null,
  "path" : null,
  "recent_create_days" : null,
  "sequence" : null,
  "user_tag" : null,
  "user_tag2" : null,
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
  "active" : null,
  "kb_id" : null,
  "kb_name" : null,
  "sync_id" : null,
  "chunk_method" : null,
  "sync_frequency" : null,
  "source_type" : null,
  "source_id" : null,
  "type" : null,
  "file" : null,
  "meta_data" : null,
  "status" : null,
  "chunk_num" : null,
  "size" : null,
  "file_type" : null,
  "key_question_list" : null,
  "custom_chunk" : null,
  "parser_config" : null,
  "parsed_content" : null,
  "doc_create_time" : null,
  "parse_error" : null,
  "tag_sets" : null,
  "intelligent_analysis" : null,
  "references" : null,
  "key_questions" : null,
  "key" : null,
  "keywords" : null,
  "content" : null,
  "categories" : null,
  "resource" : null,
  "resource_count" : null,
  "resource_id" : null,
  "page_index_info" : null,
  "summary" : null,
  "digest_code" : null,
  "path" : null,
  "recent_create_days" : null,
  "sequence" : null,
  "user_tag" : null,
  "user_tag2" : null,
}

```

## GetFullData

<el-row>
<div style="width: 80px">
<el-alert center title="GET" type="success" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_kb_documents/{key}/get_full_data" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库文档标识|




##### 响应示例： {docsify-ignore}
```json

{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "active" : null,
  "kb_id" : null,
  "kb_name" : null,
  "sync_id" : null,
  "chunk_method" : null,
  "sync_frequency" : null,
  "source_type" : null,
  "source_id" : null,
  "type" : null,
  "file" : null,
  "meta_data" : null,
  "status" : null,
  "chunk_num" : null,
  "size" : null,
  "file_type" : null,
  "key_question_list" : null,
  "custom_chunk" : null,
  "parser_config" : null,
  "parsed_content" : null,
  "doc_create_time" : null,
  "parse_error" : null,
  "tag_sets" : null,
  "intelligent_analysis" : null,
  "references" : null,
  "key_questions" : null,
  "key" : null,
  "keywords" : null,
  "content" : null,
  "categories" : null,
  "resource" : null,
  "resource_count" : null,
  "resource_id" : null,
  "page_index_info" : null,
  "summary" : null,
  "digest_code" : null,
  "path" : null,
  "recent_create_days" : null,
  "sequence" : null,
  "user_tag" : null,
  "user_tag2" : null,
}

```

## 获取完整文本

<el-row>
<div style="width: 80px">
<el-alert center title="GET" type="success" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_kb_documents/{key}/get_full_text" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库文档标识|




##### 响应示例： {docsify-ignore}
```json

{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "active" : null,
  "kb_id" : null,
  "kb_name" : null,
  "sync_id" : null,
  "chunk_method" : null,
  "sync_frequency" : null,
  "source_type" : null,
  "source_id" : null,
  "type" : null,
  "file" : null,
  "meta_data" : null,
  "status" : null,
  "chunk_num" : null,
  "size" : null,
  "file_type" : null,
  "key_question_list" : null,
  "custom_chunk" : null,
  "parser_config" : null,
  "parsed_content" : null,
  "doc_create_time" : null,
  "parse_error" : null,
  "tag_sets" : null,
  "intelligent_analysis" : null,
  "references" : null,
  "key_questions" : null,
  "key" : null,
  "keywords" : null,
  "content" : null,
  "categories" : null,
  "resource" : null,
  "resource_count" : null,
  "resource_id" : null,
  "page_index_info" : null,
  "summary" : null,
  "digest_code" : null,
  "path" : null,
  "recent_create_days" : null,
  "sequence" : null,
  "user_tag" : null,
  "user_tag2" : null,
}

```

## 获取页面目录

<el-row>
<div style="width: 80px">
<el-alert center title="GET" type="success" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_kb_documents/{key}/get_page_index" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库文档标识|




##### 响应示例： {docsify-ignore}
```json

{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "active" : null,
  "kb_id" : null,
  "kb_name" : null,
  "sync_id" : null,
  "chunk_method" : null,
  "sync_frequency" : null,
  "source_type" : null,
  "source_id" : null,
  "type" : null,
  "file" : null,
  "meta_data" : null,
  "status" : null,
  "chunk_num" : null,
  "size" : null,
  "file_type" : null,
  "key_question_list" : null,
  "custom_chunk" : null,
  "parser_config" : null,
  "parsed_content" : null,
  "doc_create_time" : null,
  "parse_error" : null,
  "tag_sets" : null,
  "intelligent_analysis" : null,
  "references" : null,
  "key_questions" : null,
  "key" : null,
  "keywords" : null,
  "content" : null,
  "categories" : null,
  "resource" : null,
  "resource_count" : null,
  "resource_id" : null,
  "page_index_info" : null,
  "summary" : null,
  "digest_code" : null,
  "path" : null,
  "recent_create_days" : null,
  "sequence" : null,
  "user_tag" : null,
  "user_tag2" : null,
}

```

## 文档解析处理

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_kb_documents/{key}/parse" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`UPDATE`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库文档标识|



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "active" : null,
  "kb_id" : null,
  "kb_name" : null,
  "sync_id" : null,
  "chunk_method" : null,
  "sync_frequency" : null,
  "source_type" : null,
  "source_id" : null,
  "type" : null,
  "file" : null,
  "meta_data" : null,
  "status" : null,
  "chunk_num" : null,
  "size" : null,
  "file_type" : null,
  "key_question_list" : null,
  "custom_chunk" : null,
  "parser_config" : null,
  "parsed_content" : null,
  "doc_create_time" : null,
  "parse_error" : null,
  "tag_sets" : null,
  "intelligent_analysis" : null,
  "references" : null,
  "key_questions" : null,
  "key" : null,
  "keywords" : null,
  "content" : null,
  "categories" : null,
  "resource" : null,
  "resource_count" : null,
  "resource_id" : null,
  "page_index_info" : null,
  "summary" : null,
  "digest_code" : null,
  "path" : null,
  "recent_create_days" : null,
  "sequence" : null,
  "user_tag" : null,
  "user_tag2" : null,
}
```



## 推理

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_kb_documents/{key}/reason" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`
针对document的原始内容的审查

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库文档标识|



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "active" : null,
  "kb_id" : null,
  "kb_name" : null,
  "sync_id" : null,
  "chunk_method" : null,
  "sync_frequency" : null,
  "source_type" : null,
  "source_id" : null,
  "type" : null,
  "file" : null,
  "meta_data" : null,
  "status" : null,
  "chunk_num" : null,
  "size" : null,
  "file_type" : null,
  "key_question_list" : null,
  "custom_chunk" : null,
  "parser_config" : null,
  "parsed_content" : null,
  "doc_create_time" : null,
  "parse_error" : null,
  "tag_sets" : null,
  "intelligent_analysis" : null,
  "references" : null,
  "key_questions" : null,
  "key" : null,
  "keywords" : null,
  "content" : null,
  "categories" : null,
  "resource" : null,
  "resource_count" : null,
  "resource_id" : null,
  "page_index_info" : null,
  "summary" : null,
  "digest_code" : null,
  "path" : null,
  "recent_create_days" : null,
  "sequence" : null,
  "user_tag" : null,
  "user_tag2" : null,
}
```



## 重新切片

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_kb_documents/{key}/rechunk" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`UPDATE`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库文档标识|



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "active" : null,
  "kb_id" : null,
  "kb_name" : null,
  "sync_id" : null,
  "chunk_method" : null,
  "sync_frequency" : null,
  "source_type" : null,
  "source_id" : null,
  "type" : null,
  "file" : null,
  "meta_data" : null,
  "status" : null,
  "chunk_num" : null,
  "size" : null,
  "file_type" : null,
  "key_question_list" : null,
  "custom_chunk" : null,
  "parser_config" : null,
  "parsed_content" : null,
  "doc_create_time" : null,
  "parse_error" : null,
  "tag_sets" : null,
  "intelligent_analysis" : null,
  "references" : null,
  "key_questions" : null,
  "key" : null,
  "keywords" : null,
  "content" : null,
  "categories" : null,
  "resource" : null,
  "resource_count" : null,
  "resource_id" : null,
  "page_index_info" : null,
  "summary" : null,
  "digest_code" : null,
  "path" : null,
  "recent_create_days" : null,
  "sequence" : null,
  "user_tag" : null,
  "user_tag2" : null,
}
```



## 重新索引

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_kb_documents/{key}/reindex" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`UPDATE`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库文档标识|



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "active" : null,
  "kb_id" : null,
  "kb_name" : null,
  "sync_id" : null,
  "chunk_method" : null,
  "sync_frequency" : null,
  "source_type" : null,
  "source_id" : null,
  "type" : null,
  "file" : null,
  "meta_data" : null,
  "status" : null,
  "chunk_num" : null,
  "size" : null,
  "file_type" : null,
  "key_question_list" : null,
  "custom_chunk" : null,
  "parser_config" : null,
  "parsed_content" : null,
  "doc_create_time" : null,
  "parse_error" : null,
  "tag_sets" : null,
  "intelligent_analysis" : null,
  "references" : null,
  "key_questions" : null,
  "key" : null,
  "keywords" : null,
  "content" : null,
  "categories" : null,
  "resource" : null,
  "resource_count" : null,
  "resource_id" : null,
  "page_index_info" : null,
  "summary" : null,
  "digest_code" : null,
  "path" : null,
  "recent_create_days" : null,
  "sequence" : null,
  "user_tag" : null,
  "user_tag2" : null,
}
```



## 文档重新解析

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_kb_documents/{key}/reparse" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`UPDATE`

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库文档标识|



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "active" : null,
  "kb_id" : null,
  "kb_name" : null,
  "sync_id" : null,
  "chunk_method" : null,
  "sync_frequency" : null,
  "source_type" : null,
  "source_id" : null,
  "type" : null,
  "file" : null,
  "meta_data" : null,
  "status" : null,
  "chunk_num" : null,
  "size" : null,
  "file_type" : null,
  "key_question_list" : null,
  "custom_chunk" : null,
  "parser_config" : null,
  "parsed_content" : null,
  "doc_create_time" : null,
  "parse_error" : null,
  "tag_sets" : null,
  "intelligent_analysis" : null,
  "references" : null,
  "key_questions" : null,
  "key" : null,
  "keywords" : null,
  "content" : null,
  "categories" : null,
  "resource" : null,
  "resource_count" : null,
  "resource_id" : null,
  "page_index_info" : null,
  "summary" : null,
  "digest_code" : null,
  "path" : null,
  "recent_create_days" : null,
  "sequence" : null,
  "user_tag" : null,
  "user_tag2" : null,
}
```



## 保存知识库文档

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_kb_documents/save" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`CREATE`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



##### 请求示例： {docsify-ignore}
```json
{
  "id" : null,
  "name" : null,
  "create_man" : null,
  "create_time" : null,
  "update_man" : null,
  "update_time" : null,
  "active" : null,
  "kb_id" : null,
  "kb_name" : null,
  "sync_id" : null,
  "chunk_method" : null,
  "sync_frequency" : null,
  "source_type" : null,
  "source_id" : null,
  "type" : null,
  "file" : null,
  "meta_data" : null,
  "status" : null,
  "chunk_num" : null,
  "size" : null,
  "file_type" : null,
  "key_question_list" : null,
  "custom_chunk" : null,
  "parser_config" : null,
  "parsed_content" : null,
  "doc_create_time" : null,
  "parse_error" : null,
  "tag_sets" : null,
  "intelligent_analysis" : null,
  "references" : null,
  "key_questions" : null,
  "key" : null,
  "keywords" : null,
  "content" : null,
  "categories" : null,
  "resource" : null,
  "resource_count" : null,
  "resource_id" : null,
  "page_index_info" : null,
  "summary" : null,
  "digest_code" : null,
  "path" : null,
  "recent_create_days" : null,
  "sequence" : null,
  "user_tag" : null,
  "user_tag2" : null,
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
  "active" : null,
  "kb_id" : null,
  "kb_name" : null,
  "sync_id" : null,
  "chunk_method" : null,
  "sync_frequency" : null,
  "source_type" : null,
  "source_id" : null,
  "type" : null,
  "file" : null,
  "meta_data" : null,
  "status" : null,
  "chunk_num" : null,
  "size" : null,
  "file_type" : null,
  "key_question_list" : null,
  "custom_chunk" : null,
  "parser_config" : null,
  "parsed_content" : null,
  "doc_create_time" : null,
  "parse_error" : null,
  "tag_sets" : null,
  "intelligent_analysis" : null,
  "references" : null,
  "key_questions" : null,
  "key" : null,
  "keywords" : null,
  "content" : null,
  "categories" : null,
  "resource" : null,
  "resource_count" : null,
  "resource_id" : null,
  "page_index_info" : null,
  "summary" : null,
  "digest_code" : null,
  "path" : null,
  "recent_create_days" : null,
  "sequence" : null,
  "user_tag" : null,
  "user_tag2" : null,
}

```

## AI知识库文档查询

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_kb_documents/fetch_ai_doc_query" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_file_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">n_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">n_kb_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_kb_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">n_kb_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">n_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">n_recent_create_days_ltandeq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">n_resource_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">n_source_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">n_status_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">n_sync_frequency_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">n_sync_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">n_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|



##### 请求示例： {docsify-ignore}
```json
{
  "page" : 0,
  "size" : 20,
  "sort" : null,
  "n_file_type_eq" : null,
  "n_id_eq" : null,
  "n_kb_id_eq" : null,
  "n_kb_name_eq" : null,
  "n_kb_name_like" : null,
  "n_name_like" : null,
  "n_recent_create_days_ltandeq" : null,
  "n_resource_eq" : null,
  "n_source_id_eq" : null,
  "n_status_eq" : null,
  "n_sync_frequency_eq" : null,
  "n_sync_id_eq" : null,
  "n_type_eq" : null,
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
    "active" : null,
    "kb_id" : null,
    "kb_name" : null,
    "sync_id" : null,
    "chunk_method" : null,
    "sync_frequency" : null,
    "source_type" : null,
    "source_id" : null,
    "type" : null,
    "file" : null,
    "meta_data" : null,
    "status" : null,
    "chunk_num" : null,
    "size" : null,
    "file_type" : null,
    "key_question_list" : null,
    "custom_chunk" : null,
    "parser_config" : null,
    "parsed_content" : null,
    "doc_create_time" : null,
    "parse_error" : null,
    "tag_sets" : null,
    "intelligent_analysis" : null,
    "references" : null,
    "key_questions" : null,
    "key" : null,
    "keywords" : null,
    "content" : null,
    "categories" : null,
    "resource" : null,
    "resource_count" : null,
    "resource_id" : null,
    "page_index_info" : null,
    "summary" : null,
    "digest_code" : null,
    "path" : null,
    "recent_create_days" : null,
    "sequence" : null,
    "user_tag" : null,
    "user_tag2" : null,
  }
]
```

## DEFAULT

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_kb_documents/fetch_default" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_file_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">n_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">n_kb_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_kb_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">n_kb_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">n_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">n_recent_create_days_ltandeq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">n_resource_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">n_source_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">n_status_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">n_sync_frequency_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">n_sync_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">n_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|



##### 请求示例： {docsify-ignore}
```json
{
  "page" : 0,
  "size" : 20,
  "sort" : null,
  "n_file_type_eq" : null,
  "n_id_eq" : null,
  "n_kb_id_eq" : null,
  "n_kb_name_eq" : null,
  "n_kb_name_like" : null,
  "n_name_like" : null,
  "n_recent_create_days_ltandeq" : null,
  "n_resource_eq" : null,
  "n_source_id_eq" : null,
  "n_status_eq" : null,
  "n_sync_frequency_eq" : null,
  "n_sync_id_eq" : null,
  "n_type_eq" : null,
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
    "active" : null,
    "kb_id" : null,
    "kb_name" : null,
    "sync_id" : null,
    "chunk_method" : null,
    "sync_frequency" : null,
    "source_type" : null,
    "source_id" : null,
    "type" : null,
    "file" : null,
    "meta_data" : null,
    "status" : null,
    "chunk_num" : null,
    "size" : null,
    "file_type" : null,
    "key_question_list" : null,
    "custom_chunk" : null,
    "parser_config" : null,
    "parsed_content" : null,
    "doc_create_time" : null,
    "parse_error" : null,
    "tag_sets" : null,
    "intelligent_analysis" : null,
    "references" : null,
    "key_questions" : null,
    "key" : null,
    "keywords" : null,
    "content" : null,
    "categories" : null,
    "resource" : null,
    "resource_count" : null,
    "resource_id" : null,
    "page_index_info" : null,
    "summary" : null,
    "digest_code" : null,
    "path" : null,
    "recent_create_days" : null,
    "sequence" : null,
    "user_tag" : null,
    "user_tag2" : null,
  }
]
```

## 导航列表数据

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_kb_documents/fetch_exp_list" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_file_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">n_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">n_kb_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_kb_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">n_kb_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">n_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">n_recent_create_days_ltandeq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">n_resource_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">n_source_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">n_status_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">n_sync_frequency_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">n_sync_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">n_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|



##### 请求示例： {docsify-ignore}
```json
{
  "page" : 0,
  "size" : 20,
  "sort" : null,
  "n_file_type_eq" : null,
  "n_id_eq" : null,
  "n_kb_id_eq" : null,
  "n_kb_name_eq" : null,
  "n_kb_name_like" : null,
  "n_name_like" : null,
  "n_recent_create_days_ltandeq" : null,
  "n_resource_eq" : null,
  "n_source_id_eq" : null,
  "n_status_eq" : null,
  "n_sync_frequency_eq" : null,
  "n_sync_id_eq" : null,
  "n_type_eq" : null,
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
    "active" : null,
    "kb_id" : null,
    "kb_name" : null,
    "sync_id" : null,
    "chunk_method" : null,
    "sync_frequency" : null,
    "source_type" : null,
    "source_id" : null,
    "type" : null,
    "file" : null,
    "meta_data" : null,
    "status" : null,
    "chunk_num" : null,
    "size" : null,
    "file_type" : null,
    "key_question_list" : null,
    "custom_chunk" : null,
    "parser_config" : null,
    "parsed_content" : null,
    "doc_create_time" : null,
    "parse_error" : null,
    "tag_sets" : null,
    "intelligent_analysis" : null,
    "references" : null,
    "key_questions" : null,
    "key" : null,
    "keywords" : null,
    "content" : null,
    "categories" : null,
    "resource" : null,
    "resource_count" : null,
    "resource_id" : null,
    "page_index_info" : null,
    "summary" : null,
    "digest_code" : null,
    "path" : null,
    "recent_create_days" : null,
    "sequence" : null,
    "user_tag" : null,
    "user_tag2" : null,
  }
]
```

## 过滤器查询

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_kb_documents/fetch_my_filter" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_file_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">n_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">n_kb_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_kb_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">n_kb_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">n_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">n_recent_create_days_ltandeq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">n_resource_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">n_source_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">n_status_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">n_sync_frequency_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">n_sync_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">n_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|



##### 请求示例： {docsify-ignore}
```json
{
  "page" : 0,
  "size" : 20,
  "sort" : null,
  "n_file_type_eq" : null,
  "n_id_eq" : null,
  "n_kb_id_eq" : null,
  "n_kb_name_eq" : null,
  "n_kb_name_like" : null,
  "n_name_like" : null,
  "n_recent_create_days_ltandeq" : null,
  "n_resource_eq" : null,
  "n_source_id_eq" : null,
  "n_status_eq" : null,
  "n_sync_frequency_eq" : null,
  "n_sync_id_eq" : null,
  "n_type_eq" : null,
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
    "active" : null,
    "kb_id" : null,
    "kb_name" : null,
    "sync_id" : null,
    "chunk_method" : null,
    "sync_frequency" : null,
    "source_type" : null,
    "source_id" : null,
    "type" : null,
    "file" : null,
    "meta_data" : null,
    "status" : null,
    "chunk_num" : null,
    "size" : null,
    "file_type" : null,
    "key_question_list" : null,
    "custom_chunk" : null,
    "parser_config" : null,
    "parsed_content" : null,
    "doc_create_time" : null,
    "parse_error" : null,
    "tag_sets" : null,
    "intelligent_analysis" : null,
    "references" : null,
    "key_questions" : null,
    "key" : null,
    "keywords" : null,
    "content" : null,
    "categories" : null,
    "resource" : null,
    "resource_count" : null,
    "resource_id" : null,
    "page_index_info" : null,
    "summary" : null,
    "digest_code" : null,
    "path" : null,
    "recent_create_days" : null,
    "sequence" : null,
    "user_tag" : null,
    "user_tag2" : null,
  }
]
```

## reader

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_kb_documents/fetch_reader" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_file_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">n_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">n_kb_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_kb_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">n_kb_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">n_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">n_recent_create_days_ltandeq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">n_resource_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">n_source_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">n_status_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">n_sync_frequency_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">n_sync_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">n_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|



##### 请求示例： {docsify-ignore}
```json
{
  "page" : 0,
  "size" : 20,
  "sort" : null,
  "n_file_type_eq" : null,
  "n_id_eq" : null,
  "n_kb_id_eq" : null,
  "n_kb_name_eq" : null,
  "n_kb_name_like" : null,
  "n_name_like" : null,
  "n_recent_create_days_ltandeq" : null,
  "n_resource_eq" : null,
  "n_source_id_eq" : null,
  "n_status_eq" : null,
  "n_sync_frequency_eq" : null,
  "n_sync_id_eq" : null,
  "n_type_eq" : null,
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
    "active" : null,
    "kb_id" : null,
    "kb_name" : null,
    "sync_id" : null,
    "chunk_method" : null,
    "sync_frequency" : null,
    "source_type" : null,
    "source_id" : null,
    "type" : null,
    "file" : null,
    "meta_data" : null,
    "status" : null,
    "chunk_num" : null,
    "size" : null,
    "file_type" : null,
    "key_question_list" : null,
    "custom_chunk" : null,
    "parser_config" : null,
    "parsed_content" : null,
    "doc_create_time" : null,
    "parse_error" : null,
    "tag_sets" : null,
    "intelligent_analysis" : null,
    "references" : null,
    "key_questions" : null,
    "key" : null,
    "keywords" : null,
    "content" : null,
    "categories" : null,
    "resource" : null,
    "resource_count" : null,
    "resource_id" : null,
    "page_index_info" : null,
    "summary" : null,
    "digest_code" : null,
    "path" : null,
    "recent_create_days" : null,
    "sequence" : null,
    "user_tag" : null,
    "user_tag2" : null,
  }
]
```

## 最近文档

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_kb_documents/fetch_recent" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_file_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">n_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">n_kb_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_kb_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">n_kb_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">n_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">n_recent_create_days_ltandeq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">n_resource_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">n_source_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">n_status_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">n_sync_frequency_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">n_sync_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">n_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|



##### 请求示例： {docsify-ignore}
```json
{
  "page" : 0,
  "size" : 20,
  "sort" : null,
  "n_file_type_eq" : null,
  "n_id_eq" : null,
  "n_kb_id_eq" : null,
  "n_kb_name_eq" : null,
  "n_kb_name_like" : null,
  "n_name_like" : null,
  "n_recent_create_days_ltandeq" : null,
  "n_resource_eq" : null,
  "n_source_id_eq" : null,
  "n_status_eq" : null,
  "n_sync_frequency_eq" : null,
  "n_sync_id_eq" : null,
  "n_type_eq" : null,
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
    "active" : null,
    "kb_id" : null,
    "kb_name" : null,
    "sync_id" : null,
    "chunk_method" : null,
    "sync_frequency" : null,
    "source_type" : null,
    "source_id" : null,
    "type" : null,
    "file" : null,
    "meta_data" : null,
    "status" : null,
    "chunk_num" : null,
    "size" : null,
    "file_type" : null,
    "key_question_list" : null,
    "custom_chunk" : null,
    "parser_config" : null,
    "parsed_content" : null,
    "doc_create_time" : null,
    "parse_error" : null,
    "tag_sets" : null,
    "intelligent_analysis" : null,
    "references" : null,
    "key_questions" : null,
    "key" : null,
    "keywords" : null,
    "content" : null,
    "categories" : null,
    "resource" : null,
    "resource_count" : null,
    "resource_id" : null,
    "page_index_info" : null,
    "summary" : null,
    "digest_code" : null,
    "path" : null,
    "recent_create_days" : null,
    "sequence" : null,
    "user_tag" : null,
    "user_tag2" : null,
  }
]
```

## 资源分类

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_kb_documents/fetch_resource_classification" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_file_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">n_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">n_kb_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_kb_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">n_kb_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">n_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">n_recent_create_days_ltandeq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">n_resource_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">n_source_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">n_status_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">n_sync_frequency_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">n_sync_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">n_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|



##### 请求示例： {docsify-ignore}
```json
{
  "page" : 0,
  "size" : 20,
  "sort" : null,
  "n_file_type_eq" : null,
  "n_id_eq" : null,
  "n_kb_id_eq" : null,
  "n_kb_name_eq" : null,
  "n_kb_name_like" : null,
  "n_name_like" : null,
  "n_recent_create_days_ltandeq" : null,
  "n_resource_eq" : null,
  "n_source_id_eq" : null,
  "n_status_eq" : null,
  "n_sync_frequency_eq" : null,
  "n_sync_id_eq" : null,
  "n_type_eq" : null,
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
    "active" : null,
    "kb_id" : null,
    "kb_name" : null,
    "sync_id" : null,
    "chunk_method" : null,
    "sync_frequency" : null,
    "source_type" : null,
    "source_id" : null,
    "type" : null,
    "file" : null,
    "meta_data" : null,
    "status" : null,
    "chunk_num" : null,
    "size" : null,
    "file_type" : null,
    "key_question_list" : null,
    "custom_chunk" : null,
    "parser_config" : null,
    "parsed_content" : null,
    "doc_create_time" : null,
    "parse_error" : null,
    "tag_sets" : null,
    "intelligent_analysis" : null,
    "references" : null,
    "key_questions" : null,
    "key" : null,
    "keywords" : null,
    "content" : null,
    "categories" : null,
    "resource" : null,
    "resource_count" : null,
    "resource_id" : null,
    "page_index_info" : null,
    "summary" : null,
    "digest_code" : null,
    "path" : null,
    "recent_create_days" : null,
    "sequence" : null,
    "user_tag" : null,
    "user_tag2" : null,
  }
]
```

## 简单查询

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_kb_documents/fetch_simple" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_file_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">n_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">n_kb_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_kb_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">n_kb_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">n_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">n_recent_create_days_ltandeq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">n_resource_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">n_source_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">n_status_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">n_sync_frequency_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">n_sync_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">n_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|



##### 请求示例： {docsify-ignore}
```json
{
  "page" : 0,
  "size" : 20,
  "sort" : null,
  "n_file_type_eq" : null,
  "n_id_eq" : null,
  "n_kb_id_eq" : null,
  "n_kb_name_eq" : null,
  "n_kb_name_like" : null,
  "n_name_like" : null,
  "n_recent_create_days_ltandeq" : null,
  "n_resource_eq" : null,
  "n_source_id_eq" : null,
  "n_status_eq" : null,
  "n_sync_frequency_eq" : null,
  "n_sync_id_eq" : null,
  "n_type_eq" : null,
}
```


##### 响应示例： {docsify-ignore}
```json
[
  {
    "name" : null,
    "update_time" : null,
    "sync_id" : null,
    "chunk_method" : null,
    "type" : null,
    "status" : null,
    "custom_chunk" : null,
    "path" : null,
    "sequence" : null,
  }
]
```

## 未解析文档

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_kb_documents/fetch_unparsed" type="info" :closable="false" ></el-alert>
</div>
</el-row>
权限标识：`READ`



##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_file_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">n_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">n_kb_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_kb_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">n_kb_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">n_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">n_recent_create_days_ltandeq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">n_resource_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">n_source_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">n_status_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">n_sync_frequency_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">n_sync_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">n_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|



##### 请求示例： {docsify-ignore}
```json
{
  "page" : 0,
  "size" : 20,
  "sort" : null,
  "n_file_type_eq" : null,
  "n_id_eq" : null,
  "n_kb_id_eq" : null,
  "n_kb_name_eq" : null,
  "n_kb_name_like" : null,
  "n_name_like" : null,
  "n_recent_create_days_ltandeq" : null,
  "n_resource_eq" : null,
  "n_source_id_eq" : null,
  "n_status_eq" : null,
  "n_sync_frequency_eq" : null,
  "n_sync_id_eq" : null,
  "n_type_eq" : null,
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
    "active" : null,
    "kb_id" : null,
    "kb_name" : null,
    "sync_id" : null,
    "chunk_method" : null,
    "sync_frequency" : null,
    "source_type" : null,
    "source_id" : null,
    "type" : null,
    "file" : null,
    "meta_data" : null,
    "status" : null,
    "chunk_num" : null,
    "size" : null,
    "file_type" : null,
    "key_question_list" : null,
    "custom_chunk" : null,
    "parser_config" : null,
    "parsed_content" : null,
    "doc_create_time" : null,
    "parse_error" : null,
    "tag_sets" : null,
    "intelligent_analysis" : null,
    "references" : null,
    "key_questions" : null,
    "key" : null,
    "keywords" : null,
    "content" : null,
    "categories" : null,
    "resource" : null,
    "resource_count" : null,
    "resource_id" : null,
    "page_index_info" : null,
    "summary" : null,
    "digest_code" : null,
    "path" : null,
    "recent_create_days" : null,
    "sequence" : null,
    "user_tag" : null,
    "user_tag2" : null,
  }
]
```



## 下载导入模板
<el-row>
<div style="width: 80px">
<el-alert center title="GET" type="success" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_kb_documents/importtemplate" type="info" :closable="false" ></el-alert>
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
<el-alert title="/ai_kb_documents/exportdata/{param},/ai_kb_documents/exportdata/{param}/{key}" type="info" :closable="false" ></el-alert>
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
<el-alert title="/ai_kb_documents/importdata" type="info" :closable="false" ></el-alert>
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
<el-alert title="/ai_kb_documents/importdata2" type="info" :closable="false" ></el-alert>
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
<el-alert title="/ai_kb_documents/asyncimportdata2" type="info" :closable="false" ></el-alert>
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
<el-alert title="/ai_kb_documents/printdata/{key}" type="info" :closable="false" ></el-alert>
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
<el-alert title="/ai_kb_documents/report" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 查询参数 {docsify-ignore}

|字段col300|类型col150|备注col400|
|---|---|----|
| srfreporttag | String | 报表标识 |
| srfcontenttype | String | 报表类型 |




## 根据知识库创建知识库文档

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库主键|




##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



## 根据知识库获取知识库文档

<el-row>
<div style="width: 80px">
<el-alert center title="GET" type="success" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/{key}" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库主键|
|key|String|知识库文档标识|




## 根据知识库删除知识库文档

<el-row>
<div style="width: 80px">
<el-alert center title="DELETE" type="error" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/{key}" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库主键|
|key|String|知识库文档标识|




## 根据知识库更新知识库文档

<el-row>
<div style="width: 80px">
<el-alert center title="PUT" type="warning" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/{key}" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库主键|
|key|String|知识库文档标识|




##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



## 根据知识库ai_kb_document_type_counters

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/ai_kb_document_type_counters" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库主键|




##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



## 根据知识库异步重新切片

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/{key}/async_build_chunk" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库主键|
|key|String|知识库文档标识|




##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



## 根据知识库异步重新索引

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/{key}/async_reindex" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库主键|
|key|String|知识库文档标识|




##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



## 根据知识库异步文档解析

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/{key}/async_reparse" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库主键|
|key|String|知识库文档标识|




##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



## 根据知识库批量解析

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/{key}/batch_parse" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库主键|
|key|String|知识库文档标识|




##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



## 根据知识库立即切片

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/{key}/build_chunk" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库主键|
|key|String|知识库文档标识|




##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



## 根据知识库立即索引

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/{key}/build_index" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库主键|
|key|String|知识库文档标识|




##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



## 根据知识库检查知识库文档主键

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/check_key" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库主键|




##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



## 根据知识库切片

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/{key}/chunk" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库主键|
|key|String|知识库文档标识|




##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



## 根据知识库统计评论数

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/{key}/comment_counters" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库主键|
|key|String|知识库文档标识|




##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



## 根据知识库提取元数据

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/extract_meta_data" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库主键|




##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



## 根据知识库获取知识库文档草稿

<el-row>
<div style="width: 80px">
<el-alert center title="GET" type="success" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/get_draft" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库主键|




##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



## 根据知识库GetFullData

<el-row>
<div style="width: 80px">
<el-alert center title="GET" type="success" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/{key}/get_full_data" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库主键|
|key|String|知识库文档标识|




## 根据知识库获取完整文本

<el-row>
<div style="width: 80px">
<el-alert center title="GET" type="success" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/{key}/get_full_text" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库主键|
|key|String|知识库文档标识|




## 根据知识库获取页面目录

<el-row>
<div style="width: 80px">
<el-alert center title="GET" type="success" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/{key}/get_page_index" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库主键|
|key|String|知识库文档标识|




## 根据知识库文档解析处理

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/{key}/parse" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库主键|
|key|String|知识库文档标识|




##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



## 根据知识库推理

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/{key}/reason" type="info" :closable="false" ></el-alert>
</div>
</el-row>
针对document的原始内容的审查

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库主键|
|key|String|知识库文档标识|




##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



## 根据知识库重新切片

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/{key}/rechunk" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库主键|
|key|String|知识库文档标识|




##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



## 根据知识库重新索引

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/{key}/reindex" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库主键|
|key|String|知识库文档标识|




##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



## 根据知识库文档重新解析

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/{key}/reparse" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库主键|
|key|String|知识库文档标识|




##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



## 根据知识库保存知识库文档

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/save" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库主键|




##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">id</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">active</el-col><el-col :span="4" style="text-align:right"></el-col> </el-row>|Integer|是否启用|
|<el-row justify="space-between"><el-col :span="20">kb_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">kb_name</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">sync_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">chunk_method</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|切片方法|
|<el-row justify="space-between"><el-col :span="20">sync_frequency</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">source_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源类型|
|<el-row justify="space-between"><el-col :span="20">source_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|
|<el-row justify="space-between"><el-col :span="20">file</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|上传文件|
|<el-row justify="space-between"><el-col :span="20">meta_data</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档元数据|
|<el-row justify="space-between"><el-col :span="20">status</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">chunk_num</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|切片数量|
|<el-row justify="space-between"><el-col :span="20">size</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|内容大小|
|<el-row justify="space-between"><el-col :span="20">file_type</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">key_question_list</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|关键问题列表|
|<el-row justify="space-between"><el-col :span="20">custom_chunk</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|自定义切片|
|<el-row justify="space-between"><el-col :span="20">parser_config</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|解析配置|
|<el-row justify="space-between"><el-col :span="20">parsed_content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析内容|
|<el-row justify="space-between"><el-col :span="20">doc_create_time</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档创建时间|
|<el-row justify="space-between"><el-col :span="20">parse_error</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|解析信息|
|<el-row justify="space-between"><el-col :span="20">tag_sets</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|标签集|
|<el-row justify="space-between"><el-col :span="20">intelligent_analysis</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|智能分析|
|<el-row justify="space-between"><el-col :span="20">references</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Object|参考引用|
|<el-row justify="space-between"><el-col :span="20">key_questions</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键问题|
|<el-row justify="space-between"><el-col :span="20">key</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|业务主键|
|<el-row justify="space-between"><el-col :span="20">keywords</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|关键字|
|<el-row justify="space-between"><el-col :span="20">content</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|内容|
|<el-row justify="space-between"><el-col :span="20">categories</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录|
|<el-row justify="space-between"><el-col :span="20">resource</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">resource_count</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|resource_count|
|<el-row justify="space-between"><el-col :span="20">resource_id</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|resource_id|
|<el-row justify="space-between"><el-col :span="20">page_index_info</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|目录信息|
|<el-row justify="space-between"><el-col :span="20">summary</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要|
|<el-row justify="space-between"><el-col :span="20">digest_code</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|摘要代码|
|<el-row justify="space-between"><el-col :span="20">path</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|路径|
|<el-row justify="space-between"><el-col :span="20">recent_create_days</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">sequence</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|BigDecimal|序号|
|<el-row justify="space-between"><el-col :span="20">user_tag</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记|
|<el-row justify="space-between"><el-col :span="20">user_tag2</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|用户标记2|



## 根据知识库AI知识库文档查询

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/fetch_ai_doc_query" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库主键|




##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_file_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">n_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">n_kb_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_kb_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">n_kb_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">n_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">n_recent_create_days_ltandeq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">n_resource_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">n_source_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">n_status_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">n_sync_frequency_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">n_sync_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">n_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|



## 根据知识库DEFAULT

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/fetch_default" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库主键|




##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_file_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">n_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">n_kb_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_kb_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">n_kb_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">n_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">n_recent_create_days_ltandeq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">n_resource_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">n_source_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">n_status_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">n_sync_frequency_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">n_sync_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">n_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|



## 根据知识库导航列表数据

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/fetch_exp_list" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库主键|




##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_file_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">n_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">n_kb_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_kb_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">n_kb_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">n_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">n_recent_create_days_ltandeq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">n_resource_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">n_source_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">n_status_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">n_sync_frequency_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">n_sync_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">n_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|



## 根据知识库过滤器查询

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/fetch_my_filter" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库主键|




##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_file_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">n_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">n_kb_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_kb_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">n_kb_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">n_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">n_recent_create_days_ltandeq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">n_resource_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">n_source_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">n_status_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">n_sync_frequency_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">n_sync_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">n_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|



## 根据知识库reader

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/fetch_reader" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库主键|




##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_file_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">n_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">n_kb_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_kb_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">n_kb_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">n_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">n_recent_create_days_ltandeq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">n_resource_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">n_source_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">n_status_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">n_sync_frequency_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">n_sync_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">n_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|



## 根据知识库最近文档

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/fetch_recent" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库主键|




##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_file_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">n_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">n_kb_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_kb_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">n_kb_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">n_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">n_recent_create_days_ltandeq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">n_resource_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">n_source_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">n_status_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">n_sync_frequency_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">n_sync_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">n_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|



## 根据知识库资源分类

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/fetch_resource_classification" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库主键|




##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_file_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">n_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">n_kb_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_kb_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">n_kb_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">n_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">n_recent_create_days_ltandeq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">n_resource_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">n_source_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">n_status_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">n_sync_frequency_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">n_sync_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">n_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|



## 根据知识库简单查询

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/fetch_simple" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库主键|




##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_file_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">n_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">n_kb_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_kb_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">n_kb_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">n_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">n_recent_create_days_ltandeq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">n_resource_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">n_source_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">n_status_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">n_sync_frequency_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">n_sync_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">n_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|



## 根据知识库未解析文档

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/fetch_unparsed" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库主键|




##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|<el-row justify="space-between"><el-col :span="20">n_file_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文件类型|
|<el-row justify="space-between"><el-col :span="20">n_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库文档标识|
|<el-row justify="space-between"><el-col :span="20">n_kb_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库标识|
|<el-row justify="space-between"><el-col :span="20">n_kb_name_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">n_kb_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|知识库|
|<el-row justify="space-between"><el-col :span="20">n_name_like</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档名称|
|<el-row justify="space-between"><el-col :span="20">n_recent_create_days_ltandeq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|Integer|最近创建日期|
|<el-row justify="space-between"><el-col :span="20">n_resource_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|资源|
|<el-row justify="space-between"><el-col :span="20">n_source_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|源标识|
|<el-row justify="space-between"><el-col :span="20">n_status_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|状态|
|<el-row justify="space-between"><el-col :span="20">n_sync_frequency_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|同步频率|
|<el-row justify="space-between"><el-col :span="20">n_sync_id_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档同步标识|
|<el-row justify="space-between"><el-col :span="20">n_type_eq</el-col><el-col :span="4" style="text-align:right"><el-text size="small" type="success">可选</el-text></el-col> </el-row>|String|文档类型|




## 根据知识库下载导入模板
<el-row>
<div style="width: 80px">
<el-alert center title="GET" type="success" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/importtemplate" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库标识|

##### 查询参数 {docsify-ignore}

|字段col300|类型col150|备注col400|
|---|---|----|
| srfimporttag | String | 导入标识 |



## 根据知识库数据导出

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/exportdata/{param},/ai_knowledge_bases/{pkey}/ai_kb_documents/exportdata/{param}/{key}" type="info" :closable="false" ></el-alert>
</div>
</el-row>

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库标识|
|param|String|导出集合方法名称|
|key|String|数据主键|

##### 查询参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|key|String|知识库标识|
|srfexporttag|String|导出模板标识|

##### 请求参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|page|Integer|page|
|size|Integer|分页大小|
|n_xxx_eq|String|过滤参数|


## 根据知识库数据导入

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/importdata" type="info" :closable="false" ></el-alert>
</div>
</el-row>

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库标识|

##### 查询参数 {docsify-ignore}

|字段col300|类型col150|备注col400|
|---|---|----|
| srfimporttag | String | 导入标识 |

##### 请求参数 {docsify-ignore}

|字段col300|类型col150|备注col400|
|---|---|----|
| file | file | 导入数据文具 |

## 根据知识库数据导入（返回错误excel）

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/importdata2" type="info" :closable="false" ></el-alert>
</div>
</el-row>

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库标识|

##### 查询参数 {docsify-ignore}

|字段col300|类型col150|备注col400|
|---|---|----|
| srfimporttag | String | 导入标识 |

##### 请求参数 {docsify-ignore}

|字段col300|类型col150|备注col400|
|---|---|----|
| file | file | 导入数据文具 |

## 根据知识库自定义表头导入（异步）
<el-row>
<div style="width: 80px">
<el-alert center title="GET" type="success" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/asyncimportdata2" type="info" :closable="false" ></el-alert>
</div>
</el-row>

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库标识|

##### 查询参数 {docsify-ignore}

|字段col300|类型col150|备注col400|
|---|---|----|
| srfimporttag | String | 导入标识 |
| srfossfileid | String | 导入文件 |
| srfimportschemaid | String | 表头定义 |


## 根据知识库数据打印
<el-row>
<div style="width: 80px">
<el-alert center title="GET" type="success" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/printdata/{key}" type="info" :closable="false" ></el-alert>
</div>
</el-row>

##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库标识|
|key|String|数据主键|

##### 查询参数 {docsify-ignore}

|字段col300|类型col150|备注col400|
|---|---|----|
| srfprinttag | String | 打印标识 |
| srfcontenttype | String | 打印类型 |



## 根据知识库报表打印

<el-row>
<div style="width: 80px">
<el-alert center title="POST" style="background-color: rgba(52, 143, 228, 0.1);color: #348fe4;" :closable="false" ></el-alert>
</div>
<div style="margin-left:5px;width: calc(100% - 85px)">
<el-alert title="/ai_knowledge_bases/{pkey}/ai_kb_documents/report" type="info" :closable="false" ></el-alert>
</div>
</el-row>


##### 路径参数 {docsify-ignore}
|字段col300|类型col150|备注col400|
|---|---|----|
|pkey|String|知识库标识|

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