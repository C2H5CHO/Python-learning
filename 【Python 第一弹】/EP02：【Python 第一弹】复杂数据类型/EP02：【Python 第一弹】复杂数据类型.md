# 一、列表类型
## 1.1 数组
- 在 Python 的标准数据类型体系中，并没有专门命名为 “数组” 的数据类型
- 第三方库 NumPy 提供的 `ndarray`（N 维数组）
- Python 内置的列表（list）
## 1.2 NumPy 的 `ndarray`
### 1.2.1 特点
1. **元素类型统一**：数组内所有元素必须为同一数据类型（如整数、浮点数），节省内存且计算高效。
2. **支持多维结构**：可创建 1 维、2 维（矩阵）甚至更高维的数组。
3. **向量运算优化**：内置大量向量化操作，避免循环，提升计算速度。
### 1.2.2 代码实操——创建数组

```python
"""
创建数组
"""

# 1. 工具包
import numpy as np

# 2. 创建1维整数数组
int_array = np.array([1, 2, 3, 4, 5])
print(f"1维整数数组：{int_array}")
print(f"类型：{int_array.dtype}")
print(f"向量化运算：{int_array*2}")

print('--'*50)

# 2. 创建2维字符串数组
str_array = np.array([['a', 'b'], ['c', 'd']])
print(f"2维字符串数组：{str_array}")
print(f"维数：{str_array.shape}")
```
- 运行结果：
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/d74a767ff56a4cf488bc564921da3f76.png)
## 1.3 Python 内置的列表（list）
### 1.3.1 定义
- 列表（list）是Python中非常常用的一种数据结构
- 列表（list）可以包含任意类型的数据项，如整数、浮点数、字符串、其他列表等，并且数据项之间是有序的
### 1.3.2 特点
- **元素类型不限**：可同时存储整数、字符串、布尔值等不同类型的数据
- **有序性**：列表中的元素具有明确的位置
- **可变性**：列表创建后，可以修改其中的元素
- **可重复性**：同一个元素可以在列表中出现多次
### 1.3.3 常用方法

| 方法/函数         | 核心功能                                                                 | 参数说明                          | 对原列表的影响 | 示例代码及输出                                                                 |
|-------------------|--------------------------------------------------------------------------|-----------------------------------|----------------|------------------------------------------------------------------------------|
| `append()`        | 在列表末尾添加单个元素                                                  | 接收1个参数（任意数据类型）       | 直接修改原列表 | ```python<br>lst = [1, 2, 3]<br>lst.append(4)<br>print(lst)  # 输出：[1, 2, 3, 4]<br>```|
| `insert()`        | 在指定索引位置前插入元素                                                | 2个参数：索引值、待插入元素       | 直接修改原列表 | ```python<br>lst = [1, 2, 3]<br>lst.insert(1, 10)  # 在索引1前插入10<br>print(lst)  # 输出：[1, 10, 2, 3]<br>```|
| `remove()`        | 删除列表中**首次出现**的指定元素（若元素不存在则报错）                    | 1个参数：待删除的元素值           | 直接修改原列表 | ```python<br>lst = [1, 2, 2, 3]<br>lst.remove(2)  # 删除第一个2<br>print(lst)  # 输出：[1, 2, 3]<br>```|
| `pop()`           | 删除并返回指定索引的元素（默认删除最后一个元素，索引无效则报错）          | 可选参数：索引值（默认-1）        | 直接修改原列表 | ```python<br>lst = [1, 2, 3]<br>val = lst.pop(1)  # 删除索引1的元素<br>print(lst, val)  # 输出：[1, 3] 2<br>```|
| `extend()`        | 将另一个可迭代对象（如列表、元组）的所有元素添加到当前列表末尾            | 1个参数：可迭代对象               | 直接修改原列表 | ```python<br>lst1 = [1, 2]<br>lst2 = [3, 4]<br>lst1.extend(lst2)<br>print(lst1)  # 输出：[1, 2, 3, 4]<br>```|
| `index()`         | 返回指定元素**首次出现**的索引（若元素不存在则报错）                      | 1个参数：目标元素值               | 不修改原列表   | ```python<br>lst = ['a', 'b', 'a']<br>print(lst.index('a'))  # 输出：0<br>```|
| `count()`         | 统计指定元素在列表中出现的总次数                                        | 1个参数：目标元素值               | 不修改原列表   | ```python<br>lst = [1, 2, 2, 3, 2]<br>print(lst.count(2))  # 输出：3<br>```|
| `sort()`          | 对列表元素进行排序（默认升序，可通过`reverse=True`改为降序）              | 可选参数：`reverse=False`（默认） | 直接修改原列表 | ```python<br>lst = [3, 1, 2]<br>lst.sort(reverse=True)  # 降序排序<br>print(lst)  # 输出：[3, 2, 1]<br>```|
| `sorted()`（内置）| 对列表元素进行排序（返回新列表，原列表不变，支持`reverse`参数）            | 1个参数：待排序的列表             | 不修改原列表   | ```python<br>lst = [3, 1, 2]<br>new_lst = sorted(lst)<br>print(lst, new_lst)  # 输出：[3, 1, 2] [1, 2, 3]<br>```|

