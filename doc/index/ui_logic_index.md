# 界面逻辑 <!-- {docsify-ignore-all} -->



## [智能体分配(AI_AGENT_ASSIGNMENT)](module/ai/ai_agent_assignment.md) :id=ai_agent_assignment

|  中文名col200 | 代码名col200 | 备注col500 |
| --------|--------|------|
|[run分配智能体逻辑](module/ai/ai_agent_assignment/uilogic/run)|run||


## [智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context.md) :id=ai_agent_context

|  中文名col200 | 代码名col200 | 备注col500 |
| --------|--------|------|
|[prompt_feedback](module/ai/ai_agent_context/uilogic/prompt_feedback)|prompt_feedback||
|[run智能体逻辑](module/ai/ai_agent_context/uilogic/run)|run||
|[template_feedback](module/ai/ai_agent_context/uilogic/template_feedback)|template_feedback||
|[提示并打开审查报告](module/ai/ai_agent_context/uilogic/open_report)|open_report|打开提示弹窗并按照用户选择打开审查报告页面|







## [智能体会话(AI_AGENT_SESSION)](module/ai/ai_agent_session.md) :id=ai_agent_session

|  中文名col200 | 代码名col200 | 备注col500 |
| --------|--------|------|
|[accept_feedback](module/ai/ai_agent_session/uilogic/accept_feedback)|accept_feedback||
|[debug_context](module/ai/ai_agent_session/uilogic/debug_context)|debug_context||
|[dyna_context](module/ai/ai_agent_session/uilogic/dyna_context)|dyna_context||
|[jenkins_build](module/ai/ai_agent_session/uilogic/jenkins_build)|jenkins_build||
|[remark_feedback](module/ai/ai_agent_session/uilogic/remark_feedback)|remark_feedback||



## [AI客户端凭证(AI_CLIENT_CREDENTIAL)](module/ai/ai_client_credential.md) :id=ai_client_credential

|  中文名col200 | 代码名col200 | 备注col500 |
| --------|--------|------|
|[复制密钥](module/ai/ai_client_credential/uilogic/copy_access_key)|copy_access_key||



## [知识库文档分块(AI_KB_CHUNK)](module/ai/ai_kb_chunk.md) :id=ai_kb_chunk

|  中文名col200 | 代码名col200 | 备注col500 |
| --------|--------|------|
|[切换显示模式](module/ai/ai_kb_chunk/uilogic/switch_show_mode)|switch_show_mode|切换表格的显示模式|
|[打开所属文档](module/ai/ai_kb_chunk/uilogic/open_doc)|open_doc||



## [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document.md) :id=ai_kb_document

|  中文名col200 | 代码名col200 | 备注col500 |
| --------|--------|------|
|[显示基本信息](module/ai/ai_kb_document/uilogic/show_info)|show_info||
|[显示评论信息](module/ai/ai_kb_document/uilogic/show_comment)|show_comment||


## [知识库文档同步(AI_KB_DOCUMENT_SYNC)](module/ai/ai_kb_document_sync.md) :id=ai_kb_document_sync

|  中文名col200 | 代码名col200 | 备注col500 |
| --------|--------|------|
|[刷新文档同步表格](module/ai/ai_kb_document_sync/uilogic/refresh_doc_sync_grid)|refresh_doc_sync_grid||


## [知识库文档向导(AI_KB_DOCUMENT_WIZARD)](module/ai/ai_kb_document_wizard.md) :id=ai_kb_document_wizard

|  中文名col200 | 代码名col200 | 备注col500 |
| --------|--------|------|
|[通知刷新](module/ai/ai_kb_document_wizard/uilogic/notify_refresh)|notify_refresh||








## [知识库成员(AI_KB_MEMBER)](module/ai/ai_kb_member.md) :id=ai_kb_member

|  中文名col200 | 代码名col200 | 备注col500 |
| --------|--------|------|
|[新建知识库默认临时成员](module/ai/ai_kb_member/uilogic/create_default_temp_members)|create_default_temp_members|创建临时数据，并将当前用户加入到知识库临时成员内|






