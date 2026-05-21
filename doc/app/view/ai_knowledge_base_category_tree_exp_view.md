# 知识库分类(ai_knowledge_base_category_tree_exp_view)  <!-- {docsify-ignore-all} -->



## 控件
#### CAPTIONBAR(captionbar)
#### 搜索栏(searchbar)
#### 树视图导航栏(treeexpbar)

## 视图界面逻辑
  * newdata(预置新建数据逻辑)
  * opendata(预置打开数据逻辑)


### 关联界面行为
  * [类别(CATEGORY)](module/Base/category) : [删除](module/Base/category#界面行为)
  * [类别(CATEGORY)](module/Base/category) : [删除](module/Base/category#界面行为)
  * [类别(CATEGORY)](module/Base/category) : [知识库分类设置](module/Base/category#界面行为)
  * [知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base) : [新建目录](module/ai/ai_knowledge_base#界面行为)

### 关联视图
  * [知识库(ai_knowledge_base_category_grid_view)](app/view/ai_knowledge_base_category_grid_view)
  * [知识库分类设置(category_kb_setting)](app/view/category_kb_setting)

<script>
 const { createApp } = Vue
  createApp({
    data() {
      return {

      }
    }
  }).use(ElementPlus).mount('#app')
</script>