- 关键区别
	1. 修改原列表 vs 返回新值：
		- `append()`、`insert()`、`remove()`、`pop()`、`extend()`、`sort()` 会直接修改原列表
   		- `index()`、`count()`、`sorted()` 不改变原列表，仅返回结果或新列表
	2. `append()` vs `extend()`：
   		- `append()` 接收单个元素（即使传入列表，也会作为整体添加）
   		- `extend()` 接收可迭代对象，将其元素逐个添加到原列表
	3. `sort()` vs `sorted()`：
   		- `sort()` 是列表方法，无返回值（返回`None`），直接修改原列表
   		- `sorted()` 是内置函数，返回排序后的新列表，原列表保持不变
### 1.3.4 代码实操——创建列表

```python
"""
创建列表
"""

# 1. []创建
lst1 = [1, 2, 3, 4, 5]
lst2 = [1, 'two', 3.0, [4, 5]]
print(lst1)
print(lst2)

# 2. list()创建
lst3 = list(range(5))
lst4 = list('Hello')
print(lst3)
print(lst4)
```
- 运行结果：
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/0a2c49cbdd104bbeaa0331096ae6c8a1.png)
# 二、字典类型
## 2.1 定义
字典是一种可变、无序且键值对（Key-Value）的数据结构
## 2.2 常见操作
### 2.2.1 创建字典
- 字典是通过大括号 `{}` 创建的，键值对之间用逗号 `,` 分隔
- 键（Key）是唯一的，通常是不可变类型，如整数、浮点数、字符串、元组
- 值（Value）可以是任意类型

#### 代码实操——创建字典

```python
student = {
    'name': "李白",
    'age': 25,
    'score': 80,
}
print(student)
```
- 运行结果：
```
{'name': '李白', 'age': 25, 'score': 80}
```
### 2.2.2 访问字典
- 通过键（Key）来访问字典的值
#### 代码实操——访问字典

```python
student2 = {
    'name': "杜甫",
    'age': 20,
}

print(student2['name'])
print(student2.get('age', '404'))
print(student2.get('hobby', '404'))
print(student2['sex'])
```
- 运行结果：
```
Traceback (most recent call last):
  File "D:\Desktop\Python-learning\【Python 第一弹】\EP02：【Python 第一弹】复杂数据类型\复杂数据类型\03_dict.py", line 22, in <module>
    print(student2['sex'])
          ~~~~~~~~^^^^^^^
KeyError: 'sex'
杜甫
20
404
```
### 2.2.3 修改字典
- 通过键（Key）来修改字典的值

```python
student3 = {
    'name': "苏轼",
    'age': 25,
}
print(student3['age'])
student3['age'] = 18
print(student3['age'])
```
- 运行结果：
```
25
18
```
### 2.2.4 添加字典值
- 如果键（Key）不存在，可以通过键值对（Key-Value）直接添加

```python
student4 = {
    'name': "王维",
    'age': 18,
}
print(student4)
student4['sex'] = '男'
print(student4)
```
- 运行结果：
```
{'name': '王维', 'age': 18}
{'name': '王维', 'age': 18, 'sex': '男'}
```
### 2.2.5 删除字典值
- 使用 `del` 或者 `pop()` 删除字典元素
- `popitem()` 按照插入顺序删除，旧版本3.7以前是随机删除并返回一个元素
- `clear()` 清空字典

