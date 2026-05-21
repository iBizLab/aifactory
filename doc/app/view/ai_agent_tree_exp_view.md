# 智能体(ai_agent_tree_exp_view)  <!-- {docsify-ignore-all} -->



## 控件
#### CAPTIONBAR(captionbar)
#### 搜索栏(searchbar)
#### 树视图导航栏(treeexpbar)

## 视图界面逻辑
  * newdata(预置新建数据逻辑)
  * opendata(预置打开数据逻辑)


### 关联界面行为
  * [团队(GROUP)](module/Base/group) : [删除](module/Base/group#界面行为)
  * [企业用户(USER)](module/Base/user) : [编辑部门](module/Base/user#界面行为)
  * [团队(GROUP)](module/Base/group) : [删除](module/Base/group#界面行为)
  * [企业用户(USER)](module/Base/user) : [删除部门](module/Base/user#界面行为)
  * [类别(CATEGORY)](module/Base/category) : [删除](module/Base/category#界面行为)
  * [扩展执行计划(EXTEND_SCHEDULE)](module/Base/extend_schedule) : [表格界面_删除操作](module/Base/extend_schedule#界面行为)
  * [团队(GROUP)](module/Base/group) : [树界面_刷新全部操作](module/Base/group#界面行为)
  * [知识库(AI_KNOWLEDGE_BASE)](module/ai/ai_knowledge_base) : [新建目录](module/ai/ai_knowledge_base#界面行为)
  * [企业用户(USER)](module/Base/user) : [编辑组织](module/Base/user#界面行为)
  * [模型提供商(AI_MODEL_PROVIDER)](module/ai/ai_model_provider) : [打开模型提供商新建视图](module/ai/ai_model_provider#界面行为)
  * [类别(CATEGORY)](module/Base/category) : [删除](module/Base/category#界面行为)
  * [企业用户(USER)](module/Base/user) : [新建下级部门](module/Base/user#界面行为)
  * [企业用户(USER)](module/Base/user) : [编辑部门](module/Base/user#界面行为)
  * [团队(GROUP)](module/Base/group) : [新建团队（分组）](module/Base/group#界面行为)
  * [企业用户(USER)](module/Base/user) : [新建下级部门](module/Base/user#界面行为)
  * [团队(GROUP)](module/Base/group) : [删除](module/Base/group#界面行为)
  * [团队(GROUP)](module/Base/group) : [新建团队](module/Base/group#界面行为)
  * [类别(CATEGORY)](module/Base/category) : [知识库分类设置](module/Base/category#界面行为)
  * [团队(GROUP)](module/Base/group) : [编辑](module/Base/group#界面行为)
  * [扩展执行计划(EXTEND_SCHEDULE)](module/Base/extend_schedule) : [打开执行计划编辑视图](module/Base/extend_schedule#界面行为)
  * [企业用户(USER)](module/Base/user) : [新建下级部门](module/Base/user#界面行为)
  * [企业用户(USER)](module/Base/user) : [删除部门](module/Base/user#界面行为)
  * [团队(GROUP)](module/Base/group) : [新建分组](module/Base/group#界面行为)

### 关联视图
  * [智能体(ai_agent_context_grid_view)](app/view/ai_agent_context_grid_view)
  * [智能体会话(ai_agent_conversation_grid_view)](app/view/ai_agent_conversation_grid_view)
  * [智能体模板(ai_agent_grid_view)](app/view/ai_agent_grid_view)
  * [智能体记忆任务实例(ai_agent_memory_task_grid_view)](app/view/ai_agent_memory_task_grid_view)
  * [AI客户端凭证(ai_client_credential_grid_view)](app/view/ai_client_credential_grid_view)
  * [AI凭证(ai_credential_grid_view)](app/view/ai_credential_grid_view)
  * [知识库图谱实体类型(ai_kb_graph_entity_type_config_grid_view)](app/view/ai_kb_graph_entity_type_config_grid_view)
  * [标签集(ai_kb_tag_set_grid_view)](app/view/ai_kb_tag_set_grid_view)
  * [知识库(ai_knowledge_base_category_grid_view)](app/view/ai_knowledge_base_category_grid_view)
  * [知识库分类(ai_knowledge_base_category_tree_exp_view)](app/view/ai_knowledge_base_category_tree_exp_view)
  * [知识库(ai_knowledge_base_grid_view)](app/view/ai_knowledge_base_grid_view)
  * [知识库源(ai_knowledge_source_grid_view)](app/view/ai_knowledge_source_grid_view)
  * [添加提供商(ai_model_provider_quick_create_view)](app/view/ai_model_provider_quick_create_view)
  * [模型提供商(ai_model_provider_tree_exp_view)](app/view/ai_model_provider_tree_exp_view)
  * [模型提供商(ai_model_provider_tree_node_edit_view)](app/view/ai_model_provider_tree_node_edit_view)
  * [智能审查报告(ai_review_report_grid_view)](app/view/ai_review_report_grid_view)
  * [AI调用工具(ai_tool_grid_view)](app/view/ai_tool_grid_view)
  * [知识库分类设置(category_kb_setting)](app/view/category_kb_setting)
  * [系统配置信息(category_settings_sys_env)](app/view/category_settings_sys_env)
  * [资源(data_resource_grid_view)](app/view/data_resource_grid_view)
  * [执行计划(extend_schedule_edit_view)](app/view/extend_schedule_edit_view)
  * [扩展计划任务(extend_scheduled_task_edit_view)](app/view/extend_scheduled_task_edit_view)
  * [扩展计划任务(extend_scheduled_task_grid_view)](app/view/extend_scheduled_task_grid_view)
  * [计划任务作业(extend_scheduled_task_tab_exp_view)](app/view/extend_scheduled_task_tab_exp_view)
  * [计划任务(extend_scheduled_task_tree_exp_view)](app/view/extend_scheduled_task_tree_exp_view)
  * [扩展任务类型(extend_task_type_grid_view)](app/view/extend_task_type_grid_view)
  * [新建团队(group_quick_create_view)](app/view/group_quick_create_view)
  * [团队(group_tree_exp_view)](app/view/group_tree_exp_view)
  * [全部视图(insight_view_all_grid_view)](app/view/insight_view_all_grid_view)
  * [组织视图(insight_view_org_grid_view)](app/view/insight_view_org_grid_view)
  * [个人视图(insight_view_person_grid_view)](app/view/insight_view_person_grid_view)
  * [团队视图(insight_view_team_grid_view)](app/view/insight_view_team_grid_view)
  * [效能度量(insight_view_tree_exp_view)](app/view/insight_view_tree_exp_view)
  * [成员(member_grid_view)](app/view/member_grid_view)
  * [自定义安装(ps_core_prd_func_custom_install_view)](app/view/ps_core_prd_func_custom_install_view)
  * [已安装应用(ps_core_prd_func_installed_grid_view)](app/view/ps_core_prd_func_installed_grid_view)
  * [应用市场(ps_core_prd_func_market_application_view)](app/view/ps_core_prd_func_market_application_view)
  * [应用市场(ps_core_prd_func_tree_exp_view)](app/view/ps_core_prd_func_tree_exp_view)
  * [核心产品(ps_core_prd_market_application_view)](app/view/ps_core_prd_market_application_view)
  * [全部规则(psde_logic_global_flow_grid_view)](app/view/psde_logic_global_flow_grid_view)
  * [自动化(psde_logic_tab_exp_view)](app/view/psde_logic_tab_exp_view)
  * [自动化(psde_logic_tree_exp_view)](app/view/psde_logic_tree_exp_view)
  * [成员帐号(user_account_tab_exp_view)](app/view/user_account_tab_exp_view)
  * [成员(user_tab_exp_view)](app/view/user_tab_exp_view)
  * [成员管理(user_tree_exp_view)](app/view/user_tree_exp_view)
  * [成员管理(user_unassigned_dept_grid_view)](app/view/user_unassigned_dept_grid_view)

<script>
 const { createApp } = Vue
  createApp({
    data() {
      return {

      }
    }
  }).use(ElementPlus).mount('#app')
</script>