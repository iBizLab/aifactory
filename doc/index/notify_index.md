# 消息通知 <!-- {docsify-ignore-all} -->


## 实体消息通知

|    实体col200|    通知名称col200          |  消息模板col300   |  使用场景col250    |  备注col300  |
| --------|------------ |   -------- | -------- | -------- |

## 通知目标

|    中文名col200   | 代码名col200       |  目标类型col150  | 数据集合col200   |  备注col500  |
| --------|------------| -----   |  -------- | -------- |
|当前空间成员|cur_space_member|实体数据集|[当前空间下成员(cur_space)](module/Wiki/space_member/dataset/cur_space)||

## 消息模板

#### 知识库通知模板(加入空间成员)(space_member_create) :id=space_member_create


模板类型：`静态`

模板引擎：`FreeMarker`

内容类型：`HTML网页`

超链接：`route://-/index/space=${data.space_id}/space_index_view/srfnav=drgroup/article_page_tree_exp_view/srfnavctx=%257B%2522srfdefaulttoroutedepth%2522%253A3%257D;srfnav=root:node@${data.space_id}/article_page_show_view/srfnavctx={"article_page":"${data.space_id}"}`

移动端超链接：`route://-/home/space=${data.space_id}/article_page_mob_list_view/srfnavctx=%257B%2522srfnavctrlid%2522%253A%2522plmmob.space_mob_list_view%2540plmmob.space.mob_list_view_mob_list%2522%252C%2522srfnavlogicid%2522%253A%252292b6112f-e53d-26c2-af0b-fc617ca4fe82%253A8eb5d724-4d71-6e1c-8b2f-63eb866708e9%2522%257D`

内容：
```
<div class="notice-card" style="display: flex; align-items: flex-start;">
    <div class="notice-card__avatar" style="flex-shrink: 0;">
        <span class="notice-card__avatar-icon" style="background-color: skyblue; border-radius: 50%; margin-right: 10px; width: 36px; height: 36px; display: flex; justify-content: center; align-items: center; font-size: 10px;">${data.create_mantext!?right_pad(2)?substring(0,2)?trim}</span>
    </div>
    <div class="notice-card__content" style="flex-grow: 1;width: calc(100% - 46px);">
        <div class="notice-card__event">
            <div class="notice-card__event-title" style="font-size: 14px; color: #000;">
                <span class="notice-card__event-name" style="color: #999; font-size: 14px; text-transform: lowercase; display: inline-block; max-width: 100%; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">${data.create_mantext}</span> 
                <span class="notice-card__event-desc" style="font-size: 14px; text-transform: lowercase; display: inline-block; max-width: 100%; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">把你加入了空间</span>
            </div>
        </div>
        <div class="notice-card-object" style="display: inline-block; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; width: 100%;">
            <span class="notice-card__object-name" title="${data.space_name}">${data.space_name}</span>
        </div>
        <div class="notice-card-pilot" style="font-size: 12px; color: #999; text-transform: lowercase; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
            <span class="notice-pilot-time">${data.create_time?string("yyyy-MM-dd HH:mm:ss")}</span>
            <span class="notice-pilot-info"> · 知识管理 · ${data.space_name}</span>
        </div>
    </div>
</div>
```

钉钉内容：
```
${data.create_mantext}把你加入了空间：${data.space_name}
```

微信消息内容：
```
${data.create_mantext}把你加入了空间：${data.space_name}
```
#### 评审通知模板(页面)(page_review_inform_template) :id=page_review_inform_template


模板类型：`静态`

模板引擎：`FreeMarker`

内容类型：`HTML网页`

超链接：`view://review_page_main_view?srfnavctx={"review":"${data.id}","space":"${data.principal_id}","product": null,"project": null,"library": null}`