```python
student5 = {
    'name': "李贺",
    'age': "20",
    'sex': "男",
    'hobby': "唱歌",
    'work': "《李凭箜篌引》"
}
print(student5)
del student5['age']
print(student5)
sex = student5.pop('sex')
print(student5)
print(sex)
student5.clear()
print(student5)
```
- 运行结果：
```
{'name': '李贺', 'age': '20', 'sex': '男', 'hobby': '唱歌', 'work': '《李凭箜篌引》'}
{'name': '李贺', 'sex': '男', 'hobby': '唱歌', 'work': '《李凭箜篌引》'}
{'name': '李贺', 'hobby': '唱歌', 'work': '《李凭箜篌引》'}
男
{}
```
## 2.3 常用方法
| 方法名       | 功能描述                                                                 | 特点                                                                 | 示例代码                                                                                     | 输出结果                                                                 |
|--------------|--------------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `keys()`     | 返回字典中所有键组成的视图对象                                           | 1. 视图对象随字典动态更新（字典修改后，视图同步变化）<br>2. 非列表类型，可通过`list()`转换为列表 | ```python<br>my_dict = {"name": "张三", "age": 25}<br>keys = my_dict.keys()<br>print(keys)<br>my_dict["gender"] = "男"<br>print(keys)<br>print(list(keys))<br>```| ```<br>dict_keys(['name', 'age'])<br>dict_keys(['name', 'age', 'gender'])<br>['name', 'age', 'gender']<br>```|
| `values()`   | 返回字典中所有值组成的视图对象                                           | 1. 视图对象随字典动态更新<br>2. 非列表类型，支持`list()`转换           | ```python<br>my_dict = {"name": "张三", "age": 25}<br>values = my_dict.values()<br>print(values)<br>my_dict["age"] = 26<br>print(values)<br>```| ```<br>dict_values(['张三', 25])<br>dict_values(['张三', 26])<br>```|
| `items()`    | 返回字典中所有键值对组成的视图对象（每个元素为`(键, 值)`元组）            | 1. 视图对象随字典动态更新（增删改键值对时同步变化）<br>2. 非列表类型，可转换为元组列表 | ```python<br>my_dict = {"name": "张三", "age": 25}<br>items = my_dict.items()<br>print(items)<br>del my_dict["age"]<br>print(items)<br>```| ```<br>dict_items([('name', '张三'), ('age', 25)])<br>dict_items([('name', '张三')])<br>```|
| `update()`   | 用另一个字典（或可迭代的键值对序列）更新当前字典，存在的键覆盖值，不存在的键新增 | 1. 直接修改原字典，无返回值<br>2. 支持传入字典、元组列表等可迭代对象   | ```python<br>my_dict = {"name": "张三", "age": 25}<br>my_dict.update({"age": 26, "city": "北京"})<br>print(my_dict)<br>my_dict.update([("gender", "男"), ("age", 27)])<br>print(my_dict)<br>```| ```<br>{'name': '张三', 'age': 26, 'city': '北京'}<br>{'name': '张三', 'age': 27, 'city': '北京', 'gender': '男'}<br>```|
## 2.4 字典推导式
### 2.4.1 基础用法
- 将两个列表分别作为键和值的来源，快速创建字典

```python
keys = ['name', 'age', 'city']
values = ['Alice', 30, 'New York']
person = {keys[i]: values[i] for i in range(len(keys))}
print(person)
```
- 运行结果：
```
{'name': 'Alice', 'age': 30, 'city': 'New York'}
```
### 2.4.2 条件过滤
- 筛选符合条件的键值对

```python
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares)
```
- 运行结果：
```
{2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
```
### 2.4.3 转换现有字典
- 对现有字典的键或值进行处理，生成新字典

```python
original = {'a': 'apple', 'b': 'banana', 'c': 'cherry'}
upper_dict = {k: v.upper() for k, v in original.items()}
print(upper_dict)
```
- 运行结果：
```
{'a': 'APPLE', 'b': 'BANANA', 'c': 'CHERRY'}
```
### 2.4.4 交换键值对
- 将现有字典的键和值互换

```python
original = {'name': 'Alice', 'age': '30'}
swapped = {v: k for k, v in original.items()}
print(swapped)
```
- 运行结果：
```
{'Alice': 'name', '30': 'age'}
```
### 2.4.5 处理字符串
- 生成字符计数字典

```python
text = 'hello world'
char_count = {char: text.count(char) for char in text if char != ' '}
print(char_count)
```
- 运行结果：
```
{'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
```
# 三、元组类型
## 3.1 定义
- 元组是一个不可变的序列类型，用于存储一系列按特定顺序排列的元素
- 元组一旦创建，其中的内容就不能被修改，即不能添加、删除或更改元组中的元素
## 3.2 特点
- **不可变性**：元组一旦创建，其元素就不能被修改
- **有序性**：元组中的元素按照定义的顺序进行排列
- **可索引**：和列表一样，元组也可以通过索引访问元素
- **可切片**：可以使用切片操作获取元组中的一部分元素
## 3.3 常见操作
### 3.3.1 拼接

