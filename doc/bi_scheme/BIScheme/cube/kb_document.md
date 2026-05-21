# 知识库文档(kb_document)  <!-- {docsify-ignore-all} -->


<br>
<p class="panel-title"><b>实体</b></p>

* [知识库文档(AI_KB_DOCUMENT)](module/ai/ai_kb_document)



### 维度
##### 常规维度
|    名称col200   | 代码名col150      | 属性col350    |  备注col500  |
| --------  |------------| -----   |  --------|
|创建时间|create_time|文档创建时间(DOC_CREATE_TIME)||
|文件类型|doc_type|文件类型(FILE_TYPE)||

### 指标
##### 计算式指标
|    名称col200   | 代码名col150  |  计算公式col501   |  备注col500  |
| --------  |------------| -----   |  --------|
|子分片数量|c_chunk|(select count(1)  from ai_kb_chunk  c  where  c.pid  is not  null and  c.document_id  = dataresult.id )||
|文档大小|size|sumif(size, 1=2)/(1024*1024)||
|文档数量|count|countif( 1= 1 )|统计所有的文档数。|
|父分片数量|p_chunk|(select count(1)  from ai_kb_chunk  c  where  c.pid  is null and  c.document_id  = dataresult.id )||

<script>
 const { createApp } = Vue
  createApp({
    data() {
      return {
      }
    },
    methods: {
    }
  }).use(ElementPlus).mount('#app')
</script>