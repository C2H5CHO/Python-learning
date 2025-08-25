# 一、基础入门知识
## 1.1 代码规范
### 1.1.1 语句分隔符
- `; `
- 换行
### 1.1.2 格式化
- 对 Windows 和 Linux 操作系统，快捷键是`Ctrl + Alt + L`
- 对 macOS 操作系统，快捷键是`Cmd + Option + L`
### 1.1.3 注释
- 单行注释

```python
# 这是一行注释
```
- 多行注释

```python
"""
这
是
多
行
注
释
"""
```
### 1.1.4 官方文档
[PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
## 1.2 变量
### 1.2.1 定义
- 变量是一个存储数据值的容器
- 数据值可以是数字、字符串、列表、元组、字典、集合、布尔值等
### 1.2.2 变量名
1. 变量名可以是任意的，但需要遵循规范
2. 变量名规范：
- 可以是数字、字母、下划线_
- 不允许是数字开头
- 不允许是关键字或者内置函数等
- 建议是“小驼峰”结构或者下划线分隔
### 1.2.3 变量值
- 变量是容器，数值是可以进行修改的
# 二、基本数据类型
## 2.1 数字类型
### 2.1.1 常见类型
- 整型

```python
x = 10
print(x)
print(type(x))
```
- 浮点型

```python
x = 3.14
print(x)
print(type(x))
```
### 2.1.2 代码实操——计算圆形的周长和面积

```python
"""
计算圆形的周长和面积
"""

# 1. 工具包
import math

# 2. 输入圆的半径
radius = 3

# 3. 计算周长 + 面积
circumference = 2 * math.pi * radius
area = math.pi * radius**2

print(f"圆形的周长：{circumference:.2f}")
print(f"圆形的面积：{area:.2f}")
```
- 结果运行图：
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/172ab52560784286b3e1c3db9e0e5b1d.png)
## 2.2 布尔类型
### 2.2.1 常见类型
- True 真
- False 假
### 2.2.2 应用场景
- 在条件语句中，控制程序的流程
- 在逻辑运算中，表示结果的真假
### 2.2.3 与其他数据类型的转换
1. 在特定的上下文中，一些数据类型（如整型、浮点型、字符串等）可以被解释为布尔值。
2. 空值（如空列表、空字典、空字符串、0、None等）一般被看作是 False，而非空值一般被看作是 True。
### 2.2.4 代码实操——逻辑运算

```python
"""
逻辑运算
"""

# 1. and运算
print(True and True)
print(True and False)

# 2. or运算
print(True or False)
print(False or False)

# 3. not运算
print(not True)
print(not False)
```
- 运行结果：
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/eb0a0cc443ce4e218da78ff34e48d048.png)
## 2.3 字符串类型
### 2.3.1 常见类型
- 单引号 `' '`
- 双引号 `" "`
- 三引号 `""" """`
### 2.3.2 转义符
1. 定义：在字符串中，插入的无法直接表示或具有特殊含义的字符
2. 常见类型：
	- `\\`：用于在字符串中插入反斜杠
	- `\'`：用于在单引号字符串中插入单引号
	- `\"`：在双引号字符串中插入双引号
	- `\n`：用于在字符串中换行
	- `\t`：用于在字符串中插入制表符
### 2.3.3 格式化输出
1. 目的：将变量或表达式的结果嵌入到字符串中，以生成有意义的输出。
2. 常见类型：
	- `%s`，`%d`，`%f`
	- `str.format()`
	- `f-string`
### 2.3.4 序列操作
- 创建、修改、查找和格式化字符串
- 通过索引获取字符
- 通过切片获取字符
- 拼接字符串
- 计算机字符串长度
- 判断某个字符或子字符串是否存在
### 2.3.5 内置方法
下面是优化后的字符串内置方法表格，增加了参数说明和示例，并保持排版清晰：

### 字符串内置方法详解

