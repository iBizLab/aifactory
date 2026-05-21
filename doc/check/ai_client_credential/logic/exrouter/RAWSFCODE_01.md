<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy

        def _default = logic.param('Default').getReal()
        // 字符串类字段保持原有处理
        def type = _default.get("access_types")?.toString() ?: ""
        
        if(type.indexOf("CHAT")>=0){
            def sysid = sys.getDeploySystemId().toLowerCase()
            def serviceHub = net.ibizsys.central.cloud.core.spring.rt.ServiceHub.getInstance()
            org.yaml.snakeyaml.Yaml yaml = new org.yaml.snakeyaml.Yaml();

            String strConfig = serviceHub.getConfig("deployapp-${sysid}-aifactoryweb-ex".toString());
            Map config = (!strConfig) ? new HashMap() : yaml.loadAs(strConfig, Map.class)

            config.routes = config.routes ?: []

            def targetRouteId = "ibizaifactory__aifactoryweb__ai"

            if (!config.routes.any { it.id == targetRouteId }) {
                config.routes << [
                        id: targetRouteId,
                        uri: "lb://servicehub-ibizaifactory",
                        order: 60,
                        predicates: ["Path=/ibizaifactory__aifactoryweb/factories/**"],
                        filters: ["StripPrefix=1", "PrefixPath=/ibizaifactory/ai"]
                ]
                serviceHub.publishConfig("deployapp-${sysid}-aifactoryweb-ex".toString(),config)
            }
        }
```
