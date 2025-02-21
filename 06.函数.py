# 1、函数的定义及调用
# 1.1 为什么要用函数
# （1）提高代码复用性--封装
# （2）将复杂大问题分解成一系列小问题，分而治之--模块化
# （3）利于代码的维护和管理

# 1.1.1 顺序式
n = 5
res = 1
for i in range(1, n+1):
    res *= i
print(res)
# 输出：120

# 1.1.2 抽象成函数
def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

print(factorial(5))
# 输出：120

# 1.2 函数的定义及调用
# 白箱子--输入-->处理-->输出
# 三要素：参数、函数体、返回值

# 1.2.1 定义
# 模板--def 函数名(参数):
#           函数体
#           return 返回值

def area_of_square(n):
    area = pow(n, 2)
    return area

# 1.2.2 调用
# 模板--函数名(参数)

area = area_of_square(5)
print(area)
# 输出：25

# 1.3 参数传递
# 1.3.1 形参和实参
# - 形参：函数定义时的参数，本质上是变量名
# - 实参：函数调用时的参数，本质上是变量值

# 1.3.2 位置参数
# （1）要求：严格按照位置顺序，用实参对形参进行赋值
# （2）适用：通常在参数比较少时
# （3）注意：实参与形参个数必须一一对应，不多不少

def function(x, y, z):
    print(x, y, z)

function(1, 2, 3)
# 输出：1 2 3
# function(1, 2, 3, 4)
# 输出：TypeError: function() takes 3 positional arguments but 4 were given

# 1.3.3 关键字参数
# （1）模板：形参名=实参值
# （2）适用：通常在参数比较多时
# （3）要求：实参与形参个数必须一一对应
def function(x, y, z):
    print(x, y, z)

function(x=1, z=2, y=3)
# 输出：1 3 2

# （4）位置参数可以与关键字参数混用，但是，位置参数必须在关键字参数之前
function(1, z=2, y=3)
# 输出：1 3 2
# function(x=1, 2, z=3)
# 输出：SyntaxError: positional argument follows keyword argument

# （5）不能为同一个形参重复传值
# function(1, z=2, x=3)
# 输出：TypeError: function() got multiple values for argument 'x'

# 1.3.4 默认参数



