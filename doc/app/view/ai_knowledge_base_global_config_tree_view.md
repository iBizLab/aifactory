# 配置中心(ai_knowledge_base_global_config_tree_view)  <!-- {docsify-ignore-all} -->



## 控件
#### CAPTIONBAR(captionbar)
#### 搜索栏(searchbar)
#### 树视图导航栏(treeexpbar)

## 视图界面逻辑
  * newdata(预置新建数据逻辑)
  * opendata(预置打开数据逻辑)


### 关联视图
  * [知识库图谱实体类型(ai_kb_graph_entity_type_config_grid_view)](app/view/ai_kb_graph_entity_type_config_grid_view)
  * [标签集(ai_kb_tag_set_grid_view)](app/view/ai_kb_tag_set_grid_view)
  * [知识库分类(ai_knowledge_base_category_tree_exp_view)](app/view/ai_knowledge_base_category_tree_exp_view)
  * [知识库源(ai_knowledge_source_grid_view)](app/view/ai_knowledge_source_grid_view)
  * [资源(data_resource_grid_view)](app/view/data_resource_grid_view)

<script>
 const { createApp } = Vue
  createApp({
    data() {
      return {

      }
    }
  }).use(ElementPlus).mount('#app')
</script>