| 方法         | 含义                 | 参数                          | 返回值          | 示例代码                                                                 |
|--------------|----------------------|-------------------------------|-----------------|--------------------------------------------------------------------------|
| `upper()`    | 转换为大写           | 无                            | 新字符串        | `print("hello".upper())` → `HELLO`                                        |
| `lower()`    | 转换为小写           | 无                            | 新字符串        | `print("WORLD".lower())` → `world`                                        |
| `title()`    | 转换为标题格式       | 无                            | 新字符串        | `print("hello world".title())` → `Hello World`                            |
| `startswith(prefix)` | 是否以指定前缀开头 | `prefix`: 前缀字符串          | 布尔值          | `print("hello".startswith("he"))` → `True`                                |
| `endswith(suffix)`   | 是否以指定后缀结尾 | `suffix`: 后缀字符串          | 布尔值          | `print("hello".endswith("lo"))` → `True`                                  |
| `isdigit()`  | 是否全为数字字符     | 无                            | 布尔值          | `print("123".isdigit())` → `True`                                         |
| `isalpha()`  | 是否全为字母字符     | 无                            | 布尔值          | `print("abc".isalpha())` → `True`                                         |
| `isalnum()`  | 是否全为字母或数字   | 无                            | 布尔值          | `print("abc123".isalnum())` → `True`                                      |
| `strip([chars])` | 去除两边指定字符   | `chars`: 要去除的字符集合     | 新字符串        | `print("  hello  ".strip())` → `hello`                                     |
| `lstrip([chars])` | 去除左边指定字符  | `chars`: 要去除的字符集合     | 新字符串        | `print("  hello".lstrip())` → `hello`                                      |
| `rstrip([chars])` | 去除右边指定字符  | `chars`: 要去除的字符集合     | 新字符串        | `print("hello  ".rstrip())` → `hello`                                      |
| `join(iterable)` | 连接可迭代对象     | `iterable`: 包含字符串的可迭代对象 | 新字符串     | `print("-".join(["a", "b", "c"]))` → `a-b-c`                              |
| `split(sep=None)` | 按分隔符分割字符串 | `sep`: 分隔符，默认为空白字符 | 字符串列表      | `print("a,b,c".split(","))` → `['a', 'b', 'c']`                           |
| `find(sub)`  | 查找子字符串首次出现位置 | `sub`: 要查找的子字符串     | 索引或-1        | `print("hello".find("l"))` → `2`                                           |
| `index(sub)` | 查找子字符串首次出现位置 | `sub`: 要查找的子字符串     | 索引或报错      | `print("hello".index("l"))` → `2`                                          |
| `count(sub)` | 统计子字符串出现次数 | `sub`: 要统计的子字符串      | 整数            | `print("hello".count("l"))` → `2`                                          |
| `replace(old, new)` | 替换指定子字符串 | `old`: 原字符串<br>`new`: 新字符串 | 新字符串   | `print("hello".replace("l", "L"))` → `heLLo`                              |
| `center(width, fillchar)` | 字符串居中填充 | `width`: 总宽度<br>`fillchar`: 填充字符 | 新字符串 | `print("hello".center(10, '*'))` → `**hello***`                            |
| `zfill(width)` | 左侧补零到指定宽度 | `width`: 总宽度               | 新字符串        | `print("42".zfill(5))` → `00042`               |

### 2.3.6 代码实操
#### （1）创建字符串

```python
"""
创建字符串
"""

# 1. 单引号
name = '李白'
print(f'姓名：{name}')

# 2. 双引号
age = "18"
print(f"年龄：{age}")

# 3. 三引号
hobby = """
1. movie
2. music
"""
print(f'兴趣：{hobby}')
```
- 运行结果：
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/8c63c1e0528f44598894488875031243.png)
#### （2）插入转义符

```python
"""
插入转义符
"""

# 1. \'
string_1 = '老师：\'论文写完了嘛？\''
print(string_1)

# 2. \"
string_2 = "学生：\"快了，快了。\""
print(string_2)

# 3. \n + \t
string_3 = "老师：\n\t\"速度！速度！\""
print(string_3)
```
- 运行结果
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/4104b532ba6e41fc91ac543be3e231e3.png)
#### （3）格式化输出

```python
"""
格式化输出
"""

# 1. %s,%d,%f
name_1 = '李白'
age_1 = 18
print("我的名字是：%s，我的年龄是：%d岁。" % (name_1, age_1))

# 2. str.format()
name_2 = '杜甫'
age_2 = 20
print("你的名字是：{}，你的年龄是：{}岁。".format(name_2, age_2))

# 3. f-string
name_3 = '苏轼'
age_3 = 22
print(f"他的名字是：{name_3}，他的年龄是：{age_3}岁。")
```
- 运行结果：
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/00c3895508124ab58f5a8bfe9f2e58b1.png)
#### （4）序列操作

```python
"""
序列操作
"""

# 1. 创建字符串
str1 = "Hello"
str2 = 'World'
str3 = """
Hello
World
"""
print(f"str1：{str1}")
print(f"str2：{str2}")
print(f"str3：{str3}")

print('--'*50)

# 2. 通过索引获取字符
print(f"第一个字符：{str1[0]}")
print(f"最后一个字符：{str1[-1]}")

print('--'*50)

# 3. 通过切片获取字符
# 取首略尾
print(f"取首略尾：{str1[1:3]}")
# 默认到尾
print(f"默认到尾：{str1[1:]}")
# 从头开始
print(f"从头开始：{str1[:4]}")
# 从左向右
print(f"从左向右：{str1[1:4:1]}")
# 隔1取1
print(f"隔1取1：{str1[1:4:2]}")
# 反向截取
print(f"反向截取：{str1[3:1:-1]}")

print('--'*50)

# 4. 拼接字符串
concat1 = str1 + " " + str2
concat2 = "".join([str1, " ", str2])
print(f"concat1：{concat1}")
print(f"contact：{concat2}")

print('--'*50)

# 5. 计算字符串长度
print(f"str1的长度：{len(str1)}")
print(f"str3的行数：{len(str3.splitlines())}")

print('--'*50)

# 6. 判断某个字符或子字符串是否存在
print(f"存在判断: 'e' 在 {str1} 中: {'e' in str1}")
print(f"子串判断: 'lo' 在 {str1} 中: {str1.find('lo') != -1}")
```
- 运行结果：
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/2c1692b4ade94eee91e3619c89a24f42.png)

-----
==微语录：被贴上标签的人，只能等待着自己应得的人生。——《信》==
