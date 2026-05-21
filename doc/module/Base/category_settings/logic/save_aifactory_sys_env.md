## save_aifactory_sys_env <!-- {docsify-ignore-all} -->

   

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
state "开始" as Begin <<start>> [[$./save_aifactory_sys_env#begin {"开始"}]]
state "更新env" as RAWSFCODE_01  [[$./save_aifactory_sys_env#rawsfcode_01 {"更新env"}]]
state "update" as DEACTION_01  [[$./save_aifactory_sys_env#deaction_01 {"update"}]]
state "结束" as END_01 <<end>> [[$./save_aifactory_sys_env#end_01 {"结束"}]]


Begin --> RAWSFCODE_01
RAWSFCODE_01 --> DEACTION_01
DEACTION_01 --> END_01


@enduml
```


### 处理步骤说明

#### 开始 :id=Begin<sup class="footnote-symbol"> <font color=gray size=1>[开始]</font></sup>



*- N/A*
#### 更新env :id=RAWSFCODE_01<sup class="footnote-symbol"> <font color=gray size=1>[直接后台代码]</font></sup>



<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
def _default = logic.param('Default').getReal()

        // 字符串类字段保持原有处理
        def id = _default.get("id")?.toString() ?: ""
        def sysid = sys.getDeploySystemId().toLowerCase()
        def agentpre = "${sysid}-ai--".toString()

        def chat_model_id=_default.getString("chat_model_id","default")
        def flash_model_id=_default.getString("flash_model_id",chat_model_id)
        def intent_model_id=_default.getString("intent_model_id",flash_model_id)
        def vl_model_id=_default.getString("vl_model_id",flash_model_id)
        def embedding_model_id=_default.getString("embedding_model_id","")
        def rerank_model_id=_default.getString("rerank_model_id","")

        def serviceHub = net.ibizsys.central.cloud.core.spring.rt.ServiceHub.getInstance()
        org.yaml.snakeyaml.Yaml yaml = new org.yaml.snakeyaml.Yaml();
        def agent_runtime = sys.dataentity('ai_model')

        def gettoken = { def model ->
            def cedpre = "credential-${sysid}-ai--".toString()
            if(model && model.get("ai_credential_id")) {
                String strai = serviceHub.getConfig(cedpre+model.get("ai_credential_id"));
                Map cloudai = (!strai) ? new HashMap() : yaml.loadAs(strai, Map.class)
                return cloudai.get("accesstoken")
            }
            return null
        }

        def getmodelmap = { def model_id ->
            String strai = serviceHub.getConfig("cloud-ai-agent-"+agentpre+model_id);
            Map cloudai = (!strai) ? new HashMap() : yaml.loadAs(strai, Map.class)
            return cloudai

        }

        def getmodel = { String model_id ->
            def filter=agent_runtime.createSearchContext()
            filter.eq("id",model_id)
            return agent_runtime.selectOne(filter,true)
        }

        try {





            def chat_model = null
            def flash_model = null
            def intent_model = null
            def vl_model = null
            def embedding_model = null
            def rerank_model = null





            if(id == "aifactory_sys_env") {
                String strConfig = serviceHub.getConfig("deploysystem-${sysid}".toString());
                //_default.set("configs",strConfig)

                if(chat_model_id) {
                    chat_model = getmodel(chat_model_id)
                    if(chat_model) {
                        if(_default.get("chat_model_id")){
                            agent_runtime.update(chat_model)
                        }
                        String strai = serviceHub.getConfig("cloud-ai");
                        Map cloudai = (!strai) ? new HashMap() : yaml.loadAs(strai, Map.class)
                        def defaultagent = cloudai.get("defaultagent")
                        def agentid=agentpre+chat_model_id
                        println "defaultagent:${defaultagent}=>${agentid}"
                        if(!defaultagent || (defaultagent!=agentid && defaultagent.startsWith(agentpre))) {
                            cloudai.put("defaultagent",agentid)
                            serviceHub.publishConfig("cloud-ai", cloudai);
                            println "cloud-ai defaultagent:${defaultagent}=>${agentid}"
                        }
                    }

                }

                def utilkey = "cloud-ai-agent-${sysid}-kb--sysknowledgebaseutil".toString()
                String strutil = serviceHub.getConfig(utilkey);
                Map kbutil = (!strutil) ? new HashMap() : yaml.loadAs(strutil, Map.class)

                def querykey = "cloud-ai-agent-${sysid}-kb--sysknowledgebaseutil-query".toString()
                String strquery = serviceHub.getConfig(querykey);
                Map kbquery = (!strquery) ? new HashMap() : yaml.loadAs(strquery, Map.class)

                if(flash_model_id) {
                    flash_model = getmodel(flash_model_id)
                    if(flash_model) {
                        if(_default.get("flash_model_id")){
                            agent_runtime.update(flash_model)
                        }
                        try{
                            def _map = getmodelmap(flash_model_id);
                            if(_map) {
                                _map.remove("credentialid")
                                kbutil.putAll(_map)
                                def token=gettoken(flash_model)
                                kbutil.put("accesstoken",token)
                                println "kbutil flash_model_id -> ${flash_model_id}, accesstoken -> ${token}"
                            }


                        }catch (Exception ex1) {
                            ex1.printStackTrace()
                            println "kbutil fill flash_model_id exception"
                        }

                    }
                }

                if(intent_model_id) {
                    intent_model = getmodel(intent_model_id)
                    if(intent_model) {
                        if(_default.get("intent_model_id")){
                            agent_runtime.update(intent_model)
                        }
                        try{
                            def _map = getmodelmap(intent_model_id);
                            if(_map){
                                _map.remove("credentialid")
                                kbquery.putAll(_map)
                                def token=gettoken(intent_model)
                                kbquery.put("accesstoken",token)
                                println "kbquery intent_model_id -> ${intent_model_id},accesstoken -> ${token}"
                            }


                        }
                        catch (Exception ex1) {
                            ex1.printStackTrace()
                            println "kbquery fill intent_model_id exception"
                        }

                    }
                }

                if(vl_model_id) {
                    vl_model = getmodel(vl_model_id)
                    if(vl_model) {
                        if(_default.get("vl_model_id")){
                            agent_runtime.update(vl_model)
                        }
                        String strOss = serviceHub.getConfig("cloud-oss");
                        Map cloudoss = (!strOss) ? new HashMap() : yaml.loadAs(strOss, Map.class)
                        Map aiimage = cloudoss.getOrDefault("aiimage", new HashMap())
                        def vlagent = aiimage.get("agent")
                        def agentid=agentpre+vl_model_id
                        println "vlagent:${vlagent}=>${agentid}"
                        if(!vlagent || vlagent!=agentid) {
                            aiimage.put("agent",agentid)
                            serviceHub.publishConfig("cloud-oss", cloudoss);
                            println "cloud-oss vlagent:${vlagent}=>${agentid}"
                        }
                    }
                }

                if(embedding_model_id) {
                    embedding_model = getmodel(embedding_model_id)
                    if(embedding_model) {
                        if(_default.get("embedding_model_id")){
                            agent_runtime.update(embedding_model)
                        }
                        try{
                            def _map = getmodelmap(embedding_model_id);
                            if(_map) {
                                kbutil.put("embeddingurl",_map.get("embeddingurl"))
                                kbutil.put("embeddingmodel",_map.get("embeddingmodel"))

                                def token=gettoken(embedding_model)
                                kbutil.put("embeddingtoken",token)
                                println "kbutil embeddingmodel -> ${_map.get("embeddingmodel")}, accesstoken -> ${token}"

                            }
                        }
                        catch (Exception ex1) {
                            ex1.printStackTrace()
                            println "kbutil fill flash_model_id exception"
                        }
                    }
                }

                if(rerank_model_id) {
                    rerank_model = getmodel(rerank_model_id)
                    if(rerank_model) {
                        if(_default.get("rerank_model_id")){
                            agent_runtime.update(rerank_model)
                        }
                        try{
                            def _map = getmodelmap(rerank_model_id)
                            if(_map) {
                                kbutil.put("textrerankurl",_map.get("textrerankurl"))
                                kbutil.put("textrerankmodel",_map.get("textrerankmodel"))

                                def token=gettoken(rerank_model)
                                kbutil.put("textreranktoken",token)
                                kbutil.put("aitype",_map.get("aitype"))
                                println "kbutil rerank_model -> ${_map.get("textrerankmodel")}, accesstoken -> ${token}"

                            }
                        }
                        catch (Exception ex1) {
                            ex1.printStackTrace()
                            println "kbutil fill textrerankmodel exception"
                        }
                    }
                }

                serviceHub.publishConfig(utilkey,kbutil)
                serviceHub.publishConfig(querykey,kbquery)







                String strkb = serviceHub.getConfig("cloud-kb");
                if(!strkb) {
                    strkb="fetchkbs:\n  url: lb://servicehub-ibizaifactory/ibizaifactory/serviceapi/ai_knowledge_bases/fetch_full_text\n  method: POST\n  agentformat: ibizaifactory-kb--{key}"
                    serviceHub.publishConfig("cloud-kb", strkb);
                }

            }




        } catch (Exception e) {
            e.printStackTrace()
        }
```

#### update :id=DEACTION_01<sup class="footnote-symbol"> <font color=gray size=1>[实体行为]</font></sup>



调用实体 [类别设置(CATEGORY_SETTINGS)](module/Base/category_settings.md) 行为 [Update](module/Base/category_settings#行为) ，行为参数为`Default(传入变量)`

将执行结果返回给参数`Default(传入变量)`

#### 结束 :id=END_01<sup class="footnote-symbol"> <font color=gray size=1>[结束]</font></sup>



返回 `Default(传入变量)`



### 实体逻辑参数

|    中文名   |    代码名    |  数据类型    |  实体   |备注 |
| --------| --------| -------- | -------- | --------   |
|传入变量(<i class="fa fa-check"/></i>)|Default|数据对象|[类别设置(CATEGORY_SETTINGS)](module/Base/category_settings.md)||
