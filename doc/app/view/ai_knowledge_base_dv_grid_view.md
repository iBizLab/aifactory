# 知识库(ai_knowledge_base_dv_grid_view)  <!-- {docsify-ignore-all} -->



## 控件
#### CAPTIONBAR(captionbar)
#### 数据表格(grid)

##### 部件逻辑
* `onLoadSuccess` : [计算表格列行为状态(ai_knowledge_base)](module/ai/ai_knowledge_base/uilogic/calc_column_action_state)
#### 搜索栏(searchbar)
#### 搜索表单(searchform)

## 视图界面逻辑
  * newdata(预置新建数据逻辑)
  * opendata(预置打开数据逻辑)


### 关联界面行为
  * [知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base) : [查看知识库成员](module/ai/ai_knowledge_base#界面行为)
  * [知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base) : [打开知识库信息视图](module/ai/ai_knowledge_base#界面行为)
  * [知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base) : [打开配置中心](module/ai/ai_knowledge_base#界面行为)
  * [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document) : [打开知识库文档同步表格视图](module/ai/ai_kb_document#界面行为)
  * [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document) : [打开知识库文档向导视图](module/ai/ai_kb_document#界面行为)
  * [知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base) : [取消星标](module/ai/ai_knowledge_base#界面行为)
  * [知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base) : [设置星标](module/ai/ai_knowledge_base#界面行为)
  * [知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base) : [编辑基本信息](module/ai/ai_knowledge_base#界面行为)
  * [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document) : [打开文档概览导航](module/ai/ai_kb_document#界面行为)
  * [知识库文档分块(AI_KB_CHUNK)](module/ai/ai_kb_chunk) : [null](module/ai/ai_kb_chunk#界面行为)
  * [知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base) : [打开知识库导航页](module/ai/ai_knowledge_base#界面行为)

### 关联界面逻辑
  * [知识库文档分块(AI_KB_CHUNK)](module/ai/ai_kb_chunk) : [打开所属文档](module/ai/ai_kb_chunk/uilogic/open_doc)
  * [知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base) : [计算表格列行为状态(ai_knowledge_base)](module/ai/ai_knowledge_base/uilogic/calc_column_action_state)

### 关联视图
  * [切片(ai_kb_chunk_chunk_info_view)](app/view/ai_kb_chunk_chunk_info_view)
  * [检索测试(ai_kb_chunk_retrieval_test_custom_view)](app/view/ai_kb_chunk_retrieval_test_custom_view)
  * [知识库文档(ai_kb_document_grid_view)](app/view/ai_kb_document_grid_view)
  * [知识库文档清单(ai_kb_document_kb_tree_exp_view)](app/view/ai_kb_document_kb_tree_exp_view)
  * [文档清单(ai_kb_document_main_grid_view)](app/view/ai_kb_document_main_grid_view)
  * [文档概览导航(ai_kb_document_main_list_exp_view)](app/view/ai_kb_document_main_list_exp_view)
  * [同步设置(ai_kb_document_sync_grid_view)](app/view/ai_kb_document_sync_grid_view)
  * [知识库文档向导(ai_kb_document_wizard_create_wizard_view)](app/view/ai_kb_document_wizard_create_wizard_view)
  * [知识图谱(ai_kb_graph_entity_custom_view)](app/view/ai_kb_graph_entity_custom_view)
  * [知识库成员(ai_kb_member_config_grid_view)](app/view/ai_kb_member_config_grid_view)
  * [高级设置(ai_knowledge_base_advanced_setting_view)](app/view/ai_knowledge_base_advanced_setting_view)
  * [基本信息(ai_knowledge_base_base_info_edit_view)](app/view/ai_knowledge_base_base_info_edit_view)
  * [知识库信息(ai_knowledge_base_base_info_view)](app/view/ai_knowledge_base_base_info_view)
  * [高级配置(ai_knowledge_base_chunk_view)](app/view/ai_knowledge_base_chunk_view)
  * [知识库(ai_knowledge_base_config_tree_exp_view)](app/view/ai_knowledge_base_config_tree_exp_view)
  * [知识库(ai_knowledge_base_index_view)](app/view/ai_knowledge_base_index_view)
  * [知识库(ai_knowledge_base_main_view)](app/view/ai_knowledge_base_main_view)
  * [知识库(ai_knowledge_base_quick_create_view)](app/view/ai_knowledge_base_quick_create_view)
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