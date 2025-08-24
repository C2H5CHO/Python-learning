# 一、定义
&emsp;&emsp;函数指将一组语句的集合通过一个变量名封装起来，调用这个函数变量名，就可以执行函数。
# 二、特点
- 减少重复逻辑代码的编写
- 将程序中的逻辑可以进行扩展
- 维护项目程序的代码更简单
# 三、创建

```python
def 函数名():
	逻辑代码1
	逻辑代码2
	return 结果
函数名()
```
## 代码实操——求和函数
```python
def sum(a, b):
    res = a + b
    return res
print(sum(1, 2))
print(sum(3, 4))
```
- 运行结果：
```
3
7
```
# 四、参数
## 4.1 形参
### 4.1.1 定义
- 在函数定义时声明的参数，用于接收调用时传递的值
- 形参是函数内部的变量名，描述了函数需要的输入类型和数量
### 4.1.2 代码实操——求积函数

```python
def oblong_area(l, w):
    area = l * w
    return area

print(oblong_area(10, 20))
```
`l`、`w`是形参

- 运行结果：
```
200
```
## 4.2 实参
### 4.2.1 定义
函数调用时传递给形参的实际值，可以是常量、变量、表达式或其他函数的返回值。
### 4.2.2 代码实操——求长方形的面积

```python
def oblong_area(l, w):
    area = l * w
    return area

width = 5
length = 10
print(oblong_area(width, length))
print(oblong_area(3 + 2, length))
```
`width`、`length`、`3 + 2`是实参

- 运行结果：
```
50
50
```
## 4.3 默认参数
### 4.3.1 定义
在函数定义时为参数指定默认值，调用时可以省略该参数。
### 4.3.2 规则
默认参数必须放在普通参数之后。
### 4.3.3 特点
默认参数使函数调用更加灵活，可以减少重复传值。
### 4.3.4 代码实操——求积函数(2)

```python
def oblong_area(w, l=10):
    area = l * w
    return area

print(oblong_area(20))
print(oblong_area(20, 5))
```
`l=10`是默认参数

- 运行结果：
```
200
100
```
## 4.4 关键参数
### 4.4.1 定义
通过参数名指定传递的值，允许不按形参顺序传参。
### 4.4.2 规则
关键参数必须放在位置参数（按顺序传递的参数）之后。
### 4.4.3 特点
关键参数提高了代码可读性，尤其适用于参数较多的函数。
### 4.4.4 代码实操——计算长方体的体积

```python
def cuboid_volume(w, h, l=10):
    volume = l * w * h
    return volume

print(cuboid_volume(10, h=3, l=20))
print(cuboid_volume(h=3, w=10, l=20))
print(cuboid_volume(l=20, 10, 3))
```
`h=3`、`l=20`、`w=10`是关键参数

- 运行结果：
```
  File "D:\Desktop\Python-learning\【Python 第一弹】\EP04：【Python 第一弹】函数编程\函数编程\02_参数.py", line 37
    print(cuboid_volume(l=20, 10, 3))
                                   ^
SyntaxError: positional argument follows keyword argument
600
600
```
## 4.5 可变参数
### 4.5.1 `*args`——接收任意数量的位置参数
1. 定义：收集所有未匹配的位置参数，组成一个元组。
2. 特点：通常用于处理不确定数量的额外参数。
#### 代码实操——学生信息

```python
def get_info(name, age, *args):
    print(f"姓名: {name}, 年龄: {age}, 其他信息: {args}")

get_info('老王', 48, '洗脚', '按摩')
get_info('老李', 30)
```
- 运行结果：
```
姓名: 老王, 年龄: 48, 其他信息: ('洗脚', '按摩')
姓名: 老李, 年龄: 30, 其他信息: ()
```
### 4.5.2 `**kwargs`——接收任意数量的关键字参数
1. 定义：收集所有未匹配的关键字参数，组成一个字典。
2. 特点：通常用于处理不确定数量的键值对参数。
#### 代码实操——学生信息(2)

```python
def get_info(name, age, **kwargs):
    print(f"姓名: {name}, 年龄: {age}, 爱好: {kwargs}")

get_info('老王', 48, hobby1='洗脚', hobby2='按摩')
get_info('老李', 30, job='工程师', city='北京')
```
- 运行结果：
```
姓名: 老王, 年龄: 48, 爱好: {'hobby1': '洗脚', 'hobby2': '按摩'}
姓名: 老李, 年龄: 30, 爱好: {'job': '工程师', 'city': '北京'}
```
## 4.6 代码实操——混合使用

```python
def func(a, b, *args, c=10, **kwargs):
    print(f"a: {a}, b: {b}, args: {args}, c: {c}, kwargs: {kwargs}")

func(1, 2, 3, 4, c=20, d=5, e=6)
```
规则：普通参数 → `*args` → 默认参数 → `**kwargs`