```python
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
sum_tuple = tuple1 + tuple2
print(sum_tuple)
```
- 运行结果：
```
(1, 2, 3, 'a', 'b', 'c')
```
### 3.3.2 重复

```python
tuple3 = ('a', 'b', 'c')
repeat_tuple = tuple3*3
print(repeat_tuple)
```
- 运行结果：
```
('a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c')
```
### 3.3.3 判断存在

```python
tuple4 = ('a', 'b', 'c')
print(3 in tuple4)
print('a' in tuple4)
```
- 运行结果：
```
False
True
```
### 3.3.4 计算长度

```python
tuple5 = (1, 2, 3, 4, 5)
print(len(tuple5))
```
- 运行结果：
```
5
```
### 3.3.5 解包

```python
tuple6 = (1, 2, 3)
a, b, c = tuple6
print(a, b, c)
```
- 运行结果：
```
1 2 3
```
### 3.3.6 判断相同

```python
tuple7 = (1, 2)
tuple8 = (1, 2)
tuple9 = (2, 1)
print(tuple7 == tuple8)
print(tuple7 == tuple9)
```
- 运行结果：
```
True
False
```
### 3.3.7 重新赋值

```python
tuple10 = (1, 2, 3)
tuple11 = tuple10 + (4, 5)
print(tuple11)
```
- 运行结果：
```
(1, 2, 3, 4, 5)
```
### 3.3.8 作为字典键

```python
dict1 = {(1, 2): "a", (2, 3): "b"}
print(dict1[(2, 3)])
```
- 运行结果：
```
b
```
## 3.4 常用方法
| 方法名       | 功能描述                                                                 | 特点                                                                 | 示例代码                                                                                     | 输出结果                                                                 |
|--------------|--------------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `count(value)` | 返回元组中指定值`value`出现的总次数                                      | 1. 若值不存在，返回0<br>2. 支持任意可比较的数据类型（如数字、字符串、元组等） | ```python<br>tuple1 = (10, 20, 10, 'hello', 10, 'hello')<br># 统计整数10出现的次数<br>print(tuple1.count(10))  # 输出：3<br># 统计字符串'hello'出现的次数<br>print(tuple1.count('hello'))  # 输出：2<br># 统计不存在的值（如30）<br>print(tuple1.count(30))  # 输出：0<br>```| ```<br>3<br>2<br>0<br>```|
| `index(value)` | 返回指定值`value`在元组中**首次出现**的索引；若值不存在，抛出`ValueError`异常 | 1. 仅返回第一个匹配项的索引<br>2. 支持指定搜索范围（通过`start`和`end`参数） | ```python<br>tuple2 = ('a', 'b', 'c', 'b', 'd')<br># 查找'b'首次出现的索引<br>print(tuple2.index('b'))  # 输出：1<br># 从索引2开始搜索（范围：[2, 末尾]）<br>print(tuple2.index('b', 2))  # 输出：3<br># 在索引1到4之间搜索（范围：[1, 4)，即索引1、2、3）<br>print(tuple2.index('c', 1, 4))  # 输出：2<br># 查找不存在的值（如'x'）<br>print(tuple2.index('x'))  # 抛出ValueError: tuple.index(x): x not in tuple<br>```| ```<br>1<br>3<br>2<br>```|

# 四、集合类型
## 4.1 定义
- 集合是一个无序且不包含重复元素的数据类型
## 4.2 特点
- **无序性**：集合中的元素没有特定的顺序
- **互异性**：集合中的元素是唯一的，不重复
## 4.3 常见操作
### 4.3.1 创建

| 创建方式         | 说明                                                                 | 示例代码                                                                 | 输出结果                 |
|------------------|----------------------------------------------------------------------|--------------------------------------------------------------------------|--------------------------|
| 大括号`{}`       | 直接列举元素，**不可用于创建空集合**（空大括号`{}`表示空字典）       | `set1 = {1, 2, 3, 2}`<br>`print(set1)`                                   | `{1, 2, 3}`（自动去重）  |
| `set()`函数      | 接收可迭代对象（如列表、元组），适合创建空集合或从其他序列转换       | `set2 = set([1, 2, 2, 3])`<br>`empty_set = set()`<br>`print(set2, empty_set)` | `{1, 2, 3} set()`        |
### 4.3.2 增删改查

