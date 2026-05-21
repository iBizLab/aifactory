# 服务插件 <!-- {docsify-ignore-all} -->

|  对象      |  实体  |  类型  | 插件  |备注|
|  --------  | ----- | -----    |-----    |----    |
|AI客户端凭证同步组件||PSSysUtilImpl|[AIClientCredentialDESyncUtilRuntime](#AIClientCredentialDESyncUtilRuntime)||
|AI凭证同步组件||PSSysUtilImpl|[CredentialDESyncUtilRuntime](#CredentialDESyncUtilRuntime)||
|AI模型同步组件||PSSysUtilImpl|[AIAgentDESyncUtilRuntime](#AIAgentDESyncUtilRuntime)||
|AI工具同步组件||PSSysUtilImpl|[AIToolDESyncUtilRuntime](#AIToolDESyncUtilRuntime)||
|KB同步组件||PSSysUtilImpl|[KBAgentDESyncUtilRuntimeEx](#KBAgentDESyncUtilRuntimeEx)||
|AI长期记忆组件||PSSysUtilImpl|[SysChatMemoryUtilRuntime](#SysChatMemoryUtilRuntime)||
|AI技能组件||PSSysUtilImpl|[SysChatSkillUtilRuntime](#SysChatSkillUtilRuntime)||
|知识库组件||PSSysUtilImpl|[SysKnowledgeBaseUtilRuntimeEx](#SysKnowledgeBaseUtilRuntimeEx)|知识库功能组件运行时|
|OpenAI服务组件||PSSysUtilImpl|[SysOpenAIServerUtilRuntime](#SysOpenAIServerUtilRuntime)||
|任务调度组件||PSSysUtilImpl|[DefaultSysDETaskUtilRuntime](#DefaultSysDETaskUtilRuntime)||
|加密转换器||PSSysTranslatorImpl|[SysEncryptTranslatorRuntimeEx](#SysEncryptTranslatorRuntimeEx)|可逆加密|
|@内容||PSSysTranslatorImpl|[SysAtContentTranslatorRuntime](#UsrSFPlugin0201416283)|评论@转换器|
|智能体业务上下文(AI_AGENT_CONTEXT)||PSDataEntityImpl|[AIAgentContextDERuntime](#AIAgentContextDERuntime)||
|记忆提取并存储(extract_and_store)|[智能体记忆任务实例(AI_AGENT_MEMORY_TASK)](module/ai/ai_agent_memory_task)|PSDEUserCustomActionImpl|[ExtractAndStoreDEActionRuntime](#ExtractAndStoreDEActionRuntime)||
|树表数据集合(tree)|[知识库文档分块(AI_KB_CHUNK)](module/ai/ai_kb_chunk)|PSDEDataSetImpl|[TreeGridDEDataSetRuntime](#UsrSFPlugin0407757309)|数据集合获取树表格层级数据|
|提取元数据(extract_meta_data)|[知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document)|PSDEUserCustomActionImpl|[ExtractMetaDataDEActionRuntime](#ExtractMetaDataDEActionRuntime)||
|AI知识库文档查询(ai_doc_query)|[知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document)|PSDEDataSetImpl|[AI知识库文档查询](#AIDocQueryListDataSetRuntime)||
|AI知识库目录查询(ai_docs_by_kb)|[知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base)|PSDEDataSetImpl|[AI知识库目录查询](#AIDocListByKBDataSetRuntime)||
|AI知识库清单查询(ai_kb_query)|[知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base)|PSDEDataSetImpl|[AI知识库清单查询](#AIKBQueryListDataSetRuntime)||
|with_record|[知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base)|PSDEDataSetImpl|[AI知识库查询(record)](#AIKBWithRecordDataSetRuntime)||
|技能代理数据(SKILL_PROXY)|[AI调用工具(AI_TOOL)](module/ai/ai_tool)|PSDEDataSetImpl|[AIChatSkillDEDataSetRuntime](#AIChatSkillDEDataSetRuntime)||
|数据记录(DATA_RECORD)||PSDataEntityImpl|[DataRecordDataEntityRuntime](#DataRecordDataEntityRuntime)|cn.ibizlab.user.plugin.groovy.dataentity.DataRecordDataEntityRuntime|
|空间页面(移动端)(normal_tree_page)|[页面(PAGE)](module/Wiki/article_page)|PSDEDataSetImpl|[TreeGridDEDataSetRuntime](#UsrSFPlugin0407757309)|数据集合获取树表格层级数据|
|多类型页面数据导入|[页面(PAGE)](module/Wiki/article_page)|PSDEDataImportImpl|[PageDataImportRuntimeEx](#PageDataImportRuntimeEx)|页面导入使用|
|version|[页面(PAGE)](module/Wiki/article_page)|PSDEUtilImpl|[DEVersionControlUtilRuntimeEx](#UsrSFPlugin0628633282)|排除新建模式行为自动建立版本|
|安装特定版本(INSTALLSPECVER)|[核心产品功能(PSCOREPRDFUNC)](module/extension/PSCorePrdFunc)|PSDEUserCustomActionImpl|[InstallSpecDEActionRuntime](#InstallSpecDEActionRuntime)||
|提交版本(COMMIT)|[版本(VERSION)](module/Base/version)|PSDEUserCustomActionImpl|[CommitVersionDEActionRuntime](#UsrSFPlugin0324806543)|创建版本数据|
|修复版本(FixCommit)|[版本(VERSION)](module/Base/version)|PSDEUserCustomActionImpl|[FixCommitVersionDEActionRuntime](#UsrSFPlugin0424197954)|初始化版本数据（修复版本）|
|恢复指定版本(RESTORE)|[版本(VERSION)](module/Base/version)|PSDEUserCustomActionImpl|[RestoreVersionDEActionRuntime](#UsrSFPlugin0324899435)||

### AIAgentContextDERuntime :id=AIAgentContextDERuntime


```cn.ibizlab.user.plugin.groovy.dataentity.AIAgentContextDERuntime```

```groovy
package cn.ibizlab.user.plugin.groovy.dataentity

import net.ibizsys.central.cloud.core.dataentity.DataEntityRuntime
import net.ibizsys.central.dataentity.IDataEntityRuntime
import net.ibizsys.central.util.IEntityDTO
import net.ibizsys.central.util.ISearchContextDTO
import net.ibizsys.model.dataentity.IPSDataEntity
import net.ibizsys.model.dataentity.action.IPSDEAction
import net.ibizsys.model.dataentity.ds.IPSDEDataSet
import net.ibizsys.runtime.IDynaInstRuntime
import net.ibizsys.runtime.util.IEntityBase
import net.ibizsys.runtime.util.ISearchContextBase
import org.springframework.util.StringUtils

public class AIAgentContextDERuntime extends DataEntityRuntime {

    private IDataEntityRuntime AIAgentDERuntime = null;

    protected IDataEntityRuntime getAIAgentDERuntimeDERuntime() {
        if(this.AIAgentDERuntime == null) {
            this.AIAgentDERuntime = this.getSystemRuntime().getDataEntityRuntime("AI_AGENT");
        }
        return this.AIAgentDERuntime;
    }

    def jsonSlurper = new groovy.json.JsonSlurper()
    
    @Override
    protected void translateEntitiesAfterProceed(ISearchContextBase arg0, List<? extends IEntityBase> list, String strDataSetName, IPSDEDataSet iPSDEDataSet, IPSDataEntity iPSDataEntity, IDynaInstRuntime iDynaInstRuntime, Object actionData) throws Throwable {
        super.translateEntitiesAfterProceed(arg0, list, strDataSetName, iPSDEDataSet, iPSDataEntity, iDynaInstRuntime, actionData);
        Map<String,List<IEntityBase>> cacheDtoMap = new LinkedHashMap<>();
        for(IEntityBase item : list) {
            IEntityDTO aiAgentContextDTO = null;
            if (item instanceof IEntityDTO) {
                aiAgentContextDTO = (IEntityDTO) item;
            }

            if (aiAgentContextDTO == null) {
                return;
            }
            if (StringUtils.hasLength(aiAgentContextDTO.get("ai_agent_id"))) {
                String agentId = aiAgentContextDTO.get("ai_agent_id") as String;
                if(!cacheDtoMap.containsKey(agentId)){
                    List<IEntityBase> dtoList = new ArrayList<>();
                    cacheDtoMap.put(agentId,dtoList);
                    dtoList.add(aiAgentContextDTO)
                }else {
                    cacheDtoMap.get(agentId).add(aiAgentContextDTO)
                }
            }
        }
        for (Map.Entry<String, List<String>> entry : cacheDtoMap.entrySet()) {
            String agentId = entry.getKey();

            List<IEntityBase> dtoList = entry.getValue();
            List<String> idList = new ArrayList<>();
            for(IEntityBase item : dtoList) {
                IEntityDTO aiAgentContextDTO = null;
                if (item instanceof IEntityDTO) {
                    aiAgentContextDTO = (IEntityDTO) item;
                }
                if (aiAgentContextDTO == null) {
                    return;
                }
                idList.add(aiAgentContextDTO.get("ai_agent_id") as String);
            }

            IDataEntityRuntime iDataEntityRuntime = this.getAIAgentDERuntimeDERuntime();
            ISearchContextDTO iSearchContextDTO =  iDataEntityRuntime.createSearchContext();
            iSearchContextDTO.all().in(iDataEntityRuntime.getKeyPSDEField().getCodeName(),idList)
            List<IEntityDTO> resList = iDataEntityRuntime.selectDataSet("full_info",iSearchContextDTO);
            for(IEntityDTO item : resList) {
                for(IEntityBase item2 : dtoList) {
                    IEntityDTO aiAgentContextDTO = null;
                    if (item2 instanceof IEntityDTO) {
                        aiAgentContextDTO = (IEntityDTO) item2;
                    }
                    if (aiAgentContextDTO == null) {
                        return;
                    }
                    if (item.getId().equals(aiAgentContextDTO.get("ai_agent_id"))) {
                        Iterator<Map.Entry<String, Object>> it = aiAgentContextDTO.any().entrySet().iterator();
                        while (it.hasNext()) {
                            Map.Entry<String, Object> itentry = it.next();
                            Object value = itentry.getValue();

                            if (value == null) {
                                it.remove();
                            }
                        }
                        item.copyToIf(aiAgentContextDTO)
                        def relTools = aiAgentContextDTO.get("ai_agent_tool_rels") ?: []
                        def extraToolsStr = aiAgentContextDTO.get("tools")

                        def relTags = relTools.findAll {
                            (it?.tool_type == 'mcp' || it?.tool_type == 'mcp_built_in_extension') && it?.tool_tag
                        }.collect { it.tool_tag } ?: []

                        def extraTags = []
                        if (extraToolsStr && extraToolsStr != "[]") {
                            try {
                                extraTags = jsonSlurper.parseText(extraToolsStr)?.findAll {
                                    (it?.tool_type == 'mcp' || it?.tool_type == 'mcp_built_in_extension') && it?.tool_tag
                                }.collect { it.tool_tag } ?: []
                            } catch (Exception e) {
                                // 打印日志或忽略解析失败
                            }
                        }

                        def finalMcpTags = (relTags + extraTags).unique().findAll { it }.join(',')
                        aiAgentContextDTO.set("mcp_server_tags", finalMcpTags)


                        def relKbs = aiAgentContextDTO.get("ai_agent_knowledge_rels") ?: []
                        def extraKbsStr = aiAgentContextDTO.get("kbs")

                        def relKbIds = relKbs.collect { it?.ai_knowledge_base_id } ?: []

                        def extraKbIds = []
                        if (extraKbsStr && extraKbsStr != "null" && extraKbsStr != "[]") {
                            try {
                                extraKbIds = jsonSlurper.parseText(extraKbsStr)?.collect { it.id } ?: []
                            } catch (Exception e) {
                                // 打印日志或忽略解析失败
                            }
                        }

                        def finalKbTags = (relKbIds + extraKbIds).unique().findAll { it }.join(',')
                        aiAgentContextDTO.set("kb_tags", finalKbTags)
                    }
                }
            }
        }
    }

    @Override
    protected void translateEntityAfterProceed(Object arg0, Object objRet, String strActionName, IPSDEAction iPSDEAction, IPSDataEntity iPSDataEntity, IDynaInstRuntime iDynaInstRuntime, Object actionData) throws Throwable {
        super.translateEntityAfterProceed(arg0, objRet, strActionName, iPSDEAction, iPSDataEntity, iDynaInstRuntime, actionData)
        if (objRet instanceof IEntityDTO && "fill_with_agent".equalsIgnoreCase(strActionName)) {
            IEntityDTO aiAgentContextDTO = (IEntityDTO) objRet;
            if (StringUtils.hasLength(aiAgentContextDTO.get("ai_agent_id"))) {
                IDataEntityRuntime iDataEntityRuntime = this.getAIAgentDERuntimeDERuntime();
                ISearchContextDTO iSearchContextDTO =  iDataEntityRuntime.createSearchContext();
                iSearchContextDTO.all().in(iDataEntityRuntime.getKeyPSDEField().getCodeName(),aiAgentContextDTO.get("ai_agent_id"))
                List<IEntityDTO> resList = iDataEntityRuntime.selectDataSet("full_info",iSearchContextDTO);
                for(IEntityDTO item : resList) {
                    Iterator<Map.Entry<String, Object>> it = aiAgentContextDTO.any().entrySet().iterator();
                    while (it.hasNext()) {
                        Map.Entry<String, Object> itentry = it.next();
                        Object value = itentry.getValue();

                        if (value == null) {
                            it.remove();
                        }
                    }
                    item.copyToIf(aiAgentContextDTO)

                    

                    def relTools = aiAgentContextDTO.get("ai_agent_tool_rels") ?: []
                    def extraToolsStr = aiAgentContextDTO.get("tools")

                    def relTags = relTools.findAll {
                        (it?.tool_type == 'mcp' || it?.tool_type == 'mcp_built_in_extension') && it?.tool_tag
                    }.collect { it.tool_tag } ?: []

                    def extraTags = []
                    if (extraToolsStr && extraToolsStr != "[]") {
                        try {
                            extraTags = jsonSlurper.parseText(extraToolsStr)?.findAll {
                                (it?.tool_type == 'mcp' || it?.tool_type == 'mcp_built_in_extension') && it?.tool_tag
                            }.collect { it.tool_tag } ?: []
                        } catch (Exception e) {
                            // 打印日志或忽略解析失败
                        }
                    }

                    def finalMcpTags = (relTags + extraTags).unique().findAll { it }.join(',')
                    aiAgentContextDTO.set("mcp_server_tags", finalMcpTags)


                    def relKbs = aiAgentContextDTO.get("ai_agent_knowledge_rels") ?: []
                    def extraKbsStr = aiAgentContextDTO.get("kbs")

                    def relKbIds = relKbs.collect { it?.ai_knowledge_base_id } ?: []

                    def extraKbIds = []
                    if (extraKbsStr && extraKbsStr != "null" && extraKbsStr != "[]") {
                        try {
                            extraKbIds = jsonSlurper.parseText(extraKbsStr)?.collect { it.id } ?: []
                        } catch (Exception e) {
                            // 打印日志或忽略解析失败
                        }
                    }

                    def finalKbTags = (relKbIds + extraKbIds).unique().findAll { it }.join(',')
                    aiAgentContextDTO.set("kb_tags", finalKbTags)
                }
            }
        }
    }
}
```
### AIAgentDESyncUtilRuntime :id=AIAgentDESyncUtilRuntime


```net.ibizsys.central.plugin.util.sysutil.AIAgentDESyncUtilRuntime```

```groovy
null
```
### AIChatSkillDEDataSetRuntime :id=AIChatSkillDEDataSetRuntime


```net.ibizsys.central.plugin.ai.dataentity.ds.AIChatSkillDEDataSetRuntime```

```groovy
null
```
### AIClientCredentialDESyncUtilRuntime :id=AIClientCredentialDESyncUtilRuntime


```net.ibizsys.central.plugin.util.sysutil.AIClientCredentialDESyncUtilRuntime```

```groovy
package net.ibizsys.central.plugin.util.sysutil;

import java.util.Date;
import java.util.LinkedHashMap;
import java.util.Map;

import net.ibizsys.central.cloud.core.IServiceSystemRuntimeBase;
import net.ibizsys.central.cloud.core.security.EmployeeContext;
import net.ibizsys.central.cloud.core.spring.rt.ServiceHub;
import net.ibizsys.central.cloud.core.util.domain.AIAccess;
import net.ibizsys.central.cloud.core.util.domain.Credential;
import net.ibizsys.model.codelist.IPSCodeItem;
import net.ibizsys.model.dataentity.action.IPSDEAction;
import net.ibizsys.model.dataentity.defield.IPSDEField;
import net.ibizsys.runtime.codelist.ICodeListRuntime;
import net.ibizsys.runtime.security.UserContext;
import net.ibizsys.runtime.util.DataTypeUtils;
import net.ibizsys.runtime.util.DateUtils;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import net.ibizsys.central.util.IEntityDTO;
import net.ibizsys.runtime.dataentity.IDataEntityRuntimeContext;
import net.ibizsys.runtime.util.YamlUtils;
import org.springframework.util.ObjectUtils;
import org.springframework.util.StringUtils;

public class AIClientCredentialDESyncUtilRuntime extends SysCloudConfigDESyncUtilRuntimeBase{
	public static final String PREDEFINEDFIELD_ACCESS_STRATEGY = "ACCESS_STRATEGY";
	public static final String PREDEFINEDFIELD_ACCESS_TYPES = "ACCESS_TYPES";
	public static final String PREDEFINEDFIELD_ACCESS_KEY = "ACCESS_KEY";
	public static final String PREDEFINEDFIELD_ACTIVE = "ACTIVE";
	public static final String PREDEFINEDFIELD_USER_ID = "USER_ID";
	public static final String PREDEFINEDFIELD_EXPIRATION_DATE = "EXPIRATION_DATE";

	public final static String FIELD_EMPLOYEE = "employee";
	public final static String FIELD_CLIENT_ACCESS = "client_access";
	public final static String FIELD_CLIENT_ACCESS_STRATEGY = "strategy";
	public final static String FIELD_CLIENT_ACCESS_TYPES = "access_types";

	/**
	 * 路径参数：AI工厂标识
	 */
	public final static String PARAM_AIFACTORY = "aifactory";

	private String strAIFactoryTag = "";

	private static final Log log = LogFactory.getLog(AIClientCredentialDESyncUtilRuntime.class);



	@Override
	protected void onInit() throws Exception {
		this.strAIFactoryTag = DataTypeUtils.asString(this.getUtilParam(PARAM_AIFACTORY, null), "ibizintelligence");
		super.onInit();
	}

	@Override
	protected String getConfig(IDataEntityRuntimeContext iDataEntityRuntimeContext, IEntityDTO iEntityDTO) throws Throwable {
		String strConfig = super.getConfig(iDataEntityRuntimeContext, iEntityDTO);
		if(StringUtils.hasLength(strConfig)) {
			return strConfig;
		}
		Map<String, Object> map = this.getConfigMap(iDataEntityRuntimeContext, iEntityDTO);
		if(!map.containsKey(FIELD_CLIENT_ACCESS)) {
			String strStrategy = "";
			String strAccessTypes = "";
			Map<String, Object> map2 = new LinkedHashMap<String, Object>();
			IPSDEField strategyPSDEField = iDataEntityRuntimeContext.getDataEntityRuntime().getPSDEFieldByTag(PREDEFINEDFIELD_ACCESS_STRATEGY, true);
			if(strategyPSDEField != null) {
				Object strategy = iEntityDTO.get(strategyPSDEField.getLowerCaseName());
				if(!ObjectUtils.isEmpty(strategy)) {
					strStrategy = String.valueOf(strategy);
					map2.put(FIELD_CLIENT_ACCESS_STRATEGY, strStrategy);
				}
			}

			IPSDEField accessTypesPSDEField = iDataEntityRuntimeContext.getDataEntityRuntime().getPSDEFieldByTag(PREDEFINEDFIELD_ACCESS_TYPES, true);
			if(accessTypesPSDEField != null) {
				Object accessTypes = iEntityDTO.get(accessTypesPSDEField.getLowerCaseName());
				if (!ObjectUtils.isEmpty(accessTypes)) {
					strAccessTypes = String.valueOf(accessTypes);
					map2.put(FIELD_CLIENT_ACCESS_TYPES, strAccessTypes);
				}
			}
			map.put(FIELD_CLIENT_ACCESS, map2);
		}

		if(!map.containsKey(FIELD_EMPLOYEE)) {
			IPSDEField userIdPSDEField = iDataEntityRuntimeContext.getDataEntityRuntime().getPSDEFieldByTag(PREDEFINEDFIELD_USER_ID, true);
			if(userIdPSDEField != null) {
				Object userId = iEntityDTO.get(userIdPSDEField.getLowerCaseName());
				if(!ObjectUtils.isEmpty(userId)) {
					String strUserId = String.valueOf(userId);
					if (StringUtils.hasLength(strUserId) && strUserId.equals(EmployeeContext.getCurrent().getUserid())) {
						Map employeeMap = YamlUtils.asMap(EmployeeContext.getCurrent().getEmployee().toString());
						map.put(FIELD_EMPLOYEE, employeeMap);
					}
				}
			}
		}

		if(!map.containsKey(Credential.FIELD_EXPIRESTIME)) {
			IPSDEField expirationDatePSDEField = iDataEntityRuntimeContext.getDataEntityRuntime().getPSDEFieldByTag(PREDEFINEDFIELD_EXPIRATION_DATE, true);
			if(expirationDatePSDEField != null) {
				Object expirationDate = iEntityDTO.get(expirationDatePSDEField.getLowerCaseName());
				if(expirationDate != null) {
					if(expirationDate instanceof String) {
						map.put(Credential.FIELD_EXPIRESTIME, expirationDate);
					}
					else
					if(expirationDate instanceof Date) {
						map.put(Credential.FIELD_EXPIRESTIME, DateUtils.toDateTimeString((Date)expirationDate));
					}
					else
					{
						try {
							map.put(Credential.FIELD_EXPIRESTIME, DateUtils.toDateTimeString(DataTypeUtils.asDateTime(expirationDate)));
						}
						catch (Throwable ex) {
							log.error(String.format("过期时间[%1$s]类型不支持", expirationDate));
						}
					}
				}
			}
		}

		if (!map.containsKey(Credential.FIELD_DISABLED)) {
			map.put(Credential.FIELD_DISABLED, 0);
			IPSDEField activePSDEField = iDataEntityRuntimeContext.getDataEntityRuntime().getPSDEFieldByTag(PREDEFINEDFIELD_ACTIVE, true);
			if (activePSDEField != null) {
				Object active = iEntityDTO.get(activePSDEField.getLowerCaseName());
				if (!ObjectUtils.isEmpty(active)) {
					Boolean bActive = DataTypeUtils.asBoolean(active, true);
					if (!bActive) {
						map.put(Credential.FIELD_DISABLED, 1);
					}
				}
			}
		}
		return this.getConfig(iDataEntityRuntimeContext, map, iEntityDTO);
	}


	protected String getConfig(IDataEntityRuntimeContext iDataEntityRuntimeContext, Map<String, Object> map, IEntityDTO iEntityDTO) throws Throwable {
		return YamlUtils.toString(map);
	}


	@Override
	protected String getCloudConfigId(IDataEntityRuntimeContext iDataEntityRuntimeContext, Map<String, Object> map, IEntityDTO iEntityDTO) throws Exception {
		IPSDEField accessKeyPSDEField = iDataEntityRuntimeContext.getDataEntityRuntime().getPSDEFieldByTag(PREDEFINEDFIELD_ACCESS_KEY, true);
		map.put(PARAM_AIFACTORY,this.strAIFactoryTag);
		map.put(PARAM_KEY, iDataEntityRuntimeContext.getDataEntityRuntime().getFieldValue(iEntityDTO,accessKeyPSDEField));
		return super.getCloudConfigId(iDataEntityRuntimeContext, map, iEntityDTO);
	}


	protected void onAfterCreate(IDataEntityRuntimeContext iDataEntityRuntimeContext, IPSDEAction iPSDEAction, IEntityDTO iEntityDTO) throws Throwable {
		IPSDEField userIdPSDEField = iDataEntityRuntimeContext.getDataEntityRuntime().getPSDEFieldByTag(PREDEFINEDFIELD_USER_ID, true);
		if(userIdPSDEField != null) {
			Object userId = iEntityDTO.get(userIdPSDEField.getLowerCaseName());
			String strUserId = String.valueOf(userId);
			if (StringUtils.hasLength(strUserId) && strUserId.equals(EmployeeContext.getCurrent().getUserid())) {
				super.onAfterCreate(iDataEntityRuntimeContext, iPSDEAction, iEntityDTO);
			}
		}
//		super.onAfterCreate(iDataEntityRuntimeContext, iPSDEAction, iEntityDTO);
	}

	protected void onAfterUpdate(IDataEntityRuntimeContext iDataEntityRuntimeContext, IPSDEAction iPSDEAction, IEntityDTO iEntityDTO) throws Throwable {
		IPSDEField userIdPSDEField = iDataEntityRuntimeContext.getDataEntityRuntime().getPSDEFieldByTag(PREDEFINEDFIELD_USER_ID, true);
		if(userIdPSDEField != null) {
			Object userId = iEntityDTO.get(userIdPSDEField.getLowerCaseName());
			String strUserId = String.valueOf(userId);
			if (StringUtils.hasLength(strUserId) && strUserId.equals(EmployeeContext.getCurrent().getUserid())) {
				super.onAfterUpdate(iDataEntityRuntimeContext, iPSDEAction, iEntityDTO);
			}
		}
//		super.onAfterUpdate(iDataEntityRuntimeContext, iPSDEAction, iEntityDTO);
	}

	protected void onBeforeRemove(IDataEntityRuntimeContext iDataEntityRuntimeContext, IPSDEAction iPSDEAction, IEntityDTO iEntityDTO) throws Throwable {
//		IPSDEField userIdPSDEField = iDataEntityRuntimeContext.getDataEntityRuntime().getPSDEFieldByTag(PREDEFINEDFIELD_USER_ID, true);
//		if(userIdPSDEField != null) {
//			Object userId = iEntityDTO.get(userIdPSDEField.getLowerCaseName());
//			String strUserId = String.valueOf(userId);
//			if (StringUtils.hasLength(strUserId) && strUserId.equals(EmployeeContext.getCurrent().getUserid())) {
//				super.onBeforeRemove(iDataEntityRuntimeContext, iPSDEAction, iEntityDTO);
//			}
//		}
		super.onBeforeRemove(iDataEntityRuntimeContext, iPSDEAction, iEntityDTO);
	}
	@Override
	protected String getDefaultCloudConfigIdFormat(IDataEntityRuntimeContext iDataEntityRuntimeContext) throws Exception {
		return "accesstoken-{system}-sysaifactory-ai-{aifactory}--webhook--{key}";
	}
}

```
### AI知识库目录查询 :id=AIDocListByKBDataSetRuntime


```cn.ibizlab.user.plugin.groovy.dataentity.ds.AIDocListByKBDataSetRuntime```

```groovy
package cn.ibizlab.user.plugin.groovy.dataentity.ds;

import net.ibizsys.central.plugin.util.dataentity.ds.DEDataSetRuntimeBase;
import org.springframework.data.domain.Page;
import net.ibizsys.central.util.IEntityDTO;
import net.ibizsys.central.util.ISearchContextDTO;
import net.ibizsys.central.util.PageImpl;

/**
 * AI知识库目录查询
 */
class AIDocListByKBDataSetRuntime extends DEDataSetRuntimeBase {

    @Override
    protected Page<?> doFetchReal(ISearchContextDTO iSearchContextDTO) throws Throwable {
        def kb_id = iSearchContextDTO.get("kb_id")
        def kb_name = iSearchContextDTO.get("kb_name")
        if (!kb_id && !kb_name) {
            throw new RuntimeException("请输入查询知识库")
        }

        def kb_search = this.getDataEntityRuntime().createSearchContext()
        def kb_list = []
        def doc_runtime = this.getSystemRuntime().dataentity("AI_KB_DOCUMENT")

        if (!kb_id) {
            kb_search.set("query", kb_name)
            kb_list = this.getDataEntityRuntime().selectDataSet("ai_kb_query", kb_search)
        } else {
            kb_search.eq("id", kb_id)
            kb_list = this.getDataEntityRuntime().select(kb_search)
        }

        //附带知识库文档目录
        for (kb in kb_list) {
            def doc_search = doc_runtime.createSearchContext().eq("kb_id", kb.get("id"))
            //获取文档清单
            def docs = doc_runtime.selectDataQuery("ai_doc_list", doc_search)
            kb.set("docs", docs)
        }

        return new PageImpl<IEntityDTO>(kb_list, iSearchContextDTO.getPageable(), kb_list.size(), 1);

    }

}

```
### AI知识库文档查询 :id=AIDocQueryListDataSetRuntime


```cn.ibizlab.user.plugin.groovy.dataentity.ds.AIDocQueryListDataSetRuntime```

```groovy
package cn.ibizlab.user.plugin.groovy.dataentity.ds;

import groovy.transform.CompileStatic;

import net.ibizsys.central.plugin.util.dataentity.ds.DEDataSetRuntimeBase
import net.ibizsys.central.util.EntityDTO;
import org.springframework.data.domain.Page;
import net.ibizsys.central.util.IEntityDTO;
import net.ibizsys.central.util.ISearchContextDTO;
import net.ibizsys.central.util.PageImpl;

/**
 * AI知识库文档查询
 */
class AIDocQueryListDataSetRuntime extends DEDataSetRuntimeBase {

    @Override
    protected Page<?> doFetchReal(ISearchContextDTO iSearchContextDTO) throws Throwable {
        def kb_id = iSearchContextDTO.get("kb_id")
        def kb_name = iSearchContextDTO.get("kb_name")
        def query = iSearchContextDTO.get("query")
        if (!kb_id && !kb_name) {
            throw new RuntimeException("请输入查询知识库")
        }
        if (!query) {
            throw new RuntimeException("请输入查询内容")
        }

        if (!kb_id) {
            def kb_runtime = this.getSystemRuntime().dataentity("AI_KNOWLEDGE_BASE")
            def kb_search = kb_runtime.createSearchContext()
            kb_search.set("query", kb_name)
            def kb_list = kb_runtime.selectDataSet("ai_kb_query", kb_search)
            if (kb_list.size() == 0) {
                throw new RuntimeException("未查询到[${kb_name}]相关的知识库")
            }
            kb_id = kb_list.get(0).get("id")
        }
        def chunk_runtime = this.getSystemRuntime().dataentity("AI_KB_CHUNK")
        def chunk_search = chunk_runtime.createSearchContext()
        chunk_search.set("kb_id", kb_id)
        chunk_search.set("query", query)
        chunk_search.set("keyword_similarity_weight", iSearchContextDTO.get("keyword_similarity_weight", "0.7"))
        chunk_search.set("similarity_threshold", iSearchContextDTO.get("keyword_similarity_weight", "0.2"))
        chunk_search.set("top_k", iSearchContextDTO.get("keyword_similarity_weight", "10"))
        chunk_search.set("n_rerank_eq", iSearchContextDTO.get("n_rerank_eq", 0))
        chunk_search.set("use_kg", iSearchContextDTO.get("use_kg", 0))
        def args = [chunk_search] as Object[]
        //检索
        Page chunk_result = chunk_runtime.fetchDataSet("retrieval_test", null, args)
        def document_ids = chunk_result.getContent()
                .collect { it.get('docid') }
                .findAll { it != null }
                .unique()

        def doc_runtime = this.getSystemRuntime().dataentity("AI_KB_DOCUMENT")
        def doc_search = doc_runtime.createSearchContext().in("id", document_ids)
        //查询文档内容
        def docs = doc_runtime.selectDataQuery("ai_doc_content", doc_search)
        for (doc in docs) {
            //"retrieveRefInfo"
            def execute_args = [doc] as Object[]
            doc_runtime.executeLogic("retrieveRefInfo", execute_args)
        }
        //根据chunk中doc出现顺序输出
        def docMap = docs.collectEntries { doc -> [doc.id, doc] }
        def orderedDocs = document_ids
                .collect { docMap[it] }
                .findAll { it != null }

        return new PageImpl<IEntityDTO>(orderedDocs, doc_search.getPageable(), orderedDocs.size(), 1);
    }

}

```
### AIFactoryAgentLogicNodeRuntime :id=AIFactoryAgentLogicNodeRuntime
AI智能体交互逻辑节点

```cn.ibizlab.user.plugin.groovy.dataentity.logic.AIFactoryAgentLogicNodeRuntime```

```groovy
package cn.ibizlab.user.plugin.groovy.dataentity.logic;

import groovy.transform.CompileStatic
import net.ibizsys.central.cloud.core.IServiceSystemRuntime
import net.ibizsys.central.cloud.core.ai.ISysAIChatAgentRuntime
import net.ibizsys.central.cloud.core.ai.ISysAIFactoryRuntime
import net.ibizsys.central.cloud.core.dataentity.logic.DELogicSysAIChatAgentNodeRuntime
import net.ibizsys.central.cloud.core.util.ChatMessagesBuilder
import net.ibizsys.central.cloud.core.util.domain.ChatCompletionRequest
import net.ibizsys.central.cloud.core.util.domain.ChatCompletionResult
import net.ibizsys.central.cloud.core.util.domain.ChatCompletionResultEx
import net.ibizsys.central.cloud.core.util.domain.ChatMessage
import net.ibizsys.central.dataentity.logic.IDELogicParamRuntime
import net.ibizsys.central.dataentity.logic.IDELogicRuntimeContext
import net.ibizsys.central.dataentity.logic.IDELogicSession
import net.ibizsys.model.dataentity.logic.IPSDELogicNode
import net.ibizsys.model.dataentity.logic.IPSDESysAIChatAgentLogic
import net.ibizsys.model.util.JsonUtils
import net.ibizsys.runtime.util.Entity
import org.springframework.util.ObjectUtils

import java.util.regex.Matcher
import java.util.regex.Pattern

@CompileStatic
class AIFactoryAgentLogicNodeRuntime extends DELogicSysAIChatAgentNodeRuntime {


	@Override
	protected void onExecute(IDELogicRuntimeContext iDELogicRuntimeContext, IDELogicSession iDELogicSession, IPSDELogicNode iPSDELogicNode) throws Throwable {
		super.onExecute(iDELogicRuntimeContext,iDELogicSession,iPSDELogicNode);
	}

	@Override
	protected void onExecuteChatDefault(IDELogicRuntimeContext iDELogicRuntimeContext, IDELogicSession iDELogicSession, IPSDESysAIChatAgentLogic iPSDESysAIChatAgentLogic, Map<String, Object> params) throws Throwable {
		IServiceSystemRuntime iServiceSystemRuntime = (IServiceSystemRuntime)iDELogicRuntimeContext.getSystemRuntime();
		ISysAIFactoryRuntime iSysAIFactoryRuntime = iServiceSystemRuntime.getSysAIFactoryRuntime(iPSDESysAIChatAgentLogic.getPSSysAIFactoryMust().getId(), false);
		ISysAIChatAgentRuntime iSysAIChatAgentRuntime = iSysAIFactoryRuntime.getAIChatAgentRuntime(iPSDESysAIChatAgentLogic.getPSSysAIChatAgentMust().getCodeName(), false);
		IDELogicParamRuntime iDELogicParamRuntime = iDELogicRuntimeContext.getDELogicRuntime().getDELogicParamRuntime(iPSDESysAIChatAgentLogic.getDstPSDELogicParamMust().getCodeName(), false);

		ChatCompletionResult chatCompletionResult = null;
		ChatCompletionRequest chatCompletionRequest = null;
		Object objParam = iDELogicParamRuntime.getParamObject(iDELogicSession);
		if(objParam instanceof ChatCompletionRequest || objParam instanceof String) {
			chatCompletionRequest = new ChatCompletionRequest();
			if(objParam instanceof ChatCompletionRequest) {
				ChatCompletionRequest chatCompletionRequest2 = (ChatCompletionRequest)objParam;
				chatCompletionRequest2.copyTo(chatCompletionRequest);
				//放入历史消息
				if(iPSDESysAIChatAgentLogic.getHistoryCount() > 0 && !ObjectUtils.isEmpty(chatCompletionRequest2.getMessages()) && chatCompletionRequest2.getMessages().size() > iPSDESysAIChatAgentLogic.getHistoryCount()) {
					List<ChatMessage> list = chatCompletionRequest2.getMessages().subList(chatCompletionRequest2.getMessages().size() - iPSDESysAIChatAgentLogic.getHistoryCount(), chatCompletionRequest2.getMessages().size());
					chatCompletionRequest.setMessages(list);
				}
				else {
					chatCompletionRequest.setMessages(chatCompletionRequest2.getMessages());
				}
			}
			else
			if(objParam instanceof String) {
				chatCompletionRequest.setMessages(new ChatMessagesBuilder().user(objParam.toString()).build());
			}

			//指定智能体
			Map<String, String> options = JsonUtils.asMap(iPSDESysAIChatAgentLogic.getNodeParams());
			if(options.get("aiagenttag")!=null){
				chatCompletionRequest.set("srfaiagenttag",options.get("aiagenttag"));
			}
			chatCompletionResult = iSysAIChatAgentRuntime.chatCompletion(new Entity() , chatCompletionRequest, new LinkedHashMap<String, Object>(), true, false);
		}
		else {
			chatCompletionRequest = new ChatCompletionRequest();
			chatCompletionRequest.from(objParam)
			//指定智能体
			Map<String, String> options = JsonUtils.asMap(iPSDESysAIChatAgentLogic.getNodeParams());
			if(options.get("aiagenttag")!=null){
				chatCompletionRequest.set("srfaiagenttag",options.get("aiagenttag"));
			}
			chatCompletionResult = iSysAIChatAgentRuntime.chatCompletion(objParam , chatCompletionRequest, new LinkedHashMap<String, Object>(), true, true);
		}
  
		Object objRet = this.getRealResult(iDELogicRuntimeContext, iDELogicSession, iPSDESysAIChatAgentLogic, chatCompletionResult, chatCompletionRequest, objParam);

		iDELogicSession.setLastReturn(chatCompletionResult);

		if(iPSDESysAIChatAgentLogic.getRetPSDELogicParam() != null) {
			IDELogicParamRuntime retDELogicParamRuntime = iDELogicRuntimeContext.getDELogicRuntime().getDELogicParamRuntime(iPSDESysAIChatAgentLogic.getRetPSDELogicParam().getCodeName(), false);
			if(retDELogicParamRuntime.getReal() instanceof ChatCompletionResult){
				iDELogicSession.setLastReturn(chatCompletionResult);
				retDELogicParamRuntime.bind(iDELogicSession, chatCompletionResult);
			}else {
				iDELogicSession.setLastReturn(objRet);
				retDELogicParamRuntime.bind(iDELogicSession, objRet);
			}
		}
	}

	protected Object getRealResult(IDELogicRuntimeContext iDELogicRuntimeContext, IDELogicSession iDELogicSession, IPSDESysAIChatAgentLogic iPSDESysAIChatAgentLogic, ChatCompletionResult chatCompletionResult, ChatCompletionRequest chatCompletionRequest, Object objParam) throws Exception {
		java.lang.Object realResult = super.getRealResult(iDELogicRuntimeContext, iDELogicSession, iPSDESysAIChatAgentLogic, chatCompletionResult, chatCompletionRequest, objParam);
		if (realResult) {
			if (realResult instanceof String) {
				List<Map<String, Object>>  patterns = [
						[p: /```json\s*([\s\S]*?)\s*```/, c: { String it -> it.replace('```json', '').replace('```', '').trim() } as Closure<String>],
						[p: /```\s*([\s\S]*?)\s*```/,     c: { String it -> it.replace('```', '').trim() } as Closure<String>],
						[p: /\{[\s\S]*?\}(?=\s*[\n\r]|$)/, c: { String it -> it.trim() } as Closure<String>],
						[p: /\[[\s\S]*?\](?=\s*[\n\r]|$)/, c: { String it -> it.trim() } as Closure<String>]
				] as List<Map<String, Object>>;

				groovy.json.JsonSlurper slurper = new groovy.json.JsonSlurper()

				for (Map<String, Object> e : patterns) {
					Pattern pattern = Pattern.compile ((String)e.get('p'))
					Matcher m = pattern.matcher(realResult)
					if (m.find()) {
						String raw = m.group(0)
						Closure<String> cleanFn = (Closure<String>) e.get('c')
						String clean = cleanFn.call(raw)

						if (clean && !clean.isEmpty()) {
							try {
								Object data = slurper.parseText(clean)
								return data
							} catch (groovy.json.JsonException ignored) {
								// 继续尝试下一个模式
							}
						}
					}
				}
			}
		}
		return realResult;
	}
}
```
### AI知识库清单查询 :id=AIKBQueryListDataSetRuntime


```cn.ibizlab.user.plugin.groovy.dataentity.ds.AIKBQueryListDataSetRuntime```

```groovy
package cn.ibizlab.user.plugin.groovy.dataentity.ds;

import net.ibizsys.central.plugin.util.dataentity.ds.DEDataSetRuntimeBase
import net.ibizsys.runtime.util.JsonUtils
import org.springframework.data.domain.Page;
import net.ibizsys.central.util.ISearchContextDTO;
import net.ibizsys.central.util.PageImpl;

/**
 * AI知识库清单查询
 */
class AIKBQueryListDataSetRuntime extends DEDataSetRuntimeBase {

    @Override
    protected Page<?> doFetchReal(ISearchContextDTO iSearchContextDTO) throws Throwable {
        String query = iSearchContextDTO.get("query")
        if (!query) {
            throw new RuntimeException("请输入查询")
        }
        def kbutil = sys.util("AI.SYSKNOWLEDGEBASEUTIL")

        def vector = JsonUtils.toString(kbutil.getEmbedding(null, query))

        //相似度查询 5 条
        String querySql = """
SELECT *
FROM (
         SELECT DISTINCT ON (kb.id)
             kb.id,
             kb.name,
             kb.description,
             kb.source_name,
             kb.category_name ,
             (1 - (chunk.content_vector <=> '${vector}')) / 2 AS similarity,
             kb.update_time,
             kb.guidance_prompt
         FROM ai_kb_chunk chunk
                  JOIN ai_kb_document doc ON chunk.document_id = doc.id
                  JOIN ai_knowledge_base kb ON doc.kb_id = kb.id
         WHERE
             (1 - (chunk.content_vector <=> '${vector}')) / 2 > 0.2
           AND chunk.pid IS NULL   
         ORDER BY
             kb.id,
             (1 - (chunk.content_vector <=> '${vector}')) / 2 DESC
     ) AS unique_kbs
ORDER BY similarity DESC
LIMIT 5
"""

        def list = this.getDataEntityRuntime().getSysDBSchemeRuntime().executeSelectSQL(querySql, null)

        return new PageImpl(list, iSearchContextDTO.getPageable(), list.size(), 1)

    }

}

```
### AI知识库查询(record) :id=AIKBWithRecordDataSetRuntime


```cn.ibizlab.user.plugin.groovy.dataentity.ds.AIKBWithRecordDataSetRuntime```

```groovy
package cn.ibizlab.user.plugin.groovy.dataentity.ds

import net.ibizsys.central.database.IDBDialect
import net.ibizsys.central.database.postgresql.PostgreSQLDialect;
import net.ibizsys.central.plugin.util.dataentity.ds.DEDataSetRuntimeBase
import net.ibizsys.central.util.EntityDTO
import net.ibizsys.psmodel.core.util.DataTypes
import net.ibizsys.runtime.util.Conditions
import net.ibizsys.runtime.util.DataTypeUtils
import net.ibizsys.runtime.util.Entity
import net.ibizsys.runtime.util.ISearchCond
import net.ibizsys.runtime.util.ISearchFieldCond
import net.ibizsys.runtime.util.ISearchGroupCond
import net.ibizsys.runtime.util.ISearchItemsCond
import net.ibizsys.runtime.util.SearchCustomCond
import org.apache.commons.collections4.CollectionUtils
import org.springframework.data.domain.Page;
import net.ibizsys.central.util.ISearchContextDTO;


/**
 * AI知识库查询(record)
 */
class AIKBWithRecordDataSetRuntime extends DEDataSetRuntimeBase {

    @Override
    protected Page<?> doFetchReal(ISearchContextDTO iSearchContextDTO) throws Throwable {
        //自定义搜索组
        ISearchCond cond = null
        Iterator<ISearchCond> iterator = iSearchContextDTO.getSearchCondsIf().iterator()
        while (iterator.hasNext()) {
            ISearchCond searchCond = iterator.next()
            if (ISearchGroupCond.CAT_SEARCHCONDS == searchCond.getCat()) {
                cond = searchCond
                iterator.remove()
                break
            }
        }

        if (iSearchContextDTO.get("resourceid")) {
            def data_resource = this.getSystemRuntime().getDataEntityRuntime("DATA_RESOURCE").get(iSearchContextDTO.get("resourceid"))
            if (cond != null && data_resource) {
                //解析SEARCHCONDS，形成jsonb的查询条件
                IDBDialect dbDialect = this.getDataEntityRuntime().getSysDBSchemeRuntime().getDBDialect()
                Entity definition = data_resource.get("schema")?.get("definition")
                if (definition && dbDialect instanceof PostgreSQLDialect) {
                    String jsonField = "T11._metadata"
                    StringBuilder sb = new StringBuilder();
                    parseSearchCond(jsonField, sb, dbDialect, definition, null, null, cond, iSearchContextDTO)
                    iSearchContextDTO.getSearchCondsIf().add(SearchCustomCond.of(sb.toString()))
                }
            }
        }

        Object[] args = [iSearchContextDTO] as Object[]
        return this.getDataEntityRuntime().fetchDataSet("DEFAULT", null, args)
    }

    /**
     *
     * 解析jsonb条件
     *
     * @param jsonField
     * @param sb
     * @param dbDialect
     * @param items
     * @param searchCond
     * @param iSearchContextDTO
     */
    private void parseSearchCond(String jsonField, StringBuilder sb, IDBDialect dbDialect, Entity definition, List<String> items, List<String> array_items, ISearchCond searchCond, ISearchContextDTO iSearchContextDTO) {
        //  集合存在xxx条件
        //  EXISTS (SELECT 1
        //              FROM jsonb_array_elements(t11._metadata -> 'HFDF_LIST') AS elem
        //              WHERE elem ->> 'AH' is not null)
        //
        //  集合存在
        // jsonb_array_length(t11._metadata->'HFDF_LIST') > 0

        if (searchCond instanceof ISearchItemsCond) {
            //子对象条件
            ISearchItemsCond searchGroupCond = (ISearchItemsCond) searchCond;
            List<ISearchCond> conds = searchGroupCond.getSearchConds()
            if (CollectionUtils.isNotEmpty(conds)) {
                List<String> subItems = new ArrayList<>()
                String subItem = searchGroupCond.getFieldName()
                if (items) {
                    subItems.addAll(items)
                }
                subItems.add(subItem)
                def obj_property = definition
                for (item in subItems) {
                    if ("object" == obj_property.get("type")) {
                        obj_property = obj_property.get("properties").get(item)
                    } else if ("array" == obj_property.get("type")) {
                        obj_property = obj_property.get("items").get("properties").get(item)
                    }
                }
                if (!obj_property) {
                    throw new Exception("[{$subItem}]字段不存在")
                }

                sb.append("(")
                if ("object" == obj_property.get("type")) {
                    for (i in 0..<conds.size()) {
                        if (i > 0) {
                            if (Conditions.OR == searchGroupCond.getCondOp()) {
                                sb.append(" " + Conditions.OR + " ")
                            } else {
                                sb.append(" " + Conditions.AND + " ")
                            }
                        }
                        parseSearchCond(jsonField, sb, dbDialect, definition, subItems, array_items, conds.get(i), iSearchContextDTO)
                    }
                } else if ("array" == obj_property.get("type")) {
                    String fieldName = jsonField
                    List<String> subArrayItems = new ArrayList<>()
                    if (array_items) {
                        subArrayItems.addAll(array_items)
                    }
                    subArrayItems.add(subItem)
                    if (jsonField == 'T11._metadata') {
                        fieldName += " -> '${subItem}'"
                    } else {
                        if (subArrayItems && subArrayItems.size() > 1) {
                            for (i in 1..<subArrayItems.size()) {
                                fieldName += " -> '${subArrayItems.get(i)}'"
                            }
                        }
                    }
                    sb.append("""
EXISTS (SELECT 1
FROM jsonb_array_elements(${fieldName}) AS ${subItem}
WHERE
""")
                    StringBuilder arrayFieldConds = new StringBuilder();
                    for (i in 0..<conds.size()) {
                        if (i > 0) {
                            if (Conditions.OR == searchGroupCond.getCondOp()) {
                                arrayFieldConds.append(" " + Conditions.OR + " ")
                            } else {
                                arrayFieldConds.append(" " + Conditions.AND + " ")
                            }
                        }
                        parseSearchCond(subItem, arrayFieldConds, dbDialect, definition, subItems, subArrayItems, conds.get(i), iSearchContextDTO)
                    }
                    sb.append(arrayFieldConds.toString())
                    sb.append(")")
                }
                sb.append(")")
            }
        } else if (searchCond instanceof ISearchGroupCond) {
            ISearchGroupCond searchGroupCond = (ISearchGroupCond) searchCond;
            List<ISearchCond> conds = searchGroupCond.getSearchConds()
            if (CollectionUtils.isNotEmpty(conds)) {
                sb.append("(")
                for (i in 0..<conds.size()) {
                    if (i > 0) {
                        if (Conditions.OR == searchGroupCond.getCondOp()) {
                            sb.append(" " + Conditions.OR + " ")
                        } else {
                            sb.append(" " + Conditions.AND + " ")
                        }
                    }
                    parseSearchCond(jsonField, sb, dbDialect, definition, items, array_items, conds.get(i), iSearchContextDTO)
                }
                sb.append(")")
            }
        } else if (searchCond instanceof ISearchFieldCond) {
            ISearchFieldCond iSearchFieldCond = (ISearchFieldCond) searchCond;
            String fieldName = jsonField

            def last_obj_property = definition
            for (item in items) {
                if ("object" == last_obj_property.get("type")) {
                    last_obj_property = last_obj_property.get("properties").get(item)
                } else if ("array" == last_obj_property.get("type")) {
                    last_obj_property = last_obj_property.get("items").get("properties").get(item)
                }
            }

            if (last_obj_property == null || "object" == last_obj_property.get("type")) {
                if (items) {
                    if(array_items) {
                        for (i in array_items.size()..<items.size()) {
                            fieldName += " -> '${items.get(i)}'"
                        }
                    } else {
                        for (item in items) {
                            fieldName += " -> '${item}'"
                        }
                    }
                }
            }
            fieldName += " ->> '" + iSearchFieldCond.getFieldName() + "'"
            int dataType = iSearchFieldCond.getDataType()
            if (!DataTypeUtils.isStringDataType(dataType) && !DataTypeUtils.isIntDataType(dataType) && !DataTypeUtils.isDoubleDataType(dataType) && !DataTypeUtils.isDateTimeDataType(dataType)) {
                dataType = DataTypes.VARCHAR
            }
            //数值
            if (DataTypeUtils.isIntDataType(dataType) || DataTypeUtils.isDoubleDataType(dataType)) {
                fieldName = "(" + fieldName + ")::NUMERIC"
            }
            String sql = dbDialect.getConditionSQL(fieldName, dataType, iSearchFieldCond.getCondOp(), iSearchFieldCond.getValue(), false, iSearchContextDTO)
            sb.append(sql)
        }
    }


}

```
### AIToolDESyncUtilRuntime :id=AIToolDESyncUtilRuntime


```net.ibizsys.central.plugin.util.sysutil.AIToolDESyncUtilRuntime```

```groovy
package net.ibizsys.central.plugin.util.sysutil;

import java.util.Date;
import java.util.LinkedHashMap;
import java.util.Map;

import net.ibizsys.central.cloud.core.spring.rt.ServiceHub;
import net.ibizsys.central.cloud.core.util.domain.Credential;
import net.ibizsys.central.dataentity.IDataEntityRuntime;
import net.ibizsys.model.dataentity.action.IPSDEAction;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.springframework.util.ObjectUtils;
import org.springframework.util.StringUtils;

import net.ibizsys.central.cloud.core.util.domain.AIAccess;
import net.ibizsys.central.util.IEntityDTO;
import net.ibizsys.central.util.expression.ExpressionUtils;
import net.ibizsys.model.codelist.IPSCodeItem;
import net.ibizsys.model.dataentity.defield.IPSDEField;
import net.ibizsys.runtime.codelist.ICodeListRuntime;
import net.ibizsys.runtime.dataentity.IDataEntityRuntimeContext;
import net.ibizsys.runtime.util.DataTypeUtils;
import net.ibizsys.runtime.util.DateUtils;
import net.ibizsys.runtime.util.JsonUtils;
import net.ibizsys.runtime.util.YamlUtils;

public class AIToolDESyncUtilRuntime extends SysCloudConfigDESyncUtilRuntimeBase{

	private static final Log log = LogFactory.getLog(AIToolDESyncUtilRuntime.class);
	private boolean bRawGet = false;
	private static String mcpPrefix = "mcp";
	private static String mcpBuiltInExtension = "mcp_built_in_extension";
	private static String builtInExtensionUrlFormat = "http://%s:%s/%s/extension/mcp/%s/sse"
	/**
	 * 路径参数：组件标识
	 */
	public final static String UTILPARAM_UTIL = "util";

	/**
	 * 预定义属性：TYPE 工具类型
	 */
	public final static String PREDEFINEDFIELD_TOOL_TYPE = "TOOL_TYPE";

	/**
	 * 预定义属性：API 地址
	 */
	public final static String PREDEFINEDFIELD_API_URL = "API_URL";

	/**
	 * 预定义属性：工具标识
	 */
	public final static String PREDEFINEDFIELD_TOOL_TAG = "TOOL_TAG";

	/**
	 * 预定义属性：TYPE 凭证类型
	 */
	public final static String PREDEFINEDFIELD_API_AUTH_TYPE = "API_AUTH_TYPE";

	/**
	 * 预定义属性：ACCESS_KEY
	 */
	public final static String PREDEFINEDFIELD_ACCESS_KEY = "ACCESS_KEY";

	/**
	 * 预定义属性：SECRET_KEY
	 */
	public final static String PREDEFINEDFIELD_SECRET_KEY = "SECRET_KEY";

	/**
	 * 预定义属性：TOKEN_URL
	 */
	public final static String PREDEFINEDFIELD_TOKEN_URL = "TOKEN_URL";

	/**
	 * 预定义属性：DIGEST/api密钥
	 */
	public final static String PREDEFINEDFIELD_DIGEST = "DIGEST";

	/**
	 * 预定义属性：BEARER_TOKEN
	 */
	public final static String PREDEFINEDFIELD_BEARER_TOKEN = "BEARER_TOKEN";

	/**
	 * 预定义属性：CLIENT_ID
	 */
	public final static String PREDEFINEDFIELD_CLIENT_ID = "CLIENT_ID";

	/**
	 * 预定义属性：CLIENT_SECRET
	 */
	public final static String PREDEFINEDFIELD_CLIENT_SECRET = "CLIENT_SECRET";

	/**
	 * 预定义属性：过期时间
	 */
	public final static String PREDEFINEDFIELD_EXPIRATION_DATE = "EXPIRATION_DATE";

	/**
	 * 预定义属性：凭证状态
	 */
	public final static String PREDEFINEDFIELD_STATUS = "STATUS";

    public final static String PREDEFINEDFIELD_ACTIVE = "active";


	public final static String STATUS_ACTIVE = "active";

	public final static String STATUS_EXPIRED = "expired";

	public final static String STATUS_DISABLED = "disabled";





	@Override
	protected void onInit() throws Exception {
		this.bRawGet = DataTypeUtils.asBoolean(this.getUtilParam("rawget", (String)null), false);
		super.onInit();
	}

	@Override
	protected String getConfig(IDataEntityRuntimeContext iDataEntityRuntimeContext, IEntityDTO iEntityDTO) throws Throwable {
		String strConfig = super.getConfig(iDataEntityRuntimeContext, iEntityDTO);
		if(StringUtils.hasLength(strConfig)) {
			return strConfig;
		}
		Map<String, Object> map = this.getConfigMap(iDataEntityRuntimeContext, iEntityDTO);
		String strToolType = "";
		String strToolTag = "";
		IPSDEField toolTagPSDEField = iDataEntityRuntimeContext.getDataEntityRuntime().getPSDEFieldByTag(PREDEFINEDFIELD_TOOL_TAG, true);
		if(toolTagPSDEField != null) {
			Object toolTag = iEntityDTO.get(toolTagPSDEField.getLowerCaseName());
			if(!ObjectUtils.isEmpty(toolTag)) {
				strToolTag = String.valueOf(toolTag);
			}
		}

		IPSDEField toolTypePSDEField = iDataEntityRuntimeContext.getDataEntityRuntime().getPSDEFieldByTag(PREDEFINEDFIELD_TOOL_TYPE, true);
		if(toolTypePSDEField != null) {
			Object toolType = iEntityDTO.get(toolTypePSDEField.getLowerCaseName());
			if (!ObjectUtils.isEmpty(toolType)) {
				strToolType = String.valueOf(toolType);
			}
		}

		if(!map.containsKey(AIAccess.FIELD_SERVICEURL)) {
			IPSDEField iPSDEField = iDataEntityRuntimeContext.getDataEntityRuntime().getPSDEFieldByTag(PREDEFINEDFIELD_API_URL, true);
			if(iPSDEField != null) {
				Object value = iEntityDTO.get(iPSDEField.getLowerCaseName());
				if(!ObjectUtils.isEmpty(value)) {
					String strValue = String.valueOf(value);
					map.put(AIAccess.FIELD_SERVICEURL, strValue);
				}else if(mcpBuiltInExtension.equals(strToolType)){
					String strBaseUrl = String.format(getBuiltInExtensionUrlFormat(), ServiceHub.getInstance().getIPAddress(), ServiceHub.getInstance().getPort(), this.getSystemRuntime().getServiceId(),strToolTag);
					map.put(AIAccess.FIELD_SERVICEURL, strBaseUrl);
				}
			}
		}

		if(!map.containsKey(PREDEFINEDFIELD_API_AUTH_TYPE)) {
			IPSDEField typePSDEField = iDataEntityRuntimeContext.getDataEntityRuntime().getPSDEFieldByTag(PREDEFINEDFIELD_API_AUTH_TYPE, true);
			if(typePSDEField != null) {
				Object type = iEntityDTO.get(typePSDEField.getLowerCaseName());
				if(!ObjectUtils.isEmpty(type)) {
					String strType = String.valueOf(type);
					map.put(PREDEFINEDFIELD_API_AUTH_TYPE.toLowerCase(), strType);
					if(typePSDEField.getPSCodeList() != null) {
						ICodeListRuntime iCodeListRuntime = this.getSystemRuntime().getCodeListRuntime(typePSDEField.getPSCodeList().getId(), true);
						if(iCodeListRuntime != null) {
							IPSCodeItem iPSCodeItem = iCodeListRuntime.getPSCodeItem(strType, true);
							if(iPSCodeItem!=null && StringUtils.hasLength(iPSCodeItem.getUserData())) {
								map.put(PREDEFINEDFIELD_API_AUTH_TYPE.toLowerCase(), iPSCodeItem.getUserData());
							}
						}
					}
				}
			}
		}

		if(!map.containsKey(Credential.FIELD_ACCESSKEY)) {
			IPSDEField iPSDEField = iDataEntityRuntimeContext.getDataEntityRuntime().getPSDEFieldByTag(PREDEFINEDFIELD_ACCESS_KEY, true);
			if(iPSDEField != null) {
				Object value = iEntityDTO.get(iPSDEField.getLowerCaseName());
				if(!ObjectUtils.isEmpty(value)) {
					String strValue = String.valueOf(value);
					map.put(Credential.FIELD_ACCESSKEY, strValue);
				}
			}
		}

		if(!map.containsKey(Credential.FIELD_SECRETKEY)) {
			IPSDEField iPSDEField = iDataEntityRuntimeContext.getDataEntityRuntime().getPSDEFieldByTag(PREDEFINEDFIELD_SECRET_KEY, true);
			if(iPSDEField != null) {
				Object value = iEntityDTO.get(iPSDEField.getLowerCaseName());
				if(!ObjectUtils.isEmpty(value)) {
					String strValue = String.valueOf(value);
					map.put(Credential.FIELD_SECRETKEY, strValue);
				}
			}
		}

		if(!map.containsKey(Credential.FIELD_TOKENURL)) {
			IPSDEField iPSDEField = iDataEntityRuntimeContext.getDataEntityRuntime().getPSDEFieldByTag(PREDEFINEDFIELD_TOKEN_URL, true);
			if(iPSDEField != null) {
				Object value = iEntityDTO.get(iPSDEField.getLowerCaseName());
				if(!ObjectUtils.isEmpty(value)) {
					String strValue = String.valueOf(value);
					map.put(Credential.FIELD_TOKENURL, strValue);
				}
			}
		}

		if(!map.containsKey(Credential.FIELD_CONTENT)) {
			IPSDEField iPSDEField = iDataEntityRuntimeContext.getDataEntityRuntime().getPSDEFieldByTag(PREDEFINEDFIELD_DIGEST, true);
			if(iPSDEField != null) {
				Object value = iEntityDTO.get(iPSDEField.getLowerCaseName());
				if(!ObjectUtils.isEmpty(value)) {
					String strValue = String.valueOf(value);
					map.put(Credential.FIELD_CONTENT, strValue);
				}
			}
		}

		if(!map.containsKey(Credential.FIELD_ACCESSTOKEN)) {
			IPSDEField iPSDEField = iDataEntityRuntimeContext.getDataEntityRuntime().getPSDEFieldByTag(PREDEFINEDFIELD_BEARER_TOKEN, true);
			if(iPSDEField != null) {
				Object value = iEntityDTO.get(iPSDEField.getLowerCaseName());
				if(!ObjectUtils.isEmpty(value)) {
					String strValue = String.valueOf(value);
					map.put(Credential.FIELD_ACCESSTOKEN, strValue);
				}else if (mcpBuiltInExtension.equals(strToolType)){
					map.put(Credential.FIELD_ACCESSTOKEN, strToolTag);
				}
			}
		}

		if(!map.containsKey(Credential.FIELD_CLIENTID)) {
			IPSDEField iPSDEField = iDataEntityRuntimeContext.getDataEntityRuntime().getPSDEFieldByTag(PREDEFINEDFIELD_CLIENT_ID, true);
			if(iPSDEField != null) {
				Object value = iEntityDTO.get(iPSDEField.getLowerCaseName());
				if(!ObjectUtils.isEmpty(value)) {
					String strValue = String.valueOf(value);
					map.put(Credential.FIELD_CLIENTID, strValue);
				}
			}
		}

		if(!map.containsKey(Credential.FIELD_CLIENTSECRET)) {
			IPSDEField iPSDEField = iDataEntityRuntimeContext.getDataEntityRuntime().getPSDEFieldByTag(PREDEFINEDFIELD_CLIENT_SECRET, true);
			if(iPSDEField != null) {
				Object value = iEntityDTO.get(iPSDEField.getLowerCaseName());
				if(!ObjectUtils.isEmpty(value)) {
					String strValue = String.valueOf(value);
					map.put(Credential.FIELD_CLIENTSECRET, strValue);
				}
			}
		}

		if (!map.containsKey(Credential.FIELD_DISABLED)) {
			map.put(Credential.FIELD_DISABLED, 0);
			IPSDEField activePSDEField = iDataEntityRuntimeContext.getDataEntityRuntime().getPSDEFieldByTag(PREDEFINEDFIELD_ACTIVE, true);
			if (activePSDEField != null) {
				Object active = iEntityDTO.get(activePSDEField.getLowerCaseName());
				if (!ObjectUtils.isEmpty(active)) {
					Boolean bActive = DataTypeUtils.asBoolean(active, true);
					if (!bActive) {
						map.put(Credential.FIELD_DISABLED, 1);
					}
				}
			}
		}

		return this.getConfig(iDataEntityRuntimeContext, map, iEntityDTO);
	}

	protected String getBuildInAccessTokenConfig(IDataEntityRuntimeContext iDataEntityRuntimeContext, IEntityDTO iEntityDTO) throws Throwable {
		String strConfig = super.getConfig(iDataEntityRuntimeContext, iEntityDTO);
		if(StringUtils.hasLength(strConfig)) {
			return strConfig;
		}

		Map<String, Object> map = this.getConfigMap(iDataEntityRuntimeContext, iEntityDTO);

		if(!map.containsKey(AIAccess.FIELD_EXPIRESTIME)) {
			IPSDEField expirationDatePSDEField = iDataEntityRuntimeContext.getDataEntityRuntime().getPSDEFieldByTag(PREDEFINEDFIELD_EXPIRATION_DATE, true);
			if(expirationDatePSDEField != null) {
				Object expirationDate = iEntityDTO.get(expirationDatePSDEField.getLowerCaseName());
				if(expirationDate != null) {
					if(expirationDate instanceof String) {
						map.put(AIAccess.FIELD_EXPIRESTIME, expirationDate);
					}
					else
					if(expirationDate instanceof Date) {
						map.put(AIAccess.FIELD_EXPIRESTIME, DateUtils.toDateTimeString((Date)expirationDate));
					}
					else
					{
						try {
							map.put(AIAccess.FIELD_EXPIRESTIME, DateUtils.toDateTimeString(DataTypeUtils.asDateTime(expirationDate)));
						}
						catch (Throwable ex) {
							log.error(String.format("过期时间[%1$s]类型不支持", expirationDate));
						}
					}
				}
			}
		}

		return this.getConfig(iDataEntityRuntimeContext, map, iEntityDTO);
	}
	protected String getConfig(IDataEntityRuntimeContext iDataEntityRuntimeContext, Map<String, Object> map, IEntityDTO iEntityDTO) throws Throwable {
		return YamlUtils.toString(map);
	}


	@Override
	protected String getCloudConfigId(IDataEntityRuntimeContext iDataEntityRuntimeContext, Map<String, Object> map, IEntityDTO iEntityDTO) throws Exception {
		if (!map.containsKey(PARAM_KEY)) {
			IPSDEField toolTagPSDEField = iDataEntityRuntimeContext.getDataEntityRuntime().getPSDEFieldByTag(PREDEFINEDFIELD_TOOL_TAG, true);
			if(toolTagPSDEField != null) {
				Object toolTag = iEntityDTO.get(toolTagPSDEField.getLowerCaseName());
				if(!ObjectUtils.isEmpty(toolTag)) {
					String strToolTag = String.valueOf(toolTag);
					map.put(PARAM_KEY, strToolTag);
				}
			}
		}

		if(!map.containsKey(UTILPARAM_UTIL)) {
			map.put(UTILPARAM_UTIL, this.getUtilParam(UTILPARAM_UTIL, "unknown"));
		}

		return super.getCloudConfigId(iDataEntityRuntimeContext, map, iEntityDTO);
	}

	protected String getBuildInCloudAccessTokenId(IDataEntityRuntimeContext iDataEntityRuntimeContext, Map<String, Object> map, IEntityDTO iEntityDTO) throws Exception {
		if (!map.containsKey(PARAM_KEY)) {
			IPSDEField toolTagPSDEField = iDataEntityRuntimeContext.getDataEntityRuntime().getPSDEFieldByTag(PREDEFINEDFIELD_TOOL_TAG, true);
			if(toolTagPSDEField != null) {
				Object toolTag = iEntityDTO.get(toolTagPSDEField.getLowerCaseName());
				if(!ObjectUtils.isEmpty(toolTag)) {
					String strToolTag = String.valueOf(toolTag);
					map.put(PARAM_KEY, strToolTag);
					map.put(AIAccess.FIELD_ACCESSTOKEN, strToolTag);
				}
			}
		}

		if(!map.containsKey(UTILPARAM_UTIL)) {
			map.put(UTILPARAM_UTIL, this.getUtilParam(UTILPARAM_UTIL, "unknown"));
		}
		if(!map.containsKey(PARAM_SYSTEM)) {
			map.put(PARAM_SYSTEM, this.getSystemRuntime().getDeploySystemId());
		}
		return ExpressionUtils.getValue(this.getDefaultCloudAccessTokenFormat(iDataEntityRuntimeContext), map).toLowerCase();
	}

	protected void onAfterCreate(IDataEntityRuntimeContext iDataEntityRuntimeContext, IPSDEAction iPSDEAction, IEntityDTO iEntityDTO) throws Throwable {
		Map<String, Object> map = new LinkedHashMap<String, Object>();
		IPSDEField toolTypePSDEField = iDataEntityRuntimeContext.getDataEntityRuntime().getPSDEFieldByTag(PREDEFINEDFIELD_TOOL_TYPE, true);
		if(toolTypePSDEField != null) {
			Object toolType = iEntityDTO.get(toolTypePSDEField.getLowerCaseName());
			if(!ObjectUtils.isEmpty(toolType)) {
				String strToolType = String.valueOf(toolType);
				if (strToolType.equals(mcpBuiltInExtension)) {
					if (this.bRawGet) {
						IEntityDTO rawEntityDTO = ((IDataEntityRuntime) iDataEntityRuntimeContext.getDataEntityRuntime()).rawGet(iDataEntityRuntimeContext.getDataEntityRuntime().getKeyFieldValue(iEntityDTO));
						String strConfigId = this.getBuildInCloudAccessTokenId(iDataEntityRuntimeContext, map, rawEntityDTO);
						String strConfig = this.getBuildInAccessTokenConfig(iDataEntityRuntimeContext, rawEntityDTO);
						ServiceHub.getInstance().publishConfig(strConfigId, strConfig);
					} else {
						String strConfigId = this.getBuildInCloudAccessTokenId(iDataEntityRuntimeContext, map, iEntityDTO);
						String strConfig = this.getBuildInAccessTokenConfig(iDataEntityRuntimeContext, iEntityDTO);
						ServiceHub.getInstance().publishConfig(strConfigId, strConfig);
					}
				}else if(!strToolType.startsWith(mcpPrefix)) {
					return;
				}
			}
		}


		super.onAfterCreate(iDataEntityRuntimeContext, iPSDEAction, iEntityDTO);
	}

	protected void onAfterUpdate(IDataEntityRuntimeContext iDataEntityRuntimeContext, IPSDEAction iPSDEAction, IEntityDTO iEntityDTO) throws Throwable {
		Map<String, Object> map = new LinkedHashMap<String, Object>();
		IPSDEField toolTypePSDEField = iDataEntityRuntimeContext.getDataEntityRuntime().getPSDEFieldByTag(PREDEFINEDFIELD_TOOL_TYPE, true);
		if(toolTypePSDEField != null) {
			Object toolType = iEntityDTO.get(toolTypePSDEField.getLowerCaseName());
			if (!ObjectUtils.isEmpty(toolType)) {
				String strToolType = String.valueOf(toolType);
				if (strToolType.equals(mcpBuiltInExtension)) {
					if (this.bRawGet) {
						IEntityDTO rawEntityDTO = ((IDataEntityRuntime) iDataEntityRuntimeContext.getDataEntityRuntime()).rawGet(iDataEntityRuntimeContext.getDataEntityRuntime().getKeyFieldValue(iEntityDTO));
						String strConfigId = this.getBuildInCloudAccessTokenId(iDataEntityRuntimeContext, map, rawEntityDTO);
						String strConfig = this.getBuildInAccessTokenConfig(iDataEntityRuntimeContext, rawEntityDTO);
						ServiceHub.getInstance().publishConfig(strConfigId, strConfig);
					} else {
						String strConfigId = this.getBuildInCloudAccessTokenId(iDataEntityRuntimeContext, map, iEntityDTO);
						String strConfig = this.getBuildInAccessTokenConfig(iDataEntityRuntimeContext, iEntityDTO);
						ServiceHub.getInstance().publishConfig(strConfigId, strConfig);
					}
				}else if(!strToolType.startsWith(mcpPrefix)) {
					return;
				}
			}
		}
		super.onAfterUpdate(iDataEntityRuntimeContext, iPSDEAction, iEntityDTO);
	}

	protected void onBeforeRemove(IDataEntityRuntimeContext iDataEntityRuntimeContext, IPSDEAction iPSDEAction, IEntityDTO iEntityDTO) throws Throwable {
		Map<String, Object> map = new LinkedHashMap<String, Object>();
		IPSDEField toolTypePSDEField = iDataEntityRuntimeContext.getDataEntityRuntime().getPSDEFieldByTag(PREDEFINEDFIELD_TOOL_TYPE, true);
		if(toolTypePSDEField != null) {
			Object toolType = iEntityDTO.get(toolTypePSDEField.getLowerCaseName());
			if (!ObjectUtils.isEmpty(toolType)) {
				String strToolType = String.valueOf(toolType);
				if (strToolType.equals(mcpBuiltInExtension)) {
					//同步移除
					if (this.bRawGet) {
						IEntityDTO rawEntityDTO = ((IDataEntityRuntime) iDataEntityRuntimeContext.getDataEntityRuntime()).rawGet(iDataEntityRuntimeContext.getDataEntityRuntime().getKeyFieldValue(iEntityDTO));
						String strConfigId = this.getBuildInCloudAccessTokenId(iDataEntityRuntimeContext, map, rawEntityDTO);
						ServiceHub.getInstance().removeConfig(strConfigId);
					} else {
						String strConfigId = this.getBuildInCloudAccessTokenId(iDataEntityRuntimeContext, map, iEntityDTO);
						ServiceHub.getInstance().removeConfig(strConfigId);
					}
				}else if(!strToolType.startsWith(mcpPrefix)) {
					return;
				}
			}
		}
		super.onBeforeRemove(iDataEntityRuntimeContext, iPSDEAction, iEntityDTO);
	}
	@Override
	protected String getDefaultCloudConfigIdFormat(IDataEntityRuntimeContext iDataEntityRuntimeContext) throws Exception {
		return "cloud-ai-mcp-{key}";
	}
	
	protected String getDefaultCloudAccessTokenFormat(IDataEntityRuntimeContext iDataEntityRuntimeContext) throws Exception {
		return "accesstoken-{system}-sysutil-extension_mcp_{key}--{accesstoken}";
	}

	protected String getBuiltInExtensionUrlFormat() throws Exception {
		return builtInExtensionUrlFormat;
	}
}

```
### CredentialDESyncUtilRuntime :id=CredentialDESyncUtilRuntime


```net.ibizsys.central.plugin.util.sysutil.CredentialDESyncUtilRuntime```

```groovy
null
```
### DataRecordDataEntityRuntime :id=DataRecordDataEntityRuntime
cn.ibizlab.user.plugin.groovy.dataentity.DataRecordDataEntityRuntime

```cn.ibizlab.user.plugin.groovy.dataentity.DataRecordDataEntityRuntime```

```groovy
package cn.ibizlab.user.plugin.groovy.dataentity

import groovy.sql.Sql
import groovy.json.JsonOutput
import groovy.json.JsonSlurper
import net.ibizsys.central.dataentity.IDataEntityRuntime
import net.ibizsys.central.plugin.util.dataentity.DynaDataEntityRuntime
import net.ibizsys.central.util.IEntityDTO
import net.ibizsys.model.dataentity.action.IPSDEAction
import net.ibizsys.runtime.util.JsonUtils
import net.ibizsys.runtime.util.KeyValueUtils
import org.postgresql.util.PGobject

import javax.sql.DataSource

class DataRecordDataEntityRuntime extends DynaDataEntityRuntime{

    private DataSource dataSource
    private static final Set<String> NATIVE_COLUMNS = [
            '_create_time', '_enabled', '_id', '_key',
            '_metadata', '_ner_flag', '_owner', '_region',
            '_summary', '_title', '_update_time', '_resource_id'
    ] as Set

    @Override
    protected Object doExecuteActionReal(String strActionName, IPSDEAction iPSDEAction, Object[] args, Object actionData) throws Throwable {
        if (strActionName.equalsIgnoreCase("upsert")||strActionName.equalsIgnoreCase("upsert_batch")
                ||strActionName.equalsIgnoreCase("update")
                ||strActionName.equalsIgnoreCase("create")
                ||strActionName.equalsIgnoreCase("save")) {
            upsert(args[0])
            return args[0]
        } else if (strActionName.equalsIgnoreCase("get")) {
            return getData(args[0])
        }else if (strActionName.equalsIgnoreCase("find_kb_id")) {
            return findKbId(args[0])
        }
        return super.doExecuteActionReal(strActionName, iPSDEAction, args, actionData)
    }

    /**
     * UPSERT 方法：已修复 hstore 错误和 ambiguous 错误
     */
    void upsert(Object input) {
        def list = input instanceof List ? input : [input]
        def sql = new Sql(net.ibizsys.central.cloud.core.spring.rt.ServiceHub.getInstance().getDataSource(this.getSysDBSchemeRuntime().getDataSourceTag(), true))

        List<String> ids = new ArrayList<>()

        try {
            list.each { dto ->
                // 1. _id 预处理
                def _id = dto.any().get('_id')
                if (!_id)
                    _id = KeyValueUtils.genMD5(dto.any().get('_resource_id') + "||" + dto.any().get('_key'))

                Map entry = new HashMap()
                if (dto instanceof IEntityDTO) {
                    dto.set("_id", _id)
                    ((IEntityDTO) dto).copyTo(entry)
                } else if (dto instanceof Map) {
                    entry.put("_id", _id)
                    entry.putAll(dto)
                } else
                    return

                if (!entry['_resource_id'] || !entry['_key']) {
                    log.error("未提供_id或_resource_id+_key")
                    return
                }

                // 2. 核心状态赋值
                def currentTime = new java.sql.Timestamp(System.currentTimeMillis())
                entry['_update_time'] = currentTime
                entry['_create_time'] = currentTime
                entry['_enabled'] = 1

                // 3. 字段分拣 (修正点：跳过 _metadata，统一在后面处理)
                Map insertNative = [:]
                Map updateNative = [:]
                Map metadata = [:]

                entry.each { k, v ->
                    // 增加 k != '_metadata' 判断，防止重复
                    if (NATIVE_COLUMNS.contains(k) && k != '_metadata') {
                        def processedValue = (v instanceof Map || v instanceof List) ? toPGobject(v) : v

                        insertNative[k] = processedValue
                        if (k != '_id' && k != '_create_time') {
                            updateNative[k] = processedValue
                        }
                    } else if (!NATIVE_COLUMNS.contains(k)) {
                        // 只有非原生列才进这个 metadata 暂存区
                        metadata[k] = v
                    }
                }

                // 4. 构建 SQL 元素
                def insertCols = insertNative.keySet().toList()
                def insertValues = insertNative.values().toList()

                def setClauses = updateNative.keySet().collect { "${it} = ?" }
                def updateParams = updateNative.values().toList()

                // 处理 metadata (这里是 _metadata 唯一进入 SQL 的地方)
                if (!metadata.isEmpty()) {
                    def pgMeta = toPGobject(metadata)
                    insertCols << "_metadata"
                    insertValues << pgMeta

                    setClauses << "_metadata = COALESCE(data_record._metadata, '{}'::jsonb) || ?"
                    updateParams << pgMeta
                }

                // 5. 组装最终 SQL
                def placeholders = (1..insertCols.size()).collect { '?' }.join(", ")
                def upsertSql = """
                    INSERT INTO data_record (${insertCols.join(", ")})
                    VALUES (${placeholders})
                    ON CONFLICT (_id) 
                    DO UPDATE SET ${setClauses.join(", ")}
                """



                // 执行
                sql.execute(upsertSql, insertValues + updateParams)
                ids.add(_id)

                //生成知识库
                def resource_id = entry.get("_resource_id")
                if(resource_id){
                    IDataEntityRuntime catSettingDERuntime = this.getSystemRuntime().getDataEntityRuntime("CATEGORY_SETTINGS")
                    def filter = catSettingDERuntime.createSearchContext()
                    filter.eq("resource_id",resource_id)
                    def catgSettings = catSettingDERuntime.select(filter)
                    catgSettings.forEach {catSeting ->
                        try{
                            String type = catSeting.getString("auto_gen_kb", "")
                            String category_id = catSeting.getString("category_id", "")

                            //生成知识库
                            if("none".equals(type)){
                                return
                            }else if("record".equals(type)){
                                IEntityDTO tempKb = findKbId(_id)
                                String kb_id = tempKb.getString("kb_id", "")
                                if(tempKb.get("_update") == 0){
                                    addRecordKb(kb_id, _id, category_id, entry)
                                }
                                addRecordKbDoc(kb_id, _id, entry)
                            }else if("resource".equals(type)){

                            }
                            //生成对应知识库文档

                        }
                        catch (Exception ex) {
                            log.error("知识库文档解析失败："+doc.get("id"))
                        }

                    }
                }

            }
        } finally {
            sql.close()
        }

        IDataEntityRuntime docDERuntime = this.getSystemRuntime().getDataEntityRuntime("AI_KB_DOCUMENT")
        def filter = docDERuntime.createSearchContext()
        filter.eq("source_type","DATA_RECORD")
        filter.in("source_id",ids)
        def docs = docDERuntime.select(filter)
        docs.forEach {doc ->
            try{
                docDERuntime.executeAction("parse", null, [doc]);
            }
            catch (Exception ex) {
                try{
                    log.error("知识库文档解析失败："+doc.get("id"))
                }
                catch (Exception ex2) {

                }
            }

        }
    }

    protected void addRecordKb(String kb_id, String record_id, String category_id, Map entry){
        try{
            IDataEntityRuntime kbDERuntime = this.getSystemRuntime().getDataEntityRuntime("AI_KNOWLEDGE_BASE")
            IEntityDTO kbDto = kbDERuntime.createEntity()
            String org_id = entry["_origin_region"] ?: entry["_region"]
            String name = entry["_origin_title"] ?: entry["_title"]
            String key = entry["_origin_key"] ?: entry["_key"]
            String description = entry["_origin_summary"] ?: entry["_summary"]
            if(description.length() > 2000){
                description = description.substring(0, 2000)
            }
            String guidance_prompt = String.format("%s:%s", name, description)
            if(guidance_prompt.length() > 2000){
                guidance_prompt = guidance_prompt.substring(0, 2000)
            }
            kbDto.set("id", kb_id)
            kbDto.set("name", name)
            kbDto.set("visibility", "private")
            kbDto.set("status", "0")
            kbDto.set("scope_type", "organization")
            kbDto.set("scope_id", org_id)
            kbDto.set("key", key)
            kbDto.set("record_id", record_id)
            kbDto.set("description", description)
            kbDto.set("guidance_prompt", guidance_prompt)
            kbDto.set("category_id", category_id)
            kbDERuntime.create(kbDto)
        }
        catch (Exception ex) {
            log.error(String.format("DataRecord[%s]同步记录知识库[%s]失败，错误原因：%s", record_id, kb_id, ex.getMessage()))
        }
    }

    protected void addRecordKbDoc(String kb_id, String record_id, Map entry){
        IDataEntityRuntime docDERuntime = this.getSystemRuntime().getDataEntityRuntime("AI_KB_DOCUMENT")
        def filter = docDERuntime.createSearchContext()
        filter.eq("id", record_id)
        def docs = docDERuntime.select(filter)
        if(docs.size() == 0){
            IEntityDTO docDto = docDERuntime.createEntity()

            String name = entry["_origin_title"] ?: entry["_title"]
            String key = entry["_origin_key"] ?: entry["_key"]
            String resource_id = entry["_resource_id"]
            String resource_name = entry["_resource_name"]

            docDto.set("id", record_id)
            docDto.set("name", name)
            docDto.set("key", key)
            docDto.set("type", resource_id)
            docDto.set("resource", resource_name)
            docDto.set("source_type", "DATA_RECORD")
            docDto.set("source_id", record_id)
            docDto.set("sequence", 0)
            docDto.set("status", 0)
            docDto.set("active", 1)
            docDto.set("kb_id", kb_id)
            docDto.set("custom_chunk", 0)
            docDERuntime.create(docDto)
        }

    }

    IEntityDTO getData(String id) {
        def sql = new Sql(net.ibizsys.central.cloud.core.spring.rt.ServiceHub.getInstance().getDataSource(this.getSysDBSchemeRuntime().getDataSourceTag(),true))
        try {
            def row = sql.firstRow("SELECT t1.* FROM data_record t1  WHERE  t1. _id = ? and t1._enabled = 1", [id])
            if (!row) return null

            Map result = [:]
            Map metadata = [:]

            row.each { k, v ->
                if (k == '_metadata' && v != null) {
                    metadata = new HashMap( new JsonSlurper().parseText(v.toString()))
                } else {
                    result[k] = v
                }
            }

            IEntityDTO dto = this.createEntity()
            result['_metadata'] = metadata
            dto.from(result)
            dto.any().putAll(metadata)
            String resource_id = dto.get("_resource_id")
            if(resource_id) {
                IEntityDTO resource = getResource(resource_id)
                if(resource) {
                    dto.set("_resource_name",resource.get("name"))
                    dto.set("_resource_code",resource.get("resource_code"))
                    dto.set("_schema",resource.get("schema_def"))
                }
            }

            return dto
        } finally {
            sql.close()
        }
    }

    private Map<String,IEntityDTO> cacheResource = new LinkedHashMap<>()

    private IEntityDTO getResource(String resource_id) {

        IEntityDTO resource = cacheResource.get(resource_id);
        if (resource != null) {
            long cacheTime = resource.get("_cache_time");
            if (System.currentTimeMillis() - cacheTime <= 10 * 60 * 1000) {
                return resource;
            }
        }
        synchronized (this) {
            resource = cacheResource.get(resource_id);
            if (resource != null) {
                long cacheTime = resource.get("_cache_time");
                if (System.currentTimeMillis() - cacheTime <= 10 * 60 * 1000) {
                    return resource;
                }
            }
            else{
                IDataEntityRuntime resourceDERuntime = this.getSystemRuntime().getDataEntityRuntime("DATA_RESOURCE")
                resource = resourceDERuntime.get(resource_id)
                resource.set("_cache_time",System.currentTimeMillis())
                resource.set("schema_def", JsonUtils.asMap(resource.get("schema")))
                cacheResource.put(resource_id,resource)

            }
        }
        return resource
    }

    private PGobject toPGobject(Object obj) {
        if (obj == null) return null
        def pgObj = new PGobject()
        pgObj.type = "jsonb"
        pgObj.value = JsonOutput.toJson(obj)
        return pgObj
    }

    IEntityDTO findKbId(Object input) {
        def record_id = input instanceof IEntityDTO ? input.get('_id') : input
        def kb_id = KeyValueUtils.genUniqueId()
        def _update = 0
        IDataEntityRuntime kbDERuntime = this.getSystemRuntime().getDataEntityRuntime("AI_KNOWLEDGE_BASE")
        def filter = kbDERuntime.createSearchContext()
        filter.eq("record_id", record_id)
        def kbs = kbDERuntime.select(filter)
        if (kbs != null && !kbs.isEmpty()) {
            kb_id = kbs[0].get('id')
            _update = 1
        }

        IEntityDTO dto = this.createEntity()
        dto.set("kb_id", kb_id)
        dto.set("_update", _update)
        return dto;
    }

}
```
### DefaultSysDETaskUtilRuntime :id=DefaultSysDETaskUtilRuntime


```net.ibizsys.central.plugin.task.sysutil.DefaultSysDETaskUtilRuntime```

```groovy
null
```
### ExtractAndStoreDEActionRuntime :id=ExtractAndStoreDEActionRuntime


```cn.ibizlab.user.plugin.groovy.dataentity.action.ExtractAndStoreDEActionRuntime```

```groovy
package cn.ibizlab.user.plugin.groovy.dataentity.action;

import groovy.transform.CompileStatic
import net.ibizsys.central.dataentity.action.DEActionRuntimeBase;
import net.ibizsys.central.util.IEntityDTO;
import java.text.SimpleDateFormat

@CompileStatic
class ExtractAndStoreDEActionRuntime extends DEActionRuntimeBase {
    private static final SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss")

    @Override
    protected Object onExecute(IEntityDTO iEntityDTO) throws Throwable {
        return iEntityDTO;
    }
}
```
### ExtractMetaDataDEActionRuntime :id=ExtractMetaDataDEActionRuntime


```cn.ibizlab.user.plugin.groovy.dataentity.action.ExtractMetaDataDEActionRuntime```

```groovy
package cn.ibizlab.user.plugin.groovy.dataentity.action

import net.ibizsys.model.util.JsonUtils
import groovy.transform.CompileStatic
import net.ibizsys.central.dataentity.action.DEActionRuntimeBase
import net.ibizsys.central.util.IEntityDTO
import com.vladsch.flexmark.ast.Image;
import com.vladsch.flexmark.ast.Link;
import com.vladsch.flexmark.parser.Parser;
import com.vladsch.flexmark.util.ast.Document;
import com.vladsch.flexmark.util.ast.NodeVisitor;
import com.vladsch.flexmark.util.ast.VisitHandler
import groovy.json.JsonSlurper
import java.text.SimpleDateFormat

@CompileStatic
class ExtractMetaDataDEActionRuntime extends DEActionRuntimeBase {
    private static final SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss")

    @Override
    protected Object onExecute(IEntityDTO iEntityDTO) throws Throwable {
        def parsed_content = iEntityDTO.get('parsed_content').toString()
        if (parsed_content) {
            def meta_data = [:]
            def references = []
            // 解析Markdown内容
            Parser parser = Parser.builder().build()
            Document document = parser.parse(parsed_content)
            // 收集所有图片节点
            List<Image> images = []
            NodeVisitor imageCollector = new NodeVisitor(new VisitHandler<>(Image, images.&add))
            imageCollector.visit(document)

            // 收集所有链接节点
            List<Link> links = []
            NodeVisitor linkCollector = new NodeVisitor(new VisitHandler<>(Link, links.&add))
            linkCollector.visit(document)

            // 处理图片
            images.each { image ->
                def path = image.getUrl().toString()
                def name = image.getText().toString()
                def position = image.getLineNumber()
                def source_markdown = image.getChars().toString()
                references.add([
                        type: "image",
                        path: path,
                        name: name,
                        position: position,
                        source_markdown: source_markdown
                ])
            }

            // 处理链接（仅包含/ibizutil/download）
            links.each { link ->
                def path = link.getUrl().toString()
                // 仅处理包含指定路径的链接
                if (path.contains("/ibizutil/download")) {
                    def name = link.getText().toString()
                    def position = link.getLineNumber()
                    def source_markdown = link.getChars().toString()
                    references.add([
                            type: "url",
                            path: path,
                            name: name,
                            position: position,
                            source_markdown : source_markdown
                    ])
                }
            }

            // 更新_meta_data
            def sourceType = iEntityDTO.get('source_type')
            meta_data.put('source_type', sourceType)
            def _type = iEntityDTO.get('type')
            if (_type == 'file'){
                def fileJson = iEntityDTO.get('file').toString()
                def file = new JsonSlurper().parseText(fileJson)as ArrayList
                def fileName = file[0].getAt("name")
                def fileType = iEntityDTO.get('file_type').toString()
                def fileSize = file[0].getAt("size")
                meta_data.put('file_size', fileSize)
                meta_data.put('file_type', fileType)
                meta_data.put('title', fileName)
                meta_data.put('source_type', "file")
            }
            def now = new Date()
            def nowStr = sdf.format(now)
            meta_data.put('parsed_at', nowStr)
            meta_data.put('references', references)
            def metaDataJson = JsonUtils.getMapper().writerWithDefaultPrettyPrinter().writeValueAsString(meta_data);
            iEntityDTO.set('meta_data', metaDataJson)
        }
        return iEntityDTO;
    }
}
```
### DynaDataEntityRuntime :id=GLOBAL_DATAENTITYRUNTIME
全局实体运行时插件

```net.ibizsys.central.plugin.util.dataentity.DynaDataEntityRuntime```

```groovy
null
```
### InstallSpecDEActionRuntime :id=InstallSpecDEActionRuntime


```cn.ibizlab.plm.user.plugin.groovy.dataentity.action.InstallSpecDEActionRuntime```

```groovy
package cn.ibizlab.plm.user.plugin.groovy.dataentity.action

import com.fasterxml.jackson.databind.JsonNode
import com.fasterxml.jackson.databind.node.ArrayNode
import net.ibizsys.central.cloud.core.spring.rt.ServiceHub
import net.ibizsys.central.cloud.core.util.domain.V2System
import net.ibizsys.central.cloud.core.util.domain.V2SystemMerge
import net.ibizsys.central.cloud.core.util.domain.V2SystemSource
import net.ibizsys.central.cloud.core.util.domain.V2SystemVersion
import net.ibizsys.central.cloud.core.util.domain.V2SystemVersionType
import net.ibizsys.central.plugin.extension.psmodel.service.PSCorePrdFuncRTService
import net.ibizsys.central.plugin.extension.psmodel.util.IExtensionPSModelRTServiceSession
import net.ibizsys.central.plugin.extension.sysutil.HubSysExtensionUtilRuntime
import net.ibizsys.central.plugin.extension.sysutil.ISysExtensionUtilRuntime
import net.ibizsys.central.plugin.util.dataentity.action.DEActionRuntimeBase
import net.ibizsys.central.util.IEntityDTO
import net.ibizsys.central.util.SearchContextDTO
import net.ibizsys.psmodel.core.domain.PSCorePrdFunc
import net.ibizsys.psmodel.core.util.IPSModelServiceSession
import net.ibizsys.psmodel.core.util.PSModelServiceSession
import net.ibizsys.psmodel.core.util.PSModels
import net.ibizsys.psmodel.runtime.util.PSModelRTServiceFactory
import net.ibizsys.runtime.util.JsonUtils
import net.ibizsys.runtime.util.ZipUtils
import org.apache.commons.io.FileUtils
import org.apache.commons.logging.LogFactory
import org.eclipse.jgit.api.CloneCommand
import org.eclipse.jgit.api.Git
import org.eclipse.jgit.api.PullCommand
import org.eclipse.jgit.api.errors.CheckoutConflictException
import org.eclipse.jgit.api.errors.WrongRepositoryStateException
import org.eclipse.jgit.internal.storage.file.FileRepository
import org.springframework.data.domain.Page
import org.springframework.util.DigestUtils
import org.springframework.util.ObjectUtils
import org.springframework.util.StringUtils
import org.yaml.snakeyaml.Yaml
import org.apache.commons.compress.utils.IOUtils


import java.nio.file.Paths
import java.util.zip.ZipInputStream


public class InstallSpecDEActionRuntime extends DEActionRuntimeBase {
    private static final org.apache.commons.logging.Log log = LogFactory.getLog(InstallSpecDEActionRuntime.class);

    private HubSysExtensionUtilRuntime hubSysExtensionUtilRuntime ;

    private HubSysExtensionUtilRuntime getHubSysExtensionUtilRuntime() {
        if(hubSysExtensionUtilRuntime == null) {
            ISysExtensionUtilRuntime iSysExtensionUtilRuntime = this.getSystemRuntime().getSysUtilRuntime(ISysExtensionUtilRuntime.class, false);
            if(iSysExtensionUtilRuntime instanceof HubSysExtensionUtilRuntime ) {
                hubSysExtensionUtilRuntime = (HubSysExtensionUtilRuntime) iSysExtensionUtilRuntime;
            }
        }
        return hubSysExtensionUtilRuntime;
    }


    @Override
    protected Object onExecute(IEntityDTO entity) throws Throwable {


        IPSModelServiceSession iPSModelServiceSession = getHubSysExtensionUtilRuntime().createPSModelServiceSession(this.getSystemRuntime());
        IPSModelServiceSession lastPSModelServiceSession = PSModelServiceSession.getCurrent(true);

        PSModelRTServiceFactory lastPSModelRTServiceFactory = PSModelRTServiceFactory.getCurrent(true);
        PSModelRTServiceFactory.setCurrent(getHubSysExtensionUtilRuntime().getPSModelRTServiceFactory(this.getSystemRuntime()));
        PSModelServiceSession.setCurrent(iPSModelServiceSession);
        try{


            PSCorePrdFuncRTService service = (PSCorePrdFuncRTService) iPSModelServiceSession.getPSModelService(PSModels.PSCOREPRDFUNC);
            PSCorePrdFunc m = service.getDomain(entity);
            String specVersion = entity.getString("version","latest").toLowerCase();
            String majorSystemId =  this.getSystemRuntime().getV2DeploySystem().getSystemId();

            String strHttpUrlToRepo = entity.getString("http_url_to_repo",entity.getString("httpurltorepo",""))
            String strBranch = entity.getString("default_branch",entity.getString("defaultbranch",""))
            String zipfile = entity.getString("zipfile","")
            if(StringUtils.hasLength(zipfile)) {
                JsonNode node = JsonUtils.toJsonNode(zipfile);
                if(node instanceof ArrayNode) {
                    node = ((ArrayNode)node).get(0);
                }
                net.ibizsys.runtime.util.domain.File ossFile = JsonUtils.as(node, net.ibizsys.runtime.util.domain.File.class);
                m.set("ossfile",ossFile)
            }
            m.setHttpUrlToRepo(strHttpUrlToRepo)

            m.set("default_branch",strBranch)

            if (!specVersion.equalsIgnoreCase("latest")) {
                if (!StringUtils.hasLength(m.getPSCorePrdFuncId())) {
                    m.setPSCorePrdFuncId("${m.getFuncType()}.${majorSystemId}.${m.getFuncSN()}");
                }
                PSCorePrdFunc existFunc = null;
                try {
                    existFunc = service.get(m.getPSCorePrdFuncId(),false)
                }catch (Exception ex) {
                    existFunc = new PSCorePrdFunc()
                    m.copyTo(existFunc)
                }

                V2System v2System = service.getV2SystemIf(existFunc);
                if(v2System!=null) {
                    List<V2SystemVersion> v2SystemVersionList = new ArrayList<V2SystemVersion>();

                    Map<String, V2SystemVersion> v2SystemVersionMap = new HashMap<String, V2SystemVersion>();
                    if (true) {
                        SearchContextDTO searchContextDTO = new SearchContextDTO();
                        searchContextDTO.all();
                        // searchContextDTO.eq(V2SystemVersion.FIELD_TYPE, "CORE");
                        Page<V2SystemVersion> v2SystemVersionPage = getHubSysExtensionUtilRuntime().getCloudExtensionClient().fetchSystemVersions(v2System.getId(), searchContextDTO);
                        if (!ObjectUtils.isEmpty(v2SystemVersionPage) && !ObjectUtils.isEmpty(v2SystemVersionPage.getContent())) {
                            v2SystemVersionList.addAll(v2SystemVersionPage.getContent());
                            for (V2SystemVersion v2SystemVersion : v2SystemVersionPage.getContent()) {
                                if (V2SystemVersionType.CORE.value.equals(v2SystemVersion.getType())) {
                                    v2SystemVersionMap.put(v2SystemVersion.getName().toLowerCase(), v2SystemVersion);
                                }
                            }
                        }
                    }
                    V2SystemVersion v2SystemVersion = v2SystemVersionMap.get(specVersion);
                    if(v2SystemVersion == null) {
                        v2SystemVersion = new V2SystemVersion();
                        v2SystemVersion.setType(V2SystemVersionType.CORE.value);
                        v2SystemVersion.setName(specVersion);

                        net.ibizsys.runtime.util.domain.File ossFile = m.get("ossfile");

                        V2SystemSource v2SystemSource = getSystemSource(v2System, m.getHttpUrlToRepo(),(String)m.get("default_branch"),ossFile,specVersion);

                        v2SystemVersion.setSystemSourceId(v2SystemSource.getId());
                        v2SystemVersion = getHubSysExtensionUtilRuntime().getCloudExtensionClient().createSystemVersion(v2System.getId(), v2SystemVersion);
                    }

                    String systemSourceId = v2SystemVersion.getSystemSourceId();
                    m.set(V2SystemMerge.FIELD_MERGE_SYSTEM_SOURCE_ID,systemSourceId);

                }
            }
            service.install(m);
            return entity;

        } finally {
            PSModelServiceSession.setCurrent(lastPSModelServiceSession);
            PSModelRTServiceFactory.setCurrent(lastPSModelRTServiceFactory);
        }
    }


    def processOssFile(net.ibizsys.runtime.util.domain.File ossFile) {
        def inputStream = null
        def zipInputStream = null

        try {
            
            if(!StringUtils.hasLength(ossFile.getOSSId()))
                ossFile.setOSSId(ossFile.getFileId());

            net.ibizsys.runtime.util.domain.File tempFile = this.getSystemRuntime().getSysFileUtilRuntime().getOSSFile(ossFile.getOSSId(), ossFile.getFolder(), true);

            // 获取输入流
            inputStream = this.getSystemRuntime()
                    .getSysFileUtilRuntime(false)
                    .getInputStream(tempFile)

            // 将流复制到字节数组
            def byteArrayOutputStream = new ByteArrayOutputStream()
            IOUtils.copy(inputStream, byteArrayOutputStream)
            def byteArray = byteArrayOutputStream.toByteArray()

            // 计算MD5并设置
            def md5Hex = DigestUtils.md5DigestAsHex(byteArray)
            println "计算得到的MD5: ${md5Hex}"
            ossFile.setDigestCode(md5Hex)  // 设置到ossFile对象

            // 检查ZIP根目录是否有系统模型文件
            zipInputStream = new ZipInputStream(new ByteArrayInputStream(byteArray))
            def zipEntry = zipInputStream.getNextEntry()
            def foundFiles = []

            while (zipEntry != null) {
                def entryName = zipEntry.name

                // 只检查根目录文件
                if (!entryName.contains("/") && !entryName.contains("\\")) {
                    if (entryName == "ibizmodel.yaml"   ||
                            entryName == "PSSYSTEM.json") {
                        foundFiles << entryName
                    }
                }

                zipEntry = zipInputStream.getNextEntry()
            }

            if (foundFiles.isEmpty()) {
                throw new RuntimeException("ZIP包不合法：根目录未找到系统模型文件(ibizmodel.yaml或PSSYSTEM.json)")
            }

            println "ZIP包校验通过，找到系统模型文件: ${foundFiles.join(', ')}"
            return true

        } finally {
            IOUtils.closeQuietly(zipInputStream)
            IOUtils.closeQuietly(inputStream)
        }
    }

    public V2SystemSource getSystemSource(V2System v2System, String strHttpUrlToRepo,String strBranch, net.ibizsys.runtime.util.domain.File ossFile,String version) {

        V2SystemSource v2SystemSource = null;

        String systemId = v2System.getId()

        if (!StringUtils.hasLength(strBranch)) {
            strBranch = "master"
        }
        if(ossFile!=null && processOssFile(ossFile)) {

            v2SystemSource = new V2SystemSource();
            v2SystemSource.setName(version);
            v2SystemSource.setOssFile(ossFile.getOSSId());


            v2SystemSource.setDigest(ossFile.getDigestCode());
            v2SystemSource.setVersion(1);
            v2SystemSource = getHubSysExtensionUtilRuntime().getCloudExtensionClient().createSystemSource(systemId, v2SystemSource);
            return v2SystemSource
        }

        boolean bGitMode = true
        String strSubFolder = null
        String strSystemPath = v2System.getName()

        if (StringUtils.hasLength(strHttpUrlToRepo)) {
            // 处理可能的子文件夹路径（如：http://example.com/repo.zip#subfolder）
            String[] parts = strHttpUrlToRepo.split("[#]")
            if (parts.length == 2) {
                strHttpUrlToRepo = parts[0]
                strSubFolder = parts[1]
                bGitMode = false
            }

            // 提取系统路径名称
            String[] items = strHttpUrlToRepo.split("[/]")
            String strLastItem = items[-1]  // Groovy 简写，获取最后一个元素

            if (bGitMode) {
                // Git 仓库
                int nPos = strLastItem.lastIndexOf(".git")
                if (nPos != -1 && nPos == strLastItem.length() - 4) {
                    strSystemPath = strLastItem[0..<nPos]
                } else {
                    bGitMode = false
                    nPos = strLastItem.lastIndexOf(".zip")
                    if (nPos != -1 && nPos == strLastItem.length() - 4) {
                        strSystemPath = strLastItem[0..<nPos]
                    }
                }
            } else {
                // Zip 文件
                int nPos = strLastItem.lastIndexOf(".zip")
                if (nPos != -1 && nPos == strLastItem.length() - 4) {
                    strSystemPath = strLastItem[0..<nPos]
                }
            }
        }

        strSystemPath = "${strSystemPath}-${version}"

        String strFilePath = Paths.get(
                ServiceHub.getInstance().getServiceHubSetting().getSystemModelFolder(),
                "systemsources3",
                systemId,
                strSystemPath,
                strBranch
        ).toString()

        File file = new File(strFilePath)
        String strPath = file.canonicalPath

        if (bGitMode && StringUtils.hasLength(strHttpUrlToRepo)) {
            log.debug("插件系统[${systemId}]使用Git路径：${strHttpUrlToRepo}")

            try {
                if (file.exists()) {
                    // 使用 withCloseable 自动管理资源
                    new FileRepository(new File("${strPath}${File.separator}.git")).withCloseable { fr ->
                        new Git(fr).withCloseable { git ->
                            PullCommand pullCommand = git.pull().setRemoteBranchName(strBranch)
                            pullCommand.call()
                        }
                    }
                    log.debug("Git仓库[${systemId}]拉取成功")
                } else {
                    // 创建目录
                    if (file.mkdirs()) {
                        log.debug("创建目录: ${file.canonicalPath}")
                    }

                    // 克隆仓库
                    CloneCommand cloneCommand = Git.cloneRepository()
                            .setURI(strHttpUrlToRepo)
                            .setDirectory(file)
                            .setBranch(strBranch)
                            .setCloneSubmodules(true)  // 如果有子模块，一并克隆



                    cloneCommand.call().withCloseable { git ->
                        log.debug("Git仓库[${systemId}]克隆成功")
                    }
                }
            } catch (WrongRepositoryStateException | CheckoutConflictException ex) {
                log.error("Git仓库状态异常，${ex.message}。执行清除目录操作[${file.canonicalPath}]", ex)
                try {
                    FileUtils.deleteDirectory(file)
                    log.info("已清除异常目录: ${file.canonicalPath}")
                } catch (IOException e) {
                    log.warn("清除目录失败: ${e.message}")
                }
                throw new Exception("签出Git项目发生异常: ${ex.message}", ex)
            } catch (Exception ex) {
                log.error("Git操作失败[${systemId}]: ${ex.message}", ex)
                throw new Exception("Git操作失败: ${ex.message}", ex)
            }
        }
        else {
            // Zip模式
            if (!StringUtils.hasLength(strHttpUrlToRepo)) {
                throw new Exception("未提供有效的代码仓库地址")
            }

            log.debug("插件系统[${systemId}]使用Zip路径：${strHttpUrlToRepo}")

            if (!file.exists()) {
                File tempFile = null
                try {
                    // 创建临时文件
                    tempFile = File.createTempFile("resource_${systemId}_${System.currentTimeMillis()}", ".zip")
                    log.debug("下载Zip文件到临时文件: ${tempFile.absolutePath}")

                    // 下载文件
                    this.getSystemRuntime().getDefaultWebClient().download(strHttpUrlToRepo, tempFile)

                    // 解压文件
                    ZipUtils.unzip(tempFile, file)
                    log.debug("Zip文件解压成功: ${file.canonicalPath}")
                } catch (Exception ex) {
                    log.error("下载或解压Zip文件失败[${systemId}]: ${ex.message}", ex)
                    throw new Exception("下载或解压文件发生异常: ${ex.message}", ex)
                } finally {
                    // 清理临时文件
                    if (tempFile?.exists()) {
                        if (!tempFile.delete()) {
                            log.warn("无法删除临时文件: ${tempFile.absolutePath}")
                        }
                    }
                }
            } else {
                log.debug("Zip目录已存在: ${file.canonicalPath}")
            }

            // 处理子文件夹
            if (StringUtils.hasLength(strSubFolder)) {
                file = new File(file.absolutePath + File.separator + strSubFolder)
                if (!file.exists() || !file.isDirectory()) {
                    throw new Exception("指定的子文件夹不存在: ${strSubFolder}")
                }
                strPath = file.canonicalPath
            }
        }

        File modelFolder = null;
        // 检查是否有ibizmodel.yaml配置文件
        File modelFile = new File("${strPath}${File.separator}ibizmodel.yaml")
        if (modelFile.exists()) {
            try {
                Yaml yaml = new Yaml()
                InputStream inputStream = null
                try {
                    inputStream = new FileInputStream(modelFile)
                    Map config = yaml.loadAs(inputStream, Map)
                    if (config?.modelfolder) {
                        String strModelFolder = config.modelfolder as String
                        modelFolder = new File(strPath + File.separator + strModelFolder)

                    }
                } finally {
                    inputStream?.close()
                }
            } catch (Exception ex) {
                log.error("加载系统模型配置发生异常: ${ex.message}", ex)
                throw new Exception("加载系统模型配置发生异常: ${ex.message}", ex)
            }
        }

        if (modelFolder == null || !modelFolder.exists() || !modelFolder.isDirectory()) {
            File systemModelFile = new File("${strPath}${File.separator}PSSYSTEM.json")
            if (systemModelFile.exists()) {
                modelFolder = file
            }
        }

        if (modelFolder!=null && modelFolder.exists() && modelFolder.isDirectory()) {
            // 建立模型压缩文件
            File zipTempFile = File.createTempFile("model_" + strSystemPath, ".zip");
            ZipUtils.zip(modelFolder, zipTempFile);
            String strFileHashCode = "";
            FileInputStream fis = null
            try {
                fis = new FileInputStream(zipTempFile)
                strFileHashCode = DigestUtils.md5DigestAsHex(fis)
            } finally {
                fis?.close()
            }
            String strOSSCat = net.ibizsys.central.cloud.core.sysutil.ISysExtensionUtilRuntime.OSSCAT_DYNAMODEL;
            ossFile = this.getSystemRuntime().getSysFileUtilRuntime(false).createOSSFile(zipTempFile, strOSSCat);

            v2SystemSource = new V2SystemSource();
            v2SystemSource.setName(version);
            v2SystemSource.setOssFile(ossFile.getOSSId());
            v2SystemSource.setDigest(strFileHashCode);
            v2SystemSource.setVersion(1);
            v2SystemSource = getHubSysExtensionUtilRuntime().getCloudExtensionClient().createSystemSource(systemId, v2SystemSource);

        }
        if (v2SystemSource == null)
            throw new Exception("根目录未找到系统模型文件(ibizmodel.yaml或PSSYSTEM.json)")
        return v2SystemSource;
    }
}

```
### KBAgentDESyncUtilRuntime :id=KBAgentDESyncUtilRuntime


```net.ibizsys.central.plugin.util.sysutil.KBAgentDESyncUtilRuntime```

```groovy
null
```
### KBAgentDESyncUtilRuntimeEx :id=KBAgentDESyncUtilRuntimeEx


```net.ibizsys.central.plugin.util.sysutil.KBAgentDESyncUtilRuntimeEx```

```groovy
package net.ibizsys.central.plugin.util.sysutil;

import java.util.LinkedHashMap;
import java.util.Map;

import net.ibizsys.central.cloud.core.spring.rt.ServiceHub;
import net.ibizsys.central.dataentity.IDataEntityRuntime;
import net.ibizsys.model.dataentity.action.IPSDEAction;
import org.apache.commons.logging.LogFactory;
import org.springframework.util.ObjectUtils;

import net.ibizsys.central.util.IEntityDTO;
import net.ibizsys.model.dataentity.defield.IPSDEField;
import net.ibizsys.runtime.dataentity.IDataEntityRuntimeContext;
import net.ibizsys.runtime.util.DataTypeUtils;

public class KBAgentDESyncUtilRuntimeEx extends KBAgentDESyncUtilRuntime{

	private static final org.apache.commons.logging.Log log = LogFactory.getLog(KBAgentDESyncUtilRuntimeEx.class);
	/**
	 * 预定义属性：代码别名
	 */
	public final static String PREDEFINEDFIELD_CODE_NAME = "CODE_NAME";

	private boolean bRawGet = false;

	protected void onInit() throws Exception {
		this.bRawGet = DataTypeUtils.asBoolean(this.getUtilParam("rawget", (String)null), false);
		super.onInit();
	}

	@Override
	protected void onAfterCreate(IDataEntityRuntimeContext iDataEntityRuntimeContext, IPSDEAction iPSDEAction, IEntityDTO iEntityDTO) throws Throwable {
		//额外注册别名
		Map<String, Object> map = new LinkedHashMap<String, Object>();
		IPSDEField iPSDEField = iDataEntityRuntimeContext.getDataEntityRuntime().getPSDEFieldByTag(PREDEFINEDFIELD_CODE_NAME, true);
		if(!ObjectUtils.isEmpty(iEntityDTO.get(iPSDEField.getLowerCaseName()))) {
			if (this.bRawGet) {
				IEntityDTO rawEntityDTO = ((IDataEntityRuntime) iDataEntityRuntimeContext.getDataEntityRuntime()).rawGet(iDataEntityRuntimeContext.getDataEntityRuntime().getKeyFieldValue(iEntityDTO));
				String strConfigId = this.getCloudAliasConfigId(iDataEntityRuntimeContext, map, rawEntityDTO);
				String strConfig = this.getConfig(iDataEntityRuntimeContext, rawEntityDTO);
				ServiceHub.getInstance().publishConfig(strConfigId, strConfig);
			} else {
				String strConfigId = this.getCloudAliasConfigId(iDataEntityRuntimeContext, map, iEntityDTO);
				String strConfig = this.getConfig(iDataEntityRuntimeContext, iEntityDTO);
				ServiceHub.getInstance().publishConfig(strConfigId, strConfig);
			}
		}
		super.onAfterUpdate(iDataEntityRuntimeContext, iPSDEAction, iEntityDTO);
	}

	@Override
	protected void onAfterUpdate(IDataEntityRuntimeContext iDataEntityRuntimeContext, IPSDEAction iPSDEAction, IEntityDTO iEntityDTO) throws Throwable {
		//额外注册别名
		Map<String, Object> map = new LinkedHashMap<String, Object>();
		IPSDEField iPSDEField = iDataEntityRuntimeContext.getDataEntityRuntime().getPSDEFieldByTag(PREDEFINEDFIELD_CODE_NAME, true);
		if(!ObjectUtils.isEmpty(iEntityDTO.get(iPSDEField.getLowerCaseName()))) {
			if (this.bRawGet) {
				IEntityDTO rawEntityDTO = ((IDataEntityRuntime) iDataEntityRuntimeContext.getDataEntityRuntime()).rawGet(iDataEntityRuntimeContext.getDataEntityRuntime().getKeyFieldValue(iEntityDTO));
				String strConfigId = this.getCloudAliasConfigId(iDataEntityRuntimeContext, map, rawEntityDTO);
				String strConfig = this.getConfig(iDataEntityRuntimeContext, rawEntityDTO);
				ServiceHub.getInstance().publishConfig(strConfigId, strConfig);
			} else {
				String strConfigId = this.getCloudAliasConfigId(iDataEntityRuntimeContext, map, iEntityDTO);
				String strConfig = this.getConfig(iDataEntityRuntimeContext, iEntityDTO);
				ServiceHub.getInstance().publishConfig(strConfigId, strConfig);
			}
		}
		super.onAfterUpdate(iDataEntityRuntimeContext, iPSDEAction, iEntityDTO);
	}

	@Override
	protected void onBeforeRemove(IDataEntityRuntimeContext iDataEntityRuntimeContext, IPSDEAction iPSDEAction, IEntityDTO iEntityDTO) throws Throwable {
		//额外注册别名
		Map<String, Object> map = new LinkedHashMap<String, Object>();
		IPSDEField iPSDEField = iDataEntityRuntimeContext.getDataEntityRuntime().getPSDEFieldByTag(PREDEFINEDFIELD_CODE_NAME, true);
		if(!ObjectUtils.isEmpty(iEntityDTO.get(iPSDEField.getLowerCaseName()))) {
			if (this.bRawGet) {
				IEntityDTO rawEntityDTO = ((IDataEntityRuntime) iDataEntityRuntimeContext.getDataEntityRuntime()).rawGet(iDataEntityRuntimeContext.getDataEntityRuntime().getKeyFieldValue(iEntityDTO));
				String strConfigId = this.getCloudAliasConfigId(iDataEntityRuntimeContext, map, rawEntityDTO);
				ServiceHub.getInstance().removeConfig(strConfigId);
			} else {
				String strConfigId = this.getCloudAliasConfigId(iDataEntityRuntimeContext, map, iEntityDTO);
				ServiceHub.getInstance().removeConfig(strConfigId);
			}
		}
		super.onBeforeRemove(iDataEntityRuntimeContext, iPSDEAction, iEntityDTO);
	}

	protected String getCloudAliasConfigId(IDataEntityRuntimeContext iDataEntityRuntimeContext, Map<String, Object> map, IEntityDTO iEntityDTO) throws Exception {
		map.putAll(map);
		if(!map.containsKey(UTILPARAM_UTIL)) {
			map.put(UTILPARAM_UTIL, this.getUtilParam(UTILPARAM_UTIL, "unknown"));
		}
		IPSDEField iPSDEField = iDataEntityRuntimeContext.getDataEntityRuntime().getPSDEFieldByTag(PREDEFINEDFIELD_CODE_NAME, true);
		map.put(PARAM_KEY, iEntityDTO.get(iPSDEField.getLowerCaseName()));
		return super.getCloudConfigId(iDataEntityRuntimeContext, map, iEntityDTO);
	}
}

```
### PageDataImportRuntimeEx :id=PageDataImportRuntimeEx
页面导入使用

```cn.ibizlab.user.plugin.groovy.dataentity.dataimport.PageDataImportRuntimeEx```

```groovy
package cn.ibizlab.user.plugin.groovy.dataentity.dataimport

import com.fasterxml.jackson.databind.JsonNode
import groovy.transform.CompileStatic;
import net.ibizsys.central.cloud.core.util.domain.V2ImportSchema;
import net.ibizsys.central.plugin.poi.dataentity.dataimport.POIDEDataImportRuntime
import net.ibizsys.central.util.IEntityDTO;
import net.ibizsys.model.dataentity.dataimport.IPSDEDataImportItem;
import net.ibizsys.model.dataentity.defield.IPSDEField;
import net.ibizsys.runtime.dataentity.DataEntityRuntimeException;
import net.ibizsys.runtime.util.IEntity;
import org.apache.poi.ss.usermodel.Workbook;
import org.springframework.util.StringUtils;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

@CompileStatic
public class PageDataImportRuntimeEx extends POIDEDataImportRuntime  {


}
```
### SysChatMemoryUtilRuntime :id=SysChatMemoryUtilRuntime


```net.ibizsys.central.plugin.ai.sysutil.SysChatMemoryUtilRuntime```

```groovy
null
```
### SysChatSkillUtilRuntime :id=SysChatSkillUtilRuntime


```net.ibizsys.central.plugin.ai.sysutil.SysChatSkillUtilRuntime```

```groovy
null
```
### SysEncryptTranslatorRuntimeEx :id=SysEncryptTranslatorRuntimeEx
可逆加密

```cn.ibizlab.user.plugin.groovy.res.SysEncryptTranslatorRuntimeEx```

```groovy
package cn.ibizlab.user.plugin.groovy.res;

import groovy.transform.CompileStatic;
import net.ibizsys.model.dataentity.defield.IPSDEField;
import net.ibizsys.runtime.dataentity.IDataEntityRuntime;
import net.ibizsys.runtime.util.IEntityBase;
import net.ibizsys.runtime.res.SysEncryptTranslatorRuntime;

@CompileStatic
public class SysEncryptTranslatorRuntimeEx extends SysEncryptTranslatorRuntime  {

    private static final org.apache.commons.logging.Log log = org.apache.commons.logging.LogFactory.getLog(SysEncryptTranslatorRuntimeEx.class);

    public Object translate(Object objValue, boolean bIn, IEntityBase iEntityBase, IPSDEField iPSDEField, IDataEntityRuntime entityDataEntityRuntime) throws Throwable {
         Object ret = objValue;
         
         try
         {
            ret =   super.translate(objValue,bIn,iEntityBase,iPSDEField,entityDataEntityRuntime);
         }catch(Exception ex) {
             log.warn("转换错误: " + ex);
         }

         return ret;
    }

}
```
### SysKnowledgeBaseUtilRuntimeEx :id=SysKnowledgeBaseUtilRuntimeEx
知识库功能组件运行时

```net.ibizsys.central.plugin.ai.sysutil.SysKnowledgeBaseUtilRuntimeEx```

```groovy
package net.ibizsys.central.plugin.ai.sysutil

import net.ibizsys.central.cloud.core.util.domain.Chunk
import net.ibizsys.central.util.IEntityDTO
import net.ibizsys.central.util.ISearchContextDTO
import net.ibizsys.model.dataentity.ds.IPSDEDataSet
import net.ibizsys.runtime.util.DataTypeUtils
import org.apache.commons.logging.Log
import org.apache.commons.logging.LogFactory
import org.springframework.data.domain.Page
import org.springframework.util.ObjectUtils
import org.springframework.util.StringUtils

class SysKnowledgeBaseUtilRuntimeEx extends SysKnowledgeBaseUtilRuntime {

    private static final Log log = LogFactory.getLog(SysKnowledgeBaseUtilRuntimeEx.class);

    @Override
    protected void runParseKnowledgeBaseTimer() {
        boolean bRunParse = this.getSystemRuntime().getSystemRuntimeSetting().getParam(this.getConfigFolder() + ".runparse", "ibizaifactory".equals(this.getSystemRuntime().getDeploySystemId()));
        if(!bRunParse)
            return;
        runParseKnowledgeBaseTimer(false);
    }

    protected void reloadKnowledgeBaseEntityDTOs() throws Throwable {
        try {
            //安装子系统 导致 isThreadRunning() false ,导致知识库检索 使用 threadRunAllOf 失败
            def field = SysKnowledgeBaseUtilRuntimeBase.getDeclaredField('bRunParseKnowledgeBaseTimer')
            field.setAccessible(true)
            field.set(this, true)
        } catch (Exception e) {

        }
        //分页处理
        try {
            final IKnowledgeBaseProxyDERuntime knowledgeBaseProxyDERuntime = this.getKnowledgeBaseProxyDERuntime(false);
            IPSDEDataSet iPSDEDataSet = knowledgeBaseProxyDERuntime.getPSDEDataSet(KnowledgeBaseDataSet.VALID);
            List<IEntityDTO> list = []
            int page = 0;
            ISearchContextDTO iSearchContextDTO = knowledgeBaseProxyDERuntime.getReal().createSearchContext()
            Page result = null
            while (result == null || list.size() < result.getTotalElements()) {
                iSearchContextDTO.setPageable(page, 1000, 0)
                Object[] args = [iSearchContextDTO] as Object[]
                result = knowledgeBaseProxyDERuntime.getReal().fetchDataSet("", iPSDEDataSet, args);
                if (result != null && result.getContent().size() > 0) {
                    list.addAll(result.getContent())
                }
                page++
            }

            Map<Object, IEntityDTO> knowledgeBaseEntityDTOMap = new LinkedHashMap<Object, IEntityDTO>();
            if (!ObjectUtils.isEmpty(list)) {
                for (IEntityDTO iEntityDTO : list) {
                    Object objKey = knowledgeBaseProxyDERuntime.getReal().getKeyFieldValue(iEntityDTO);
                    knowledgeBaseEntityDTOMap.put(objKey, iEntityDTO);
                }
            }
            def field = SysKnowledgeBaseUtilRuntimeBase.getDeclaredField('knowledgeBaseEntityDTOMap')
            field.setAccessible(true)
            field.set(this, knowledgeBaseEntityDTOMap)
        } catch (Exception e) {
            log.error(e.getMessage(), e)
            super.reloadKnowledgeBaseEntityDTOs()
        }
    }

    @Override
    protected void onChunkBeforeCreate(IEntityDTO et) throws Throwable {
        IChunkProxyDERuntime chunkProxyDERuntime = this.getChunkProxyDERuntime(false);
        if (!chunkProxyDERuntime.getFieldValue(et, ChunkField.DOCUMENT_ID)) {
            log.warn("文档ID为空,忽略chunk向量处理")
            return
        }
        super.onChunkBeforeCreate(et)
    }

    @Override
    protected void onChunkBeforeUpdate(IEntityDTO et) throws Throwable {
        IChunkProxyDERuntime chunkProxyDERuntime = this.getChunkProxyDERuntime(false);
        if (!chunkProxyDERuntime.getFieldValue(et, ChunkField.DOCUMENT_ID)) {
            log.warn("文档ID为空,忽略chunk向量处理")
            return
        }
        super.onChunkBeforeUpdate(et)
    }

//     @Override
//     protected void fillRaptorClusterChunks(List<Chunk> chunkList, Map<String, Chunk> chunkMap) throws Throwable {
//         final IChunkProxyDERuntime chunkProxyDERuntime = this.getChunkProxyDERuntime(false);

//         Map<String, Chunk> validChunkMap = new HashMap<>();

//         // 补充全部片段
//         for (Chunk chunk : chunkList) {
//             chunk.set("",1)
//             validChunkMap.put(chunk.getId(), chunk);

//             if (!StringUtils.hasLength(chunk.getPid())) {
//                 continue;
//             }

//             String strPId = chunk.getPid();
//             while (StringUtils.hasLength(strPId)) {
//                 Chunk parentChunk = chunkMap.get(strPId);
//                 if (parentChunk == null) {
//                     IEntityDTO parentChunkDTO = chunkProxyDERuntime.getReal().get(strPId, true);
//                     if (parentChunkDTO == null) {
//                         log.error(String.format("无法获取父片段[%s]", strPId));
//                         break;
//                     }

//                     Map<String, Object> item = chunkProxyDERuntime.getDataItem(parentChunkDTO);
//                     parentChunk = new Chunk();
//                     parentChunk.setId(DataTypeUtils.asString(item.get(FIELD_ID)));
//                     parentChunk.setPid(DataTypeUtils.asString(item.get(ChunkField.PID.name())));
//                     parentChunk.setContent(DataTypeUtils.asString(item.get(ChunkField.CONTENT.name())));
//                     parentChunk.set(ChunkField.SEQUENCE.name(), item.get(ChunkField.SEQUENCE.name()));
//                     parentChunk.setDocId(DataTypeUtils.asString(item.get(ChunkField.DOCUMENT_ID.name())));
//                     parentChunk.setDocName(DataTypeUtils.asString(item.get(ChunkField.DOCUMENT_NAME.name())));
//                     //不用类型
//                     //parentChunk.setType(DataTypeUtils.asString(item.get(ChunkField.TYPE.name())));
//                     chunkMap.put(parentChunk.getId(), parentChunk);
//                 }
//                 validChunkMap.put(parentChunk.getId(), parentChunk);
//                 strPId = parentChunk.getPid();
//             }
//         }

//         List<Chunk> chunkList2 = new ArrayList<>(validChunkMap.values());
//         Collections.sort(chunkList2, new Comparator<Chunk>() {
//             @Override
//             public int compare(Chunk o1, Chunk o2) {
//                 Integer s1 = DataTypeUtils.asInteger(o1.get(ISysKnowledgeBaseUtilRuntime.ChunkField.SEQUENCE.name()), 0);
//                 Integer s2 = DataTypeUtils.asInteger(o2.get(ISysKnowledgeBaseUtilRuntime.ChunkField.SEQUENCE.name()), 0);
//                 return s1.compareTo(s2);
//             }
//         });

//         List<Chunk> realChunkList = new ArrayList<>();
//         for (Chunk chunk : chunkList) {
//             realChunkList.add(chunk);

//             if (!StringUtils.hasLength(chunk.getPid())) {
//                 continue;
//             }

//             if (net.ibizsys.central.cloud.core.util.domain.ChunkType.SOURCE.getValue().equals(chunk.getType())) {
//                 continue;
//             }

//             // 计算当前块的顶级块
//             Chunk rootChunk = null;
//             String strPId = chunk.getPid();
//             while (StringUtils.hasLength(strPId)) {
//                 Chunk parentChunk = chunkMap.get(strPId);
//                 if (parentChunk == null) {
//                     log.warn(String.format("未能获取父标识[%s]指定片段", strPId));
//                     break;
//                 }
//                 rootChunk = parentChunk;
//                 strPId = parentChunk.getPid();
//             }

//             if (rootChunk != null) {
//                 // 合并内容
//                 StringBuilder sb = new StringBuilder();
//                 List<Chunk> childChunks = new ArrayList<>();
//                 fillRaptorClusterChunkContent(sb, rootChunk, rootChunk, chunkList2, childChunks);

//                 //移除已存在的chunk
// //                Set existingIds = chunkList.collect { it.getId() } as Set
// //                childChunks.removeAll { it.getId() in existingIds }
//                 //截取前5条chunk
// //                List<Chunk> top5ChildChunks = childChunks.take(5)
//                 sb = new StringBuilder();
//                 sb.append(rootChunk.getContent())
//                 for (Chunk childChunk : childChunks) {
//                     sb.append("\r\n");
//                     sb.append(childChunk.getContent())
//                 }

//                 //设置根相关信息
//                 rootChunk.setSimilarity(chunk.getSimilarity());
//                 rootChunk.setContent(sb.toString());
//                 rootChunk.setType(net.ibizsys.central.cloud.core.util.domain.ChunkType.CLUSTER.getValue());

//                 //插入到当前位置得得上一片
//                 realChunkList.add(realChunkList.size() - 1, rootChunk);

//                 //chunk.setContent(sb.toString());
//                 //chunk.setType(net.ibizsys.central.cloud.core.util.domain.ChunkType.CLUSTER.getValue());
//             }
//         }

//         chunkList.clear();
//         chunkList.addAll(realChunkList);
//     }


//     protected void fillRaptorClusterChunkContent(StringBuilder sb, Chunk rootChunk, Chunk parentChunk, List<Chunk> chunkList, List<Chunk> childChunks) throws Throwable {
//         for (Chunk chunk : chunkList) {
//             if (!StringUtils.hasLength(chunk.getPid())) {
//                 continue;
//             }

//             if (parentChunk.getId().equals(chunk.getPid())) {
//                 chunk.setType(net.ibizsys.central.cloud.core.util.domain.ChunkType.SOURCE.getValue());
//                 boolean exists = childChunks.any { it.getId() == chunk.getId() }
//                 if (!exists) {
//                     childChunks.add(chunk)
//                 }
//                 this.fillRaptorClusterChunkContent(sb, rootChunk, chunk, chunkList, childChunks);
//                 //修改碎片得父标识
//                 chunk.setPid(rootChunk.getId());
//             }
//         }
//     }
}

```
### SysMcpServerUtilRuntime :id=SysMcpServerUtilRuntime


```net.ibizsys.central.plugin.ai.sysutil.SysMcpServerUtilRuntime```

```groovy
null
```
### SysOpenAIServerUtilRuntime :id=SysOpenAIServerUtilRuntime


```net.ibizsys.central.plugin.ai.sysutil.SysOpenAIServerUtilRuntime```

```groovy
null
```
### SysAtContentTranslatorRuntime :id=UsrSFPlugin0201416283
评论@转换器

```net.ibizsys.central.res.SysAtContentTranslatorRuntime```

```groovy
null
```
### CommitVersionDEActionRuntime :id=UsrSFPlugin0324806543
创建版本数据

```net.ibizsys.central.plugin.version.dataentity.action.CommitVersionDEActionRuntime```

```groovy
null
```
### RestoreVersionDEActionRuntime :id=UsrSFPlugin0324899435


```net.ibizsys.central.plugin.version.dataentity.action.RestoreVersionDEActionRuntime```

```groovy
null
```
### TreeGridDEDataSetRuntime :id=UsrSFPlugin0407757309
数据集合获取树表格层级数据

```net.ibizsys.central.plugin.util.dataentity.ds.TreeGridDEDataSetRuntime```

```groovy
null
```
### FillVersionDataDEDataSetRuntime :id=UsrSFPlugin0421357755
cn.ibizlab.plm.user.plugin.groovy.dataentity.ds.FillVersionDataDEDataSetRuntime

```cn.ibizlab.user.plugin.groovy.dataentity.ds.FillVersionDataDEDataSetRuntime```

```groovy
package cn.ibizlab.user.plugin.groovy.dataentity.ds;

import groovy.transform.CompileStatic;

import java.util.function.Predicate
import java.util.stream.Collectors;

import net.ibizsys.central.dataentity.IDataEntityRuntime;
import net.ibizsys.central.plugin.util.dataentity.ds.DEDataSetRuntimeBase;
import net.ibizsys.model.PSModelEnums;
import org.springframework.data.domain.Page;

import net.ibizsys.central.util.IEntityDTO;
import net.ibizsys.central.util.ISearchContextDTO;
import net.ibizsys.central.util.PageImpl;
import org.springframework.util.ObjectUtils;
import org.springframework.util.StringUtils;

@CompileStatic
class FillVersionDataDEDataSetRuntime extends DEDataSetRuntimeBase {

	@Override
	protected Page<?> doFetchReal(ISearchContextDTO iSearchContextDTO) throws Throwable {

		if (this.getDataEntityRuntime().getSystemPersistentAdapter() == null) {
			throw new Exception("实体未提供系统持久化设置器");
		}


		Page<?> ret = this.getDataEntityRuntime().getSystemPersistentAdapter().fetchDataSet(this.getDataEntityRuntime(), this.getPSDEDataSet(), iSearchContextDTO, null);
		Page<IEntityDTO> page = this.getDataEntityRuntime().getEntityDTOPage(ret, this.getPSDEDataSet(), iSearchContextDTO.getPageable());

		return new PageImpl<IEntityDTO>(fillVersionData(page.getContent(),iSearchContextDTO), iSearchContextDTO.getPageable(), ret.getTotalElements(), page.getTotalPages());

	}

	@Override
	public boolean isValid(Object[] args) {
		return true;
	}

	protected List<IEntityDTO> fillVersionData(List<IEntityDTO> dtos,ISearchContextDTO iSearchContextDTO){
		List<IEntityDTO> entityDTOList = new ArrayList<IEntityDTO>();
		//后续可以用参数指定
		String ownerDataKeyFieldName = "target_id";
		String ownerDataVersionKeyFieldName = "target_version_id";
		String ownerDataEntityTypeFieldName = "target_type";
		String ownerDataEntityName = "";
		List<String> fetchVersionIdList = new ArrayList<String>();
		for (IEntityDTO dto : dtos) {
			ownerDataEntityName = (String) dto.get(ownerDataEntityTypeFieldName);
			if (dto.get(ownerDataVersionKeyFieldName) == null) {
				continue;
			}
			fetchVersionIdList.add((String) dto.get(ownerDataVersionKeyFieldName));
		}
		if(!StringUtils.hasLength(ownerDataEntityName)){
			ownerDataEntityName = (String)iSearchContextDTO.get("owner_type");
		}
		if(!StringUtils.hasLength(ownerDataEntityName)){
			return dtos;
		}
		IDataEntityRuntime versionOwnerDERutime = this.getSystemRuntime().getDataEntityRuntime(ownerDataEntityName.toUpperCase());
		Map<String, IEntityDTO> versionDateMap = new LinkedHashMap<>();
		List<String> fetchLatestDataIdList = new ArrayList<String>();
		Map<String, IEntityDTO> latestVersionDateMap = new LinkedHashMap<>();
		if(versionOwnerDERutime.getDEVersionControlUtilRuntime() != null) {
			IDataEntityRuntime versionDERuntime = versionOwnerDERutime.getDEVersionControlUtilRuntime().getVersionDataEntityRuntime();
			try {
				ISearchContextDTO versionSearchContextDTO = versionDERuntime.createSearchContext();
				versionSearchContextDTO.count(false).limit(1000).in(versionDERuntime.getKeyPSDEField().getLowerCaseName(), fetchVersionIdList);
				List versionQueryRet = versionDERuntime.getSystemPersistentAdapter().query(versionDERuntime, versionDERuntime.getViewPSDEDataQuery(), versionSearchContextDTO, null);
				List<IEntityDTO> versionDTOList = versionDERuntime.getEntityDTOList(versionQueryRet, versionDERuntime.getViewPSDEDataQuery());
				for (IEntityDTO versionDTO : versionDTOList) {
					String strVersionDataId = versionDTO.getString(versionDERuntime.getPSDEFieldByPredefinedType(PSModelEnums.PredefinedFieldType.PARENTID.value, false).getLowerCaseName(), null);
					String strVersionData = versionDTO.getString("data", null);
					if (!StringUtils.isEmpty(strVersionDataId) && !StringUtils.isEmpty(strVersionData)) {
						IEntityDTO versionDataDTO = (IEntityDTO) versionOwnerDERutime.deserializeEntity(strVersionData);
						//移除ID源对象ID字段
						versionDataDTO.reset(versionOwnerDERutime.getKeyPSDEField().getLowerCaseName());
						versionDateMap.put(strVersionDataId, versionDataDTO);
					}
					if (StringUtils.isEmpty(strVersionData)) {
						fetchLatestDataIdList.add(strVersionDataId);
					}
				}
				if (fetchLatestDataIdList.size() > 0) {
					ISearchContextDTO versionOwnerSearchContextDTO = versionDERuntime.createSearchContext();
					versionOwnerSearchContextDTO.count(false).limit(1000).in(versionOwnerDERutime.getKeyPSDEField().getLowerCaseName(), fetchLatestDataIdList);
					Page<?> ownerDataFetchRet = versionOwnerDERutime.getSystemPersistentAdapter().fetchDataSet(versionOwnerDERutime, versionOwnerDERutime.getDefaultPSDEDataSet(), versionOwnerSearchContextDTO, null);
					Page<IEntityDTO> ownerDataPage = versionOwnerDERutime.getEntityDTOPage(ownerDataFetchRet, versionOwnerDERutime.getDefaultPSDEDataSet(), versionOwnerSearchContextDTO.getPageable());
					for (IEntityDTO ownerDataDTO : ownerDataPage.getContent()) {
						String strOwnerDataDTOId = ownerDataDTO.getString(versionOwnerDERutime.getKeyPSDEField().getLowerCaseName(), null);
						ownerDataDTO.reset(versionOwnerDERutime.getKeyPSDEField().getLowerCaseName());
						latestVersionDateMap.put(strOwnerDataDTOId, ownerDataDTO);
					}
				}

			} catch (Throwable e) {
				throw new RuntimeException("查询目标版本数据异常");
			}
		}
		for(IEntityDTO dto : dtos) {
			String strVersionOwnerId = (String) dto.get(ownerDataKeyFieldName);
			if(versionDateMap.containsKey(strVersionOwnerId)){
				dto.putAll(versionDateMap.get(strVersionOwnerId).any());
			}
			if(latestVersionDateMap.containsKey(strVersionOwnerId)){
				dto.putAll(latestVersionDateMap.get(strVersionOwnerId).any());
			}
			entityDTOList.add(dto);
		}
		entityDTOList = filterVersionData(entityDTOList,iSearchContextDTO);
		return entityDTOList;
	}

	protected List<IEntityDTO> filterVersionData(List<IEntityDTO> dtos,ISearchContextDTO iSearchContextDTO){
		List<IEntityDTO> filterDtos = new ArrayList<>();
		//轻量级过滤
		Map<String, Object> params = iSearchContextDTO.any();
		List<String> strSearchConds = params.keySet().stream().filter({ key -> key.startsWith("n_") && key.split("_").length == 3 && this.getDataEntityRuntime().getPSDEFieldByCodeName(key.split("_")[1], true) != null }).collect(Collectors.toList());
		for (int i = 0;i< strSearchConds.size();i++ ) {
			String key = strSearchConds.get(i)
			List<IEntityDTO> filterResults = new ArrayList<>();
            Object objValue = params.get(key);
            String fieldName = key.split("_")[1];
            String operator = key.split("_")[2];
            if (operator.equalsIgnoreCase("eq")) {
				filterDtos.addAll(dtos.stream().filter({IEntityDTO iEntityDTO -> !ObjectUtils.isEmpty(iEntityDTO.get(fieldName)) && iEntityDTO.get(fieldName).equals(objValue)} as Predicate<IEntityDTO>).collect(Collectors.toList()));
            } else if (operator.equalsIgnoreCase("isnull")) {
				filterDtos.addAll(dtos.stream().filter({IEntityDTO iEntityDTO -> ObjectUtils.isEmpty(iEntityDTO.get(fieldName)) } as Predicate<IEntityDTO>).collect(Collectors.toList()));
            } else if (operator.equalsIgnoreCase("isnotnull")) {
				filterDtos.addAll(dtos.stream().filter({IEntityDTO iEntityDTO -> !ObjectUtils.isEmpty(iEntityDTO.get(fieldName)) } as Predicate<IEntityDTO>).collect(Collectors.toList()));
            }
        }
		if(strSearchConds.size() == 0){
			return dtos;
		}
		return filterDtos;
	}
}

```
### FixCommitVersionDEActionRuntime :id=UsrSFPlugin0424197954
初始化版本数据（修复版本）

```net.ibizsys.central.plugin.version.dataentity.action.FixCommitVersionDEActionRuntime```

```groovy
null
```
### HtmlToPdfTransRuntime :id=UsrSFPlugin0612360832
Html转PDF格式

```cn.ibizlab.user.plugin.groovy.dataentity.logicnode.HtmlToPdfTransRuntime```

```groovy
package cn.ibizlab.user.plugin.groovy.dataentity.logicnode;

import groovy.transform.CompileStatic
import net.ibizsys.central.dataentity.IDataEntityRuntime
import net.ibizsys.central.dataentity.logic.DELogicNodeRuntimeBase
import net.ibizsys.central.dataentity.logic.IDELogicParamRuntime
import net.ibizsys.central.dataentity.logic.IDELogicRuntimeContext
import net.ibizsys.central.dataentity.logic.IDELogicSession
import net.ibizsys.central.util.IEntity
import net.ibizsys.model.dataentity.logic.IPSDELogicNode

@CompileStatic
class HtmlToPdfTransRuntime extends DELogicNodeRuntimeBase {
    @Override
	protected void onExecute(IDELogicRuntimeContext iDELogicRuntimeContext, IDELogicSession iDELogicSession, IPSDELogicNode iPSDELogicNode) throws Throwable {

    }
}
```
### DEVersionControlUtilRuntimeEx :id=UsrSFPlugin0628633282
排除新建模式行为自动建立版本

```cn.ibizlab.user.plugin.groovy.dataentity.util.DEVersionControlUtilRuntimeEx```

```groovy
package cn.ibizlab.user.plugin.groovy.dataentity.util;

import groovy.transform.CompileStatic;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import net.ibizsys.central.dataentity.IDataEntityRuntime;
import net.ibizsys.central.util.IEntityDTO;
import net.ibizsys.central.util.ISearchContextDTO;
import net.ibizsys.model.PSModelEnums.DER1NMasterRS;
import net.ibizsys.model.PSModelEnums.DERSubType;
import net.ibizsys.model.PSModelEnums.DERType;
import net.ibizsys.model.PSModelEnums.DEUtilType;
import net.ibizsys.model.PSModelEnums.PredefinedFieldType;
import net.ibizsys.model.PSModelEnums.SortDir;
import net.ibizsys.model.dataentity.IPSDataEntity;
import net.ibizsys.model.dataentity.action.IPSDEAction;
import net.ibizsys.runtime.dataentity.DataEntityRuntimeException;
import net.ibizsys.runtime.util.ActionSessionManager;
import net.ibizsys.runtime.util.DataTypeUtils;
import net.ibizsys.runtime.util.IAction;
import net.ibizsys.runtime.util.IEntityBase;
import net.ibizsys.runtime.util.KeyValueUtils;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.springframework.util.Assert;
import org.springframework.util.ObjectUtils;
import org.springframework.util.StringUtils;
import net.ibizsys.central.dataentity.util.DEVersionControlUtilRuntime;

@CompileStatic
public class DEVersionControlUtilRuntimeEx extends DEVersionControlUtilRuntime {

    @Override
    public boolean isCommit(String strActionName, IPSDEAction iPSDEAction) {
        if ("create".equalsIgnoreCase(strActionName)) {
            return true;
        } else {
            return this.isAutoCommit() && "update".equalsIgnoreCase(strActionName);
        }
    }
}

```






