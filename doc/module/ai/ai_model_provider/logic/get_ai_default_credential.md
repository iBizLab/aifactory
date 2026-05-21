## 获取已登记AI凭证 <!-- {docsify-ignore-all} -->

   

### 处理过程

```plantuml
@startuml
hide empty description
<style>
root {
  HyperlinkColor #42b983
}
</style>

hide empty description
state "开始" as Begin <<start>> [[$./get_ai_default_credential#begin {"开始"}]]
state "获取凭证" as DEACTION_03  [[$./get_ai_default_credential#deaction_03 {"获取凭证"}]]
state "提供商是否已存在" as DEDATASET_01  [[$./get_ai_default_credential#dedataset_01 {"提供商是否已存在"}]]
state "结束" as END_01 <<end>> [[$./get_ai_default_credential#end_01 {"结束"}]]
state "准备参数" as PREPAREPARAM_01  [[$./get_ai_default_credential#prepareparam_01 {"准备参数"}]]
state "准备参数" as PREPAREPARAM_03  [[$./get_ai_default_credential#prepareparam_03 {"准备参数"}]]


Begin --> PREPAREPARAM_01
PREPAREPARAM_01 --> DEDATASET_01
DEDATASET_01 --> DEACTION_03 : [[$./get_ai_default_credential#dedataset_01-deaction_03{存在且token不为空} 存在且token不为空]]
DEACTION_03 --> PREPAREPARAM_03
PREPAREPARAM_03 --> END_01


@enduml
```


### 处理步骤说明

#### 提供商是否已存在 :id=DEDATASET_01<sup class="footnote-symbol"> <font color=gray size=1>[实体数据集]</font></sup>



调用实体 [AI凭证(AI_CREDENTIAL)](module/ai/ai_credential.md) 数据集合 [DEFAULT](module/ai/ai_credential#数据集合) ，查询参数为`credential_filter`

将执行结果返回给参数`credentials`

#### 准备参数 :id=PREPAREPARAM_01<sup class="footnote-symbol"> <font color=gray size=1>[准备参数]</font></sup>



1. 将`Default(传入变量).ID(标识)` 设置给  `credential_filter.N_ID_EQ`
2. 将`Default(传入变量).ID(标识)` 设置给  `credential.ID(标识)`

#### 开始 :id=Begin<sup class="footnote-symbol"> <font color=gray size=1>[开始]</font></sup>



*- N/A*
#### 获取凭证 :id=DEACTION_03<sup class="footnote-symbol"> <font color=gray size=1>[实体行为]</font></sup>



调用实体 [AI凭证(AI_CREDENTIAL)](module/ai/ai_credential.md) 行为 [Get](module/ai/ai_credential#行为) ，行为参数为`credential`

将执行结果返回给参数`credential`

#### 准备参数 :id=PREPAREPARAM_03<sup class="footnote-symbol"> <font color=gray size=1>[准备参数]</font></sup>



1. 将`credential.BEARER_TOKEN(Bearer令牌)` 设置给  `Default(传入变量).DEFAULT_TOKEN(API 密钥)`

#### 结束 :id=END_01<sup class="footnote-symbol"> <font color=gray size=1>[结束]</font></sup>



返回 `Default(传入变量)`


### 连接条件说明
#### 存在且token不为空 :id=DEDATASET_01-DEACTION_03

`credentials(credentials).size` GT `0`


### 实体逻辑参数

|    中文名   |    代码名    |  数据类型    |  实体   |备注 |
| --------| --------| -------- | -------- | --------   |
|传入变量(<i class="fa fa-check"/></i>)|Default|数据对象|[模型提供商(AI_MODEL_PROVIDER)](module/ai/ai_model_provider.md)||
|credential|credential|数据对象|[AI凭证(AI_CREDENTIAL)](module/ai/ai_credential.md)||
|credential_filter|credential_filter|过滤器|||
|credentials|credentials|分页查询|||