| 操作类型       | 方法/函数                | 说明                                                                 | 示例代码                                                                                     | 输出结果                 |
|----------------|--------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------------------------------|--------------------------|
| **添加元素**   | `add(value)`             | 向集合中添加单个元素，若元素已存在则不生效                           | `set1 = {1, 2, 3}`<br>`set1.add(4)`<br>`set1.add(2)`（重复元素，无变化）<br>`print(set1)`     | `{1, 2, 3, 4}`           |
|                | `update(iterable)`       | 向集合中添加多个元素（接收可迭代对象，如列表、元组）                 | `set1.update([5, 6])`<br>`print(set1)`                                                       | `{1, 2, 3, 4, 5, 6}`     |
| **删除元素**   | `remove(value)`          | 删除指定元素，若元素不存在则抛出`KeyError`                           | `set1.remove(3)`<br>`print(set1)`                                                             | `{1, 2, 4, 5, 6}`        |
|                | `discard(value)`         | 删除指定元素，若元素不存在则**不报错**（推荐用于不确定元素是否存在的场景） | `set1.discard(5)`<br>`set1.discard(10)`（元素不存在，无变化）<br>`print(set1)`               | `{1, 2, 4, 6}`           |
|                | `pop()`                  | 随机删除并返回集合中的一个元素（集合为空时抛出`KeyError`）             | `removed = set1.pop()`<br>`print(removed, set1)`  # 假设删除1                                 | `1 {2, 4, 6}`            |
| **判断存在性** | `in`关键字               | 判断元素是否在集合中，返回布尔值                                     | `print(2 in set1)`<br>`print(10 in set1)`                                                    | `True`<br>`False`         |
| **获取长度**   | `len()`函数              | 返回集合中元素的个数                                                 | `print(len(set1))`                                                                           | `3`（此时set1为{2,4,6}） |
### 4.3.3 集合运算

| 运算类型   | 运算符 | 对应方法         | 含义                                                                 | 示例代码                | 输出结果               |
|------------|--------|------------------|----------------------------------------------------------------------|-------------------------|------------------------|
| 交集       | `&`    | `intersection()` | 两个集合中**共同存在**的元素                                         | `print(set1 & set2)`<br>`print(set1.intersection(set2))` | `{3, 4}`               |
| 并集       | `|`    | `union()`        | 两个集合中**所有元素**（合并去重）                                   | `print(set1 | set2)`<br>`print(set1.union(set2))`        | `{1, 2, 3, 4, 5, 6}`   |
| 差集       | `-`    | `difference()`   | 属于第一个集合但**不属于第二个集合**的元素                           | `print(set1 - set2)`<br>`print(set1.difference(set2))`   | `{1, 2}`               |
| 对称差集   | `^`    | `symmetric_difference()` | 两个集合中**不同时存在**的元素（并集减去交集）                       | `print(set1 ^ set2)`<br>`print(set1.symmetric_difference(set2))` | `{1, 2, 5, 6}` |

## 4.4 常用方法

| 方法名    | 功能描述                                                                 | 特点                                                                 | 示例代码                                                                                     | 输出结果                     |
|-----------|--------------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------------------------------|------------------------------|
| `clear()` | 清空集合中所有元素，使集合变为空集（`set()`）                             | 1. 直接修改原集合，无返回值<br>2. 清空后集合仍存在（类型为`set`）     | ```python<br>set1 = {1, 2, 3, 4}<br>print("清空前：", set1)  # 输出：清空前：{1, 2, 3, 4}<br>set1.clear()<br>print("清空后：", set1)  # 输出：清空后：set()<br>print("类型：", type(set1))  # 输出：类型：<class 'set'><br>```| ```<br>清空前：{1, 2, 3, 4}<br>清空后：set()<br>类型：<class 'set'><br>```|
| `copy()`  | 创建并返回原集合的浅拷贝（新集合与原集合元素相同，但内存地址不同）         | 1. 返回新集合，不修改原集合<br>2. 浅拷贝意味着：若集合包含可变元素（如列表），新集合与原集合共享该元素的引用 | ```python<br>original = {1, 2, (3, 4)}  # 包含不可变元素（元组）<br>copy_set = original.copy()<br>print("原集合：", original, id(original))<br>print("拷贝集合：", copy_set, id(copy_set))  # id不同，说明是不同对象<br><br># 验证修改原集合不影响拷贝集合<br>original.add(5)<br>print("原集合添加元素后：", original)<br>print("拷贝集合：", copy_set)<br>```| ```<br>原集合：{1, 2, (3, 4)} 140704234567840<br>拷贝集合：{1, 2, (3, 4)} 140704234568192<br>原集合添加元素后：{1, 2, 5, (3, 4)}<br>拷贝集合：{1, 2, (3, 4)}<br>```|

-----
==微语录：闭上眼睛，好好回想之前的努力，自信会喷涌而出。——《放学后》==
