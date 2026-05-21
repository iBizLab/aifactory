<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
def filter = logic.param("Default").getReal();

// 1. 获取三个来源，不做任何假设
def kw1 = filter.get("keyword")  // 可能为 String 或 null
def kw2 = filter.get("keywords") // 可能为 String[] 或 List 或 null
def kw3 = filter.get("queries")    // 可能为 String 或 null

def allTokens = []

// 2. 逐个手动处理，确保不触发非法转换
[kw1, kw2, kw3].each { item ->
    if (item == null) return
    
    if (item instanceof Object[]) { 
        // 专门处理 String[] 数组，这是你报错的根源
        item.each { if (it) allTokens.add(it.toString()) }
    } else if (item instanceof Collection) {
        // 专门处理 List
        item.each { if (it) allTokens.add(it.toString()) }
    } else if (item instanceof String) {
        // 专门处理字符串，按空格切分
        item.split('[,\\s]+').each { if (it) allTokens.add(it) }
    }
}

// 3. 统一清洗：去掉首尾空格，去掉空字符串
allTokens = allTokens.collect { it.trim() }.findAll { it != "" }.unique()

// 4. 校验与合并
if (allTokens.isEmpty()) {
    throw new IllegalArgumentException("搜索关键词不能为空")
}

def finalKeyword = allTokens.join(" ")

filter.set("keyword",finalKeyword)
```
