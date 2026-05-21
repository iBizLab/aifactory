# 评论(comment)  <!-- {docsify-ignore-all} -->


用于存储用户在需求、工单、工作项、页面、等内容上发布的评论。


## 属性
|    中文名col150 | 属性名称col200           | 类型col200     | 长度col100    |允许为空col100    |  备注col500  |
| --------   |------------| -----  | -----  | :----: | -------- |
|内容|CONTENT|长文本，没有长度限制|1048576|是||
|建立人|CREATE_MAN|文本，可指定长度|100|否||
|建立时间|CREATE_TIME|日期时间型||否||
|内容格式|FORMAT_TYPE|文本，可指定长度|100|是||
|标识<sup class="footnote-symbol"><font color=orange>[PK]</font></sup>|ID|全局唯一标识，文本类型，用户不可见|100|否||
|是否置顶|IS_TOP|是否逻辑||是||
|名称|NAME|文本，可指定长度|200|是||
|所属数据对象|OWNER_TYPE|文本，可指定长度|100|是||
|父内容|PCONTENT|外键值附加数据|1048576|是||
|父建立人|PCREATE_MAN|外键值附加数据|100|是||
|父标识|PID|外键值|100|是||
|评论主体标识|PRINCIPAL_ID|文本，可指定长度|100|是||
|评论主体名称|PRINCIPAL_NAME|文本，可指定长度|100|是||
|评论主体类型|PRINCIPAL_TYPE|[文本，可指定长度](index/dictionary_index#principal_type "评论主体类型")|100|是||
|更新人|UPDATE_MAN|文本，可指定长度|100|否||
|更新时间|UPDATE_TIME|日期时间型||否||


## 关系

<el-row>
<el-tabs v-model="show_der">
<el-tab-pane label="主关系" name="major">

| 名称col350     |   从实体col200 | 关系类型col200     |   备注col500  |
| -------- |---------- |------------|----- |
|[DER1N_COMMENT_COMMENT_PID](der/DER1N_COMMENT_COMMENT_PID)|[评论(COMMENT)](module/Base/comment)|1:N关系||


</el-tab-pane>
<el-tab-pane label="从关系" name="minor">

|  名称col350   | 主实体col200   | 关系类型col200   |    备注col500  |
| -------- |---------- |-----------|----- |
|[DER1N_COMMENT_COMMENT_PID](der/DER1N_COMMENT_COMMENT_PID)|[评论(COMMENT)](module/Base/comment)|1:N关系||
|[DERCUSTOM_COMMENT_AI_KB_DOCUMENT](der/DERCUSTOM_COMMENT_AI_KB_DOCUMENT)|[知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document)|自定义关系||
|[DERCUSTOM_COMMENT_PAGE](der/DERCUSTOM_COMMENT_PAGE)|[页面(PAGE)](module/Wiki/article_page)|自定义关系||

</el-tab-pane>
</el-tabs>
</el-row>

## 行为
| 中文名col200    | 代码名col150    | 类型col150    | 事务col100   | 批处理col100   | 附加操作col100  | 插件col150    |  备注col300  |
| -------- |---------- |----------- |:----:|:----:|---------| ----- | ----- |
|CheckKey|CheckKey|内置方法|默认|不支持||||
|Create|Create|内置方法|默认|不支持||||
|Get|Get|内置方法|默认|不支持||||
|GetDraft|GetDraft|内置方法|默认|不支持||||
|Remove|Remove|内置方法|默认|支持||||
|Save|Save|内置方法|默认|不支持||||
|Update|Update|内置方法|默认|不支持||||
|删除评论|delete|[实体处理逻辑](module/Base/comment/logic/delete "删除评论")|默认|不支持||||
|取消置顶|no_top|[实体处理逻辑](module/Base/comment/logic/no_top "取消置顶")|默认|不支持||||
|评论置顶|top|[实体处理逻辑](module/Base/comment/logic/top "评论置顶")|默认|不支持||||

## 处理逻辑
| 中文名col200    | 代码名col150    | 子类型col150    | 插件col200    |  备注col550  |
| -------- |---------- |----------- |------------|----------|
|[删除评论](module/Base/comment/logic/delete)|delete|无||评论数据的删除，将评论内容重置为：该评论已删除|
|[取消置顶](module/Base/comment/logic/no_top)|no_top|无|||
|[评论置顶](module/Base/comment/logic/top)|top|无|||

## 数据查询
| 中文名col200    | 代码名col150    | 默认查询col100 | 权限使用col100 | 自定义SQLcol100 |  备注col600|
| --------  | --------   | :----:  |:----:  | :----:  |----- |
|[数据查询(DEFAULT)](module/Base/comment/query/Default)|DEFAULT|是|否 |否 ||

## 数据集合
| 中文名col200  | 代码名col150  | 类型col100 | 默认集合col100 |   插件col200|   备注col500|
| --------  | --------   | :----:   | :----:   | ----- |----- |
|[数据集(DEFAULT)](module/Base/comment/dataset/Default)|DEFAULT|数据查询|是|||

## 数据权限

##### 全部数据（读写） :id=comment-ALL_RW

<p class="panel-title"><b>数据范围</b></p>

* `全部数据`

<p class="panel-title"><b>数据能力</b></p>

* `CREATE(知识库文档(CREATE))`
* `READ`
* `DELETE`
* `UPDATE`




## 搜索模式
|   搜索表达式col350   |    属性名col200    |    搜索模式col200        |备注col500  |
| -------- |------------|------------|------|
|N_CREATE_MAN_EQ|建立人|EQ||
|N_CREATE_TIME_EQ|建立时间|EQ||
|N_CREATE_TIME_GTANDEQ|建立时间|GTANDEQ||
|N_CREATE_TIME_LTANDEQ|建立时间|LTANDEQ||
|N_ID_EQ|标识|EQ||
|N_NAME_LIKE|名称|LIKE||
|N_OWNER_TYPE_EQ|所属数据对象|EQ||
|N_PID_EQ|父标识|EQ||
|N_PRINCIPAL_ID_EQ|评论主体标识|EQ||

## 界面行为
|  中文名col200 |  代码名col150 |  标题col100   |     处理目标col100   |    处理类型col200        |  备注col500       |
| --------| --------| -------- |------------|------------|------------|
| AI评论 | ai_comment | AI评论 |单项数据|用户自定义||
| 编辑 | panel_usr0228764297_button_calluilogic1_click | 编辑 |单项数据|用户自定义||
| 发送评论（知识库） | send_comment_wiki | 发送评论 |无数据|用户自定义||
| 清空评论（知识库） | clear_comment_wiki | 清空 |无数据|用户自定义||
| 删除评论（知识库） | delete_comment_space | 删除评论 |单项数据（主键）|<details><summary>后台调用</summary>[delete](#行为)||
| 回复 | panel_usr0228764297_button_calluilogic2_click | 回复 |单项数据|用户自定义||
| 刷新评论列表 | refresh_comment_list | 刷新评论列表 |无数据|用户自定义||

## 界面逻辑
|  中文名col200 | 代码名col150 | 备注col900 |
| --------|--------|--------|
|[ai添加评论](module/Base/comment/uilogic/ai_comment)|ai_comment||
|[刷新评论列表](module/Base/comment/uilogic/refresh_comment_list)|refresh_comment_list|刷新|
|[发送评论(知识库)](module/Base/comment/uilogic/send_comment_wiki)|send_comment_wiki|发送评论，并关闭评论输入框，刷新评论列表|
|[回复评论（知识库）](module/Base/comment/uilogic/reply_comment_wiki)|reply_comment_wiki|获取回复对象评论信息，并展开评论输入框，显示回复组件|
|[控制评论按钮显示（知识库）](module/Base/comment/uilogic/comment_icon_show_wiki)|comment_icon_show_wiki|知识库评论按钮显示|
|[控制评论按钮隐藏（知识库）](module/Base/comment/uilogic/comment_icon_hidden_wiki)|comment_icon_hidden_wiki|知识库评论按钮隐藏|
|[清空评论（知识库）](module/Base/comment/uilogic/clear_comment_wiki)|clear_comment_wiki|清空知识库当前输入框评论|
|[编辑评论（知识库）](module/Base/comment/uilogic/edit_comment_wiki)|edit_comment_wiki|编辑评论，获取评论数据，展开评论输入框并赋值|

<div style="display: block; overflow: hidden; position: fixed; top: 140px; right: 100px;">

##### 导航
<el-anchor >
<el-anchor-link :href="`#/module/Base/comment?id=属性`">
  属性
</el-anchor-link>
<el-anchor-link :href="`#/module/Base/comment?id=关系`">
  关系
</el-anchor-link>
<el-anchor-link :href="`#/module/Base/comment?id=行为`">
  行为
</el-anchor-link>
<el-anchor-link :href="`#/module/Base/comment?id=处理逻辑`">
  处理逻辑
</el-anchor-link>
<el-anchor-link :href="`#/module/Base/comment?id=数据查询`">
  数据查询
</el-anchor-link>
<el-anchor-link :href="`#/module/Base/comment?id=数据集合`">
  数据集合
</el-anchor-link>
<el-anchor-link :href="`#/module/Base/comment?id=数据权限`">
  数据权限
</el-anchor-link>
<el-anchor-link :href="`#/module/Base/comment?id=搜索模式`">
  搜索模式
</el-anchor-link>
<el-anchor-link :href="`#/module/Base/comment?id=界面行为`">
  界面行为
</el-anchor-link>
<el-anchor-link :href="`#/module/Base/comment?id=界面逻辑`">
  界面逻辑
</el-anchor-link>
</el-anchor>
</div>

<script>
 const { createApp } = Vue
  createApp({
    data() {
      return {
show_der:'major',


      }
    },
    methods: {
    }
  }).use(ElementPlus).mount('#app')
</script>