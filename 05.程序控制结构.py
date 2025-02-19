# 1、条件测试
# 1.1 比较运算
a = 10
b = 6
print(a > b)
# 输出：True
print(a < b)
# 输出：False
print(a >= b)
# 输出：True
print(a <= b)
# 输出：False
print(a == b)
# 输出：False
print(a != b)
# 输出：True

# 非空
lst = [3]
if lst:
    print("非空")
else:
    print("空的")
# 输出：非空

# 1.2 逻辑运算
# 1.2.1 与、或、非
a = 12
b = 8
c = 24
print((a > b) and (b > c))  # 与
# 输出：False
print((a > b) or (b > c))  # 非
# 输出：True
print(not (a > b))  # 非
# 输出：False

# 1.2.2 优先级
# 非 > 与 > 或
print(True or True and False)
# 输出：True
print((True or True) and False)
# 输出：False

# 1.3 存在运算
# 1.3.1 元素 in 列表/字符串
cars = ['Ford', 'Volvo', 'Mercedes']
print("BMW" in cars)
# 输出：False
print("Ford" in cars)
# 输出：True

# 1.3.2 元素 not in 列表/字符串
print("Volvo" not in cars)
# 输出：False
print("BENZ" not in cars)
# 输出：True

# 2、分支结构--if语句
# 2.1 单分支
# 模板--if 条件:
#           缩进的代码块
age = 8
if age > 6:
    print("可以入学了！")
# 输出：可以入学了！

# 2.2 二分支
# 模板--if 条件:
#           缩进的代码块
#      else:
#           缩进的代码块
age = 2
if age > 6:
    print("可以入学了！")
else:
    print("不可以入学。")
# 输出：不可以入学。

# 2.2.3 多分支
# 模板--if 条件:
#           缩进的代码块
#      elif 条件:
#           缩进的代码块
#      elif 条件:
#           缩进的代码块
#      else:
#           缩进的代码块
age = 20
if age < 6:
    print("再玩两年泥巴。")
elif age < 24:
    print("好好上学！")
elif age < 65:
    print("好好工作！")
else:
    print("享受退休生活。")
# 输出：好好上学！

# 2.2.4 嵌套语句
# 题目：年满18周岁，在非公共场合可抽烟，判断某种情形下是否可以抽烟
"""
age = eval(input("请输入您的年龄："))
if age < 18:
    print("抽烟有害健康！")
else:
    is_public = bool(eval(input("若在公共场合请输1，反之输0：")))
    print(is_public)
    if not is_public:
        print("可以抽烟")
    else:
        print("公共场合禁止抽烟！")
"""

# 3、遍历循环--for循环
# 主要形式--for 元素 in 可迭代对象:
#              执行语句
# 执行过程：从可迭代对象中，依次取出每一个元素，并执行相应操作
# 1.直接迭代--列表[]，元组()，集合{}，字符串""
students = ("张三", "李四", "赵五")
for student in students:
    print("welcome，" + student)
# 输出：welcome，张三
#      welcome，李四
#      welcome，赵五

# 2.变换迭代--字典{}
students = {2025: "小雪", 2024: "小明", 2023: "小强"}
for k, v in students.items():
    print(k, v)
# 输出：2025 小雪
#      2024 小明
#      2023 小强
for student in students.keys():
    print(student)
# 输出：2025
#      2024
#      2023

# 3.range()
lst = []
for i in range(10):
    lst.append(i**2)
print(lst[:-5])
# 输出：[0, 1, 4, 9, 16]
print(lst[-1])
# 输出：81

lst1 = []
for i in range(1, 20, 2):
    lst1.append(i**2)
print(lst1)
# 输出：[1, 9, 25, 49, 81, 121, 169, 225, 289, 361]

# 循环控制--break  continue
products = [89, 90, 99, 70, 66, 100, 88, 72]
i = 0
for product in products:
    if product < 80:
        i += 1
    if i == 2:
        print("产品抽检不合格")
        break
# 输出：产品抽检不合格

for j in range(len(products)):
    if products[j] >= 80:
        continue
    print(f"第{j}个产品，分数为{products[j]}，不合格")
# 输出：第3个产品，分数为70，不合格
#      第4个产品，分数为66，不合格
#      第7个产品，分数为72，不合格

# for 与 else 的结合
i = 0
for product in products:
    if product < 60:
        i += 1
    if i == 2:
        print("产品抽检不合格")
        break
else:
    print("产品抽检合格")
# 输出：
# 若for循环全部执行完毕，没有被break终止，则运行else模块

# 4、无限循环--while循环
# 4.1 while循环的用途
# 题目：猜数字
number = 18







