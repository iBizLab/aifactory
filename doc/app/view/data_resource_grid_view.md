# 资源(data_resource_grid_view)  <!-- {docsify-ignore-all} -->



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
  * [数据资源(DATA_RESOURCE)](module/meta/data_resource) : [表格界面_新建操作](module/meta/data_resource#界面行为)

### 关联视图
  * [资源管理(data_resource_edit_view)](app/view/data_resource_edit_view)

<script>
 const { createApp } = Vue
  createApp({
    data() {
      return {

      }
    }
  }).use(ElementPlus).mount('#app')
</script>