# 一、顺序结构
## 1.1 定义
在顺序结构里，程序会依照代码书写的先后顺序，一条接一条地执行指令，直至所有指令都执行完毕。
## 1.2 特点
- **执行的有序性**：程序会严格按照代码排列的先后顺序执行，先执行第一行代码，接着执行第二行，以此类推
- **执行的唯一性**：在顺序结构中，每一条语句都会被执行，而且只会被执行一次
- **结构的简单性**：顺序结构是最简单的程序结构，不需要使用额外的控制语句，是构建复杂程序的基础
## 1.3 应用场景
- 执行简单的数学运算
- 依次读取和处理数据
- 按照固定流程输出信息
## 1.4 代码实操——计算圆的面积并输出结果

```python
"""
计算圆的面积并输出结果
"""

# 1. 定义常量
PI = 3.14159

# 2. 读取用户输入
radius = float(input("请输入圆的半径："))

# 3. 进行计算
area = PI * radius ** 2

# 4. 输出结果
print(f"圆的半径是：{radius}")
print(f"圆的面积是：{area}")
```
- 运行结果：
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/aaace65fe4ef46aeab4218627b0846d2.png)
# 二、分支结构
## 2.1 双分支语句

```python
if 表达式:
	语句1
	语句2
else:
	语句3
	语句4
```
### 代码实操——判断学生成绩

```python
score = int(input('请输入分数:'))
if score >= 60:
    print('及格')
else:
    print('不及格')
```
- 运行结果：
```
请输入分数:70
及格
```
## 2.2 多分支语句

```python
if 条件1:
	语句1
elif 条件2:
	语句2
elif 条件3:
	语句3
else:
	语句4
```
### 代码实操——判断学生成绩(2)

```python
score = int(input('请输入分数:'))
if score >= 90:
    print('优秀')
elif score >= 80:
    print('良好')
elif score >= 70:
    print('中等')
elif score >= 60:
    print('及格')
else:
    print('不及格')
```
- 运行结果：
```
请输入分数:70
中等
```
# 三、分支循环
## 3.1 while 循环语句

```python
while 判断表达式:
		语句1
```
### 代码实操——随机生成验证码

```python
import random
import string
str1 = ''
for i in range(4):
    random_char = random.choice(string.ascii_uppercase)
    str1 += random_char
print(str1)
```
- 运行结果：
```
UNFY
```
## 3.2 for 循环语句

```python
for 变量名 in 可迭代对象:
		# 循环体，每次代码执行的代码块
		# 可以通过变量名引用迭代对象的元素
```
### 代码实操——打印字符串的每个字符

```python
for item in '黄鹤楼送孟浩然之广陵':
        print(item)
```
- 运行结果：
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/72cf129787204ca3a2aab6f54555135e.png)
## 3.3 循环退出
### 3.3.1 break
- 立即退出当前循环（无论是`for`循环还是`while`循环）
- 当遇到`break`语句时，程序将不会执行循环体中的剩余语句，而是直接跳转到循环之后的语句
### 3.3.2 continue
- 跳过当前循环的剩余部分，并立即开始下一次迭代
- 当遇到`continue`语句时，程序将不会执行循环体中的`continue`之后的语句，而是直接跳转到下一次循环的开始

-----
==微语录：人活着不存在什么意义，但活着本身就是一种意义。==
