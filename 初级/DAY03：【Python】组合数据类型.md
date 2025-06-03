# 1、列表
## 1.1 列表的表达
> 1. 序列类型：内部元素有位置关系，能通过位置序号访问其中元素
> 2. 序列特点：可使用多种类型元素，支持元素的增删查改

```python
lst = ["python", 2025, True, {"age": 20}]
print(lst)
# 输出：['python', 2025, True, {'age': 20}]
```
- list(可迭代类型)
### 1.1.1 字符串转列表

```python
lst1 = list("人工智能")
print(lst1)
# 输出：['人', '工', '智', '能']
```
### 1.1.2 元组转列表

```python
lst2 = list(("我", "们", "爱", "中", "国"))
print(lst2)
# 输出：['我', '们', '爱', '中', '国']
```
### 1.1.3 集合转列表

```python
lst3 = list({"Mike", "Jim", "Tim", "Jerry", "Tom"})
print(lst3)
# 输出：['Tom', 'Tim', 'Jerry', 'Jim', 'Mike']
```
### 1.1.4 特殊的range(开始数据, 结束数据, 数字间隔)

```python
for i in [1,2,3]:
    print(i)
# 输出：1
#      2
#      3

for i in range(3):
    print(i)
# 输出：0
#      1
#      2
```
> 注意：
> &emsp;&emsp;1. 开始数据若为0，则可以省略
> &emsp;&emsp;2. 结束数据不可以省略
> &emsp;&emsp;3. 数字间隔默认为1

```python
for i in range(1, 11, 2):
    print(i)
# 输出：1
#      3
#      5
#      7
#      9

print(list(range(1, 11, 2)))
# 输出：[1, 3, 5, 7, 9]
```
## 1.2 列表的性质
### 1.2.1 列表的长度——len(列表)

```python
lst = [1,2,3,4,5,6,7,8,9]
print(len(lst))
# 输出：9
```
### 1.2.2 列表的索引——变量名[位置编号]

```python
cars = ["BYD", "BMW", "HRV"]
print(cars[0])
# 输出：BYD
print(cars[-1])
# 输出：HRV
```
> 用法与==字符串==完全相同
### 1.2.3 列表的切片——变量名[开始位置:结束位置:切片间隔]

```python
cars = ["BYD", "BMW", "HRV", "AUDI"]
print(cars[1:4:2])  # 正向切片
# 输出：['BMW', 'AUDI']
print(cars[:-4:-1])  # 反向切片
# 输出：['AUDI', 'HRV', 'BMW']
print(cars[:])  # 遍历
# 输出：['BYD', 'BMW', 'HRV', 'AUDI']
```
## 1.3 列表的操作符
### 1.3.1 列表的拼接——lst1 + lst2

```python
lst1 = [1, 2]
lst2 = [3, 4, 5]
c = lst1 + lst2
print(c)
# 输出：[1, 2, 3, 4, 5]
```
### 1.3.2 列表的成倍复制——lst*n

```python
lst3 = [0]*10
print(lst3)
# 输出：[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```
> 初始化列表的一种方式
## 1.4 列表的操作方法
### 1.4.1 增加元素
#### （1）在末尾增加——lst.append(待增元素)

```python
language = ["Python", "Java", "C++", "JavaScript", "PHP", "C#"]
language.append("R")
print(language)
# 输出：['Python', 'Java', 'C++', 'JavaScript', 'PHP', 'C#', 'R']
```
#### （2）在任意位置增加——lst.insert(位置编号, 待增元素)

```python
language.insert(1, "C")
print(language)
# 输出：['Python', 'C', 'Java', 'C++', 'JavaScript', 'PHP', 'C#', 'R']
```
#### （3）在末尾整体并入另一列表

```python
language.append(["MySQL", "CSS"])  # 整体添加
print(language)
# 输出：['Python', 'C', 'Java', 'C++', 'JavaScript', 'PHP', 'C#', 'R', ['MySQL', 'CSS']]

language.extend(["SQL", "go"])  # 逐个添加
print(language)
# 输出：['Python', 'C', 'Java', 'C++', 'JavaScript', 'PHP', 'C#', 'R', ['MySQL', 'CSS'], 'SQL', 'go']
```
### 1.4.2 删除元素
#### （1）删除位置i处的元素——lst.pop(位置编号)

```python
language.pop(0)
print(language)
# 输出：['C', 'Java', 'C++', 'JavaScript', 'PHP', 'C#', 'R', ['MySQL', 'CSS'], 'SQL', 'go']
language.pop()  # 若空白，则默认删除最后一个
print(language)
# 输出：['C', 'Java', 'C++', 'JavaScript', 'PHP', 'C#', 'R', ['MySQL', 'CSS'], 'SQL']
```
#### （2）删除列表第一次出现的待删元素——lst.remove(待删元素)

```python
language.remove("Java")
print(language)
# 输出：['C', 'C++', 'JavaScript', 'PHP', 'C#', 'R', ['MySQL', 'CSS'], 'SQL']

while "R" in language:
    language.remove("R")
print(language)
# 输出：['C', 'C++', 'JavaScript', 'PHP', 'C#', ['MySQL', 'CSS'], 'SQL']
```
### 1.4.3 查找元素
> lst.index(待查元素)：查找列表中第一次出现待查元素的位置

