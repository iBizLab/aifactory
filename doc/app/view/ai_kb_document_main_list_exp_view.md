# 文档概览导航(ai_kb_document_main_list_exp_view)  <!-- {docsify-ignore-all} -->



## 控件
#### CAPTIONBAR(captionbar)
#### 列表(list)
#### 列表视图导航栏(listexpbar)
#### 搜索栏(searchbar)

## 视图界面逻辑
* `onCreated`
```javascript
delete context.ai_kb_document;
```
  * newdata(预置新建数据逻辑)
  * opendata(预置打开数据逻辑)


### 关联界面行为
  * [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document) : [打开文档概览导航](module/ai/ai_kb_document#界面行为)
  * [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document) : [打开知识库文档向导视图](module/ai/ai_kb_document#界面行为)

### 关联视图
  * [文档展示页(ai_kb_document_main_show_view)](app/view/ai_kb_document_main_show_view)
  * [知识库文档向导(ai_kb_document_wizard_create_wizard_view)](app/view/ai_kb_document_wizard_create_wizard_view)

<script>
 const { createApp } = Vue
  createApp({
    data() {
      return {

      }
    }
  }).use(ElementPlus).mount('#app')
</script>