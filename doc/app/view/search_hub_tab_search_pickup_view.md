# 高级搜索(search_hub_tab_search_pickup_view)  <!-- {docsify-ignore-all} -->


系统自动添加



## 控件
#### CAPTIONBAR(captionbar)
#### 搜索栏(searchbar)
#### 分页导航面板(tabexppanel)

## 视图界面逻辑
* `onSelectionChange`
```javascript
console.log("");
view.evt.emit('onSelectionChange', { data });
```
* `onMounted`
```javascript
const searchBar = view.getController('searchbar');
if (searchBar) {
searchBar.state.query = view.params.srfquery ? view.params.srfquery : '';
}
```
* `onCreated`
```javascript
view.ctx.evt.on('onRegister', (name, c) => {
    if(name==='tabexppanel'){
        c.state.expViewParams={query: viewParam.srfquery}
    }
});
```


### 关联视图
  * [文档(ai_kb_document_advanced_search_grid_pickview)](app/view/ai_kb_document_advanced_search_grid_pickview)
  * [页面(article_page_advanced_search_grid_pickview)](app/view/article_page_advanced_search_grid_pickview)

<script>
 const { createApp } = Vue
  createApp({
    data() {
      return {

      }
    }
  }).use(ElementPlus).mount('#app')
</script>