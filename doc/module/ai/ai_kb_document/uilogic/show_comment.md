## 显示评论信息 <!-- {docsify-ignore-all} -->

   

### 处理过程

```plantuml
@startuml
hide footbox
<style>
root {
  HyperlinkColor #42b983
}
</style>

hide empty description
state "开始" as Begin <<start>> [[$./show_comment#begin {开始}]]
state "调试逻辑参数#####" as DEBUGPARAM_01  [[$./show_comment#debugparam_01 {调试逻辑参数#####}]]
state "设置视图参数" as PREPAREJSPARAM_01  [[$./show_comment#preparejsparam_01 {设置视图参数}]]
state "结束" as END1 <<end>> [[$./show_comment#end1 {结束}]]
state "设置工具栏项、评论列表显隐" as PREPAREJSPARAM2  [[$./show_comment#preparejsparam2 {设置工具栏项、评论列表显隐}]]
state "准备界面元素" as PREPAREJSPARAM1  [[$./show_comment#preparejsparam1 {准备界面元素}]]


Begin --> PREPAREJSPARAM1
PREPAREJSPARAM1 --> PREPAREJSPARAM2
PREPAREJSPARAM2 --> PREPAREJSPARAM_01
PREPAREJSPARAM_01 --> DEBUGPARAM_01
DEBUGPARAM_01 --> END1


@enduml
```


### 处理步骤说明

#### 准备界面元素 :id=PREPAREJSPARAM1<sup class="footnote-symbol"> <font color=gray size=1>[准备参数]</font></sup>



1. 将`view.layoutPanel.panelItems.right_container.state` 设置给  `right_grouppanel_state(容器状态)`
2. 将`view.layoutPanel.panelItems.comment.state` 设置给  `comment_state(容器状态)`
3. 将`view.layoutPanel.panelItems.info.state` 设置给  `info_state(容器状态)`
4. 将`toolbar(工具栏).state.buttonsState.deuiaction4` 设置给  `button4_state_obj(关闭按钮状态)`
5. 将`toolbar(工具栏).state.buttonsState.deuiaction2` 设置给  `button2_state_obj(评论按钮状态)`
6. 将`toolbar(工具栏).state.buttonsState.deuiaction1` 设置给  `button1_state_obj(基本信息按钮状态)`

#### 设置工具栏项、评论列表显隐 :id=PREPAREJSPARAM2<sup class="footnote-symbol"> <font color=gray size=1>[准备参数]</font></sup>



1. 将`true` 设置给  `right_grouppanel_state(容器状态).visible`
2. 将`true` 设置给  `comment_state(容器状态).visible`
3. 将`false` 设置给  `info_state(容器状态).visible`
4. 将`false` 设置给  `button2_state_obj(评论按钮状态).visible`
5. 将`true` 设置给  `button1_state_obj(基本信息按钮状态).visible`

#### 设置视图参数 :id=PREPAREJSPARAM_01<sup class="footnote-symbol"> <font color=gray size=1>[准备参数]</font></sup>



1. 将`true` 设置给  `view.comment_list_isshow`

#### 调试逻辑参数##### :id=DEBUGPARAM_01<sup class="footnote-symbol"> <font color=gray size=1>[调试逻辑参数]</font></sup>



> [!NOTE|label:调试信息|icon:fa fa-bug]
> 调试输出参数`view`的详细信息

#### 开始 :id=Begin<sup class="footnote-symbol"> <font color=gray size=1>[开始]</font></sup>




#### 结束 :id=END1<sup class="footnote-symbol"> <font color=gray size=1>[结束]</font></sup>






### 实体逻辑参数

|    中文名   |    代码名    |  数据类型      |备注 |
| --------| --------| --------  | --------   |
|关闭按钮状态|button3_state_obj|数据对象||
|view|view|当前视图对象||
|form|form|部件对象||
|基本信息按钮状态|button1_state_obj|数据对象||
|容器状态|right_grouppanel_state|数据对象||
|工具栏|toolbar|部件对象||
|关闭按钮状态|button4_state_obj|数据对象||
|容器状态|info_state|数据对象||
|传入变量(<i class="fa fa-check"/></i>)|Default|数据对象||
|评论按钮状态|button2_state_obj|数据对象||
|容器状态|comment_state|数据对象||
