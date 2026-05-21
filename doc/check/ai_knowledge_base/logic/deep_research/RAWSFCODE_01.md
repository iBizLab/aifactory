<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
def query_chunk_result = logic.param("query_chunk_result").getReal();
def retrieved_chunks = logic.param("retrieved_chunks").getReal();

if (!query_chunk_result || !query_chunk_result.getContent()) {
    return
}

//只取前五条
def query_chunks = query_chunk_result.getContent().take(5)

// 计算当前 retrieved_chunks 中所有 content 的总长度
def currentTotalLength = 0
if(retrieved_chunks){
    currentTotalLength = retrieved_chunks.sum { it.getContent() ? it.getContent().length() : 0 }
}

if(currentTotalLength > 30000) {
    return
}


// 构建已存在 ID 的集合（用于快速去重）
Set existingIds = retrieved_chunks.collect { it.getId() } as Set

for (def chunk in query_chunks) {
    if(currentTotalLength > 30000) {
        break
    }
    if (existingIds.contains(chunk.getId())) {
        continue
    }

    retrieved_chunks.add(chunk)
    existingIds.add(chunk.getId())
    currentTotalLength += chunk.getContent() ? chunk.getContent().length() : 0

    println "------------------------retrieved_chunks lenght：" + currentTotalLength
}


```
