# 知识库(ai_knowledge_base_tree_exp_view)  <!-- {docsify-ignore-all} -->



## 控件
#### CAPTIONBAR(captionbar)
#### 搜索栏(searchbar)
#### 树视图导航栏(treeexpbar)

## 视图界面逻辑
  * newdata(预置新建数据逻辑)
  * opendata(预置打开数据逻辑)


### 关联界面行为
  * [知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base) : [取消星标](module/ai/ai_knowledge_base#界面行为)
  * [知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base) : [打开知识库主页面](module/ai/ai_knowledge_base#界面行为)

### 关联视图
  * [文档(ai_kb_document_filter_grid_view)](app/view/ai_kb_document_filter_grid_view)
  * [知识库(ai_knowledge_base_category_grid_view)](app/view/ai_knowledge_base_category_grid_view)
  * [配置中心(ai_knowledge_base_global_config_tree_view)](app/view/ai_knowledge_base_global_config_tree_view)
  * [知识库(ai_knowledge_base_grid_view)](app/view/ai_knowledge_base_grid_view)
  * [知识库(ai_knowledge_base_index_view)](app/view/ai_knowledge_base_index_view)
  * [组织知识库(ai_knowledge_base_org_grid_view)](app/view/ai_knowledge_base_org_grid_view)
  * [个人知识库(ai_knowledge_base_person_grid_view)](app/view/ai_knowledge_base_person_grid_view)
  * [团队知识库(ai_knowledge_base_team_grid_view)](app/view/ai_knowledge_base_team_grid_view)

<script>
 const { createApp } = Vue
  createApp({
    data() {
      return {

      }
    }
  }).use(ElementPlus).mount('#app')
</script>