## [知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base.md) :id=ai_knowledge_base

|  中文名col200 | 代码名col200 | 备注col500 |
| --------|--------|------|
|[刷新当前表格](module/ai/ai_knowledge_base/uilogic/refresh_current_grid)|refresh_current_grid|刷新当前表格|
|[提示词填充](module/ai/ai_knowledge_base/uilogic/prompt_feedback)|prompt_feedback||
|[新建目录](module/ai/ai_knowledge_base/uilogic/create_category)|create_category|新建空间目录|
|[查找知识库首页模版](module/ai/ai_knowledge_base/uilogic/find_template)|find_template||
|[计算表格列行为状态(ai_knowledge_base)](module/ai/ai_knowledge_base/uilogic/calc_column_action_state)|calc_column_action_state|用于动态控制收藏和取消收藏的禁用状态|





## [智能审查报告(AI_REVIEW_REPORT)](module/ai/ai_review_report.md) :id=ai_review_report

|  中文名col200 | 代码名col200 | 备注col500 |
| --------|--------|------|
|[AI添加审查报告](module/ai/ai_review_report/uilogic/ai_add)|ai_add||



## [附件(ATTACHMENT)](module/Base/attachment.md) :id=attachment

|  中文名col200 | 代码名col200 | 备注col500 |
| --------|--------|------|
|[计算附件是否隐藏逻辑](module/Base/attachment/uilogic/calc_attachment_hidden)|calc_attachment_hidden|根据表格数据判断附件表格的显示或隐藏|
|[附件删除](module/Base/attachment/uilogic/remove_attachment)|remove_attachment|自动判断为表格或表单附件，按类别删除|
|[附件预览](module/Base/attachment/uilogic/attachment_preview)|attachment_preview||



## [类别(CATEGORY)](module/Base/category.md) :id=category

|  中文名col200 | 代码名col200 | 备注col500 |
| --------|--------|------|
|[删除类别或分组](module/Base/category/uilogic/remove_section_or_category)|remove_section_or_category|调用树节点删除方法，删除当前树节点数据|
|[新建子类别](module/Base/category/uilogic/create_children_category)|create_children_category|调用树节点新建方法，新建子模块|
|[编辑类别或分组](module/Base/category/uilogic/edit_section_or_category)|edit_section_or_category|调用树节点修改方法，编辑当前树节点的类别或分组|



## [评论(COMMENT)](module/Base/comment.md) :id=comment

|  中文名col200 | 代码名col200 | 备注col500 |
| --------|--------|------|
|[ai添加评论](module/Base/comment/uilogic/ai_comment)|ai_comment||
|[刷新评论列表](module/Base/comment/uilogic/refresh_comment_list)|refresh_comment_list|刷新|
|[发送评论(知识库)](module/Base/comment/uilogic/send_comment_wiki)|send_comment_wiki|发送评论，并关闭评论输入框，刷新评论列表|
|[回复评论（知识库）](module/Base/comment/uilogic/reply_comment_wiki)|reply_comment_wiki|获取回复对象评论信息，并展开评论输入框，显示回复组件|
|[控制评论按钮显示（知识库）](module/Base/comment/uilogic/comment_icon_show_wiki)|comment_icon_show_wiki|知识库评论按钮显示|
|[控制评论按钮隐藏（知识库）](module/Base/comment/uilogic/comment_icon_hidden_wiki)|comment_icon_hidden_wiki|知识库评论按钮隐藏|
|[清空评论（知识库）](module/Base/comment/uilogic/clear_comment_wiki)|clear_comment_wiki|清空知识库当前输入框评论|
|[编辑评论（知识库）](module/Base/comment/uilogic/edit_comment_wiki)|edit_comment_wiki|编辑评论，获取评论数据，展开评论输入框并赋值|








## [动态数据看板(DYNADASHBOARD)](module/Base/dyna_dashboard.md) :id=dyna_dashboard

