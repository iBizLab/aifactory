<p class="panel-title"><b>执行代码</b></p>

```javascript
var _kb_entity = uiLogic.kb_entity;
console.log('正在设置知识库首页动态看板');
if(_kb_entity){
    const c = view.ctx.controllersMap.get('drbar');
    if(c){
        c.context.dyna_dashboard = _kb_entity.dyna_dashboard_id;
        c.context.srfdynadashboardid = _kb_entity.dyna_dashboard_id;
    }
}
```
