## 复制密钥 <!-- {docsify-ignore-all} -->

   

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
state "开始" as Begin <<start>> [[$./copy_access_key#begin {开始}]]
state " 复制密钥" as RAWJSCODE_01  [[$./copy_access_key#rawjscode_01 { 复制密钥}]]
state "结束" as END_01 <<end>> [[$./copy_access_key#end_01 {结束}]]


Begin --> RAWJSCODE_01
RAWJSCODE_01 --> END_01


@enduml
```


### 处理步骤说明

#### 开始 :id=Begin<sup class="footnote-symbol"> <font color=gray size=1>[开始]</font></sup>




####  复制密钥 :id=RAWJSCODE_01<sup class="footnote-symbol"> <font color=gray size=1>[直接前台代码]</font></sup>



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

#### 结束 :id=END_01<sup class="footnote-symbol"> <font color=gray size=1>[结束]</font></sup>






### 实体逻辑参数

|    中文名   |    代码名    |  数据类型      |备注 |
| --------| --------| --------  | --------   |
|传入变量(<i class="fa fa-check"/></i>)|Default|数据对象||
