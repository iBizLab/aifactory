<p class="panel-title"><b>执行代码[Groovy]</b></p>

```groovy
def mainlist = logic.param("mainlist").getReal();
def curselectedlist = logic.param("curselectedlist").getReal()
curselectedlist.addAll(mainlist)
```
