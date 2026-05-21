<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
def _default = logic.param("default").getReal();
def retrieved_chunks = logic.param("retrieved_chunks").getReal();
def verification_checklist = logic.param("verification_checklist").getReal();

def retrieved_chunk_contents = retrieved_chunks
    .collect { it.getContent() } 
    .findAll { it && it.trim() }

String strMessage = ""

// strMessage += "下面将输出根据会话从资料库中检索的内容，供你在后续的交谈中使用。如你的回答涉及引用资料，则必须精准、客观 。杜绝信息幻觉：严禁编造、夸大或组合片段信息来生成片段中不存在的答案。对于片段信息不足的问题，必须如实告知。\n"
// strMessage += "**注意**：输出内容如引用资料片段，需要显式声明及提供资料片段的访问链接`url`，如::[资料片段01](chunkview://chunkid)"
// strMessage += "\r\n\r\n"

strMessage += "retrieved_chunks : \n"

int nIndex = 1;
for (int i = 0; i < retrieved_chunks.size(); i++) {
    def chunk = retrieved_chunks.get(i);
    if (!chunk.getContent()) {
        continue;
    }
    // if (chunk.getDocName()) {
    //     strMessage += String.format("# 资料片段`%1\$s`，url`chunkview://%2\$s`，来自文档`%3\$s`\r\n", nIndex, chunk.getId(), chunk.getDocName());
    // } else {
    //     strMessage += String.format("# 资料片段`%1\$s`，url`chunkview://%2\$s`\r\n", nIndex, chunk.getId());
    // }
    // strMessage += "---\r\n";
    strMessage += chunk.getContent();
    strMessage += "\r\n";
    nIndex++;
}

strMessage += "\nverification_checklist :" + sys.serialize(verification_checklist)


_default.getMessagesIf().addAll(net.ibizsys.central.cloud.core.util.ChatMessagesBuilder.create().user(strMessage).build());



def _content = logic.param("content")
_content.bind(strMessage)
```
