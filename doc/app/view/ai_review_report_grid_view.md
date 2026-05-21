# 智能审查报告(ai_review_report_grid_view)  <!-- {docsify-ignore-all} -->



## 控件
#### CAPTIONBAR(captionbar)
#### 数据表格(grid)
#### 搜索栏(searchbar)
#### 搜索表单(searchform)

## 视图界面逻辑
  * newdata(预置新建数据逻辑)
  * opendata(预置打开数据逻辑)


### 关联界面行为
  * [智能审查报告(AI_REVIEW_REPORT)](module/ai/ai_review_report) : [表格界面_删除操作](module/ai/ai_review_report#界面行为)

### 关联视图
  * [智能审查报告(ai_review_report_main_view)](app/view/ai_review_report_main_view)

<script>
 const { createApp } = Vue
  createApp({
    data() {
      return {

      }
    }
  }).use(ElementPlus).mount('#app')
</script>