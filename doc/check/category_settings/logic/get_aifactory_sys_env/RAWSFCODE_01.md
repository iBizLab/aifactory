<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
def _default = logic.param('Default').getReal()
        // 字符串类字段保持原有处理
        def id = _default.get("id")?.toString() ?: ""
        def sysid = sys.getDeploySystemId().toLowerCase()
        def agentpre = "${sysid}-ai--".toString()

        def serviceHub = net.ibizsys.central.cloud.core.spring.rt.ServiceHub.getInstance()
        org.yaml.snakeyaml.Yaml yaml = new org.yaml.snakeyaml.Yaml();
        def agent_runtime = sys.dataentity('ai_model')
        def getmodel = { String model_id ->
            def filter=agent_runtime.createSearchContext()
            filter.eq("id",model_id)
            return agent_runtime.selectOne(filter,true)
        }
        
        
        try {

            

            if(id == "aifactory_sys_env") {
                String strConfig = serviceHub.getConfig("deploysystem-${sysid}".toString());
                _default.set("configs",strConfig)

                String strOss = serviceHub.getConfig("cloud-oss");
                Map cloudoss = (!strOss) ? new HashMap() : yaml.loadAs(strOss, Map.class)
                Map aiimage = cloudoss.getOrDefault("aiimage", new HashMap())
                def vlagent = aiimage.get("agent")
                if(vlagent && vlagent.startsWith(agentpre)) {
                    vlagent = vlagent.replace(agentpre,"")
                    def agent = getmodel(vlagent)
                    if(agent) {
                        _default.set("vl_model_id",agent.get("id"))
                        _default.set("vl_model",agent.get("name"))
                    }
                }

                String strai = serviceHub.getConfig("cloud-ai");
                Map cloudai = (!strai) ? new HashMap() : yaml.loadAs(strai, Map.class)
                def defaultagent = cloudai.get("defaultagent")
                if(defaultagent && defaultagent.startsWith(agentpre)) {
                    defaultagent = defaultagent.replace(agentpre,"")
                    def agent = getmodel(defaultagent)
                    if(agent) {
                        _default.set("chat_model_id",agent.get("id"))
                        _default.set("chat_model",agent.get("name"))
                    }
                }

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
