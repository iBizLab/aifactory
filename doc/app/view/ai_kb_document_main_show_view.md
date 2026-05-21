# 文档展示页(ai_kb_document_main_show_view)  <!-- {docsify-ignore-all} -->



## 控件
#### CAPTIONBAR(captionbar)
#### DATAINFOBAR(datainfobar)
#### 编辑表单(form)

##### 部件逻辑
* `onLoadSuccess`
```
const filestr = ctrl.state.data.file;
const parsed_content = ctrl.state.data.parsed_content;
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
    const name = ctrl.state.data.name;
    const file = {
        name:name+".md",
        content: parsed_content,
    };
    ctrl.state.data.file_preview = file;
}
```
#### 编辑表单(form1)

##### 部件逻辑
#### 列表(list)
#### 工具栏(toolbar)

## 视图界面逻辑
* `onLoadSuccess`
```javascript
ctrl.state.buttonsState.deuiaction1.selected = true
```


### 关联界面行为
  * [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document) : [清空评论（知识库）](module/ai/ai_kb_document#界面行为)
  * [评论(COMMENT)](module/Base/comment) : [刷新评论列表](module/Base/comment#界面行为)
  * [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document) : [重新索引](module/ai/ai_kb_document#界面行为)
  * [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document) : [研究](module/ai/ai_kb_document#界面行为)
  * [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document) : [AI+](module/ai/ai_kb_document#界面行为)
  * [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document) : [设置元数据](module/ai/ai_kb_document#界面行为)
  * [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document) : [关闭评论，打开基础信息](module/ai/ai_kb_document#界面行为)
  * [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document) : [关闭](module/ai/ai_kb_document#界面行为)
  * [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document) : [文档解析](module/ai/ai_kb_document#界面行为)
  * [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document) : [删除评论（知识库）](module/ai/ai_kb_document#界面行为)
  * [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document) : [编辑](module/ai/ai_kb_document#界面行为)
  * [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document) : [回复](module/ai/ai_kb_document#界面行为)
  * [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document) : [重新切片](module/ai/ai_kb_document#界面行为)
  * [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document) : [打开评论](module/ai/ai_kb_document#界面行为)
  * [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document) : [打开切片树表格](module/ai/ai_kb_document#界面行为)
  * [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document) : [打开知识库文档切片视图](module/ai/ai_kb_document#界面行为)
  * [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document) : [打开文档概览导航](module/ai/ai_kb_document#界面行为)
  * [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document) : [发送评论（知识库）](module/ai/ai_kb_document#界面行为)

### 关联界面逻辑
  * [评论(COMMENT)](module/Base/comment) : [控制评论按钮显示（知识库）](module/Base/comment/uilogic/comment_icon_show_wiki)
  * [评论(COMMENT)](module/Base/comment) : [控制评论按钮隐藏（知识库）](module/Base/comment/uilogic/comment_icon_hidden_wiki)

### 关联视图
  * [智能体选择器(ai_agent_assignment_selector)](app/view/ai_agent_assignment_selector)
  * [文档切片(ai_kb_chunk_list_view9)](app/view/ai_kb_chunk_list_view9)
  * [知识库文档分块(ai_kb_chunk_tree_grid_view)](app/view/ai_kb_chunk_tree_grid_view)
  * [文档切片设置(ai_kb_document_chunk_view)](app/view/ai_kb_document_chunk_view)
  * [文档概览导航(ai_kb_document_main_list_exp_view)](app/view/ai_kb_document_main_list_exp_view)
  * [文档元数据(ai_kb_document_meta_data_view)](app/view/ai_kb_document_meta_data_view)
  * [重新切片(ai_kb_document_rechunk_option_view)](app/view/ai_kb_document_rechunk_option_view)

<script>
 const { createApp } = Vue
  createApp({
    data() {
      return {

      }
    }
  }).use(ElementPlus).mount('#app')
</script>