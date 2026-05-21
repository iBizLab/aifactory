# 切片(ai_kb_chunk_chunk_info_view)  <!-- {docsify-ignore-all} -->


系统自动添加



## 控件
#### CAPTIONBAR(captionbar)
#### DATAINFOBAR(datainfobar)
#### 编辑表单(form)

##### 部件逻辑
* `onLoadSuccess`
```
const filestr = ctrl.state.data.doc_file;
const parsed_content = ctrl.state.data.doc_parsed_content;
if (filestr) {
    const arr = JSON.parse(filestr);
    const app = ibiz.hub.getApp(context.srfappid);
    const file = {
        id: arr[0].id,
        name: arr[0].name,
        cat:
        arr[0].folder ||
        ibiz.env.defaultOSSCat ||
        app.model.defaultOSSCat ||
        app.model.userParam?.DefaultOSSCat ||
        '',
    };
    ctrl.state.data.file_preview = file;
}else if(parsed_content){
    const name = ctrl.state.data.doc_name;
    const file = {
        name:name+".md",
        content: parsed_content,
    };
    ctrl.state.data.file_preview = file;
}
```
#### 工具栏(toolbar)


<script>
 const { createApp } = Vue
  createApp({
    data() {
      return {

      }
    }
  }).use(ElementPlus).mount('#app')
</script>