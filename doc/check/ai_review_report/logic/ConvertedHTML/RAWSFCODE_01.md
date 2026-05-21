<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
def _default = logic.param('Default').getReal(); 
def _review_report = _default.get("review_report")

com.vladsch.flexmark.parser.Parser parser = com.vladsch.flexmark.parser.Parser.builder().build();
com.vladsch.flexmark.util.ast.Node document = parser.parse(_review_report);
com.vladsch.flexmark.html.HtmlRenderer renderer = com.vladsch.flexmark.html.HtmlRenderer.builder().build();
def htmlContent = renderer.render(document);

_default.set("review_report_html",htmlContent);
```
