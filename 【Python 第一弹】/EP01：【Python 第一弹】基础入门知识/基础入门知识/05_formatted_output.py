"""
格式化输出
"""

# 1. %s,%d,%f
name_1 = '李白'
age_1 = 18
print("我的名字是：%s，我的年龄是：%d岁。" % (name_1, age_1))

# 2. str.format()
name_2 = '杜甫'
age_2 = 20
print("你的名字是：{}，你的年龄是：{}岁。".format(name_2, age_2))

# 3. f-string
name_3 = '苏轼'
age_3 = 22
print(f"他的名字是：{name_3}，他的年龄是：{age_3}岁。")