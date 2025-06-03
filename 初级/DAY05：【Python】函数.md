# 1、函数的定义及调用
## 1.1 为什么需要函数
> 1. 提高代码复用性——封装
> 2. 将复杂问题分而治之——模块化
> 3. 利于代码的维护和管理
### 1.1.1 顺序式

```python
n = 5
res = 1
for i in range(1, n+1):
    res *= i
print(res)
# 输出：120
```
### 1.1.2 抽象成函数

```python
def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

print(factorial(5))
# 输出：120
```
## 1.2 函数定义及调用
> 1. 白箱子：输入，处理，输出
> 2. 三要素：参数、函数体、返回值
### 1.2.1 定义
> 模块——def 函数名(参数):
> &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;函数体
> &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;return 返回值

```python
def area_of_square(n):
    area = pow(n, 2)
    return area
```
### 1.2.2 调用
> 模块——函数名(参数)

```python
area = area_of_square(5)
print(area)
# 输出：25
```
## 1.3 参数传递
### 1.3.1 形参和实参
#### （1）形参：
> 函数定义时的参数，本质上是变量名
#### （2）实参：
> 函数调用时的参数，本质上是变量值
### 1.3.2 位置参数
> 1. 要求：严格按照位置顺序，用实参对形参进行赋值
> 2. 适用：通常在参数比较少时
> 3. 注意：实参与形参个数必须一一对应，不多不少

```python
def function(x, y, z):
    print(x, y, z)

function(1, 2, 3)
# 输出：1 2 3
function(1, 2, 3, 4)
# 输出：TypeError: function() takes 3 positional arguments but 4 were given
```
### 1.3.3 关键字参数
> 1. 模板：形参名=实参值
> 2. 适用：通常在参数比较多时
> 3. 要求：实参与形参必须一 一对应

```python
def function(x, y, z):
    print(x, y, z)

function(x=1, z=2, y=3)
# 输出：1 3 2
```
- 位置参数可以和关键字参数混用，但位置参数必须在关键字参数之前

```python
function(1, z=2, y=3)
# 输出：1 3 2
function(x=1, 2, z=3)
# 输出：SyntaxError: positional argument follows keyword argument
```
- 不能为同一个形参重复传值

```python
function(1, z=2, x=3)
# 输出：TypeError: function() got multiple values for argument 'x'
```
### 1.3.4 默认参数
> 1. 定义：默认参数是编程语言中函数定义的一种特性，它允许在声明函数时为参数指定一个默认值。如果调用函数时没有提供该参数的值，则使用默认值。
- 默认参数必须在非默认参数后面
- 调用函数时，可不对默认参数的形参传值

```python
def greet(name, message="你好, "):
    print(f"{message}{name}")

# 使用默认的message参数
greet("小李")
# 输出：你好, 小李
# 覆盖默认的message参数
greet("小张", "欢迎你, ")
# 输出：欢迎你, 小张
```
- 默认参数应设置为==不可变类型==（数字、字符串、元组）

```python
def add_item(item, my_list=[]):
    my_list.append(item)
    return my_list

print(add_item('apple'))
# 输出: ['apple']
print(add_item('banana'))
# 输出: ['apple', 'banana']

def add_item(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

print(add_item('apple'))
# 输出: ['apple']
print(add_item('banana'))
# 输出: ['banana']
```
- 参数可选

```python
def name(first_name, last_name, middle_name=None):
    if middle_name:
        return first_name + middle_name + last_name
    else:
        return first_name + last_name

print(name("王", "源"))
# 输出：王源
print(name("王", "凯", "俊"))
# 输出：王俊凯
```
### 1.3.5 可变长参数——*args和*kwargs
> 1. 定义：允许函数接受任意数量的位置参数和关键字参数
> 2. 用途：当你不确定一个函数将接收多少个参数时
#### （1）*args：
> 传递一个非键值对的可变数量的参数列表给函数。星号（*）表示将参数应该视为元组来处理

```python
def test_var_args(f_arg, *argv):
    print("第一个常规参数:", f_arg)
    print(argv)
    for arg in argv:
        print("另一个通过*args传入的参数:", arg)

test_var_args('Python', 'Rocks', 'For', 'Data', 'Science')
# 输出：第一个常规参数: Python
#      ('Rocks', 'For', 'Data', 'Science')
#      另一个通过*args传入的参数: Rocks
#      另一个通过*args传入的参数: For
#      另一个通过*args传入的参数: Data
#      另一个通过*args传入的参数: Science
```
#### （2）*kwargs：
> 允许将不定长度的键值对作为参数传递给一个函数。双星号（**）表示将参数视为字典来处理

```python
def greet_me(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

greet_me(name="小李", age=25, city="北京")
# 输出：{'name': '小李', 'age': 25, 'city': '北京'}
#      name = 小李
#      age = 25
#      city = 北京
```
## 1.4 函数体和变量作用域
> 1. 函数体：指在定义一个函数时，包含在函数声明和结束之间的所有代码块
> 2. 局部变量：在函数内部定义的变量，其作用范围仅限于定义它的函数内部，不能在函数外部被访问或修改
> 3. 全局变量：在所有函数之外定义的变量，可以在文件的任何地方被访问（包括所有函数内部）

