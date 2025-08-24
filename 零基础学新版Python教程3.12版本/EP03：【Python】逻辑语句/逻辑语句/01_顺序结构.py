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