|  中文名col200 | 代码名col200 | 备注col500 |
| --------|--------|------|
|[仪表盘操作列](module/Base/dyna_dashboard/uilogic/control_del)|control_del|仪表盘为最后一个时禁止删除|
|[使用此模板(禁止关闭)](module/Base/dyna_dashboard/uilogic/use_cur_template_no_closed)|use_cur_template_no_closed|使用此模板(禁止关闭)|
|[列表加载完成](module/Base/dyna_dashboard/uilogic/list_load_success)|list_load_success|列表加载完成|
|[获取选中模板名称](module/Base/dyna_dashboard/uilogic/fill_choosed_board_name)|fill_choosed_board_name|获取选中模板名称|
|[通知刷新](module/Base/dyna_dashboard/uilogic/notify_refresh)|notify_refresh||








## [团队(GROUP)](module/Base/group.md) :id=group

|  中文名col200 | 代码名col200 | 备注col500 |
| --------|--------|------|
|[删除类别或分组](module/Base/group/uilogic/remove_section_or_category)|remove_section_or_category|调用树节点删除方法，删除当前树节点数据|
|[新建分组](module/Base/group/uilogic/create_section)|create_section|团队页左侧树的新建分组逻辑|
|[编辑类别或分组](module/Base/group/uilogic/edit_section_or_category)|edit_section_or_category|调用树节点修改方法，编辑当前树节点的类别或分组|


## [效能成员(INSIGHT_MEMBER)](module/Insight/insight_member.md) :id=insight_member

|  中文名col200 | 代码名col200 | 备注col500 |
| --------|--------|------|
|[新建视图默认临时成员](module/Insight/insight_member/uilogic/create_default_temp_members)|create_default_temp_members|创建临时数据，并将当前用户加入到视图临时成员内|


## [效能报表(INSIGHT_REPORT)](module/Insight/insight_report.md) :id=insight_report

|  中文名col200 | 代码名col200 | 备注col500 |
| --------|--------|------|
|[使用此模板](module/Insight/insight_report/uilogic/use_cur_template)|use_cur_template|使用此模板|
|[导出为pdf](module/Insight/insight_report/uilogic/export_pdf)|export_pdf||
|[导出表格](module/Insight/insight_report/uilogic/export_excel)|export_excel||
|[新建分组](module/Insight/insight_report/uilogic/create_section)|create_section|新建效能度量报表分组|
|[新建类别](module/Insight/insight_report/uilogic/create_category)|create_category|调用树节点新建方法新建类别|


## [效能视图(INSIGHT_VIEW)](module/Insight/insight_view.md) :id=insight_view

|  中文名col200 | 代码名col200 | 备注col500 |
| --------|--------|------|
|[批量删除视图成员临时数据](module/Insight/insight_view/uilogic/remove_batch_temp)|remove_batch_temp|获取视图内所有临时成员数据并删除|
|[计算表格列行为状态(insight)](module/Insight/insight_view/uilogic/calc_column_action_state)|calc_column_action_state|用于动态控制收藏和取消收藏的禁用状态|
|[选择模板](module/Insight/insight_view/uilogic/choose_template)|choose_template|选择模板|
|[通知刷新](module/Insight/insight_view/uilogic/notify_refresh)|notify_refresh|通知页面刷新|




## [成员(MEMBER)](module/Base/member.md) :id=member

|  中文名col200 | 代码名col200 | 备注col500 |
| --------|--------|------|
|[添加页面共享成员](module/Base/member/uilogic/add_shared_member)|add_shared_member|添加页面共享成员：非空间下成员|


## [通知事件(NOTIFY_EVENT)](module/extension/notify_event.md) :id=notify_event

|  中文名col200 | 代码名col200 | 备注col500 |
| --------|--------|------|
|[保存列表多数据部件](module/extension/notify_event/uilogic/save_list_mdctrl)|save_list_mdctrl|保存列表多数据部件|