- 运行结果：
```
a: 1, b: 2, args: (3, 4), c: 20, kwargs: {'d': 5, 'e': 6}
```
# 五、变量
## 5.1 全局变量
### 5.1.1 定义
在函数外部定义的变量，作用域覆盖整个程序（除函数内部的同名局部变量作用域外），在程序运行期间始终存在。
### 5.1.2 特点
- 可以被程序中的任何函数、代码块访问（除非被局部变量遮蔽）
- 函数内部操作全局变量：
	- **仅访问全局变量**：无需声明，直接使用即可
	- **修改全局变量**：必须用`global`关键字声明，否则 Python 会将其视为局部变量
### 5.1.3 代码实操

```python
global_var = "全局的变量"

def print_global_var():
    print(global_var)

print_global_var()
print(global_var)
```
- 运行结果：
```
全局的变量
全局的变量
```
## 5.2 局部变量
### 5.2.1 定义
在函数内部定义的变量，作用域仅限于该函数内部，函数调用时创建，函数执行结束后自动销毁。
### 5.2.2 特点
- 仅在定义它的函数内部有效，外部无法直接访问
- 如果函数内部的局部变量与全局变量同名，函数会优先使用局部变量（局部变量遮蔽全局变量）
### 5.2.3 代码实操

```python
def print_local_var():
    local_var = '局部变量'
    print(local_var)

print_local_var()
print(local_var)
```
- 运行结果：
```
局部变量
Traceback (most recent call last):
  File "D:\Desktop\Python-learning\【Python 第一弹】\EP04：【Python 第一弹】函数编程\函数编程\03_变量.py", line 16, in <module>
    print(local_var)
          ^^^^^^^^^
NameError: name 'local_var' is not defined. Did you mean: 'global_var'?
```
# 六、内置函数
[Built-in Functions](https://docs.python.org/3/library/functions.html)
## 6.1 数学运算类
### 6.1.1 `abs(x)`
1. 功能：返回数字的绝对值。
2. 示例：
  ```python
  print(abs(-5))       # 输出: 5
  print(abs(3.14))     # 输出: 3.14
  print(abs(-3+4j))    # 输出: 5.0（复数的模）
  ```
### 6.1.2 `divmod(a, b)`
1. 功能：返回 `(a // b, a % b)` 的元组（商和余数）。
2. 示例：
  ```python
  print(divmod(10, 3))  # 输出: (3, 1)
  print(divmod(5, 2.5)) # 输出: (2.0, 0.0)
  ```
### 6.1.3 `pow(x, y[, z])`
1. 功能：返回 `x**y`，若提供`z`则计算`(x**y) % z`（更高效）
2. 示例：
  ```python
  print(pow(2, 3))      # 输出: 8（2³）
  print(pow(2, 3, 5))   # 输出: 3（8 % 5）
  ```
### 6.1.4 `round(number[, ndigits])`
1. 功能：对浮点数四舍五入，`ndigits`指定保留小数位数（默认为0）。
2. 示例：
  ```python
  print(round(3.14159))     # 输出: 3
  print(round(3.14159, 2))  # 输出: 3.14
  print(round(2.5))         # 输出: 2（银行家舍入：取最接近的偶数）
  ```
## 6.2 类型转换类
### 6.2.1 `int(x[, base])`
1. 功能：将数值或字符串转换为整数，`base`指定进制（默认为10）。
2. 示例：
  ```python
  print(int(3.9))          # 输出: 3（直接截断小数部分）
  print(int('101', 2))     # 输出: 5（二进制转十进制）
  print(int('FF', 16))     # 输出: 255（十六进制转十进制）
  ```
### 6.2.2 `float(x)`
1. 功能：将数值或字符串转换为浮点数。
2. 示例：
  ```python
  print(float(5))          # 输出: 5.0
  print(float('3.14'))     # 输出: 3.14
  ```
### 6.2.3 `str(object='')`
1. 功能：将对象转换为字符串。
2. 示例：
  ```python
  print(str(123))          # 输出: '123'
  print(str([1, 2, 3]))    # 输出: '[1, 2, 3]'
  ```
### 6.2.4 `bool(x)`
1. 功能：将对象转换为布尔值（遵循Python的真值测试规则）。
2. 示例：
  ```python
  print(bool(0))           # 输出: False
  print(bool(''))          # 输出: False
  print(bool([]))          # 输出: False
  print(bool(None))        # 输出: False
  print(bool(42))          # 输出: True
  ```
### 6.2.5 `list([iterable])`
1. 功能：将可迭代对象转换为列表。
2. 示例：
  ```python
  print(list('abc'))       # 输出: ['a', 'b', 'c']
  print(list((1, 2, 3)))   # 输出: [1, 2, 3]
  ```
### 6.2.6 `tuple([iterable])`
1. 功能：将可迭代对象转换为元组。
2. 示例：
  ```python
  print(tuple([1, 2, 3]))  # 输出: (1, 2, 3)
  print(tuple('xyz'))      # 输出: ('x', 'y', 'z')
  ```
### 6.2.7 `dict(**kwarg)` / `dict(mapping, **kwarg)` / `dict(iterable, **kwarg)`
1. 功能：创建字典。
2. 示例：
  ```python
  print(dict(a=1, b=2))    # 输出: {'a': 1, 'b': 2}
  print(dict([('x', 1), ('y', 2)]))  # 输出: {'x': 1, 'y': 2}
  ```
## 6.3 序列操作类
### 6.3.1 `len(s)`
1. 功能：返回对象的长度（元素个数）。
2. 示例：
  ```python
  print(len('hello'))      # 输出: 5
  print(len([1, 2, 3, 4])) # 输出: 4
  ```
### 6.3.2 `max(iterable[, key])` / `max(arg1, arg2, *args[, key])`
1. 功能：返回可迭代对象中的最大值，或多个参数中的最大值。`key`为可选的比较函数。
2. 示例：
  ```python
  print(max([3, 1, 4]))    # 输出: 4
  print(max(5, 2, 9))      # 输出: 9
  # 按字符串长度比较
  print(max(['apple', 'banana', 'cherry'], key=len))  # 输出: 'banana'
  ```
### 6.3.3 `min(iterable[, key])` / `min(arg1, arg2, *args[, key])`
1. 功能：返回最小值（用法同`max`）。
2. 示例：
  ```python
  print(min([3, 1, 4]))    # 输出: 1
  print(min('apple', 'banana', 'cherry', key=lambda x: x[1]))  # 输出: 'apple'（比较第二个字符）
  ```
### 6.3.4 `sum(iterable[, start])`
1. 功能：返回可迭代对象中所有元素的和，`start`为初始值（默认为0）。
2. 示例：
  ```python
  print(sum([1, 2, 3]))    # 输出: 6
  print(sum([1, 2, 3], 10)) # 输出: 16（10+1+2+3）
  ```
### 6.3.5 `sorted(iterable[, key][, reverse])`
1. 功能：返回一个新的已排序列表，原对象不变。
2. 示例：
  ```python
  print(sorted([3, 1, 4]))    # 输出: [1, 3, 4]
  print(sorted('hello', reverse=True))  # 输出: ['o', 'l', 'l', 'e', 'h']
  # 按绝对值排序
  print(sorted([-3, 1, -2], key=abs))   # 输出: [1, -2, -3]
  ```
### 6.3.6 `reversed(seq)`
1. 功能：返回一个反向迭代器。
2. 示例：
  ```python
  print(list(reversed([1, 2, 3])))  # 输出: [3, 2, 1]
  print(''.join(reversed('hello'))) # 输出: 'olleh'
  ```
## 6.4 类型检查类
### 6.4.1 `type(object)`
1. 功能：返回对象的类型。
2. 示例：
  ```python
  print(type(42))          # 输出: <class 'int'>
  print(type([1, 2]))      # 输出: <class 'list'>
  ```
### 6.4.2 `isinstance(object, classinfo)`
1. 功能：判断对象是否是某个类或子类的实例。
2. 示例：
  ```python
  print(isinstance(5, int))        # 输出: True
  print(isinstance([], (list, tuple)))  # 输出: True（判断是否属于元组中任意一个类型）
  ```
### 6.4.3 `issubclass(class, classinfo)`
1. 功能：判断类是否是另一个类或子类的子类。
2. 示例：
  ```python
  class A: pass
  class B(A): pass
  
  print(issubclass(B, A))  # 输出: True
  print(issubclass(int, object))  # 输出: True（所有类都继承自object）
  ```
## 6.5 输入输出类
### 6.5.1 `print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`
1. 功能：将对象打印到标准输出。
2. 示例：
  ```python
  print('Hello', 'World', sep='-')  # 输出: Hello-World
  print('Data', end='; ')           # 输出: Data; （不换行）
  ```
### 6.5.2 `input([prompt])`
1. 功能：从标准输入读取一行文本（返回字符串）。
2. 示例：
  ```python
  name = input("请输入你的名字：")
  print(f"你好，{name}！")
  ```
## 6.6 文件操作类
### 6.6.1 `open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)`
1. 功能：打开文件并返回文件对象。
2. 示例：
  ```python
  # 写入文件
  with open('test.txt', 'w', encoding='utf-8') as f:
      f.write('Hello\nWorld')
  
  # 读取文件
  with open('test.txt', 'r', encoding='utf-8') as f:
      content = f.read()
      print(content)
  ```
## 6.7 迭代器与生成器类
### 6.7.1 `range(start, stop[, step])`
1. 功能：返回一个不可变的整数序列（常用于循环）。
2. 示例：
  ```python
  print(list(range(5)))       # 输出: [0, 1, 2, 3, 4]
  print(list(range(1, 10, 2))) # 输出: [1, 3, 5, 7, 9]
  ```
### 6.7.2 `enumerate(iterable, start=0)`
1. 功能：返回一个枚举对象（包含索引和值的元组）。
2. 示例：
  ```python
  for i, char in enumerate('abc'):
      print(f"索引 {i}: {char}")
  # 输出:
  # 索引 0: a
  # 索引 1: b
  # 索引 2: c
  ```
### 6.7.3 `zip(*iterables)`
1. 功能：将多个可迭代对象的元素打包成元组。
2. 示例：
  ```python
  names = ['Alice', 'Bob']
  ages = [25, 30]
  print(list(zip(names, ages)))  # 输出: [('Alice', 25), ('Bob', 30)]
  
  # 解压
  zipped = zip(names, ages)
  n, a = zip(*zipped)
  print(n)  # 输出: ('Alice', 'Bob')
  ```
## 6.8 高阶函数类
### 6.8.1 `map(function, iterable, *iterables)`
1. 功能：对可迭代对象的每个元素应用函数，返回迭代器。
2. 示例：
  ```python
  nums = [1, 2, 3]
  squared = map(lambda x: x**2, nums)
  print(list(squared))  # 输出: [1, 4, 9]
  
  # 多个可迭代对象
  a = [1, 2, 3]
  b = [4, 5, 6]
  sums = map(lambda x, y: x + y, a, b)
  print(list(sums))  # 输出: [5, 7, 9]
  ```
### 6.8.2 `filter(function, iterable)`
1. 功能：过滤可迭代对象中的元素，返回符合条件的元素迭代器。
2. 示例：
  ```python
  nums = [1, 2, 3, 4, 5]
  even = filter(lambda x: x % 2 == 0, nums)
  print(list(even))  # 输出: [2, 4]
  ```
### 6.8.3 `reduce(function, iterable[, initializer])`
1. 功能：对可迭代对象的元素进行累积计算（需从`functools`导入）。
2. 示例：
  ```python
  from functools import reduce
  nums = [1, 2, 3, 4]
  product = reduce(lambda x, y: x * y, nums)
  print(product)  # 输出: 24（1×2×3×4）
  ```
## 6.9 其他常用函数
### 6.9.1 `help([object])`
1. 功能：查看对象的帮助文档（交互式环境中常用）。
2. 示例：
  ```python
  help(len)  # 查看len函数的帮助信息
  ```
### 6.9.2 `id(object)`
1. 功能：返回对象的唯一标识符（内存地址）。
2. 示例：
  ```python
  x = [1, 2, 3]
  print(id(x))  # 输出: 140123456789012（具体值因环境而异）
  ```
### 6.9.3 `dir([object])`
1. 功能：返回对象的所有属性和方法名（默认返回当前作用域的所有名称）。
2. 示例：
  ```python
  print(dir(list))  # 列出列表类的所有属性和方法
  ```
### 6.9.4 `globals()`
1. 功能：返回当前全局符号表的字典。
2. 示例：
  ```python
  x = 42
  print(globals()['x'])  # 输出: 42
  ```
### 6.9.5 `locals()`
1. 功能：返回当前局部符号表的字典。
2. 示例：
  ```python
  def test():
      y = 99
      print(locals())  # 输出: {'y': 99}
  
  test()
  ```
## 6.10 不常用但有用的函数
### 6.10.1 `eval(expression[, globals[, locals]])`
1. 功能：执行字符串表达式并返回结果。
2. 示例：
  ```python
  result = eval('2 + 3 * 4')
  print(result)  # 输出: 14
  ```
### 6.10.2 `exec(object[, globals[, locals]])`
1. 功能：执行Python代码（如字符串或代码对象）。
2. 示例：
  ```python
  code = """
  for i in range(3):
      print(i)
  """
  exec(code)  # 输出: 0 1 2
  ```
### 6.10.3 `ord(c)`
1. 功能：返回单个字符的Unicode码点。
2. 示例：
  ```python
  print(ord('A'))  # 输出: 65
  print(ord('中'))  # 输出: 20013
  ```
### 6.10.4 `chr(i)`
1. 功能：返回Unicode码点对应的字符。
2. 示例：
  ```python
  print(chr(65))   # 输出: 'A'
  print(chr(20013)) # 输出: '中'
  ```

----
==微语录：人是为了救赎自己而活着的。==