```python
# 定义一个全局变量
global_var = "我是全局变量"

def check_scope():
    # 定义一个局部变量
    local_var = "我是局部变量"
    print(local_var)  # 可以访问局部变量
    # 输出：我是局部变量

    """
    # 访问全局变量
    print(global_var)
    # 输出：UnboundLocalError: cannot access local variable 'global_var' where it is not associated with a value
    """

    # 尝试修改全局变量的值，不使用global时会创建一个新的局部变量
    global_var = "尝试修改全局变量失败"
    print(global_var)
    # 输出：尝试修改全局变量失败

def modify_global_var():
    global global_var  # 使用global关键字声明我们要使用全局变量
    global_var = "全局变量已被修改"
    print(global_var)
    # 输出：全局变量已被修改

# 调用函数
check_scope()
print(global_var)
# 输出：我是全局变量
modify_global_var()
print(global_var)
# 输出：全局变量已被修改
"""
# 在函数外部无法访问局部变量
print(local_var)
# 输出：NameError: name 'local_var' is not defined. Did you mean: 'global_var'?
"""
```
## 1.5 返回值
### 1.5.1 单个返回值

```python
def function(x):
    return x**3

res = function(2)
print(res)
# 输出：8
```
### 1.5.2 多个返回值

```python
def function1(x):
    return x, x**2, x**3

print(function1(2))
# 输出：(2, 4, 8)
a, b, c = function1(3)
print(a, b, c)
# 输出：3 9 27
```
### 1.5.3 多个return语句（只执行其中一个）

```python
def function2(x):
    if x in ['Sunday', 'Saturday']:
        return "weekend"
    else:
        return "weekday"

    print("这一句根本没有机会不执行")

print(function2('Saturday'))
# 输出：weekend
print(function2('Monday'))
# 输出：weekday
```
### 1.5.4 没有return语句（返回值为None）

```python
def function3(x):
    print("没有返回值")

print(function3(1))
# 输出：没有返回值
#      None
```
# 2、匿名函数
## 2.1 基本形式
> lambda 变量:
> &emsp;&emsp;函数体
## 2.2 常见用法
### 2.2.1 排序——sort()/sorted()

```python
ls = [(98, 88), (78, 99), (86, 74), (90, 90), (78, 96)]
ls.sort()  # 基于每个元组的第一个元素进行排序
print(ls)
# 输出：[(78, 96), (78, 99), (86, 74), (90, 90), (98, 88)]

ls.sort(key=lambda x: x[1])  # 基于每个元组的第二个元素进行排序
print(ls)
# 输出：[(86, 74), (98, 88), (90, 90), (78, 96), (78, 99)]

ls1 = sorted(ls, key=lambda x: x[1]+x[0], reverse=True)
print(ls1)
# 输出：[(98, 88), (90, 90), (78, 99), (78, 96), (86, 74)]
```
### 2.2.2 最值——max()/min()

```python
ls2 = max(ls, key=lambda x: x[1])
print(ls2)
# 输出：(78, 99)

ls3 = min(ls, key=lambda x: x[1])
print(ls3)
# 输出：(86, 74)
```
# 3、面向过程和面向对象
## 3.1 面向过程
### 3.1.1 定义
> 一种编程范式，通过一系列的过程或函数来组织代码
### 3.1.2 关注
> ==“怎么做”==，即如何一步步地解决问题
### 3.1.3 特点
#### （1）流程控制：
> 程序由一系列顺序执行的语句组成，包括条件判断、循环等
#### （2）模块化：
> 将代码分解为多个函数或过程，每个函数或过程负责完成一个特定的任务
#### （3）数据与操作分离：
> 数据和对数据的操作通常是分开定义的。函数接收数据作为参数，处理后可能返回结果
#### （4）易于理解和实现：
> 对于简单的任务或者逻辑较为直接的问题，面向过程的方法通常更加直观易懂

```python
def calculate_area(radius):
    pi = 3.14159
    return pi * (radius**2)

def main():
    r = 5
    area = calculate_area(r)
    print("半径为", r, "的圆的面积为:", area)

main()
# 输出：半径为 5 的圆的面积为: 78.53975
```
## 3.2 面向对象
### 3.2.1 定义
> 一种基于“对象”概念的编程范式，对象可以包含数据（属性）和方法（行为）
### 3.2.2 关注
> ==“是什么”==，即把问题分解成一组相互关联的对象，每个对象都是某个类的实例
### 3.2.3 特点
#### （1）封装：
> 将数据和操作数据的方法捆绑在一起，隐藏内部状态，并要求所有交互都通过对象的公开接口进行
#### （2）继承：
> 一个类可以从另一个类继承属性和方法，这促进了代码重用并允许创建层次结构
#### （3）多态：
> 允许子类提供其父类方法的不同实现，使得同一类型的对象可以以不同的方式响应相同的方法调用
#### （4）抽象：
> 简化复杂性的一种策略，通过隐藏具体的实现细节，只暴露必要的功能给用户

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        pi = 3.14159
        return pi * (self.radius ** 2)

def main():
    c = Circle(5)
    print("半径为", c.radius, "的圆的面积为:", c.calculate_area())

main()
# 输出：半径为 5 的圆的面积为: 78.53975
```
## 3.3 区别
### 3.3.1 设计理念
> 面向过程编程注重算法的设计，而面向对象编程更关心数据结构的设计及其上的操作
### 3.3.2 扩展性
> 由于封装、继承和多态的存在，面向对象编程更容易扩展和维护，特别是在大型项目中
### 3.3.3 复用性
> 面向对象编程通过类和继承机制提高了代码的复用性，减少了重复代码
### 3.3.4 适用场景
> 面向过程编程适合解决小规模、线性的任务；面向对象编程更适合于构建大型、复杂的软件系统，尤其是那些需要长期维护和发展的情况
---
`微语录：万物皆有裂痕，那是光照进来的地方。`

