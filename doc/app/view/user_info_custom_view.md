# 用户信息自定义视图(user_info_custom_view)  <!-- {docsify-ignore-all} -->



## 控件
#### CAPTIONBAR(captionbar)


### 关联界面行为
  * [企业用户(USER)](module/Base/user) : [主题设置](module/Base/user#界面行为)
  * [企业用户(USER)](module/Base/user) : [帐号设置](module/Base/user#界面行为)
  * [企业用户(USER)](module/Base/user) : [应用登出](module/Base/user#界面行为)

### 关联视图
  * [帐号设置(user_setting_view)](app/view/user_setting_view)

<script>
 const { createApp } = Vue
  createApp({
    data() {
      return {

      }
    }
  }).use(ElementPlus).mount('#app')
</script>