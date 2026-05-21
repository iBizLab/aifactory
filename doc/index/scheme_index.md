# 数据结构 <!-- {docsify-ignore-all} -->

### db2
#### 应用视图主题(APP_VIEW_THEME)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|APP_TAG|应用标记|VARCHAR|是|100|||
|APP_VIEW_TAG|应用视图标记|VARCHAR|是|100|||
|CAPTION|标题|VARCHAR|是|200|||
|CREATE_MAN|建立人|VARCHAR|是|100|||
|CREATE_TIME|建立时间|DATETIME|是||||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|NAME|名称|VARCHAR|是|200|||
|ORDER_VALUE|排序值|INT|是||||
|OWNER_TYPE|所有者类型|VARCHAR|是|30|||
|SYSTEM_TAG|系统标记|VARCHAR|是|100|||
|THEME_MODEL|主题模型|TEXT|是|1048576|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
|VALID_FLAG|启用标记|INT|是||||
#### 认证日志(IBZAUTHLOG)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|AUTHAGENT|认证方式|VARCHAR|是|100|||
|AUTHCODE|认证结果|VARCHAR|是|15|||
|AUTHTIME|认证时间|DATETIME|是||||
|DOMAINS|域|VARCHAR|是|100|||
|IPADDR|IP地址|VARCHAR|是|100|||
|LOGID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|MACADDR|MAC地址|VARCHAR|是|100|||
|PERSONNAME|用户名称|VARCHAR|是|100|||
|USERAGENT|客户端|VARCHAR|是|500|||
|USERID|用户全局标识|VARCHAR|是|100|||
|USERNAME|用户全局名|VARCHAR|是|100|||
#### 第三方用户(IBZOPENUSER)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CREATEDATE|建立时间|DATETIME|是||||
|CREATEMAN|创建人|VARCHAR|是|100|||
|DEPTS|部门|VARCHAR|是|100|||
|ISBINDING|是否绑定|INT|是||||
|MOBILE|手机|VARCHAR|是|100|||
|OPENUSERCODE|第三方用户代码|VARCHAR|是|100|||
|OPENUSERID<i class="fa fa-key"></i>|第三方用户标识|VARCHAR|否|60|||
|OPENUSERNAME|第三方用户名称|VARCHAR|是|100|||
|OPEN_TYPE|第三方用户类型|VARCHAR|是|100|||
|ORGID|组织标识|VARCHAR|是|100|||
|UPDATEDATE|更新时间|DATETIME|是||||
|UPDATEMAN|最后更新人|VARCHAR|是|100|||
|USERID|用户标识|VARCHAR|是|100|||
### 默认数据库架构
#### 活动(ACTIVITY)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|AUDITINFO|审计信息|TEXT|是|1048576|||
|AUDITTYPE|审计类型|VARCHAR|是|100|||
|CREATE_MAN|建立人|VARCHAR|是|100|||
|CREATE_TIME|建立时间|DATETIME|是||||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|IPADDRESS|访问地址|VARCHAR|是|500|||
|NAME|名称|VARCHAR|是|200|||
|OBJECTID|对象标识|VARCHAR|是|100|||
|OBJECTTYPE|对象类型|VARCHAR|是|100|||
|OPPERSONID|操作人|VARCHAR|是|100|||
|OPPERSONNAME|操作人|VARCHAR|是|100|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
#### 智能体(AI_AGENT)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|ACTIVE|是否启用该规格|INT|是||||
|AGENT_GROUP_TAG|代理分组标记|VARCHAR|是|200|||
|AI_MODEL_ID|模型标识|VARCHAR|是|100|||
|CODE_NAME|代码标识|VARCHAR|是|100|||
|CREATE_MAN|建立人|VARCHAR|是|100|||
|CREATE_TIME|建立时间|DATETIME|是||||
|CUSTOM_SUGGESTION_PROMPT|自定义建议提示词|TEXT|是|1048576|||
|DEFAULT_SYSTEM_PROMPT|默认系统提示词|TEXT|是|1048576|||
|ENABLE_SEARCHING|支持联网搜索|INT|是||||
|ENABLE_SUGGESTED_QUESTIONS|启用问题建议|INT|是||||
|ENABLE_THINKING|启用思考链|INT|是||||
|ENABLE_TOOLS|调用工具|INT|是||||
|GENERATION_MODE|生成模式|VARCHAR|是|60|||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|IS_DEFAULT|是否默认Agent|INT|是||||
|KB_MODE|知识库模式|VARCHAR|是|60|||
|MAX_INPUT_TOKENS|最大输入token数|INT|是||||
|MEMORY_DOC_TAG|记忆存储文档标记|VARCHAR|是|200|||
|MEMORY_ISOLATION_MODE|记忆隔离模式|VARCHAR|是|60|||
|MEMORY_KB_TAG|记忆存储知识库标记|VARCHAR|是|200|||
|MEMORY_MAX_TURNS|记忆对话轮数|INT|是||||
|MEMORY_MODE|记忆模式|VARCHAR|是|200|||
|NAME|名称|VARCHAR|是|200|||
|PAGE_INDEX|启用增强目录召回|INT|是||||
|PUBLISH_SKILL|发布技能|INT|是||||
|RERANK|召回重排|INT|是||||
|RERANK_MODEL|召回重排模型|VARCHAR|是|100|||
|RERANK_MODEL_ID|模型标识|VARCHAR|是|100|||
|SEQUENCE|排序|INT|是||||
|SIMILARITY_THRESHOLD|召回相似度阈值|DECIMAL|是||2||
|SKILL_LOAD_MODE|技能加载模式|VARCHAR|是|60|||
|SKILL_PROMPT|技能提示词|TEXT|是|1048576|||
|SKILL_TAGS|激活技能|TEXT|是|1048576|||
|STREAM|流式输出|INT|是||||
|STREAM_ENABLED|启用流式输出|INT|是||||
|SUGGESTED_QUESTIONS|预制建议问题|TEXT|是|1000|||
|TEMPERATURE|模型随机性参数|DECIMAL|是||2||
|THINKING_ENABLED|启用思考链|INT|是||||
|TOOLS_ENABLED|调用工具|INT|是||||
|TOOL_EXCEED_MESSAGE|工具调用超限提示语|TEXT|是|1048576|||
|TOOL_MAX_CALLS|最大工具调用次数|INT|是||||
|TOP_K|最大召回数量|INT|是||||
|TOP_P|概率核采样|DECIMAL|是||2||
|TRIMMING_STRATEGY|截断策略|VARCHAR|是|60|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
|USE_KG|使用知识图谱|INT|是||||
|VECTOR_SIMILARITY_WEIGHT|向量相似度权重|DECIMAL|是||1||
|VLM_PROMPT|视觉识别提示词|TEXT|是|1048576|||
|WELCOME_MESSAGE|欢迎消息模板|TEXT|是|1048576|||
#### 智能体分配(AI_AGENT_ASSIGNMENT)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CONTEXT_ID|智能体业务上下文标识|VARCHAR|是|100|||
|CREATE_MAN|创建人|VARCHAR|是|100|||
|CREATE_TIME|创建时间|DATETIME|是||||
|CTRL_TAG|部件标记|VARCHAR|是|100|||
|ENTITY_TAG|实体标记|VARCHAR|是|100|||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|NAME|名称|VARCHAR|是|200|||
|SYSTEM_FLAG|系统标记|INT|是||||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
|USE_TAG|引用标记|VARCHAR|是|100|||
|VIEW_TAG|视图标记|VARCHAR|是|100|||
#### 智能体业务上下文(AI_AGENT_CONTEXT)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|ACTIVE|有效|INT|是||||
|AGENT_GROUP_TAG|代理分组标记|VARCHAR|是|200|||
|AI_AGENT_ID|智能体标识|VARCHAR|是|100|||
|AI_AGENT_KNOWLEDGE_RELS|引用知识库集合|TEXT|是|1048576|||
|AI_MODEL_ID|模型标识|VARCHAR|是|100|||
|ALLOW_ANY_KNOWLEDGE_BASE|允许任意知识库|INT|是||||
|CODE_NAME|代码标识|VARCHAR|是|100|||
|CONTEXT_DEBUG_DATA|调试数据|TEXT|是|1048576|||
|CREATE_MAN|建立人|VARCHAR|是|100|||
|CREATE_TIME|建立时间|DATETIME|是||||
|CUSTOM_CODE|自定义代码|TEXT|是|16777215|||
|CUSTOM_SUGGESTION_PROMPT|自定义建议提示词|TEXT|是|1048576|||
|DEFAULT_SYSTEM_PROMPT|默认系统提示词|TEXT|是|1048576|||
|DESCRIPTION|描述|VARCHAR|是|2000|||
|ENABLE_SEARCHING|支持联网搜索|INT|是||||
|ENABLE_SUGGESTED_QUESTIONS|启用问题建议|INT|是||||
|ENABLE_THINKING|启用思考链|INT|是||||
|ENABLE_TOOLS|调用工具|INT|是||||
|FLOW_MODE|智能体工作流模式|VARCHAR|是|60|||
|GENERATION_MODE|生成模式|VARCHAR|是|60|||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|IS_DEFAULT|是否默认Agent|INT|是||||
|KBS|引用知识库|VARCHAR|是|4000|||
|KB_MODE|知识库模式|VARCHAR|是|60|||
|MAX_INPUT_TOKENS|最大输入token数|INT|是||||
|MEMORY_DOC_TAG|记忆存储文档标记|VARCHAR|是|200|||
|MEMORY_ISOLATION_MODE|记忆隔离模式|VARCHAR|是|60|||
|MEMORY_KB_TAG|记忆存储知识库标记|VARCHAR|是|200|||
|MEMORY_MAX_TURNS|记忆对话轮数|INT|是||||
|MEMORY_MODE|记忆模式|VARCHAR|是|60|||
|NAME|名称|VARCHAR|是|200|||
|PAGE_INDEX|启用增强目录召回|INT|是||||
|PUBLISH_SKILL|发布技能|INT|是||||
|RERANK|召回重排|INT|是||||
|RERANK_MODEL|召回重排模型|VARCHAR|是|100|||
|RERANK_MODEL_ID|模型标识|VARCHAR|是|100|||
|SCOPES|业务范围|VARCHAR|是|500|||
|SEQUENCE|排序|INT|是||||
|SIMILARITY_THRESHOLD|召回相似度阈值|DECIMAL|是||2||
|SKILL_LOAD_MODE|技能加载模式|VARCHAR|是|60|||
|SKILL_PROMPT|技能提示词|TEXT|是|1048576|||
|SKILL_README|技能说明|TEXT|是|1048576|||
|SKILL_TAGS|激活技能标记|TEXT|是|1048576|||
|SPEC_KB_ID|规格库标识|VARCHAR|是|100|||
|STREAM|流式输出|INT|是||||
|SUGGESTED_QUESTIONS|预置建议问题|TEXT|是|1000|||
|SYNTHESIZER|总结智能体|VARCHAR|是|100|||
|SYSTEM_FLAG|系统标记|INT|是||||
|TEMPERATURE|模型随机性参数|DECIMAL|是||2||
|TOOLS|引用工具|VARCHAR|是|4000|||
|TOOL_EXCEED_MESSAGE|工具调用超限提示语|TEXT|是|1048576|||
|TOOL_MAX_CALLS|最大工具调用次数|INT|是||||
|TOP_K|最大召回数量|INT|是||||
|TOP_P|概率核采样|DECIMAL|是||2||
|TRIMMING_STRATEGY|截断策略|VARCHAR|是|60|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
|USE_FULLTEXT|使用全文推理|INT|是||||
|USE_KG|使用知识图谱|INT|是||||
|VECTOR_SIMILARITY_WEIGHT|向量相似度权重|DECIMAL|是||1||
|VLM_PROMPT|视觉识别提示词|TEXT|是|1048576|||
|WELCOME_MESSAGE|欢迎消息模板|TEXT|是|1048576|||
#### 智能体会话(AI_AGENT_CONVERSATION)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|AI_AGENT_CONTEXT_ID|智能体业务上下文标识|VARCHAR|是|100|||
|AI_AGENT_ID|智能体标识|VARCHAR|是|100|||
|CREATE_MAN|建立人|VARCHAR|是|100|||
|CREATE_TIME|建立时间|DATETIME|是||||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|IS_TOP|置顶|INT|是||||
|NAME|名称|VARCHAR|是|200|||
|SCOPE|业务范围|VARCHAR|是|200|||
|SEQUENCE|序号|BIGINT|是||||
|SESSION_ID|外部会话ID|VARCHAR|是|200|||
|STATUS|会话状态|VARCHAR|是|60|||
|TITLE|会话标题|VARCHAR|是|200|||
|TYPE|会话类型|VARCHAR|是|60|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
|USER_ID|用户ID|VARCHAR|是|100|||
#### 智能体回复反馈(AI_AGENT_FEEDBACK)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CONVERSATION_ID|会话标识|VARCHAR|是|100|||
|CREATE_MAN|创建人|VARCHAR|是|100|||
|CREATE_TIME|创建时间|DATETIME|是||||
|ENABLE|逻辑有效标识|INT|是||||
|FEEDBACK_CONTENT|反馈内容|VARCHAR|是|2000|||
|FEEDBACK_TYPE|反馈类型|VARCHAR|是|60|||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|MESSAGE_ID|消息标识|VARCHAR|是|100|||
|NAME|名称|VARCHAR|是|200|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
|USER_ID|用户标识|VARCHAR|是|100|||
#### 智能体知识库引用(AI_AGENT_KNOWLEDGE_REL)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|AI_AGENT_ID|智能体标识|VARCHAR|是|100|||
|AI_KNOWLEDGE_BASE_ID|知识库标识|VARCHAR|是|100|||
|CONTEXT_ID|智能体标识|VARCHAR|是|100|||
|CREATE_MAN|建立人|VARCHAR|是|100|||
|CREATE_TIME|建立时间|DATETIME|是||||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|NAME|名称|VARCHAR|是|200|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
#### 智能体记忆任务实例(AI_AGENT_MEMORY_TASK)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CONVERSATION_ID|会话标识|VARCHAR|是|100|||
|CONVERSATION_SNAPSHOT|会话快照|TEXT|是|16777215|||
|CREATE_MAN|创建人|VARCHAR|是|100|||
|CREATE_TIME|创建时间|DATETIME|是||||
|DOC_ID|记忆存储文档标识|VARCHAR|是|100|||
|DOC_PATH|记忆文档路径|VARCHAR|是|2000|||
|ENABLE|逻辑有效标识|INT|是||||
|END_AT|结束时间|DATETIME|是||||
|EXECUTED_AT|执行时间|DATETIME|是||||
|EXTRACTED_CONTENT|提取内容|TEXT|是|16777215|||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|KB_TAG|记忆库标识|VARCHAR|是|100|||
|LAST_MSG_TIME|最后消息时间|DATETIME|是||||
|MEMORY_ISOLATION_MODE|记忆隔离模式|VARCHAR|是|60|||
|NAME|名称|VARCHAR|是|200|||
|RESULT|执行结果|TEXT|是|16777215|||
|SCHEDULED_AT|计划执行时间|DATETIME|是||||
|STATUS|属性|VARCHAR|是|60|||
|TRIGGER_TYPE|触发类型|VARCHAR|是|60|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_STRATEGY|更新策略|TEXT|是|16777215|||
|UPDATE_TIME|更新时间|DATETIME|是||||
#### 智能体会话消息(AI_AGENT_MESSAGE)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CONTENT|消息内容|TEXT|是|1048576|||
|CONTENT_TYPE|内容类型|VARCHAR|是|100|||
|CONVERSATION_ID|会话标识|VARCHAR|是|100|||
|CREATE_MAN|创建人|VARCHAR|是|100|||
|CREATE_TIME|创建时间|DATETIME|是||||
|ENABLE|逻辑有效标识|INT|是||||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|METADATA|消息元数据|TEXT|是|1048576|||
|NAME|名称|VARCHAR|是|200|||
|SENDER_TYPE|发送者类型|VARCHAR|是|60|||
|SEQUENCE|消息序号|BIGINT|是||||
|STATUS|消息状态|VARCHAR|是|60|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
#### 智能体工具引用(AI_AGENT_TOOL_REL)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|AI_AGENT_ID|智能体标识|VARCHAR|是|100|||
|AI_TOOL_ID|AI调用工具标识|VARCHAR|是|100|||
|CONTEXT_ID|智能体标识|VARCHAR|是|100|||
|CREATE_MAN|建立人|VARCHAR|是|100|||
|CREATE_TIME|建立时间|DATETIME|是||||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|NAME|名称|VARCHAR|是|200|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
#### AI客户端凭证(AI_CLIENT_CREDENTIAL)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|ACCESS_KEY|访问密钥|TEXT|是|1048576|||
|ACCESS_STRATEGY|访问策略|VARCHAR|是|60|||
|ACCESS_TYPES|访问类型|VARCHAR|是|2000|||
|ACTIVE|启用凭证|INT|是||||
|CREATE_MAN|创建人|VARCHAR|是|100|||
|CREATE_TIME|创建时间|DATETIME|是||||
|DESCRIPTION|用途说明|VARCHAR|是|2000|||
|EXPIRATION_DATE|过期时间|DATETIME|是||||
|EXPIRES_TIME|过期时间|DATETIME|是||||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|NAME|名称|VARCHAR|是|200|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
|USER_ID|用户标识|VARCHAR|是|100|||
#### AI凭证(AI_CREDENTIAL)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|ACCESS_KEY|访问密钥|TEXT|是|1048576|||
|ACTIVE|是否启用|INT|是||||
|API_KEY|api密钥|VARCHAR|是|200|||
|BEARER_TOKEN|Bearer令牌|TEXT|是|1048576|||
|CLIENT_ID|客户端ID|VARCHAR|是|200|||
|CLIENT_SECRET|客户端密钥|TEXT|是|1048576|||
|CODE_NAME|代码标识|VARCHAR|是|100|||
|CREATE_MAN|建立人|VARCHAR|是|100|||
|CREATE_TIME|建立时间|DATETIME|是||||
|CREDENTIAL_TYPE|凭证类型|VARCHAR|是|200|||
|DESCRIPTION|用途说明|VARCHAR|是|2000|||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|NAME|名称|VARCHAR|是|200|||
|PROVIDER|模型提供商|VARCHAR|是|200|||
|REGION|区域|VARCHAR|是|100|||
|SCOPE|权限范围|VARCHAR|是|100|||
|SECRET_KEY|安全密钥|TEXT|是|1048576|||
|TOKEN_URL|令牌地址|VARCHAR|是|2000|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
#### 知识库文档分块(AI_KB_CHUNK)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|ACTIVE|是否启用|INT|是||||
|CHUNK_TYPE|分块类型|VARCHAR|是|60|||
|CONTENT|块内容|TEXT|是|1048576|||
|CONTENT_FTS_VECTOR|内容全文检索向量|TSVECTOR|是||||
|CONTENT_PREVIEW|块内容（预览）|VARCHAR|是|100|||
|CONTENT_VECTOR|块内容向量|VECTOR|是|1024|||
|CREATE_MAN|建立人|VARCHAR|是|100|||
|CREATE_TIME|建立时间|DATETIME|是||||
|DOCUMENT_ID|知识库文档标识|VARCHAR|是|100|||
|DOCUMENT_TYPE|文档类型|VARCHAR|是|100|||
|ID<i class="fa fa-key"></i>|分块标识|VARCHAR|否|100|||
|KEYWORDS|关键词|VARCHAR|是|4000|||
|KEY_QUESTIONS|关键问题|VARCHAR|是|4000|||
|KEY_QUESTIONS_VECTOR|关键问题向量|VECTOR|是|1024|||
|META_DATA|元数据|VARCHAR|是|4000|||
|NAME|分块名称|VARCHAR|是|200|||
|PATH|分块路径|VARCHAR|是|2000|||
|PID|父分块标识|VARCHAR|是|100|||
|POSITIONS|文档位置|VARCHAR|是|1000|||
|SEQUENCE|文档索引顺序|INT|是||||
|SOURCE_COUNT|源分块计数|INT|是||||
|SOURCE_INDICES|源分块索引|TEXT|是|1048576|||
|TAGS|标签|VARCHAR|是|2000|||
|TYPE|分块类型|VARCHAR|是|60|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
|USER_TAG|用户标记|VARCHAR|是|200|||
|USER_TAG2|用户标记2|VARCHAR|是|200|||
#### 知识库文档切片策略(AI_KB_CHUNKING_STRATEGY)
#### 知识库文档(AI_KB_DOCUMENT)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|ACTIVE|是否启用|INT|是||||
|CATEGORIES|目录|VARCHAR|是|1000|||
|CHUNK_METHOD|切片方法|VARCHAR|是|100|||
|CHUNK_NUM|切片数量|DECIMAL|是||||
|CONTENT|内容|TEXT|是|1048576|||
|CREATE_MAN|建立人|VARCHAR|是|100|||
|CREATE_TIME|建立时间|DATETIME|是||||
|CUSTOM_CHUNK|自定义切片|INT|是||||
|DIGEST_CODE|摘要代码|VARCHAR|是|64|||
|FILE|上传文件|VARCHAR|是|500|||
|FILE_TYPE|文件类型|VARCHAR|是|100|||
|ID<i class="fa fa-key"></i>|知识库文档标识|VARCHAR|否|100|||
|KB_ID|知识库标识|VARCHAR|是|100|||
|KEY|业务主键|VARCHAR|是|100|||
|META_DATA|文档元数据|TEXT|是|1048576|||
|NAME|知识库文档名称|VARCHAR|是|200|||
|PARSED_CONTENT|解析内容|TEXT|是|1048576|||
|PARSER_CONFIG|解析配置|TEXT|是|1048576|||
|PARSE_ERROR|错误信息|TEXT|是|1048576|||
|RESOURCE|资源|VARCHAR|是|200|||
|SEQUENCE|序号|DECIMAL|是||||
|SIZE|内容大小|DECIMAL|是||||
|SOURCE_ID|源标识|VARCHAR|是|200|||
|SOURCE_TYPE|源类型|VARCHAR|是|60|||
|STATUS|状态|VARCHAR|是|60|||
|SYNC_FREQUENCY|同步频率|VARCHAR|是|60|||
|SYNC_ID|文档同步标识|VARCHAR|是|100|||
|TYPE|文档类型|VARCHAR|是|60|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
|USER_TAG|用户标记|VARCHAR|是|200|||
|USER_TAG2|用户标记2|VARCHAR|是|200|||
#### 知识库文档同步(AI_KB_DOCUMENT_SYNC)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|AI_KNOWLEDGE_BASE_ID|知识库标识|VARCHAR|是|100|||
|CREATE_MAN|创建人|VARCHAR|是|100|||
|CREATE_TIME|创建时间|DATETIME|是||||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|NAME|名称|VARCHAR|是|200|||
|SOURCE_ID|源标识|VARCHAR|是|200|||
|SOURCE_TYPE|源类型|VARCHAR|是|60|||
|SYNC_FREQUENCY|同步频率|VARCHAR|是|60|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
#### 知识库图谱实体(AI_KB_GRAPH_ENTITY)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CONFIDENCE|置信度|DECIMAL|是||2||
|CONTEXT|上下文|VARCHAR|是|1000|||
|CONTEXT_VECTOR|上下文向量|VECTOR|是|1024|||
|CREATE_MAN|创建人|VARCHAR|是|100|||
|CREATE_TIME|创建时间|DATETIME|是||||
|DESCRIPTION|描述|VARCHAR|是|2000|||
|DESCRIPTION_VECTOR|描述向量|VECTOR|是|1024|||
|DOCUMENT_ID|知识库文档标识|VARCHAR|是|100|||
|ID<i class="fa fa-key"></i>|实体标识|VARCHAR|否|100|||
|KB_ID|知识库标识|VARCHAR|是|100|||
|KEYWORDS|关键词|VARCHAR|是|1000|||
|NAME|名称|VARCHAR|是|500|||
|NORMALIZED_NAME|规范名称|VARCHAR|是|500|||
|REFERENCE_TYPE|引用类型|VARCHAR|是|30|||
|TYPE|类型|VARCHAR|是|100|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
#### 知识库图谱实体文档分块(AI_KB_GRAPH_ENTITY_CHUNK)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CHUNK_ID|分块标识|VARCHAR|是|100|||
|CREATE_MAN|创建人|VARCHAR|是|100|||
|CREATE_TIME|创建时间|DATETIME|是||||
|ENTITY_ID|实体标识|VARCHAR|是|100|||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|NAME|名称|VARCHAR|是|200|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
#### 知识库图谱实体类型(AI_KB_GRAPH_ENTITY_TYPE)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CREATE_MAN|创建人|VARCHAR|是|100|||
|CREATE_TIME|创建时间|DATETIME|是||||
|DESCRIPTION|描述|VARCHAR|是|2000|||
|ENABLE|逻辑有效标识|INT|是||||
|ICON|显示图标|VARCHAR|是|500|||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|NAME|名称|VARCHAR|是|200|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
|VALUE|类型值|VARCHAR|是|100|||
#### 知识库图谱关系(AI_KB_GRAPH_RELATION)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|ACTIVE|是否启用|INT|是||||
|CONFIDENCE|置信度|DECIMAL|是||2||
|CREATE_MAN|创建人|VARCHAR|是|100|||
|CREATE_TIME|创建时间|DATETIME|是||||
|DESCRIPTION|描述|VARCHAR|是|2000|||
|DESCRIPTION_VECTOR|描述向量|VECTOR|是|1024|||
|ID<i class="fa fa-key"></i>|关系标识|VARCHAR|否|100|||
|KB_ID|知识库标识|VARCHAR|是|100|||
|NAME|关系名称|VARCHAR|是|500|||
|OBJECT_ID|客体标识|VARCHAR|是|100|||
|PREDICATE|关系谓词|VARCHAR|是|200|||
|SUBJECT_ID|主体标识|VARCHAR|是|100|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
#### 知识库图谱关系文档分块(AI_KB_GRAPH_RELATION_CHUNK)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CHUNK_ID|分块标识|VARCHAR|是|100|||
|CREATE_MAN|创建人|VARCHAR|是|100|||
|CREATE_TIME|创建时间|DATETIME|是||||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|NAME|名称|VARCHAR|是|200|||
|RELATION_ID|关系标识|VARCHAR|是|100|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
#### 知识库成员(AI_KB_MEMBER)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|ACTIVE|是否启用|INT|是||||
|CREATE_MAN|创建人|VARCHAR|是|100|||
|CREATE_TIME|创建时间|DATETIME|是||||
|ENABLE|逻辑有效标识|INT|是||||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|KB_ID|知识库标识|VARCHAR|是|100|||
|NAME|名称|VARCHAR|是|200|||
|ROLE_ID|角色|VARCHAR|是|60|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
|USER_ID|标识|VARCHAR|是|100|||
#### 知识库检索记录(AI_KB_SEARCH_QUERY)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CREATE_MAN|创建人|VARCHAR|是|100|||
|CREATE_TIME|创建时间|DATETIME|是||||
|EMBEDDING|查询向量|VECTOR|是||||
|FEEDBACK|用户反馈信息|VARCHAR|是|2000|||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|IS_ANSWERED|有效回答|INT|是||||
|IS_KNOWLEDGE_GAP|知识缺口|INT|是||||
|NAME|名称|VARCHAR|是|200|||
|NORMALIZED_QUERY|标准化问题|VARCHAR|是|100|||
|RAW_QUERY|原始问题|TEXT|是|1048576|||
|RETRIEVAL_CONFIG|召回配置|TEXT|是|1048576|||
|SOURCE|来源|VARCHAR|是|60|||
|SOURCE_METADATA|来源元数据|TEXT|是|1048576|||
|TAGS|检索标签|VARCHAR|是|2000|||
|TOTAL_DURATION|总耗时|DECIMAL|是||||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
|USER_ID|用户标识|VARCHAR|是|100|||
|USER_SATISFACTION|满意度评分|INT|是||||
#### 知识库检索结果(AI_KB_SEARCH_RESULT)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CHUNK_SNAPSHOTS|分块快照集合|TEXT|是|1048576|||
|CREATE_MAN|创建人|VARCHAR|是|100|||
|CREATE_TIME|创建时间|DATETIME|是||||
|DOCUMENT_ID|文档标识|VARCHAR|是|100|||
|HIT_CONTENT|命中内容快照|TEXT|是|1048576|||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|KB_ID|知识库标识|VARCHAR|是|100|||
|MERGED_CONTENT|合并内容快照|TEXT|是|1048576|||
|NAME|名称|VARCHAR|是|200|||
|QUERY_ID|标识|VARCHAR|是|100|||
|RANK|结果排序|INT|是||||
|RETRIEVAL_MODE|召回模式|VARCHAR|是|100|||
|SIMILARITY|相似度得分|DECIMAL|是||||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
#### 知识库标签(AI_KB_TAG)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CREATE_MAN|创建人|VARCHAR|是|100|||
|CREATE_TIME|创建时间|DATETIME|是||||
|DESCRIPTION|描述|VARCHAR|是|2000|||
|ENABLE|逻辑有效标识|INT|是||||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|NAME|名称|VARCHAR|是|200|||
|SET_ID|标签集标识|VARCHAR|是|100|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
|VALUE|标签值|VARCHAR|是|100|||
#### 知识库标签集(AI_KB_TAG_SET)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CREATE_MAN|创建人|VARCHAR|是|100|||
|CREATE_TIME|创建时间|DATETIME|是||||
|DESCRIPTION|描述|VARCHAR|是|2000|||
|ENABLE|逻辑有效标识|INT|是||||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|NAME|展示名称|VARCHAR|是|200|||
|OWNER_ID|范围所属标识|VARCHAR|是|100|||
|SCOPE|范围|VARCHAR|是|60|||
|SOURCE_ID|源标识|VARCHAR|是|100|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
#### 知识库(AI_KNOWLEDGE_BASE)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CATEGORY_ID|标识|VARCHAR|是|100|||
|CATEGORY_NAME|目录|VARCHAR|是|200|||
|CHAT_MODEL|交谈模型|VARCHAR|是|100|||
|CHAT_MODEL_ID|交谈模型标识|VARCHAR|是|100|||
|CHUNK_METHOD|切片方法|VARCHAR|是|100|||
|CODE_NAME|代码标识|VARCHAR|是|200|||
|CREATE_MAN|建立人|VARCHAR|是|100|||
|CREATE_TIME|建立时间|DATETIME|是||||
|DESCRIPTION|描述|VARCHAR|是|2000|||
|DESCRIPTION_VECTOR|描述向量|VECTOR|是|1024|||
|EMBEDDING_MODEL|embedding模型|VARCHAR|是|100|||
|EMBEDDING_MODEL_ID|模型标识|VARCHAR|是|100|||
|GUIDANCE_PROMPT|引导提示词|VARCHAR|是|2000|||
|GUIDANCE_PROMPT_VECTOR|引导词向量|VECTOR|是|1024|||
|ID<i class="fa fa-key"></i>|知识库标识|VARCHAR|否|100|||
|IS_ARCHIVED|是否已归档|INT|是||||
|IS_DELETED|是否已删除|INT|是||||
|KEY|业务键值|VARCHAR|是|100|||
|META_DATA|文档元数据|TEXT|是|1048576|||
|NAME|知识库名称|VARCHAR|是|200|||
|PAGEINDEX|智能目录索引|INT|是||||
|PARSER_CONFIG|解析配置|TEXT|是|1048576|||
|RECORD_ID|标识|VARCHAR|是|60|||
|RERANK|召回重排|INT|是||||
|RERANK_MODEL|召回重排模型|VARCHAR|是|100|||
|RERANK_MODEL_ID|模型标识|VARCHAR|是|100|||
|RESOURCE|数据资源|VARCHAR|是|200|||
|RESOURCE_CODE|数据资源|VARCHAR|是|100|||
|RESOURCE_ID|标识|VARCHAR|是|100|||
|SCOPE_ID|所属对象|VARCHAR|是|100|||
|SCOPE_TYPE|所属|VARCHAR|是|60|||
|SIMILARITY_THRESHOLD|召回相似度阈值|DECIMAL|是||2||
|SOURCE_ID|知识库源标识|VARCHAR|是|100|||
|SOURCE_NAME|知识库源名称|VARCHAR|是|200|||
|SOURCE_TYPE|资源类型|VARCHAR|是|2000|||
|STATUS|状态|VARCHAR|是|60|||
|TAG_SETS|标签集|VARCHAR|是|2000|||
|TOP_K|最大召回数量|INT|是||||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
|USE_KG|使用知识图谱|INT|是||||
|VECTOR_SIMILARITY_WEIGHT|向量相似度权重|DECIMAL|是||1||
|VISIBILITY|可见范围|VARCHAR|是|60|||
#### 知识库源(AI_KNOWLEDGE_SOURCE)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|ACTIVE|是否启用|INT|是||||
|API_KEY|API密钥|TEXT|是|1048576|||
|BASE_URL|接口URL|VARCHAR|是|500|||
|CONFIG|配置|TEXT|是|1048576|||
|CREATE_MAN|建立人|VARCHAR|是|100|||
|CREATE_TIME|建立时间|DATETIME|是||||
|ID<i class="fa fa-key"></i>|知识库源标识|VARCHAR|否|100|||
|LAST_SYNC_TIME|最后同步时间|DATETIME|是||||
|NAME|知识库源名称|VARCHAR|是|200|||
|PASSWORD|密码|VARCHAR|是|200|||
|TYPE|源类型|VARCHAR|是|60|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
|USER_NAME|用户名|VARCHAR|是|200|||
#### AI大模型(AI_MODEL)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|ACTIVE|是否启用该模型|INT|是||||
|AI_CREDENTIAL_ID|AI凭证标识|VARCHAR|是|100|||
|API_BASE_URL|模型 API 地址|VARCHAR|是|255|||
|CODE_NAME|代码标识|VARCHAR|是|100|||
|CREATE_MAN|建立人|VARCHAR|是|100|||
|CREATE_TIME|建立时间|DATETIME|是||||
|DESC_OSS_IMAGE|多模态图片解析|INT|是||||
|EXTRA_PARAMS|模型额外参数|TEXT|是|1048576|||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|MAX_CONTEXT_TOKENS|最大上下文长度（token）|INT|是||||
|MAX_OUTPUT_TOKENS|最大输出长度|INT|是||||
|MODEL_CAPABILITY|模型能力|VARCHAR|是|2000|||
|MODEL_CATEGORY|模型类别|VARCHAR|是|60|||
|NAME|名称|VARCHAR|是|200|||
|OSS_IMAGE_VL_PROMPT|图片文件解析提示词|TEXT|是|1048576|||
|PROVIDER|模型提供商|VARCHAR|是|60|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
#### 模型提供商(AI_MODEL_PROVIDER)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|BASE_URL|API 地址|VARCHAR|是|300|||
|DEFAULT_TOKEN|API 密钥|VARCHAR|是|1000|||
|DEFAULT_VERSION|默认版本号后缀|VARCHAR|是|100|||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|NAME|名称|VARCHAR|是|200|||
|UPDATE_TIME|更新时间|DATETIME|是||||
#### 智能审查报告(AI_REVIEW_REPORT)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|AGENT_TAG|智能体标记|VARCHAR|是|200|||
|CHECK_INFO|校验信息|TEXT|是|1048576|||
|CREATE_MAN|创建人|VARCHAR|是|100|||
|CREATE_TIME|创建时间|DATETIME|是||||
|DOCUMENT_ID|知识库文档标识|VARCHAR|是|100|||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|KB_ID|知识库标识|VARCHAR|是|100|||
|NAME|审查事项|VARCHAR|是|200|||
|RECORD_ID|记录标识|VARCHAR|是|60|||
|REVIEW_REPORT|报告|TEXT|是|1048576|||
|REVIEW_RESULT|审查结果|VARCHAR|是|2000|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
#### AI调用工具(AI_TOOL)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|ACCESS_KEY|访问密钥|TEXT|是|1048576|||
|ACTIVE|启用|INT|是||||
|API_AUTH_TYPE|认证方式|VARCHAR|是|60|||
|API_HEADERS|请求头|VARCHAR|是|2000|||
|API_KEY|api密钥|VARCHAR|是|200|||
|API_METHOD|HTTP 方法|VARCHAR|是|60|||
|API_URL|接口地址|VARCHAR|是|500|||
|BEARER_TOKEN|Bearer令牌|TEXT|是|1048576|||
|CLIENT_ID|客户端ID|VARCHAR|是|200|||
|CLIENT_SECRET|客户端密钥|TEXT|是|1048576|||
|CREATE_MAN|建立人|VARCHAR|是|100|||
|CREATE_TIME|建立时间|DATETIME|是||||
|DESCRIPTION|描述|VARCHAR|是|2000|||
|EXPIRATION_DATE|过期时间|DATETIME|是||||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|INPUT_SCHEMA|输入参数 Schema|TEXT|是|1048576|||
|NAME|名称|VARCHAR|是|200|||
|SECRET_KEY|安全密钥|TEXT|是|1048576|||
|SKILL_PROMPT|技能提示词|TEXT|是|1048576|||
|SKILL_REFERENCES|技能引用资料|TEXT|是|16777215|||
|SKILL_SCRIPTS|技能脚本集合|TEXT|是|16777215|||
|TIMEOUT|超时时间|INT|是||||
|TOKEN_URL|令牌地址|VARCHAR|是|2000|||
|TOOL_TAG|工具标记|VARCHAR|是|200|||
|TOOL_TYPE|工具类型|VARCHAR|是|60|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
#### 附件(ATTACHMENT)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CREATE_MAN|建立人|VARCHAR|是|100|||
|CREATE_TIME|建立时间|DATETIME|是||||
|FILE_ID|文件标识|VARCHAR|是|500|||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|NAME|名称|VARCHAR|是|200|||
|OWNER_ID|所属数据标识|VARCHAR|是|100|||
|OWNER_SUBTYPE|所属对象子类型|VARCHAR|是|100|||
|OWNER_TYPE|所属数据对象|VARCHAR|是|100|||
|PARENT_VERSION_ID|父对象版本标识|VARCHAR|是|100|||
|TITLE|标题|VARCHAR|是|100|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
#### 关注(ATTENTION)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CREATE_MAN|建立人|VARCHAR|是|100|||
|CREATE_TIME|建立时间|DATETIME|是||||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|NAME|名称|VARCHAR|是|200|||
|OWNER_ID|所属数据标识|VARCHAR|是|100|||
|OWNER_SUBTYPE|所属对象子类型|VARCHAR|是|100|||
|OWNER_TYPE|所属数据对象|VARCHAR|是|100|||
|TITLE|职位|VARCHAR|是|100|||
|TYPE|关注类型|VARCHAR|是|60|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
|USER_ID|关注人|VARCHAR|是|100|||
#### 类别(CATEGORY)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CATEGORIES|类别路径|VARCHAR|是|2000|||
|CREATE_MAN|建立人|VARCHAR|是|100|||
|CREATE_TIME|建立时间|DATETIME|是||||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|IS_DELETED|是否删除|INT|是||||
|IS_LEAF|是否叶子节点|INT|是||||
|IS_LEAF2|是否叶子节点2|INT|是||||
|IS_LEAF3|是否叶子节点3|INT|是||||
|IS_LEAF4|是否叶子节点4|INT|是||||
|NAME|名称|VARCHAR|是|200|||
|OWNER_ID|所属数据标识|VARCHAR|是|100|||
|OWNER_SUBTYPE|所属对象子类型|VARCHAR|是|100|||
|OWNER_TYPE|所属数据对象|VARCHAR|是|100|||
|PARSER_CONFIG|解析配置|TEXT|是|1048576|||
|PID|父标识|VARCHAR|是|100|||
|SECTION_ID|分组标识|VARCHAR|是|100|||
|SEQUENCE|序号|DECIMAL|是||||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
|USER_TAG|用户标记|VARCHAR|是|200|||
|USER_TAG2|用户标记2|VARCHAR|是|200|||
|WF_VERSION_ID|工作流版本|VARCHAR|是|100|||
#### 类别设置(CATEGORY_SETTINGS)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|AUTO_GEN_KB|自动创建资源知识库|VARCHAR|是|200|||
|CHAT_MODEL|交谈模型|VARCHAR|是|100|||
|CHAT_MODEL_ID|交谈模型标识|VARCHAR|是|100|||
|CHUNK_METHOD|切片方法|VARCHAR|是|100|||
|CONFIGS|configs|TEXT|是|1048576|||
|CREATE_MAN|创建人|VARCHAR|是|100|||
|CREATE_TIME|创建时间|DATETIME|是||||
|EMBEDDING_MODEL|embedding模型|VARCHAR|是|100|||
|EMBEDDING_MODEL_ID|嵌入模型标识|VARCHAR|是|100|||
|ENABLE|逻辑有效标识|INT|是||||
|FLASH_MODEL|交谈模型|VARCHAR|是|100|||
|FLASH_MODEL_ID|交谈模型标识|VARCHAR|是|100|||
|GUIDED_PROMPT_AGENT_ID|引导提示词智能体标识|VARCHAR|是|100|||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|INTENT_MODEL_ID|模型标识|VARCHAR|是|100|||
|NAME|名称|VARCHAR|是|200|||
|PARSER_CONFIG|解析配置|TEXT|是|1048576|||
|RERANK|召回重排|INT|是||||
|RERANK_MODEL|召回重排模型|VARCHAR|是|100|||
|RERANK_MODEL_ID|召回重排模型标识|VARCHAR|是|100|||
|RESOURCE_ID|标识|VARCHAR|是|100|||
|SIMILARITY_THRESHOLD|召回相似度阈值|DECIMAL|是||2||
|SOURCE_ID|知识库源标识|VARCHAR|是|100|||
|SOURCE_NAME|知识库源名称|VARCHAR|是|200|||
|TOP_K|最大召回数量|INT|是||||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
|USE_KG|使用知识图谱|INT|是||||
|VECTOR_SIMILARITY_WEIGHT|向量相似度权重|DECIMAL|是||1||
|VISIBILITY|可见范围|VARCHAR|是|60|||
|VL_MODEL|多模态模型|VARCHAR|是|100|||
|VL_MODEL_ID|多模态模型标识|VARCHAR|是|100|||
#### 评论(COMMENT)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CONTENT|内容|TEXT|是|1048576|||
|CREATE_MAN|建立人|VARCHAR|是|100|||
|CREATE_TIME|建立时间|DATETIME|是||||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|IS_TOP|是否置顶|INT|是||||
|NAME|名称|VARCHAR|是|200|||
|OWNER_TYPE|所属数据对象|VARCHAR|是|100|||
|PID|父标识|VARCHAR|是|100|||
|PRINCIPAL_ID|评论主体标识|VARCHAR|是|100|||
|PRINCIPAL_NAME|评论主体名称|VARCHAR|是|100|||
|PRINCIPAL_TYPE|评论主体类型|VARCHAR|是|100|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
#### 通用规则(COMMON_FLOW)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CREATE_MAN|创建人|VARCHAR|是|100|||
|CREATE_TIME|创建时间|DATETIME|是||||
|ENABLE|逻辑有效标识|INT|是||||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|NAME|名称|VARCHAR|是|200|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
#### 数据记录(DATA_RECORD)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|_CREATE_TIME|创建时间|DATETIME|是||||
|_CREATOR|创建人|VARCHAR|是|100|||
|_ENABLED|逻辑有效标记|INT|是||||
|_ID<i class="fa fa-key"></i>|标识|VARCHAR|否|60|||
|_KEY|编号|VARCHAR|是|100|||
|_METADATA|Metadata|TEXT|是|1048576|||
|_NER_FLAG|NER标记|INT|是||||
|_OWNER|所有者|TEXT|是|1000|||
|_REGION|区域标识|VARCHAR|是|100|||
|_RESOURCE_ID|资源标识|VARCHAR|是|100|||
|_SCHEMA|格式定义|VARCHAR|是|100|||
|_SUMMARY|摘要|TEXT|是|1048576|||
|_TITLE|标题|VARCHAR|是|1000|||
|_UPDATER|最后更新人|VARCHAR|是|100|||
|_UPDATE_TIME|最后更新时间|DATETIME|是||||
#### 数据资源(DATA_RESOURCE)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CREATE_TIME|创建时间|DATETIME|是||||
|ENABLED|逻辑有效标记|INT|是||||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|NAME|名称|VARCHAR|是|200|||
|RESOURCE_CODE|资源代码|VARCHAR|是|100|||
|SCHEMA|格式定义|TEXT|是|1048576|||
|SORT|排序|BIGINT|是||||
|UPDATE_TIME|最后更新时间|DATETIME|是||||
#### 数据字典(DICTIONARY)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CATALOG|字典目录|VARCHAR|是|60|||
|COLOR|颜色|VARCHAR|是|100|||
|CREATE_MAN|建立人|VARCHAR|是|100|||
|CREATE_TIME|建立时间|DATETIME|是||||
|DESCRIPTION|描述|VARCHAR|是|2000|||
|ICON|图标|TEXT|是|100|||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|IS_SYSTEM|是否系统默认|INT|是||||
|NAME|名称|VARCHAR|是|200|||
|SEQUENCE|序号|DECIMAL|是||||
|STYLE|背景样式|VARCHAR|是|100|||
|TYPE|类型|VARCHAR|是|60|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
|VAL|值|VARCHAR|是|100|||
#### 动态数据看板(DYNADASHBOARD)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|APPID|应用标识|VARCHAR|是|100|||
|CREATEDATE|建立时间|DATETIME|是|8|||
|CREATEMAN|建立人|VARCHAR|是|60|||
|DESC|描述|TEXT|是|1048576|||
|DESCRIPTION|描述|TEXT|是|1048576|||
|DYNADASHBOARDID<i class="fa fa-key"></i>|动态数据看板标识|VARCHAR|否|200|||
|DYNADASHBOARDNAME|名称|VARCHAR|是|200|||
|EXAMPLE_CHART|示例图|TEXT|是|1048576|||
|IS_SYSTEM|是否系统类型|INT|是||||
|MODEL|模型|TEXT|是|1048576|||
|MODELID|模型标识|VARCHAR|是|100|||
|OWNER_ID|所属数据标识|VARCHAR|是|100|||
|OWNER_TYPE|所属数据类型|VARCHAR|是|100|||
|SEQUENCES|序号|DECIMAL|是||||
|TYPE|看板类型|VARCHAR|是|100|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
|USERID|用户标识|VARCHAR|是|100|||
#### 扩展日志(EXTEND_LOG)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CATEGORY|类别|VARCHAR|是|100|||
|CREATE_MAN|建立人|VARCHAR|是|100|||
|CREATE_TIME|建立时间|DATETIME|是||||
|DEBUG_INFO|调试日志信息|TEXT|是|1048576|||
|ELAPSED_TIME|持续时间|INT|是|11|||
|END_AT|结束时间|DATETIME|是||||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|INFO|日志信息|TEXT|是|1048576|||
|LEVEL|级别|VARCHAR|是|100|||
|NAME|名称|VARCHAR|是|200|||
|OWNER_ID|所属数据标识|VARCHAR|是|200|||
|OWNER_SUBTYPE|所属对象子类型|VARCHAR|是|100|||
|OWNER_TYPE|所属数据对象|VARCHAR|是|100|||
|START_AT|起始时间|DATETIME|是||||
|STATE|状态|VARCHAR|是|100|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
#### 扩展执行计划(EXTEND_SCHEDULE)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CREATE_MAN|创建人|VARCHAR|是|100|||
|CREATE_TIME|创建时间|DATETIME|是||||
|DESCRIPTION|描述|VARCHAR|是|2000|||
|ENABLE|逻辑有效标识|INT|是||||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|NAME|名称|VARCHAR|是|200|||
|NEXT_TRIGGER_TIME|下一次执行时间|DATETIME|是||||
|PAYLOAD|任务执行参数|TEXT|是|1048576|||
|PRINCIPAL_ID|任务主体标识|VARCHAR|是|100|||
|PRINCIPAL_NAME|任务主体名称|VARCHAR|是|100|||
|PRINCIPAL_TYPE|任务主体类型|VARCHAR|是|100|||
|SCHEDULE_TYPE|调度类型|VARCHAR|是|60|||
|TASK_TYPE|任务类型|VARCHAR|是|100|||
|TIMER_POLICY|定时器策略|VARCHAR|是|200|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
#### 扩展计划任务(EXTEND_SCHEDULED_TASK)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CREATE_MAN|创建人|VARCHAR|是|100|||
|CREATE_TIME|创建时间|DATETIME|是||||
|DESCRIPTION|描述|VARCHAR|是|2000|||
|ENABLE|逻辑有效标识|INT|是||||
|FINISHED_AT|执行完成时间|DATETIME|是||||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|MAX_RETRY|最大重试次数|INT|是||||
|NAME|名称|VARCHAR|是|200|||
|PAYLOAD|任务执行参数|TEXT|是|1048576|||
|PRINCIPAL_ID|任务主体标识|VARCHAR|是|100|||
|PRINCIPAL_NAME|任务主体名称|VARCHAR|是|100|||
|PRINCIPAL_TYPE|任务主体类型|VARCHAR|是|100|||
|RESULT|执行结果|TEXT|是|1048576|||
|RESULT_MESSAGE|执行信息|VARCHAR|是|2000|||
|RETRY_COUNT|已重试次数|INT|是||||
|SCHEDULED_AT|计划执行时间|DATETIME|是||||
|SCHEDULE_ID|执行计划标识|VARCHAR|是|100|||
|STARTED_AT|实际开始时间|DATETIME|是||||
|STATUS|任务状态|VARCHAR|是|60|||
|TASK_TYPE|任务类型标识|VARCHAR|是|60|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
#### 扩展计划任务历史(EXTEND_SCHEDULED_TASK_HIS)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CREATE_MAN|创建人|VARCHAR|是|100|||
|CREATE_TIME|创建时间|DATETIME|是||||
|DESCRIPTION|描述|VARCHAR|是|2000|||
|ENABLE|逻辑有效标识|INT|是||||
|FINISHED_AT|执行完成时间|DATETIME|是||||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|MAX_RETRY|最大重试次数|INT|是||||
|NAME|名称|VARCHAR|是|200|||
|PAYLOAD|任务执行参数|TEXT|是|1048576|||
|PRINCIPAL_ID|任务主体标识|VARCHAR|是|100|||
|PRINCIPAL_NAME|任务主体名称|VARCHAR|是|100|||
|PRINCIPAL_TYPE|任务主体类型|VARCHAR|是|100|||
|RESULT|执行结果|TEXT|是|1048576|||
|RESULT_MESSAGE|执行信息|VARCHAR|是|2000|||
|RETRY_COUNT|已重试次数|INT|是||||
|SCHEDULED_AT|计划执行时间|DATETIME|是||||
|STARTED_AT|实际开始时间|DATETIME|是||||
|STATUS|任务状态|VARCHAR|是|60|||
|TASK_TYPE|任务类型|VARCHAR|是|60|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
#### 扩展任务类型(EXTEND_TASK_TYPE)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CODE|执行代码|TEXT|是|1048576|||
|CREATE_MAN|创建人|VARCHAR|是|100|||
|CREATE_TIME|创建时间|DATETIME|是||||
|DESCRIPTION|详细说明|VARCHAR|是|2000|||
|EXECUTOR_CONFIG|执行器配置|TEXT|是|1048576|||
|EXECUTOR_SUBTYPE|执行器子类型|VARCHAR|是|60|||
|EXECUTOR_TAG|执行器标记|VARCHAR|是|200|||
|EXECUTOR_TYPE|执行器类型|VARCHAR|是|60|||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|MAX_RETRY|默认最大重试次数|INT|是||||
|NAME|名称|VARCHAR|是|200|||
|RETRYABLE|是否允许重试|INT|是||||
|TIMEOUT_SEC|任务超时时间（秒）|INT|是||||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
#### 收藏(FAVORITE)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CREATE_MAN|建立人|VARCHAR|是|100|||
|CREATE_TIME|建立时间|DATETIME|是||||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|NAME|名称|VARCHAR|是|200|||
|OWNER_ID|所属数据标识|VARCHAR|是|100|||
|OWNER_SUBTYPE|所属对象子类型|VARCHAR|是|100|||
|OWNER_TYPE|所属数据对象|VARCHAR|是|100|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
#### 效能报表(INSIGHT_REPORT)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|APP_TAG|应用标记|VARCHAR|是|100|||
|CATEGORIES|类别|VARCHAR|是|2000|||
|CATEGORY|组别|VARCHAR|是|60|||
|CHART_TYPE|图表类型|VARCHAR|是|60|||
|CREATE_MAN|建立人|VARCHAR|是|100|||
|CREATE_TIME|建立时间|DATETIME|是||||
|DESC|描述|TEXT|是|1048576|||
|DESCRIPTION|描述|TEXT|是|1048576|||
|GROUP|组别|VARCHAR|是|60|||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|IS_SYSTEM|是否系统类型|INT|是||||
|NAME|名称|VARCHAR|是|200|||
|TEMPLATE_MODEL|模板模型|TEXT|是|1048576|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
|VIEW_ID|视图标识|VARCHAR|是|100|||
#### 效能视图(INSIGHT_VIEW)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CREATE_MAN|建立人|VARCHAR|是|100|||
|CREATE_TIME|建立时间|DATETIME|是||||
|DESCRIPTION|描述|VARCHAR|是|2000|||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|IDENTIFIER|视图标识|VARCHAR|是|100|||
|IS_ARCHIVED|是否已归档|INT|是||||
|IS_DELETED|是否已删除|INT|是||||
|NAME|名称|VARCHAR|是|200|||
|SCOPE_ID|所属对象|VARCHAR|是|100|||
|SCOPE_TYPE|所属|VARCHAR|是|60|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
|VISIBILITY|可见范围|VARCHAR|是|60|||
#### 成员(MEMBER)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CREATE_MAN|建立人|VARCHAR|是|100|||
|CREATE_TIME|建立时间|DATETIME|是||||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|NAME|名称|VARCHAR|是|200|||
|OWNER_ID|所属数据标识|VARCHAR|是|100|||
|OWNER_SUBTYPE|所属对象子类型|VARCHAR|是|100|||
|OWNER_TYPE|所属数据对象|VARCHAR|是|100|||
|POSITION_ID|职位标识|VARCHAR|是|100|||
|ROLE_ID|角色|VARCHAR|是|60|||
|TITLE|职位|VARCHAR|是|100|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
|USER_ID|登录名|VARCHAR|是|100|||
#### 页面(PAGE)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|ACCESS_PASSWORD|访问密码|VARCHAR|是|100|||
|CATEGORIES|类别路径|VARCHAR|是|2000|||
|CONTENT|正文|TEXT|是|1048576|||
|CREATE_MAN|建立人|VARCHAR|是|100|||
|CREATE_TIME|建立时间|DATETIME|是||||
|CUR_VERSION_ID|当前版本标识|VARCHAR|是|100|||
|CUR_VERSION_NAME|当前版本名称|VARCHAR|是|100|||
|DATA|数据|TEXT|是|1048576|||
|EXPIRATION_DATE|共享有效期|DATETIME|是||||
|FORMAT_TYPE|正文格式|VARCHAR|是|60|||
|ICON|图标|VARCHAR|是|500|||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|IDENTIFIER|编号|VARCHAR|是|100|||
|IS_ARCHIVED|是否已归档|INT|是||||
|IS_DELETED|是否已删除|INT|是||||
|IS_LEAF|是否叶子节点|INT|是||||
|IS_LOCK|是否锁定|INT|是||||
|IS_PUBLISHED|是否发布|INT|是||||
|IS_SHARED|是否开启共享|VARCHAR|是|60|||
|IS_SHARED_SUBSET|是否同时共享子页面|VARCHAR|是|60|||
|NAME|名称|VARCHAR|是|200|||
|PARENT_ID|父页面标识|VARCHAR|是|100|||
|PUBLISHED|发布状态|INT|是||||
|PUBLISH_CONTENT|发布正文|TEXT|是|1048576|||
|PUBLISH_MAN|发布人|VARCHAR|是|100|||
|PUBLISH_NAME|发布主题|VARCHAR|是|200|||
|PUBLISH_TIME|发布时间|DATETIME|是||||
|REVIEW_RESULT_STATE|评审结果|VARCHAR|是|60|||
|SEQUENCE|序号|DECIMAL|是||||
|SHARED_BY|共享人|VARCHAR|是|100|||
|SHARED_TIME|共享时间|DATETIME|是||||
|SPACE_ID|空间标识|VARCHAR|是|100|||
|TYPE|类型|VARCHAR|是|60|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
|USER_TAG|用户标记|VARCHAR|是|200|||
|USER_TAG2|用户标记2|VARCHAR|是|200|||
#### 文件夹(PORTFOLIO)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|ASSIGNEE_ID|负责人标识|VARCHAR|是|100|||
|ASSIGNEE_NAME|负责人|VARCHAR|是|100|||
|CREATE_MAN|建立人|VARCHAR|是|100|||
|CREATE_TIME|建立时间|DATETIME|是||||
|DESCRIPTION|描述|VARCHAR|是|2000|||
|END_AT|结束时间|DATETIME|是||||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|IDENTIFIER|文件夹标识|VARCHAR|是|100|||
|IS_DELETED|是否已删除|INT|是||||
|NAME|名称|VARCHAR|是|200|||
|START_AT|开始时间|DATETIME|是||||
|STATE|状态|VARCHAR|是|60|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
#### 文件夹成员(PORTFOLIO_MEMBER)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CREATE_MAN|建立人|VARCHAR|是|100|||
|CREATE_TIME|建立时间|DATETIME|是||||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|NAME|名称|VARCHAR|是|200|||
|PORTFOLIO_ID|文件夹标识|VARCHAR|是|100|||
|ROLE_ID|角色|VARCHAR|是|60|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
|USER_ID|用户标识|VARCHAR|是|100|||
#### 职位(POSITION)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CATEGORY_ID|分组标识|VARCHAR|是|100|||
|CREATE_MAN|建立人|VARCHAR|是|100|||
|CREATE_TIME|建立时间|DATETIME|是||||
|ENABLE|逻辑有效标志|INT|是|8|||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|IS_LEAF|是否叶子节点|INT|是||||
|NAME|名称|VARCHAR|是|200|||
|SEQUENCE|序号|DECIMAL|是||||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
#### 最近访问(RECENT)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CREATE_MAN|建立人|VARCHAR|是|100|||
|CREATE_TIME|建立时间|DATETIME|是||||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|IDENTIFIER|编号|VARCHAR|是|100|||
|IS_DELETED|是否已删除|INT|是||||
|NAME|名称|VARCHAR|是|500|||
|OWNER_ID|所属数据标识|VARCHAR|是|100|||
|OWNER_SUBTYPE|所属对象子类型|VARCHAR|是|100|||
|OWNER_TYPE|所属数据对象|VARCHAR|是|100|||
|RECENT_PARENT|访问父类|VARCHAR|是|200|||
|RECENT_PARENT_IDENTIFIER|访问父类编号|VARCHAR|是|100|||
|RECENT_PARENT_NAME|访问父类名称|VARCHAR|是|100|||
|TYPE|访问类型|VARCHAR|是|100|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
#### 分组(SECTION)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CREATE_MAN|建立人|VARCHAR|是|100|||
|CREATE_TIME|建立时间|DATETIME|是||||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|IS_LEAF|是否叶子节点|INT|是||||
|IS_LEAF2|是否叶子节点2|INT|是||||
|NAME|名称|VARCHAR|是|200|||
|OWNER_ID|所属数据标识|VARCHAR|是|100|||
|OWNER_SUBTYPE|所属对象子类型|VARCHAR|是|100|||
|OWNER_TYPE|所属数据对象|VARCHAR|是|100|||
|SEQUENCE|序号|DECIMAL|是||||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
|USER_TAG|用户标记|VARCHAR|是|200|||
|USER_TAG2|用户标记2|VARCHAR|是|200|||
#### 序列(SEQUENCE_GENERATOR)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CREATE_MAN|建立人|VARCHAR|是|100|||
|CREATE_TIME|建立时间|DATETIME|是||||
|CURRENT_VALUE|当前值|BIGINT|是||||
|GROUP_TAG|分组标记|VARCHAR|是|200|||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|NAME|名称|VARCHAR|是|200|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
#### 空间(SPACE)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|ACCESS_PASSWORD|访问密码|VARCHAR|是|100|||
|CATEGORY_ID|分类|VARCHAR|是|100|||
|CREATE_MAN|建立人|VARCHAR|是|100|||
|CREATE_TIME|建立时间|DATETIME|是||||
|DESCRIPTION|描述|VARCHAR|是|2000|||
|EXPIRATION_DATE|共享链接有效期|DATETIME|是||||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|IDENTIFIER|空间标识|VARCHAR|是|100|||
|IS_ARCHIVED|是否已归档|INT|是||||
|IS_DELETED|是否已删除|INT|是||||
|IS_SHARED|是否开启共享|VARCHAR|是|60|||
|NAME|名称|VARCHAR|是|200|||
|SCOPE_ID|所属对象|VARCHAR|是|100|||
|SCOPE_TYPE|所属|VARCHAR|是|60|||
|SHARED_BY|共享人|VARCHAR|是|100|||
|SHARED_PAGES|共享页面标识|TEXT|是|1048576|||
|SHARED_TIME|共享时间|DATETIME|是||||
|SHOW_LOGO|共享展示图标|VARCHAR|是|100|||
|SHOW_TITLE|共享展示标题|VARCHAR|是|100|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
|USER_TAG|用户标记|VARCHAR|是|200|||
|USER_TAG2|用户标记2|VARCHAR|是|200|||
|VISIBILITY|可见范围|VARCHAR|是|60|||
#### 空间成员(SPACE_MEMBER)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CREATE_MAN|建立人|VARCHAR|是|100|||
|CREATE_TIME|建立时间|DATETIME|是||||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|NAME|名称|VARCHAR|是|200|||
|ROLE_ID|角色|VARCHAR|是|60|||
|SPACE_ID|空间标识|VARCHAR|是|100|||
|TITLE|职位|VARCHAR|是|100|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
|USER_ID|用户标识|VARCHAR|是|100|||
#### 页面模板(STENCIL)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CONTENT|正文|TEXT|是|1048576|||
|CREATE_MAN|建立人|VARCHAR|是|100|||
|CREATE_TIME|建立时间|DATETIME|是||||
|FORMAT_TYPE|正文格式|VARCHAR|是|60|||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|IS_GLOBAL|全局模板|INT|是||||
|NAME|名称|VARCHAR|是|200|||
|SPACE_ID|空间标识|VARCHAR|是|100|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
#### 团队(USER_GROUP)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|AVATAR|头像|VARCHAR|是|500|||
|CREATE_MAN|建立人|VARCHAR|是|100|||
|CREATE_TIME|建立时间|DATETIME|是||||
|DESCRIPTION|描述|VARCHAR|是|2000|||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|NAME|名称|VARCHAR|是|200|||
|SECTION_ID|分组标识|VARCHAR|是|100|||
|SEQUENCE|序号|DECIMAL|是||||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||
|VISIBILITY|可见范围|VARCHAR|是|60|||
#### 项目发布(VERSION)
|  列名col150 |  中文名col150 | 数据类型col150 |允许为空col100 |长度col100|精度col100 | 备注col500 |
| --------|------------ |   -------- | -------- | -------- | -------- |-------- |
|CREATE_MAN|建立人|VARCHAR|是|100|||
|CREATE_TIME|建立时间|DATETIME|是||||
|DATA|数据|TEXT|是|1048576|||
|DESCRIPTION|描述|VARCHAR|是|2000|||
|FILTER|过滤属性|VARCHAR|是|100|||
|ID<i class="fa fa-key"></i>|标识|VARCHAR|否|100|||
|IDENTIFIER|版本|DECIMAL|是||||
|IS_NAMED|是否命名|INT|是||||
|MANUAL|手动提交|INT|是||||
|NAME|名称|VARCHAR|是|200|||
|OWNER_ID|所属数据标识|VARCHAR|是|100|||
|OWNER_TYPE|所属数据对象|VARCHAR|是|100|||
|OWNER_VERSION_ID|所属对象版本标识|VARCHAR|是|100|||
|RESTORABLE|支持恢复|VARCHAR|是|100|||
|SUB_OWNER_ID|所属子数据标识|VARCHAR|是|100|||
|SUB_OWNER_TYPE|所属子数据对象|VARCHAR|是|100|||
|UPDATE_MAN|更新人|VARCHAR|是|100|||
|UPDATE_TIME|更新时间|DATETIME|是||||






