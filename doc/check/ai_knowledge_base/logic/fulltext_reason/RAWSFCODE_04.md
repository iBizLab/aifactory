<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
def _fulltext_chunk_list = logic.param("fulltext_chunk_list").getReal();
def _doc_fulltext = logic.param("doc_fulltext").getReal();

def  fulltext = _doc_fulltext.get("content")
// 按行分割，保留换行结构（便于段落感知）
    def lines = fulltext.readLines()
    def chunks = []
    def currentChunk = []
    def currentWordCount = 0

    for (line in lines) {
        // 计算当前行的字数（中文/英文通用：按字符数或按空格+中文字符？这里按字符数更稳妥）
        def lineWordCount = line.length()

        // 如果当前行本身超过 maxWordsPerChunk，强制分割（极端情况）
        if (lineWordCount > 20000) {
            // 先 flush 当前 chunk
            if (currentChunk) {
                chunks << currentChunk.join('\n')
                currentChunk = []
                currentWordCount = 0
            }

            // 对超长行进行句子级分割
            def sentences = line.split(/(?<=[。！？.!?])\s*/)
            def tempSentences = []
            def tempCount = 0

            for (sent in sentences) {
                def sentLen = sent.length()
                if (tempCount + sentLen > 20000 && tempSentences) {
                    chunks << tempSentences.join('')
                    tempSentences = [sent]
                    tempCount = sentLen
                } else {
                    tempSentences << sent
                    tempCount += sentLen
                }
            }
            if (tempSentences) {
                chunks << tempSentences.join('')
            }
            continue
        }

        // 正常行：判断加入后是否超限
        if (currentWordCount + lineWordCount > 20000) {
            // 超了，先保存当前 chunk
            if (currentChunk) {
                chunks << currentChunk.join('\n')
            }
            // 开启新 chunk
            currentChunk = [line]
            currentWordCount = lineWordCount
        } else {
            // 未超限，加入当前 chunk
            currentChunk << line
            currentWordCount += lineWordCount
        }
    }

    // 处理最后一块
    if (currentChunk) {
        chunks << currentChunk.join('\n')
    }

_fulltext_chunk_list = chunks

println "------------------------拆分后的文档块：" + _fulltext_chunk_list

```
