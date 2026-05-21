# 知识库(ai_knowledge_base_config_tree_exp_view)  <!-- {docsify-ignore-all} -->


系统自动添加



## 控件
#### CAPTIONBAR(captionbar)
#### 搜索栏(searchbar)
#### 树视图导航栏(treeexpbar)

## 视图界面逻辑
  * newdata(预置新建数据逻辑)
  * opendata(预置打开数据逻辑)


### 关联视图
  * [知识库文档(ai_kb_document_grid_view)](app/view/ai_kb_document_grid_view)
  * [知识库成员(ai_kb_member_config_grid_view)](app/view/ai_kb_member_config_grid_view)
  * [高级设置(ai_knowledge_base_advanced_setting_view)](app/view/ai_knowledge_base_advanced_setting_view)
  * [基本信息(ai_knowledge_base_base_info_edit_view)](app/view/ai_knowledge_base_base_info_edit_view)
  * [高级配置(ai_knowledge_base_chunk_view)](app/view/ai_knowledge_base_chunk_view)
  * [召回策略(ai_knowledge_base_recall_view)](app/view/ai_knowledge_base_recall_view)

<script>
 const { createApp } = Vue
  createApp({
    data() {
      return {

      }
    }
  }).use(ElementPlus).mount('#app')
</script>