# 智能体记忆任务实例(ai_agent_memory_task_grid_view)  <!-- {docsify-ignore-all} -->



## 控件
#### CAPTIONBAR(captionbar)
#### 数据表格(grid)
#### 搜索栏(searchbar)
#### 搜索表单(searchform)
#### 工具栏(toolbar)

## 视图界面逻辑
  * newdata(预置新建数据逻辑)
  * opendata(预置打开数据逻辑)


### 关联界面行为
  * [智能体记忆任务实例(AI_AGENT_MEMORY_TASK)](module/ai/ai_agent_memory_task) : [表格界面_删除操作](module/ai/ai_agent_memory_task#界面行为)
  * [智能体记忆任务实例(AI_AGENT_MEMORY_TASK)](module/ai/ai_agent_memory_task) : [记忆提取并存储](module/ai/ai_agent_memory_task#界面行为)

### 关联视图
  * [智能体记忆任务实例(ai_agent_memory_task_edit_view)](app/view/ai_agent_memory_task_edit_view)

<script>
 const { createApp } = Vue
  createApp({
    data() {
      return {

      }
    }
  }).use(ElementPlus).mount('#app')
</script>