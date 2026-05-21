# 文档(ai_kb_document_filter_grid_view)  <!-- {docsify-ignore-all} -->



## 控件
#### CAPTIONBAR(captionbar)
#### 数据表格(grid)
#### 搜索栏(searchbar)
#### 工具栏(toolbar)

## 视图界面逻辑
* `onSelectionChange`
```javascript
console.log(view)
console.log("打开知识库文档")

const KBId = ctrl.state.selectedData[0]?.kb_id;
const DocId = ctrl.state.selectedData[0]?.id;
const File = ctrl.state.selectedData[0]?.file;
/*const encodedFile = encodeURIComponent(File);
const ctx = `{"srfnavctrlid":"aifactoryweb.ai_kb_document_main_list_exp_view@aifactoryweb.ai_kb_document.main_list_exp_view_list","file":"${File}","ai_kb_document":"${DocId}"}`
const encodedCTX = encodeURIComponent(ctx);
const Url = `/-/index/ai_knowledge_base=${KBId}/ai_knowledge_base_index_view/srfnav=index_view/ai_kb_document_main_list_exp_view/srfnav=${DocId}/ai_kb_document_main_show_view/srfnavctx=${encodedCTX}`;
const encodedUrl = encodeURI(Url);*/

ibiz.openView.push(
    `/-/index/ai_knowledge_base=${KBId}/ai_knowledge_base_index_view/srfnav=index_view/ai_kb_document_main_list_exp_view/srfnav=${DocId}/ai_kb_document_main_show_view/srfnavctx=%7B%22srfnavctrlid%22:%22aifactoryweb.ai_kb_document_main_list_exp_view@aifactoryweb.ai_kb_document.main_list_exp_view_list%22,%22ai_kb_document%22:%22${DocId}%22%7D`
  );
/*
ibiz.openView.push(
    `/-/index/ai_knowledge_base=${KBId}/ai_knowledge_base_index_view/srfnav=index_view/ai_kb_document_main_list_exp_view/srfnav=${DocId}/ai_kb_document_main_show_view/srfnavctx=%7B%22srfnavctrlid%22:%22aifactoryweb.ai_kb_document_main_list_exp_view@aifactoryweb.ai_kb_document.main_list_exp_view_list%22%2C%22file%22%3A%22${encodedFile}%22%2C%22ai_kb_document%22%3A%22${DocId}%22%7D`
  );
  */
```
  * newdata(预置新建数据逻辑)
  * opendata(预置打开数据逻辑)


### 关联界面行为
  * [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document) : [表格界面_删除操作](module/ai/ai_kb_document#界面行为)
  * [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document) : [设置元数据](module/ai/ai_kb_document#界面行为)
  * [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document) : [重新索引](module/ai/ai_kb_document#界面行为)
  * [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document) : [重新切片](module/ai/ai_kb_document#界面行为)
  * [知识库文档分块(AI_KB_CHUNK)](module/ai/ai_kb_chunk) : [null](module/ai/ai_kb_chunk#界面行为)
  * [知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base) : [打开知识库导航页](module/ai/ai_knowledge_base#界面行为)
  * [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document) : [文档重新解析](module/ai/ai_kb_document#界面行为)

### 关联界面逻辑
  * [知识库文档分块(AI_KB_CHUNK)](module/ai/ai_kb_chunk) : [打开所属文档](module/ai/ai_kb_chunk/uilogic/open_doc)

### 关联视图
  * [切片(ai_kb_chunk_chunk_info_view)](app/view/ai_kb_chunk_chunk_info_view)
  * [检索测试(ai_kb_chunk_retrieval_test_custom_view)](app/view/ai_kb_chunk_retrieval_test_custom_view)
  * [知识库文档(ai_kb_document_edit_view)](app/view/ai_kb_document_edit_view)
  * [知识库文档(ai_kb_document_grid_view)](app/view/ai_kb_document_grid_view)
  * [知识库文档清单(ai_kb_document_kb_tree_exp_view)](app/view/ai_kb_document_kb_tree_exp_view)
  * [文档元数据(ai_kb_document_meta_data_view)](app/view/ai_kb_document_meta_data_view)
  * [重新切片(ai_kb_document_rechunk_option_view)](app/view/ai_kb_document_rechunk_option_view)
  * [知识图谱(ai_kb_graph_entity_custom_view)](app/view/ai_kb_graph_entity_custom_view)
  * [知识库成员(ai_kb_member_config_grid_view)](app/view/ai_kb_member_config_grid_view)
  * [高级设置(ai_knowledge_base_advanced_setting_view)](app/view/ai_knowledge_base_advanced_setting_view)
  * [基本信息(ai_knowledge_base_base_info_edit_view)](app/view/ai_knowledge_base_base_info_edit_view)
  * [高级配置(ai_knowledge_base_chunk_view)](app/view/ai_knowledge_base_chunk_view)
  * [知识库(ai_knowledge_base_config_tree_exp_view)](app/view/ai_knowledge_base_config_tree_exp_view)
  * [知识库(ai_knowledge_base_index_view)](app/view/ai_knowledge_base_index_view)
  * [召回策略(ai_knowledge_base_recall_view)](app/view/ai_knowledge_base_recall_view)
  * [知识库(ai_knowledge_base_tree_exp_view)](app/view/ai_knowledge_base_tree_exp_view)
  * [智能审查记录(ai_review_report_review_grid)](app/view/ai_review_report_review_grid)

<script>
 const { createApp } = Vue
  createApp({
    data() {
      return {

      }
    }
  }).use(ElementPlus).mount('#app')
</script>