## [页面(PAGE)](module/Wiki/article_page.md) :id=article_page

|  中文名col200 | 代码名col200 | 备注col500 |
| --------|--------|------|
|[ai添加page](module/Wiki/article_page/uilogic/ai_add_page)|ai_add_page||
|[共享设置表单加载数据](module/Wiki/article_page/uilogic/shared_form_data)|shared_form_data|共享设置表单加载数据|
|[关闭模板中心](module/Wiki/article_page/uilogic/close_stencil)|close_stencil|关闭模板中心|
|[关闭评论区](module/Wiki/article_page/uilogic/close_comment)|close_comment|隐藏评论区，同时显示评论按钮|
|[切换导航树显示状态](module/Wiki/article_page/uilogic/change_tree_state)|change_tree_state|切换页面导航树显示状态|
|[删除页面](module/Wiki/article_page/uilogic/delete_page)|delete_page|调用树节点的删除方法，删除指定页面|
|[删除页面显示隐藏](module/Wiki/article_page/uilogic/deleted_visible)|deleted_visible|已删除页面显示隐藏|
|[后续刷新](module/Wiki/article_page/uilogic/refresh)|refresh|后续刷新页面共享视图|
|[复制共享链接](module/Wiki/article_page/uilogic/copy_shared_url)|copy_shared_url|复制共享页面链接|
|[恢复历史版本并通知刷新](module/Wiki/article_page/uilogic/page_refresh)|page_refresh|恢复到指定版本，并调用刷新方法|
|[新建分组](module/Wiki/article_page/uilogic/create_section)|create_section|调用树节点新建方法，新建分组|
|[新建发布并通知刷新](module/Wiki/article_page/uilogic/save_notify_refresh)|save_notify_refresh|保存当前页面内容并刷新页面，点击发布按钮，触发保存非草稿页面|
|[新建子分组](module/Wiki/article_page/uilogic/create_children_section)|create_children_section|调用树节点新建方法，新建子分组|
|[显示评论区](module/Wiki/article_page/uilogic/show_commnet)|show_commnet|打开评论区，同时隐藏评论按钮|
|[添加附件数据](module/Wiki/article_page/uilogic/add_attachment)|add_attachment|调用附件上传行为，添加附件数据|
|[编辑节点](module/Wiki/article_page/uilogic/edit_section_or_category)|edit_section_or_category|编辑树节点|


## [页面版本(PAGE_VERSION)](module/Wiki/page_version.md) :id=page_version

|  中文名col200 | 代码名col200 | 备注col500 |
| --------|--------|------|
|[查看已发布版本](module/Wiki/page_version/uilogic/is_published_version)|is_published_version|查看已发布的版本（页面）|




## [职位(POSITION)](module/Base/position.md) :id=position

|  中文名col200 | 代码名col200 | 备注col500 |
| --------|--------|------|
|[删除类别或分组](module/Base/position/uilogic/remove_section_or_category)|remove_section_or_category|调用树节点删除方法，删除当前树节点数据|
|[新建分组](module/Base/position/uilogic/create_category)|create_category|调用树节点新建方法新建分组|
|[新建职位](module/Base/position/uilogic/create_position)|create_position|调用树节点新建方法，新建职位|
|[编辑类别或分组](module/Base/position/uilogic/edit_section_or_category)|edit_section_or_category|调用树节点修改方法，编辑当前树节点的类别或分组|





## [核心产品功能(PSCOREPRDFUNC)](module/extension/PSCorePrdFunc.md) :id=PSCorePrdFunc

