# 全部规则(psde_logic_global_flow_grid_view)  <!-- {docsify-ignore-all} -->


系统自动添加



## 控件
#### CAPTIONBAR(captionbar)
#### 数据表格(grid)

##### 部件逻辑
#### 搜索栏(searchbar)
#### 搜索表单(searchform)
#### 工具栏(toolbar)

## 视图界面逻辑
  * newdata(预置新建数据逻辑)
  * opendata(预置打开数据逻辑)


### 关联界面行为
  * [实体处理逻辑(PSDELOGIC)](module/extension/PSDELogic) : [编辑界面_刷新操作](module/extension/PSDELogic#界面行为)
  * [实体处理逻辑(PSDELOGIC)](module/extension/PSDELogic) : [表格界面_删除操作](module/extension/PSDELogic#界面行为)
  * [实体处理逻辑(PSDELOGIC)](module/extension/PSDELogic) : [打开webhook调试视图](module/extension/PSDELogic#界面行为)
  * [实体处理逻辑(PSDELOGIC)](module/extension/PSDELogic) : [打开全部日志](module/extension/PSDELogic#界面行为)
  * [实体处理逻辑(PSDELOGIC)](module/extension/PSDELogic) : [打开配置视图](module/extension/PSDELogic#界面行为)
  * [实体处理逻辑(PSDELOGIC)](module/extension/PSDELogic) : [应用扩展模型](module/extension/PSDELogic#界面行为)
  * [扩展日志(EXTEND_LOG)](module/Base/extend_log) : [打开详情信息](module/Base/extend_log#界面行为)

### 关联视图
  * [日志信息(extend_log_info_view)](app/view/extend_log_info_view)
  * [全部日志(psde_logic_all_log_grid_view)](app/view/psde_logic_all_log_grid_view)
  * [实体处理逻辑(psde_logic_edit_view)](app/view/psde_logic_edit_view)
  * [自动化规则(psde_logic_flow_main_view)](app/view/psde_logic_flow_main_view)
  * [自动化规则看板(psde_logic_flow_panel_view)](app/view/psde_logic_flow_panel_view)
  * [自动化规则(psde_logic_quick_cfg_view)](app/view/psde_logic_quick_cfg_view)
  * [WebHook调试(psde_logic_web_hook_debug_view)](app/view/psde_logic_web_hook_debug_view)
  * [实体处理逻辑(psdelogiclogicdesign)](app/view/psdelogiclogicdesign)

<script>
 const { createApp } = Vue
  createApp({
    data() {
      return {

      }
    }
  }).use(ElementPlus).mount('#app')
</script>