# cfeditor

cf输入数据智能载入器

> 运行环境：Python 3.10
    
## 格式定义：

    样例数量：T
    单个变量：ABCDEFGHIJK
    字符串：S
    横列表：L
    竖列表：VX(X表示行数，可以是整数1~9，也可以是变量名)
    数字矩阵：NX(X含义同上)
    字符串矩阵：MX(X含义同上)
    分隔符：逗号

例如：

"A" 表示输入单个变量；

"AB" 表示输入空格分隔的两个变量；

"T,AB" 表示输入数据的第一行表示样例的数量，第2到T+1行是具体样例，每个样例都由A/B两个变量组成。

"T,AB,MB" 表示输入数据的第一行表示样例的数量，第2到T+1行是具体样例，每个样例都由A/B两个变量组成。


[样例1](samply1.py)