```python
idx = language.index("C++")
print(idx)
# 输出：1
```
###  1.4.4 修改元素
> lst[位置]=新值：先索引，后赋值

```python
language[1] = "R"
print(language)
# 输出：['C', 'R', 'JavaScript', 'PHP', 'C#', ['MySQL', 'CSS'], 'SQL']
```
### 1.4.5 列表的复制
#### （1）错误的方式

```python
codes = ["python", "java", "C"]
codes1 = codes
print(codes1)
# 输出：['python', 'java', 'C']

codes.pop()
print(codes)
# 输出：['python', 'java']
print(codes1)
# 输出：['python', 'java']
```
#### （2）浅拷贝

```python
# lst.copy()
codes2 = codes.copy()
codes.pop()
print(codes)
# 输出：['python']
print(codes2)
# 输出：['python', 'java']

# --------------------------------------------------

# lst[:]
codes3 = codes2[:]
codes2.pop()
print(codes2)
# 输出：['python']
print(codes3)
# 输出：['python', 'java']
```
### 1.4.6 列表的排序
#### （1）lst.sort()——永久排序，原列表改变，无返回值

```python
lst = [1, 3, 5, 11, 2, 9]
lst.sort()
print(lst)
# 输出：[1, 2, 3, 5, 9, 11]
lst.sort(reverse=True)  # 递减排序
print(lst)
# 输出：[11, 9, 5, 3, 2, 1]
```
#### （2）sorted(列表名)——临时排序，原列表不变，返回值是排序后的类别

```python
lst = [2, 5, 1, 20, 7]
lst1 = sorted(lst)
lst2 = sorted(lst1, reverse=True)
print(lst)
# 输出：[2, 5, 1, 20, 7]
print(lst1)
# 输出：[1, 2, 5, 7, 20]
print(lst2)
# 输出：[20, 7, 5, 2, 1]
```
### 1.4.7 列表的翻转
> lst.reverse()：永久翻转，原列表改变，无返回值

```python
lst = [1, 2, 3, 4, 5, 6]
print(lst[::-1])
# 输出：[6, 5, 4, 3, 2, 1]
print(lst)
# 输出：[1, 2, 3, 4, 5, 6]
lst.reverse()
print(lst)
# 输出：[6, 5, 4, 3, 2, 1]
```
### 1.4.8 for循环遍历

```python
lst = [1, 2, 3, 4, 5, 6]
for i in lst:
    print(i)
# 输出：1
#      2
#      3
#      4
#      5
#      6
```
# 2、元组
## 2.1 元组的表达
> 特点：
> &emsp;&emsp;1. 支持多种类型的元素
> &emsp;&emsp;2. 内部元素不支持增删改的序列操作

```python
names = ["Mike", "Jim", "Tim", "Jerry", "Tom"]
```
## 2.2 元组的操作
> 1. 不支持元素增加、元素删除、元素修改
> 2. 其他操作与==列表==一致
## 2.3 元组的常见用处——打包与解包
- 例1

```python
def f1(x):  # 返回x的平方和立方
    return x**2, x**3  # 实现打包返回

print(f1(3))
# 输出：(9, 27)
print(type(f1(3)))
# 输出：<class 'tuple'>
```

- 例2

```python
numbers = [202501, 202502, 202503]
names = ["小红", "小蓝", "小绿"]
list(zip(numbers, names))  # 实现打包返回

for number, name in zip(numbers, names):
    print(number, name)
# 输出：202501 小红
#      202502 小蓝
#      202503 小绿
```
# 3、字典
## 3.1 字典的表达
> 1. 映射类型：通过“键”-“值”的映射实现数据存储和查找
> 2. 常规的字典是==无序==的

```python
students = {202501: "小红", 202502: "小蓝", 202503: "小绿"}
print(students)
# 输出：{202501: '小红', 202502: '小蓝', 202503: '小绿'}
```
> 字典键的要求：
- 字典键不能重复

```python
students = {202501: "小红", 202502: "小蓝", 202501: "小红"}
print(students)
# 输出：{202501: '小红', 202502: '小蓝'}
```
- 字典键是不可变类型
> 1. 不可变类型：数字、字符串、元组
> 2. 可变类型：列表、字典、集合

```python
d1 = {1: 3}
d2 = {"a": 1}
d3 = {(1, 2): 3}

# --------------------------------------------------

d = {[1, 2]: 3}
# 输出：TypeError: unhashable type: 'list'
d = {{1: 2}: 3}
# 输出：TypeError: unhashable type: 'dict'
d = {{1, 2}: 3}
# 输出：TypeError: unhashable type: 'set'
```
##  3.2 字典的性质
### 3.2.1 字典的长度——键值对的个数

```python
children = {2025: "小明", 2024: "李华", 2023: "张三"}
print(len(children))
# 输出：3
```
### 3.2.2 字典的索引——d[键]

