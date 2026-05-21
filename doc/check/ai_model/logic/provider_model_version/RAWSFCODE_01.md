<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
def page_temp = logic.param('page_temp').getReal()
def _default = logic.param('default').getReal()

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
def base_url=_default.get("base_url")
def default_version=_default.get("default_version")
if(!default_version) {
    default_version="/v1"
}
def default_token=_default.get("default_token")
if(!default_token) {
    default_token=_default.get("access_token")
}

def api_base_url = _default.get("api_base_url")
if(!api_base_url) {
    api_base_url = base_url+default_version
}
def _uri = getBaseUrl(api_base_url,default_version)+"/models"



page_temp.set("provider_models",null)

try {
    def _webclient = sys.webclient()
    def _param =  [:]
    def _headers = [
        "Authorization": "Bearer "+default_token,
        "Content-Type": "application/json"
    ]

    def rep = _webclient.get(_uri,_param,_headers)
    List contentList = new ArrayList<>();
    def jsonMap = net.ibizsys.central.service.client.WebClientBase.MAPPER.readValue(rep.getBody(), Map.class)
    def dataList = jsonMap.get("data")

    if(!org.springframework.util.ObjectUtils.isEmpty(dataList)) {
        for(Object objItem: dataList) {
            net.ibizsys.central.util.EntityDTO dto = net.ibizsys.central.service.client.WebClientBase.MAPPER.convertValue(objItem, net.ibizsys.central.util.EntityDTO.class);
            def modelId = dto.get("id"); 
            if(modelId) {
                dto.set("name", modelId);
            }

            contentList.add(dto);
        }

        def  nPage = _default.page
        def nSize = _default.size
        def _models= new net.ibizsys.central.util.PageImpl(contentList, org.springframework.data.domain.PageRequest.of(nPage, nSize), contentList.size())
        page_temp.set("provider_models",_models)
    }   
}catch(Exception e){
     println("获取模型提供商版本错误: " + e.message)
}

```
