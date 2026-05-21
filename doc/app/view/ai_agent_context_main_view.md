# 智能体上下文(ai_agent_context_main_view)  <!-- {docsify-ignore-all} -->


系统自动添加



## 控件
#### CAPTIONBAR(captionbar)
#### DATAINFOBAR(datainfobar)
#### 编辑表单(form)

##### 部件逻辑
* `onCustomAction`
```
if(args && args.data && args.data.length > 0){
    console.log("开始填充数据---");
    const materials = [];
    args.data.forEach(tempData => {
        const material = {
          id: tempData.id,
          type: tempData.type,
          data: tempData.data || {},
          metadata: tempData.metadata || {},
        };
        if (args.tag) {
          Object.assign(material.metadata, { actionId: args.tag });
        }
        materials.push(material);
    });
    if(materials.length > 0){
        function  stringifyMaterials(resources) {
            const doc = document.implementation.createDocument(null, null, null);
            const root = doc.createElement('resources');
            root.setAttribute('version', '1.0');

            // 添加换行和缩进
            function indent(level){
				return `\n${'  '.repeat(level)}`;
			}
            const currentIndentLevel = 1;

            resources.forEach(res => {
            // 添加资源间的换行和缩进
            root.appendChild(doc.createTextNode(indent(currentIndentLevel)));

            const resourceEl = doc.createElement('resource');
            resourceEl.setAttribute('type', res.type);
            resourceEl.setAttribute('version', '1.0');

            // 创建带缩进的子元素
            function createChildWithCdata(name, content){
                const el = doc.createElement(name);
                el.appendChild(doc.createTextNode(indent(currentIndentLevel + 1)));
                const cdata = doc.createTextNode(JSON.stringify(content));
                el.appendChild(cdata);
                el.appendChild(doc.createTextNode(indent(currentIndentLevel)));
                return el;
            };

            resourceEl.appendChild(
                doc.createTextNode(indent(currentIndentLevel + 1)),
            );
            resourceEl.appendChild(createChildWithCdata('data', res.data));
            resourceEl.appendChild(
                doc.createTextNode(indent(currentIndentLevel + 1)),
            );
            resourceEl.appendChild(createChildWithCdata('metadata', res.metadata));
            resourceEl.appendChild(doc.createTextNode(indent(currentIndentLevel)));

            root.appendChild(resourceEl);
            });

            root.appendChild(doc.createTextNode('\n'));
            doc.appendChild(root);

            // 使用XMLSerializer生成带格式的字符串
            return "<assistant>\n"+"<![CDATA["+new XMLSerializer().serializeToString(doc).replace(/></g, '>\n<')+"]]>"+"\n</assistant>"; // 在标签间添加换行
        }
        const materialStr = stringifyMaterials(materials);
        ctrl.details.welcome_message.editor.mdeditor.insert(materialStr);
        console.log("填充数据完成---",materialStr);
    }
}
```
#### 工具栏(toolbar)
#### 工具栏(toolbar1)


### 关联界面行为
  * [智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context) : [编辑界面_保存并新建操作](module/ai/ai_agent_context#界面行为)
  * [智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context) : [编辑界面_保存操作](module/ai/ai_agent_context#界面行为)
  * [智能体业务上下文(AI_AGENT_CONTEXT)](module/ai/ai_agent_context) : [取消变更](module/ai/ai_agent_context#界面行为)

### 关联视图
  * [智能体(ai_agent_pickup_view)](app/view/ai_agent_pickup_view)
  * [知识库(ai_knowledge_base_pickup_view)](app/view/ai_knowledge_base_pickup_view)
  * [AI大模型(ai_model_pickup_view)](app/view/ai_model_pickup_view)
  * [实体处理逻辑(psdelogiclogicdesign_readonly)](app/view/psdelogiclogicdesign_readonly)

<script>
 const { createApp } = Vue
  createApp({
    data() {
      return {

      }
    }
  }).use(ElementPlus).mount('#app')
</script>