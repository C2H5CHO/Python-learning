"""
calculator_ 模块
"""

# 定义变量
PI = 3.1415926

# 定义函数
def add(a, b):
    """返回两个数的和"""
    return a + b

def multiply(a, b):
    """返回两个数的积"""
    return a * b

# 定义类
class Circle:
    """圆的类，计算周长和面积"""

    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        """计算周长"""
        return 2 * PI * self.radius

    def area(self):
        """计算面积"""
        return PI * self.radius ** 2

# 模块内的可执行代码（导入模块时会执行）
if __name__ == "__main__":
    # 仅在当前模块作为主程序运行时执行（测试代码）
    print("模块自测：")
    print(add(2, 3))
    print(Circle(2).area())