内容：
```
<div class="notice-card" style="display: flex; align-items: flex-start;">
    <div class="notice-card__avatar" style="flex-shrink: 0;">
        <span class="notice-card__avatar-icon" style="background-color: skyblue; border-radius: 50%; margin-right: 10px; width: 36px; height: 36px; display: flex; justify-content: center; align-items: center; font-size: 10px;">${data.reviewertext!?right_pad(2)?substring(0,2)?trim}</span>
    </div>
    <div class="notice-card__content" style="flex-grow: 1;width: calc(100% - 46px);">
        <div class="notice-card__event">
            <div class="notice-card__event-title" style="font-size: 14px; color: #000;">
                <span class="notice-card__event-name" style="color: #999; font-size: 14px; text-transform: lowercase; display: inline-block; max-width: 100%; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">${data.reviewertext}</span> 
                <span class="notice-card__event-desc" style="font-size: 14px; text-transform: lowercase; display: inline-block; max-width: 100%; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">给你分配了页面评审</span>
            </div>
        </div>
        <div class="notice-card-object" style="display: inline-block; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; width: 100%;">
            <#if data.identifier??>
                <span class="notice-card__object-id" style="color: #999; font-size:14px;">${data.identifier}</span>
            </#if>
            <span class="notice-card__object-name" title="${data.name}">${data.name}</span>
        </div>
        <div class="notice-card-pilot" style="font-size: 12px; color: #999; text-transform: lowercase; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
            <span class="notice-pilot-time">${.now?string("yyyy-MM-dd HH:mm:ss")}</span>
            <span class="notice-pilot-info"> · 知识管理 · ${data.principal_name}</span>
        </div>
    </div>
</div>
```
#### 空间通知模板(归档/激活空间)(space_archived_or_activate) :id=space_archived_or_activate


模板类型：`静态`

模板引擎：`FreeMarker`

内容类型：`HTML网页`

超链接：`<#if data.is_archived==0>route://-/index/space=${data.id}/space_index_view/srfnav=drgroup/article_page_tree_exp_view/srfnavctx=%257B%2522srfdefaulttoroutedepth%2522%253A3%257D;srfnav=root:node@${data.id}/article_page_show_view/srfnavctx={"article_page":"${data.id}"}</#if>`

移动端超链接：`<#if data.is_archived==0>
route://-/home/space=${data.id}/article_page_mob_list_view/srfnavctx=%257B%2522srfnavctrlid%2522%253A%2522plmmob.space_mob_list_view%2540plmmob.space.mob_list_view_mob_list%2522%252C%2522srfnavlogicid%2522%253A%252292b6112f-e53d-26c2-af0b-fc617ca4fe82%253A8eb5d724-4d71-6e1c-8b2f-63eb866708e9%2522%257D
</#if>`

内容：
```
<div class="notice-card" style="display: flex; align-items: flex-start;">
    <div class="notice-card__avatar" style="flex-shrink: 0;">
        <span class="notice-card__avatar-icon" style="background-color: skyblue; border-radius: 50%; margin-right: 10px; width: 36px; height: 36px; display: flex; justify-content: center; align-items: center; font-size: 10px;">${data.update_mantext!?right_pad(2)?substring(0,2)?trim}</span>
    </div>
    <div class="notice-card__content" style="flex-grow: 1;width: calc(100% - 46px);">
        <div class="notice-card__event">
            <div class="notice-card__event-title" style="font-size: 14px; color: #000;">
                <span class="notice-card__event-name" style="color: #999; font-size: 14px; text-transform: lowercase; display: inline-block; max-width: 100%; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">${data.update_mantext}</span> 
                <span class="notice-card__event-desc" style="font-size: 14px; text-transform: lowercase; display: inline-block; max-width: 100%; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;"><#if data.is_archived==1>归档<#else>激活</#if>了空间</span>
            </div>
        </div>
        <div class="notice-card-object" style="display: inline-block; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; width: 100%;">
            <#if data.identifier??>
                <span class="notice-card__object-id" style="color: #999; font-size:14px;">${data.identifier}</span>
            </#if>
            <span class="notice-card__object-name" title="${data.name}">${data.name}</span>
        </div>
        <div class="notice-card-pilot" style="font-size: 12px; color: #999; text-transform: lowercase; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
            <span class="notice-pilot-time">${data.update_time?string("yyyy-MM-dd HH:mm:ss")}</span>
            <span class="notice-pilot-info"> · 知识管理 · ${data.name}</span>
        </div>
    </div>
</div>
```

