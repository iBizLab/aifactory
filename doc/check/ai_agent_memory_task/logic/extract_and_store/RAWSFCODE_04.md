<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
def _checkQueries = logic.param('check_queries').getReal()
def _default = logic.param('Default').getReal()
def verification_result_str =null
def _chat_temp = logic.param('chat_temp').getReal();
def _log = org.apache.commons.logging.LogFactory.getLog("cn.ibizlab.central.core.dataentity.logic.DELogicRuntimeBase")

if (_chat_temp){
    verification_result_str = _chat_temp.get('verification_result')
    println("核验结果："+ verification_result_str)
    _default.update_strategy=verification_result_str//设置更新策略
    
    if (!verification_result_str || verification_result_str.trim() == "[]") {
        _default.set("latest_chunks",null)
        return  _default
    } 
}   

// 工具：安全转换实体列表为 Map 列表
def convertToMapList = { list ->
    if (!list) return []
    list.collect { item ->
        [
            id: item?.id,
            content: (item?.content ? item.content.split(/\r?\n/) as List<String> : [])
        ]
    }
}

def generateId = { "chunk_${System.currentTimeMillis()}_${(Math.random() * 1000).toInteger()}" }

// 根据行号变化动态计算偏移量
def applyOperations = { List<String> lines, List<Map> ops ->
    int offset = 0
    // 按行号升序排序，确保偏移量计算正确
    ops.sort { a, b ->
        int posA = (a.operation == 'UPDATE_LINES') ? a.line_range.start : a.insert_after_line
        int posB = (b.operation == 'UPDATE_LINES') ? b.line_range.start : b.insert_after_line
        posA <=> posB
    }

    ops.each { op ->
        if (op.operation == 'UPDATE_LINES') {
            int start = op.line_range.start + offset
            int end = op.line_range.end + offset
            int size = lines.size()

            if (start < 1 || end > size) throw new RuntimeException("行号越界：${start}-${end}, 当前行数：${size}")

            int from = start - 1
            int to = end // subList end is exclusive

            lines = lines[0..<from] + (op.new_content_lines as List<String>) + lines[to..<size]
            offset += (op.new_content_lines.size() - (end - start + 1))

        } else if (op.operation == 'INSERT_LINES') {
            int rawIdx = op.insert_after_line + offset
            int idx = Math.max(0, Math.min(rawIdx, lines.size()))
            lines = lines[0..<idx] + (op.new_content_lines as List<String>) + lines[idx..<lines.size()]
            offset += op.new_content_lines.size()
        }
    }
    lines
}

// 内容块更新处理
def processChunks = { chunks, opsJson ->
    def existing = convertToMapList(chunks)
    def ops = new groovy.json.JsonSlurper().parseText(opsJson)
    
    // 建立索引方便查找
    def chunkMap = existing.collectEntries { [(it.id): it] }
    def newChunks = []

    // 1. 处理 CREATE
    ops.findAll { it.operation == 'CREATE' }.each { op ->
        def chunk = [
            id: op.target_chunk_id ?: generateId(),
            content: op.final_content
        ]
        newChunks << chunk
        _log.debug("✅ [CREATE] ${chunk.id} ")
    }

    // 2. 处理 MODIFY (UPDATE/INSERT)
    ops.findAll { it.operation != 'CREATE' }.groupBy { it.target_chunk_id }.each { id, chunkOps ->
        def target = chunkMap[id]
        if (!target) {
            log.debug("⚠️ 警告：未找到 Chunk ${id}, 跳过")
            return
        }
        target.content = applyOperations(target.content, chunkOps)
    }

    // 合并：原有(已修改) + 新增
    def result = chunkMap.values() + newChunks
        // 将 content 列表重新合并为带换行符的字符串
    return result.collect { chunk ->
        def finalContent = (chunk.content instanceof List) ? chunk.content.join('\n') : chunk.content  
        return [
            id: chunk.id,
            content: finalContent 
        ]
    }

}

// 执行入口
try {
    def latest_chunks = processChunks(_checkQueries, verification_result_str)
    _default.set("latest_chunks", latest_chunks ? latest_chunks : null)
    _default.set("status","SUCCESS")
    _default.set("result", "执行成功!")
} catch (Exception e) {
    _default.set("status","FAILED")
    _default.set("result", "记忆内容块处理发生异常!")
    _log.debug("❌ [ERROR] 内容块更新处理异常,处理 Chunk 失败: ${e.message}")
}

return  _default

```
