# 知识库(ai_knowledge_base_quick_create_view)  <!-- {docsify-ignore-all} -->


系统自动添加



## 控件
#### CAPTIONBAR(captionbar)
#### DATAINFOBAR(datainfobar)
#### 编辑表单(form)

##### 部件逻辑
* `onLoadSuccess`
```
var chunk_method = data[0].chunk_method
data[0].parser_config.method = chunk_method
```
* `onLoadDraftSuccess`
```
var chunk_method = data[0].chunk_method
data[0].parser_config.method = chunk_method
```
#### 工具栏(toolbar)


### 关联界面行为
  * [知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base) : [编辑界面_删除并退出操作](module/ai/ai_knowledge_base#界面行为)
  * [知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base) : [编辑界面_拷贝操作](module/ai/ai_knowledge_base#界面行为)
  * [知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base) : [编辑界面_保存操作](module/ai/ai_knowledge_base#界面行为)

### 关联视图
  * [知识库源(ai_knowledge_source_pickup_view)](app/view/ai_knowledge_source_pickup_view)

<script>
 const { createApp } = Vue
  createApp({
    data() {
      return {

      }
    }
  }).use(ElementPlus).mount('#app')
</script>