钉钉内容：
```
${data.update_mantext}<#if data.is_archived==1>归档<#else>激活</#if>了空间：${data.name}
```

微信消息内容：
```
${data.update_mantext}<#if data.is_archived==1>归档<#else>激活</#if>了空间：${data.name}
```
#### 空间通知模板(删除/恢复空间)(space_remove_or_recover) :id=space_remove_or_recover


模板类型：`静态`

模板引擎：`FreeMarker`

内容类型：`HTML网页`

超链接：`<#if data.is_deleted==0>route://-/index/space=${data.id}/space_index_view/srfnav=drgroup/article_page_tree_exp_view/srfnavctx=%257B%2522srfdefaulttoroutedepth%2522%253A3%257D;srfnav=root:node@${data.id}/article_page_show_view/srfnavctx={"article_page":"${data.id}"}</#if>`

移动端超链接：`<#if data.is_deleted==0>
route://-/home/space=${data.id}/article_page_mob_list_view/srfnavctx=%257B%2522srfnavctrlid%2522%253A%2522plmmob.space_mob_list_view%2540plmmob.space.mob_list_view_mob_list%2522%252C%2522srfnavlogicid%2522%253A%252292b6112f-e53d-26c2-af0b-fc617ca4fe82%253A8eb5d724-4d71-6e1c-8b2f-63eb866708e9%2522%257D
</#if>`

内容：
```
<div class="notice-card" style="display: flex; align-items: flex-start;">
    <div class="notice-card__avatar" style="flex-shrink: 0;">
        <span class="notice-card__avatar-icon" style="background-color: skyblue; border-radius: 50%; margin-right: 10px; width: 36px; height: 36px; display: flex; justify-content: center; align-items: center; font-size: 10px;">${data.update_mantext!?right_pad(2)?substring(0,2)?trim}</span>
    </div>
    <div class="notice-card__content" style="flex-grow: 1;width: calc(100% - 46px);">
        <div class="notice-card__event">
            <div class="notice-card__event-title" style="font-size: 14px; color: #000;">
                <span class="notice-card__event-name" style="color: #999; font-size: 14px; text-transform: lowercase; display: inline-block; max-width: 100%; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">${data.update_mantext}</span> 
                <span class="notice-card__event-desc" style="font-size: 14px; text-transform: lowercase; display: inline-block; max-width: 100%; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;"><#if data.is_deleted==1>删除<#else>恢复</#if>了空间</span>
            </div>
        </div>
        <div class="notice-card-object" style="display: inline-block; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; width: 100%;">
            <#if data.identifier??>
                <span class="notice-card__object-id" style="color: #999; font-size:14px;">${data.identifier}</span>
            </#if>
            <span class="notice-card__object-name" title="${data.name}">${data.name}</span>
        </div>
        <div class="notice-card-pilot" style="font-size: 12px; color: #999; text-transform: lowercase; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
            <span class="notice-pilot-time">${data.update_time?string("yyyy-MM-dd HH:mm:ss")}</span>
            <span class="notice-pilot-info"> · 知识管理 · ${data.name}</span>
        </div>
    </div>
</div>
```

钉钉内容：
```
${data.update_mantext}<#if data.is_deleted==1>删除<#else>恢复</#if>了空间：${data.name}
```

微信消息内容：
```
${data.update_mantext}<#if data.is_deleted==1>删除<#else>恢复</#if>了空间：${data.name}
```
#### 评审完成通知模板(空间页面)(page_review_complete) :id=page_review_complete


