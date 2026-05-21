# 文档(ai_kb_document_advanced_search_grid_pickview)  <!-- {docsify-ignore-all} -->



## 控件
#### CAPTIONBAR(captionbar)
#### 数据表格(grid)
#### 搜索栏(searchbar)
#### 搜索表单(tabsearchform)

## 视图界面逻辑
* `onSelectionChange`
```javascript
console.log("");
data.forEach(item => {
  item.srfdename = 'ai_kb_document';
});
//获取选择视图
view.parentView.parentView.state['srfpickupdata'] = data;

```
  * newdata(预置新建数据逻辑)
  * opendata(预置打开数据逻辑)


### 关联界面行为
  * [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document) : [重新切片](module/ai/ai_kb_document#界面行为)
  * [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document) : [设置元数据](module/ai/ai_kb_document#界面行为)
  * [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document) : [重新索引](module/ai/ai_kb_document#界面行为)
  * [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document) : [文档重新解析](module/ai/ai_kb_document#界面行为)
  * [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document) : [表格界面_删除操作](module/ai/ai_kb_document#界面行为)

### 关联视图
  * [知识库文档(ai_kb_document_edit_view)](app/view/ai_kb_document_edit_view)
  * [文档元数据(ai_kb_document_meta_data_view)](app/view/ai_kb_document_meta_data_view)
  * [重新切片(ai_kb_document_rechunk_option_view)](app/view/ai_kb_document_rechunk_option_view)

<script>
 const { createApp } = Vue
  createApp({
    data() {
      return {

      }
    }
  }).use(ElementPlus).mount('#app')
</script>