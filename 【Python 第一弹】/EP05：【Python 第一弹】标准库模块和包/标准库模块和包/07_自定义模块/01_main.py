"""
模块与主程序在同一目录
"""

# 方式1：导入整个模块，通过"模块名.成员"访问
import calculator
print(calculator.add(5, 3))
print(calculator.PI)

# 方式2：导入模块中的特定成员，直接使用成员名
from calculator import add, Circle
print(add(10, 20))
circle = Circle(3)
print(circle.perimeter())

# 方式3：导入模块所有成员（不推荐，可能引发命名冲突）
from calculator import *
print(multiply(4, 5))