模板类型：`静态`

模板引擎：`FreeMarker`

内容类型：`HTML网页`

超链接：`view://review_page_main_view?srfnavctx={"review":"${data.id}","space":"${data.principal_id}","product": null,"project": null,"library": null}`

内容：
```
<div class="notice-card" style="display: flex; align-items: flex-start;">
    <div class="notice-card__avatar" style="flex-shrink: 0;">
        <span class="notice-card__avatar-icon" style="background-color: skyblue; border-radius: 50%; margin-right: 10px; width: 36px; height: 36px; display: flex; justify-content: center; align-items: center; font-size: 10px;">${data.reviewertext!?right_pad(2)?substring(0,2)?trim}</span>
    </div>
    <div class="notice-card__content" style="flex-grow: 1;width: calc(100% - 46px);">
        <div class="notice-card__event">
            <div class="notice-card__event-title" style="font-size: 14px; color: #000;">
                <span class="notice-card__event-name" style="color: #999; font-size: 14px; text-transform: lowercase; display: inline-block; max-width: 100%; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">${data.reviewertext}</span> 
                <span class="notice-card__event-desc" style="font-size: 14px; text-transform: lowercase; display: inline-block; max-width: 100%; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">完成了页面评审</span>
            </div>
        </div>
        <div class="notice-card-object" style="display: inline-block; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; width: 100%;">
            <#if data.identifier??>
                <span class="notice-card__object-id" style="color: #999; font-size:14px;">${data.identifier}</span>
            </#if>
            <span class="notice-card__object-name" title="${data.name}">${data.name}</span>
        </div>
        <div class="notice-card-pilot" style="font-size: 12px; color: #999; text-transform: lowercase; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
            <span class="notice-pilot-time">${.now?string("yyyy-MM-dd HH:mm:ss")}</span>
            <span class="notice-pilot-info"> · 知识管理 · ${data.principal_name}</span>
        </div>
    </div>
</div>
```
#### 知识库通知模板(移除空间成员)(space_member_remove) :id=space_member_remove


模板类型：`静态`

模板引擎：`FreeMarker`

内容类型：`HTML网页`

内容：
```
<div class="notice-card" style="display: flex; align-items: flex-start;">
    <div class="notice-card__avatar" style="flex-shrink: 0;">
        <span class="notice-card__avatar-icon" style="background-color: skyblue; border-radius: 50%; margin-right: 10px; width: 36px; height: 36px; display: flex; justify-content: center; align-items: center; font-size: 10px;">${data.update_mantext!?right_pad(2)?substring(0,2)?trim}</span>
    </div>
    <div class="notice-card__content" style="flex-grow: 1;width: calc(100% - 46px);">
        <div class="notice-card__event">
            <div class="notice-card__event-title" style="font-size: 14px; color: #000;">
                <span class="notice-card__event-name" style="color: #999; font-size: 14px; text-transform: lowercase; display: inline-block; max-width: 100%; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">${data.update_mantext}</span> 
                <span class="notice-card__event-desc" style="font-size: 14px; text-transform: lowercase; display: inline-block; max-width: 100%; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">把你移除了空间</span>
            </div>
        </div>
        <div class="notice-card-object" style="display: inline-block; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; width: 100%;">
            <span class="notice-card__object-name" title="${data.space_name}">${data.space_name}</span>
        </div>
        <div class="notice-card-pilot" style="font-size: 12px; color: #999; text-transform: lowercase; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
            <span class="notice-pilot-time">${data.update_time?string("yyyy-MM-dd HH:mm:ss")}</span>
            <span class="notice-pilot-info"> · 知识管理 · ${data.space_name}</span>
        </div>
    </div>
</div>
```

钉钉内容：
```
${data.update_mantext}把你移除了空间：${data.space_name}
```

微信消息内容：
```
${data.update_mantext}把你移除了空间：${data.space_name}
```
