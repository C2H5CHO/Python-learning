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