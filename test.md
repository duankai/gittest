# 使用Atom Markdown 编辑器

------

> * 学习机器学习
> * 学习经济知识


### 2016年目标

>使用快捷键`Ctrl + Alt + N`


----

## Markdown 语法


### 1. Latex 公式

$$E=mc^2$$

$$\sum_i^m{log(p(x^{(i)},z^{(i)};)}$$

### 2.高亮一段代码

```python

@requires_authorization
class ClassName(object):
  """docstring for """
  def __init__(self, arg):
    super(, self).__init__()
    self.arg = arg

```

```c++
struct
{
    int a = 0;
}
```
---

### 3.高效绘制--流程图

```flow
st=>start: Start
io=>inputoutput: verification
op=>operation: Your Operation
cond=>condition: Yes or No?
sub=>subroutine: Your Subroutine
e=>end

st->io->op->cond
cond(yes)->e
cond(no)->sub->io
```
