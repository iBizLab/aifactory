# 模型提供商(ai_model_provider_tree_exp_view)  <!-- {docsify-ignore-all} -->



## 控件
#### CAPTIONBAR(captionbar)
#### 搜索栏(searchbar)
#### 树视图导航栏(treeexpbar)

## 视图界面逻辑
  * newdata(预置新建数据逻辑)
  * opendata(预置打开数据逻辑)


### 关联界面行为
  * [模型提供商(AI_MODEL_PROVIDER)](module/ai/ai_model_provider) : [打开模型提供商新建视图](module/ai/ai_model_provider#界面行为)

### 关联视图
  * [添加提供商(ai_model_provider_quick_create_view)](app/view/ai_model_provider_quick_create_view)
  * [模型提供商(ai_model_provider_tree_node_edit_view)](app/view/ai_model_provider_tree_node_edit_view)

<script>
 const { createApp } = Vue
  createApp({
    data() {
      return {

      }
    }
  }).use(ElementPlus).mount('#app')
</script>