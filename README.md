# cfeditor

cf输入数据智能载入器

> 运行环境：Python 3.10

## 使用方法：

1. 引入智能输入器：

```python []
from cfinput import *
```

2. 调用输入数据智能载入器：

```python []
formart = "T,AB,NB" #formart格式参考后续说明
tp = cfinput(formart)
solve(*tp)
```

## 格式定义：

    样例数量：T
    单个变量：ABCDEFGHIJK
    字符串：S
    横列表：L
    竖列表：VX(X表示行数，可以是整数1~9，也可以是变量名)
    数字矩阵：NX(X含义同上)
    字符串矩阵：MX(X含义同上)
    分隔符：逗号

## 格式样例：

"A" 表示输入单个变量；

"AB" 表示输入空格分隔的两个变量；

"T,AB" 表示输入数据的第一行是样例的数量T，之后是T个样例，每个样例是空格分隔的A/B两个变量。

"T,AB,NB" 表示输入数据的第一行是样例的数量T，之后是T个样例，每个样例的第一行是空格分隔的A/B两个变量，之后是一个B行的数字矩阵，矩阵的每个元素都由空格分隔。


[样例1](samply1.py)