# 绑定智能体(ai_agent_context_bind_view)  <!-- {docsify-ignore-all} -->



## 控件
#### CAPTIONBAR(captionbar)
#### 数据表格(grid)
#### 搜索栏(searchbar)
#### 搜索表单(searchform)
#### 工具栏(toolbar)

## 视图界面逻辑
* `onCloseView`
```javascript
ibiz.mc.command.create.send({ srfdecodename: 'ai_agent_assignment'});
```
  * newdata(预置新建数据逻辑)
  * opendata(预置打开数据逻辑)


### 关联界面行为
  * [智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context) : [绑定智能体](module/ai/ai_agent_context#界面行为)

### 关联视图
  * [智能体(ai_agent_context_edit_view)](app/view/ai_agent_context_edit_view)
  * [智能体上下文(ai_agent_context_main_view)](app/view/ai_agent_context_main_view)

<script>
 const { createApp } = Vue
  createApp({
    data() {
      return {

      }
    }
  }).use(ElementPlus).mount('#app')
</script>