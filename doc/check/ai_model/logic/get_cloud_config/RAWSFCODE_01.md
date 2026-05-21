<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
def _default = logic.param('Default').getReal()
        def agentkey = _default.get("id")
        def _map = logic.param('map').getReal()

        def VERSION_PATTERN = ~/\/v\d+$/

        List<String> ENDPOINT_SUFFIXES = [
                "/chat/completions",
                "/embeddings",
                "/v1/embeddings",      // 某些厂商带 v1 的全路径
                "/v1/chat/completions",
                "/rerank",
                "/v1/rerank",
                "/services/rerank/text-rerank/text-rerank",
                "/v1/models",              // 查询模型清单的接口
                "/models"
        ]


        def getBaseUrl = { String userInput, String defaultVer = "/v1" ->
            if (!userInput?.trim()) return ""

            String url = userInput.trim().replaceAll(/\/+$/, "")


            for (suffix in ENDPOINT_SUFFIXES) {
                if (url.endsWith(suffix)) {
                    url = url.substring(0, url.length() - suffix.length()).replaceAll(/\/+$/, "")
                    break // 匹配到一个就跳出，防止重复切除
                }
            }

            if (!(url =~ VERSION_PATTERN) && !url.endsWith("/api")) {
                String path = defaultVer.startsWith("/") ? defaultVer : "/${defaultVer}"
                url += path
            }

            return url
        }

        try {

            def isModelActive = _default.getBoolean("ACTIVE",true)
            def isEnableDescOssImage = _default.getBoolean("DESC_OSS_IMAGE",false)

            // 字符串类字段保持原有处理
            def modelCapability = _default.get("MODEL_CAPABILITY")?.toString() ?: ""
            def apiBaseUrl = (_default.get("API_BASE_URL")?.toString() ?: "").trim().replaceAll(/\/+$/, "")
            def baseUrl = getBaseUrl(apiBaseUrl)
            def modelCategory = _default.get("MODEL_CATEGORY")?.toString() ?: ""
            def codeName = _default.get("CODE_NAME")?.toString() ?: ""
            def ossImageVlPrompt = _default.get("OSS_IMAGE_VL_PROMPT")?.toString()
            def serviceHub = net.ibizsys.central.cloud.core.spring.rt.ServiceHub.getInstance()
            org.yaml.snakeyaml.Yaml yaml = new org.yaml.snakeyaml.Yaml();


            if (!isModelActive) {
                _map.set("disabled", true)
            }

            _map.set("serviceurl", apiBaseUrl)

            _map.set("baseurl", baseUrl)

            if (modelCapability.contains("reasoning")) {
                _map.set("think", true)
            }

            if (modelCapability.contains("function_calling")) {
                _map.set("tools", true)
                _map.set("toolmaxcalls", 200) // 改为数字类型更规范
            }

            if (apiBaseUrl.contains("https://api.deepseek.com")) {
                _map.set("aitype", "DEEPSEEK")
            }
            else if (modelCategory == "text_ranking" && apiBaseUrl.contains("/rerank") && apiBaseUrl != "https://dashscope.aliyuncs.com/api/v1/services/rerank/text-rerank/text-rerank") {
                _map.set("aitype", "OPENAI")
            }
            else if (modelCategory == "vision") {
                _map.set("aitype", "QWENVL")
            }
             else if (apiBaseUrl.contains("siliconflow.cn")) {
                _map.set("aitype", "SILICONFLOW")
            }
            else {
                _map.set("aitype", "QWEN")
            }

            if (modelCapability.contains("streaming")) {
                _map.set("stream", true)
            }
            else {
                _map.set("stream", false)
            }

            if (modelCategory == "vision") {
                _map.set("descossimage", true)
                if (ossImageVlPrompt != null) {
                    _map.set("ossimagevlprompt", ossImageVlPrompt)
                }
            }

            if (modelCategory == "embedding" ) {
                _map.set("embeddingmodel", codeName)
                if(apiBaseUrl.contains("embeddings"))
                    _map.set("embeddingurl", apiBaseUrl)
                else
                    _map.set("embeddingurl", baseUrl+"/embeddings")
            }

            if (modelCategory == "text_ranking") {
                _map.set("textrerankmodel", codeName)
                if(apiBaseUrl.contains("rerank"))
                    _map.set("textrerankurl", apiBaseUrl)
                else
                    _map.set("textrerankurl", baseUrl+"/rerank")
            }

            if ((modelCategory == "chat" || modelCategory == "vision") ) {

                if(apiBaseUrl.contains("chat/completions"))
                    _map.set("chatcompletionurl", apiBaseUrl)
                else
                    _map.set("chatcompletionurl", baseUrl+"/chat/completions")
            }

            if (isEnableDescOssImage) {
                _map.set("descossimage", true)
                if (ossImageVlPrompt != null) {
                    _map.set("ossimagevlprompt", ossImageVlPrompt)
                }
            }


            // ==============================
            // 系统OSS配置更新逻辑（保持原逻辑，仅增加空安全处理）
            // ==============================
            if(modelCategory == "vision") {
                String strConfig = serviceHub.getConfig("cloud-oss");
                Map config = (!strConfig) ? new HashMap() : yaml.loadAs(strConfig, Map.class);

                Map aiimage = config.getOrDefault("aiimage", new HashMap());
                aiimage.put("agent", "${sys.getDeploySystemId()}-ai--${agentkey}".toString());
                config.put("aiimage", aiimage);


                // 补全文件存储路径
                if(!config.containsKey("filepath")) {
                    String filepath = "/app/file/oss/file";
                    String allinone = serviceHub.getConfig("servicehub-allinone");
                    if(allinone){
                        Map allinoneConfig = yaml.loadAs(allinone, Map.class);
                        if(allinoneConfig.containsKey("systemsettings")) {
                            Map systemsettings  = allinoneConfig.getOrDefault("systemsettings",new HashMap());
                            if(systemsettings.containsKey("cloudossutil")) {
                                Map cloudossutil  = systemsettings.getOrDefault("cloudossutil",new HashMap());
                                if(cloudossutil.containsKey("filepath")) {
                                    filepath = cloudossutil.remove("filepath")?.toString() ?: filepath
                                    systemsettings.remove("cloudossutil");
                                    serviceHub.publishConfig("servicehub-allinone",allinoneConfig)
                                }
                            }
                            else if (!strConfig){
                                filepath = "/app/file/datafile/gateway/ibizutil"
                            }
                        }
                    }
                    config.put("filepath", filepath)
                }

                // 补全libreoffice配置
                if(!config.containsKey("libreoffice")) {
                    config.put("libreoffice", [path: "/usr/bin/soffice"])
                }

                // 补全7z解压配置
                if(!config.containsKey("unzip_7z")) {
                    config.put("unzip_7z", [command: "7z x {zip_file} -o{unzip_folder}"])
                }

                if(!config.containsKey("ocr")) {
                    // 补全OCR别名配置
                    if(!config.containsKey("osstext") ) {
                        config.put("osstext", [aliases: ["ENGINE.OCR": "ENGINE.VLOCR"]])
                    }
                    aiimage.put("ocragent", "${sys.getDeploySystemId()}-ai--${agentkey}".toString());
                }
            


                serviceHub.publishConfig("cloud-oss", config);
            }




        } catch (Exception e) {
            e.printStackTrace()
        }
```
