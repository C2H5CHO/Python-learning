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