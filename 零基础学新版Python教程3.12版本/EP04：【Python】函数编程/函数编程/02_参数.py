"""
函数的参数
"""

# 1. 形参——求积函数
def oblong_area(l, w):
    area = l * w
    return area

print(oblong_area(10, 20))

# 2. 实参——求长方形的面积
def oblong_area(l, w):
    area = l * w
    return area

width = 5
length = 10
print(oblong_area(width, length))
print(oblong_area(3 + 2, length))

# 3. 默认参数——求积函数(2)
def oblong_area(w, l=10):
    area = l * w
    return area

print(oblong_area(20))
print(oblong_area(20, 5))

# 4. 关键参数——求长方体的体积
def cuboid_volume(w, h, l=10):
    volume = l * w * h
    return volume

print(cuboid_volume(10, h=3, l=20))
print(cuboid_volume(h=3, w=10, l=20))
# print(cuboid_volume(l=20, 10, 3))

# 5. 可变参数——学生信息
def get_info(name, age, *args):
    print(f"姓名: {name}, 年龄: {age}, 其他信息: {args}")

get_info('老王', 48, '洗脚', '按摩')
get_info('老李', 30)

def get_info(name, age, **kwargs):
    print(f"姓名: {name}, 年龄: {age}, 爱好: {kwargs}")

get_info('老王', 48, hobby1='洗脚', hobby2='按摩')
get_info('老李', 30, job='工程师', city='北京')

# 6. 混合使用
def func(a, b, *args, c=10, **kwargs):
    print(f"a: {a}, b: {b}, args: {args}, c: {c}, kwargs: {kwargs}")

func(1, 2, 3, 4, c=20, d=5, e=6)