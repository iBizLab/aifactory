<p class="panel-title"><b>执行代码</b></p>

```javascript
var _default = uiLogic.default;
var access_key = _default.access_key;

if(access_key !== null && access_key !== undefined){
    var textArea = document.createElement("textarea");
    // 在 textarea 中放入需要复制的文本
    textArea.value = access_key;
    // 将 textarea 添加到 DOM 中
    document.body.appendChild(textArea);
    // 选中 textarea 中的文本
    textArea.select();
    // 执行复制命令
    var successful = document.execCommand('copy');
    var msg = successful ? '' : '复制密钥失败!';
    if(successful){
        util.message.success('复制密钥成功!');
    } else {
        util.message.error('复制密钥失败!');
    }
} else {
    util.message.error('复制密钥失败!');
}

```
