"""
元组的常见操作
"""

# 1. 拼接
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
sum_tuple = tuple1 + tuple2
print(sum_tuple)

print('--'*50)

# 2. 重复
tuple3 = ('a', 'b', 'c')
repeat_tuple = tuple3*3
print(repeat_tuple)

print('--'*50)

# 3. 判断存在
tuple4 = ('a', 'b', 'c')
print(3 in tuple4)
print('a' in tuple4)

print('--'*50)

# 4. 计算长度
tuple5 = (1, 2, 3, 4, 5)
print(len(tuple5))

print('--'*50)

# 5. 解包
tuple6 = (1, 2, 3)
a, b, c = tuple6
print(a, b, c)

print('--'*50)

# 6. 判断相同
tuple7 = (1, 2)
tuple8 = (1, 2)
tuple9 = (2, 1)
print(tuple7 == tuple8)
print(tuple7 == tuple9)

print('--'*50)

# 7. 重新赋值
tuple10 = (1, 2, 3)
tuple11 = tuple10 + (4, 5)
print(tuple11)

print('--'*50)

# 8. 作为字典键
dict1 = {(1, 2): "a", (2, 3): "b"}
print(dict1[(2, 3)])

print('--'*50)