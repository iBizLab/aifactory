# 智能体管理(ai_agent_context_card_view)  <!-- {docsify-ignore-all} -->



## 控件
#### CAPTIONBAR(captionbar)
#### 数据视图(dataview)
#### 搜索栏(searchbar)
#### 搜索表单(searchform)
#### 工具栏(toolbar)

## 视图界面逻辑
  * newdata(预置新建数据逻辑)
  * opendata(预置打开数据逻辑)


### 关联界面行为
  * [智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context) : [智能创建](module/ai/ai_agent_context#界面行为)

### 关联视图
  * [创建智能体(ai_agent_context_ai_create_view)](app/view/ai_agent_context_ai_create_view)
  * [智能体(ai_agent_context_quick_create_view)](app/view/ai_agent_context_quick_create_view)
  * [智能体(ai_agent_context_view)](app/view/ai_agent_context_view)

<script>
 const { createApp } = Vue
  createApp({
    data() {
      return {

      }
    }
  }).use(ElementPlus).mount('#app')
</script>