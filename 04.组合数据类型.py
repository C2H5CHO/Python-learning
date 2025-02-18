# 四、组合数据类型
# 4.1 列表
# 4.1.1 列表的表达
# 序列类型：内部元素有位置关系，能通过位置序号访问其中元素
# 序列特点：可以使用多种类型元素，支持元素的增删查改
lst = ["python", 2025, True, {"age": 20}]
print(lst)
# 输出：['python', 2025, True, {'age': 20}]

# 另一种方式：list(可迭代类型)
# 字符串转列表
lst1 = list("人工智能")
print(lst1)
# 输出：['人', '工', '智', '能']

# 元组转列表
lst2 = list(("我", "们", "爱", "中", "国"))
print(lst2)
# 输出：['我', '们', '爱', '中', '国']

# 集合转列表
lst3 = list({"Mike", "Jim", "Tim", "Jerry", "Tom"})
print(lst3)
# 输出：['Tom', 'Tim', 'Jerry', 'Jim', 'Mike']

# 特殊的range()
for i in [1,2,3]:
    print(i)
# 输出：1
#      2
#      3

for i in range(3):
    print(i)
# 输出：0
#      1
#      2

# range(开始数据, 结束数据, 数字间隔)
# 开始数据若为0，则可以省略
# 结束数据不得省略
# 数字间隔默认为1

for i in range(1, 11, 2):
    print(i)
# 输出：1
#      3
#      5
#      7
#      9

print(list(range(1, 11, 2)))
# 输出：[1, 3, 5, 7, 9]



















