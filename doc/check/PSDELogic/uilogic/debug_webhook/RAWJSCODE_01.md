<p class="panel-title"><b>执行代码</b></p>

```javascript
var _default = uiLogic.default;
const webhookurl=_default.webhookurl;
const webhookdebugparams=_default.webhookdebugparams  || {} ;
const url = new URL(webhookurl);
const headers = {
    "Content-Type": "application/json"
};

fetch(url, {
    method: 'POST',
    headers: headers,
    body: webhookdebugparams
});

ibiz.message.success('执行指令已发出...');

```