|  中文名col200 | 代码名col200 | 备注col500 |
| --------|--------|------|
|[clone此应用](module/extension/PSCorePrdFunc/uilogic/clone_git)|clone_git||
|[准备版本数据](module/extension/PSCorePrdFunc/uilogic/prepare_version_info)|prepare_version_info||
|[初始化插件信息](module/extension/PSCorePrdFunc/uilogic/init_plugin_info)|init_plugin_info|进入扩展设置时，从setting中获取插件标识和插件库|
|[更新插件设置](module/extension/PSCorePrdFunc/uilogic/update_plugin_setting)|update_plugin_setting|插件库更改后，更新setting字段|
|[自定义版本安装](module/extension/PSCorePrdFunc/uilogic/custom_version_info)|custom_version_info||
|[跳转gitlab](module/extension/PSCorePrdFunc/uilogic/skip_gitlab)|skip_gitlab||
|[跳转应用详情页面](module/extension/PSCorePrdFunc/uilogic/open_app_info)|open_app_info||
|[跳转设置页面](module/extension/PSCorePrdFunc/uilogic/skip_setting)|skip_setting||


## [实体处理逻辑(PSDELOGIC)](module/extension/PSDELogic.md) :id=PSDELogic

|  中文名col200 | 代码名col200 | 备注col500 |
| --------|--------|------|
|[webhook调试](module/extension/PSDELogic/uilogic/debug_webhook)|debug_webhook||












## [最近访问(RECENT)](module/Base/recent.md) :id=recent

|  中文名col200 | 代码名col200 | 备注col500 |
| --------|--------|------|
|[最近访问跳转其他视图](module/Base/recent/uilogic/recent_jump_other_view)|recent_jump_other_view|首页最近访问点击后跳转其他视图|





## [共享空间(SHARED_SPACE)](module/Wiki/shared_space.md) :id=shared_space

|  中文名col200 | 代码名col200 | 备注col500 |
| --------|--------|------|
|[后续刷新](module/Wiki/shared_space/uilogic/refresh)|refresh|后续刷新空间共享视图|
|[复制共享链接](module/Wiki/shared_space/uilogic/copy_shared_url)|copy_shared_url|复制共享空间链接|


## [空间(SPACE)](module/Wiki/space.md) :id=space

|  中文名col200 | 代码名col200 | 备注col500 |
| --------|--------|------|
|[刷新当前表格](module/Wiki/space/uilogic/refresh_current_grid)|refresh_current_grid|刷新当前表格|
|[批量删除空间成员临时数据](module/Wiki/space/uilogic/remove_batch_temp)|remove_batch_temp|获取空间内所有临时成员数据并删除|
|[新建目录](module/Wiki/space/uilogic/create_category)|create_category|新建空间目录|
|[计算表格列行为状态(space)](module/Wiki/space/uilogic/calc_column_action_state)|calc_column_action_state|用于动态控制收藏和取消收藏的禁用状态|


## [空间成员(SPACE_MEMBER)](module/Wiki/space_member.md) :id=space_member

|  中文名col200 | 代码名col200 | 备注col500 |
| --------|--------|------|
|[新建空间默认临时成员](module/Wiki/space_member/uilogic/create_default_temp_members)|create_default_temp_members|创建临时数据，并将当前用户加入到空间临时成员内|


## [页面模板(STENCIL)](module/Wiki/stencil.md) :id=stencil

|  中文名col200 | 代码名col200 | 备注col500 |
| --------|--------|------|
|[发布](module/Wiki/stencil/uilogic/release)|release||
|[打开新建页面并关闭模板中心](module/Wiki/stencil/uilogic/open_new_page)|open_new_page|打开新建页并关闭模板中心|









## [企业用户(USER)](module/Base/user.md) :id=user

|  中文名col200 | 代码名col200 | 备注col500 |
| --------|--------|------|
|[修改密码（表单）](module/Base/user/uilogic/change_pas)|change_pas|修改密码|
|[删除部门](module/Base/user/uilogic/trash_dept)|trash_dept||
|[新建下级根部门](module/Base/user/uilogic/new_root_dept)|new_root_dept||
|[新建下级部门](module/Base/user/uilogic/new_dept)|new_dept||
|[编辑组织](module/Base/user/uilogic/edit_org)|edit_org||
|[编辑部门](module/Base/user/uilogic/edit_dept)|edit_dept||


