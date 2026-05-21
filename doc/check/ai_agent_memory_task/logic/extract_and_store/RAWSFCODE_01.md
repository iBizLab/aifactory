<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
def _chat_temp = logic.param('chat_temp').getReal();
def _chat_temp2 = logic.param('chat_temp2').getReal();
def _default = logic.param('Default').getReal();
def _message_list = logic.param('message_list').getReal();
def messages = _message_list.content

if (_chat_temp  && messages){
    //设置会话快照
    def conversation_snapshot = messages.collect { item ->"[${item.sender_type}]${item.content}"}.join('\n')
   _default.conversation_snapshot=conversation_snapshot;

    def last_message = messages.last()
    //设置最后消息时间
    _default.last_msg_time=last_message.create_time

    def extract_memory_str = _chat_temp.get('extract_memory')
        //设置提取的新记忆
    _default.extracted_content=extract_memory_str;
    
    def extract_memory_obj= new groovy.json.JsonSlurper().parseText(net.ibizsys.central.cloud.core.ai.util.AIChatUtils.getJsonContent(extract_memory_str))
    def candidates_list = extract_memory_obj['candidates']
    def fact_source_candidates = candidates_list.findAll { it['mem_type'] == 'fact_source' }?: []
    def fact_content_list = fact_source_candidates.collect { it.content }
    def fact_source_str = fact_source_candidates ? net.ibizsys.model.util.JsonUtils.getMapper().writeValueAsString(fact_source_candidates) : null
    _chat_temp2.set("fact_source_candidates", fact_source_str)
    _chat_temp2.set("fact_content_list", fact_content_list)

     def daily_log_candidates = candidates_list.findAll { it['mem_type'] == 'daily_log' }?: []
     _default.set("daily_logs",daily_log_candidates)

     println"\n---记忆提取的后的default----${_default}"
 }   

```