```python
print(children[2024])
# 输出：李华
```
## 3.3 字典的操作方法
### 3.3.1 增加键值对——变量名[新键]=新值

```python
students = {2025: "张三", 2024: "李四", 2023: "赵五"}
students[2023] = "小雪"
print(students)
# 输出：{2025: '张三', 2024: '李四', 2023: '小雪'}
```
### 3.3.2 删除键值对
#### （1）del 变量名[待删除键]

```python
del students[2025]  # del 变量名[待删除键]
print(students)
# 输出：{2024: '李四', 2023: '小雪'}
```
#### （2）变量名.pop(待删除键)

```python
value = students.pop(2024)  # 变量名.pop(待删除键)
print(value)
# 输出：李四
print(students)
# 输出：{2023: '小雪'}
```
#### （3）变量名.popitem()
> **随机**删除一个键值对，并以==元组==返回待删除的键值对

```python
key, value = students.popitem()  # 变量名.popitem()--随机删除一个键值对，并以元组返回待删除的键值对
print(key, value)
# 输出：2023 小雪
print(students)
# 输出：{}
```
### 3.3.3 修改值

```python
students = {2025: "小明", 2024: "小强"}
students[2025] = "小雪"
print(students)
# 输出：{2025: '小雪', 2024: '小强'}
```
### 3.3.4 &emsp;d.get(key, default())
> 从字典中获取key对应的value，若没有这个键，则返回default

```python
s = "牛奶奶找刘奶奶买牛奶"
d = {}
print(d)
for i in s:
    d[i] = d.get(i, 0) + 1
    print(d)
# 输出：{}
#      {'牛': 1}
#      {'牛': 1, '奶': 1}
#      {'牛': 1, '奶': 2}
#      {'牛': 1, '奶': 2, '找': 1}
#      {'牛': 1, '奶': 2, '找': 1, '刘': 1}
#      {'牛': 1, '奶': 3, '找': 1, '刘': 1}
#      {'牛': 1, '奶': 4, '找': 1, '刘': 1}
#      {'牛': 1, '奶': 4, '找': 1, '刘': 1, '买': 1}
#      {'牛': 2, '奶': 4, '找': 1, '刘': 1, '买': 1}
#      {'牛': 2, '奶': 5, '找': 1, '刘': 1, '买': 1}
```
### 3.3.5 &emsp;d.keys() &emsp; d.values()

```python
students = {2025: "小明", 2024: "小强", 2023: "小雪"}
print(list(students.values()))
# 输出：['小明', '小强', '小雪']
print(list(students.keys()))
# 输出：[2025, 2024, 2023]
```
### 3.3.6 &emsp;d.items()

```python
print(list(students.items()))
# 输出：[(2025, '小明'), (2024, '小强'), (2023, '小雪')]
for k, v in students.items():
    print(k, v)
# 输出：2025 小明
#      2024 小强
#      2023 小雪
```
# 4、集合
## 4.1 集合的表达
> 特点：
> &emsp;&emsp;1. 一系列互不相等的无序集合
> &emsp;&emsp;2. 元素必须是不可变类型（数字、字符串或元组），可视为字典的键
> &emsp;&emsp;3. 可看作没有值或者值为None的字典

```python
teachers = {"小明", "小强", "小雪"}
print(teachers)
# 输出：{'小明', '小强', '小雪'}
```
## 4.2 集合的运算
### 4.2.1 &emsp;S&T
> 返回一个新集合，包括**同时**在S和T中的元素

```python
Chinese = {"小明", "小雪", "小强", "小红", "小绿"}
maths = {"小雪", "小绿", "小蓝"}
print(Chinese & maths)
# 输出：{'小绿', '小雪'}
```
###  4.2.2 &emsp;S|T
> 返回一个新集合，包括**所有**在S和T中的元素

```python
print(Chinese | maths)
# 输出：{'小绿', '小明', '小蓝', '小雪', '小强', '小红'}
```
### 4.2.3 &emsp;S^T
> 返回一个新集合，包括集合S和T中的**非共同**元素

```python
print(Chinese^maths)
# 输出：{'小红', '小蓝', '小明', '小强'}
```
### 4.2.4 &emsp;S-T
> 返回一个新集合，包括在集合S但不在集合T中的元素

```python
print(Chinese-maths)
# 输出：{'小红', '小明', '小强'}
```
## 4.3 集合的操作方法
### 4.3.1 增加元素——s.add(x)

```python
stars = {"wjk", "wy", "yyqx"}
stars.add("薛之谦")
print(stars)
# 输出：{'wjk', 'yyqx', '薛之谦', 'wy'}
```
### 4.3.2 移除元素——s.remove(x)

```python
stars.remove("wjk")
print(stars)
# 输出：{'薛之谦', 'yyqx', 'wy'}
```
### 4.3.3 集合的长度——len(s)

```python
print(len(stars))
# 输出：3
```
### 4.3.4 集合的遍历

```python
for star in stars:
    print(star)
# 输出：wy
#      yyqx
#      薛之谦
```
----
`微语录：在年轻的飞奔里，你是迎面而来的风。`
