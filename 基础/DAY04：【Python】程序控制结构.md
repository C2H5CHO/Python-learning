# 1、条件测试
## 1.1 比较运算

```python
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
```
- 非空

```python
lst = [3]
if lst:
    print("非空")
else:
    print("空的")
# 输出：非空
```
## 1.2 逻辑运算
### 1.2.1 与、或、非

```python
a = 12
b = 8
c = 24
print((a > b) and (b > c))  # 与
# 输出：False
print((a > b) or (b > c))  # 非
# 输出：True
print(not (a > b))  # 非
# 输出：False
```
### 1.2.2 优先级
- 非 > 与 > 或

```python
print(True or True and False)
# 输出：True
print((True or True) and False)
# 输出：False
```
## 1.3 存在运算
### 1.3.1 元素 in 列表/字符串

```python
cars = ['Ford', 'Volvo', 'Mercedes']
print("BMW" in cars)
# 输出：False
print("Ford" in cars)
# 输出：True
```
### 1.3.2 元素 not in 列表/字符串

```python
print("Volvo" not in cars)
# 输出：False
print("BENZ" not in cars)
# 输出：True
```
# 2、分支结构——if语句
## 2.1  单分支
> 模板：if 条件:
> &emsp;&emsp;&emsp;&emsp;&emsp;缩进的代码块

```python
age = 8
if age > 6:
    print("可以入学了！")
# 输出：可以入学了！
```
## 2.2 二分支
> 模板：if 条件:
> &emsp;&emsp;&emsp;&emsp;&emsp;缩进的代码块
> &emsp;&emsp;&emsp;else:
> &emsp;&emsp;&emsp;&emsp;&emsp;缩进的代码块

```python
age = 2
if age > 6:
    print("可以入学了！")
else:
    print("不可以入学。")
# 输出：不可以入学。
```
## 2.3 多分支
> 模板：if 条件:
> &emsp;&emsp;&emsp;&emsp;&emsp;缩进的代码块
> &emsp;&emsp;&emsp;elif 条件:
> &emsp;&emsp;&emsp;&emsp;&emsp;缩进的代码块
> &emsp;&emsp;&emsp;elif 条件:
> &emsp;&emsp;&emsp;&emsp;&emsp;缩进的代码块
> &emsp;&emsp;&emsp;else:
> &emsp;&emsp;&emsp;&emsp;&emsp;缩进的代码块

```python
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
```
## 2.4 嵌套语句
- 题目：年满18岁，在非公共场合可抽烟，判断某种情形下是否可以抽烟

```python
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
```
# 3、遍历循环——for循环
## 3.1 主要形式
> for 元素 in 可迭代对象:
> &emsp;&emsp;执行语句
## 3.2 执行过程
> 可迭代对象中，依次取出每一个元素，并执行相应操作
### 3.2.1 直接迭代——列表[]、元组()、集合{}，字符串""

```python
students = ("张三", "李四", "赵五")
for student in students:
    print("welcome，" + student)
# 输出：welcome，张三
#      welcome，李四
#      welcome，赵五
```
### 3.2.2 变换迭代——字典{}

```python
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
```
### 3.2.3 range()

```python
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
```
## 3.3 循环控制——break、continue

```python
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
```
## 3.4 for与else的结合

```python
i = 0
for product in products:
    if product < 60:
        i += 1
    if i == 2:
        print("产品抽检不合格")
        break
else:
    print("产品抽检合格")
```
> 若for循环全部执行完毕，没有被break终止，则运行else模块
# 4、无限循环——while循环
## 4.1 while的用途
> 若用if语句，代码需要重复执行，但又**不清楚具体需要执行的次数**，故引入while循环
## 4.2 while的一般形式
> 模板：while 判断条件:
> &emsp;&emsp;&emsp;&emsp;&emsp;条件为真，执行语句
> &emsp;&emsp;&emsp;&emsp;&emsp;条件为假，结束循环
- 经典题目：猜数字

```python
number = 18
guess = int(input("请输入正整数："))
while guess != number:
    if guess < number:
        print("猜小了...")
    elif guess > number:
        print("猜大了...")
    guess = int(input(">>："))
print("Congratulation！猜对了！")
```
## 4.3 while与风向标

```python
number = 20
flag = True
while flag:
    guess = int(input("请输入正整数："))
    if guess < number:
        print("猜小了...")
    elif guess > number:
        print("猜大了...")
    else:
        print("Congratulation！猜对了！")
        flag = False
```
## 4.4 while与break、continue
- break

```python
number = 8
while True:
    guess = int(input("请输入正整数："))
    if guess < number:
        print("猜小了...")
    elif guess > number:
        print("猜大了...")
    else:
        print("Congratulation！猜对了！")
        break
```
- continue

```python
i = 0
while i < 5:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
# 输出：1
#      3
#      5
```
## 4.5 while与else

```python
count = 0
while count < 5:
    count += 1
    print("Time", count)
else:
    print("循环结束")
# 输出：Time 1
#      Time 2
#      Time 3
#      Time 4
#      Time 5
#      循环结束
```
> 若while循环全部执行完毕，且没有被break终止，则执行else模块
## 4.6 两个经典例子
- 删除未读书籍列表中的已读书籍

```python
def remove_specific_value(lst, value):
    while value in lst:
        lst.remove(value)
    return lst

books = ['Python基础', '数据结构', 'Python基础', '算法导论', 'Python基础']
print("原始书籍列表：", books)
# 输出：原始书籍列表： ['Python基础', '数据结构', 'Python基础', '算法导论', 'Python基础']
books = remove_specific_value(books, 'Python基础')
print("删除特定值后的书籍列表：", books)
# 输出：删除特定值后的书籍列表： ['数据结构', '算法导论']
```
- 将未读书籍列表存入已读书籍列表

```python
def move_books_to_read(unread_books, read_books):
    while unread_books:
        current_book = unread_books.pop(0)  # 取出列表中的第一个元素
        print("正在阅读: ", current_book)
        read_books.append(current_book)
        print("已读书籍列表更新为: ", read_books)
    return read_books

unread_books = ['Python基础', '数据结构', '算法导论']
read_books = []
print("初始未读书籍列表：", unread_books)
# 输出：初始未读书籍列表： ['Python基础', '数据结构', '算法导论']
print("初始已读书籍列表：", read_books)
# 输出：初始已读书籍列表： []

read_books = move_books_to_read(unread_books, read_books)

print("最终未读书籍列表：", unread_books)
# 输出：最终未读书籍列表： []
print("最终已读书籍列表：", read_books)
# 输出：最终已读书籍列表： ['Python基础', '数据结构', '算法导论']
```
# 5、注意问题
## 5.1 尽可能少使用多层嵌套
> 可读性差，容易逼疯自己，折磨别人

```python
x = y = z = 1
if x > 0:
    if y > 0:
        if z > 0:
            print("x, y, z are all positive")
```
- 优化后：

```python
if x > 0 and y > 0 and z > 0:
    print("x, y, z are all positive")
```
## 5.2 避免死循环
> 条件一直成立，循环永无止境

```python
i = 0
while i < 5:
    print(i)  # 忘记了i的递增操作，导致死循环
```
- 优化后：

```python
i = 0
while i < 5:
    print(i)
    i += 1  # 增加计数器，避免死循环
```
## 5.3 封装的条件
> 可读性差，可维护性差

```python
user_input = input(">>：")
if (user_input.isdigit() and int(user_input) > 0 and int(user_input) % 2 == 0) or \
   (user_input.find('.') != -1 and len(user_input.split('.')[1]) == 2):
    print("输入有效")
```
- 优化后——封装为函数：

```python
def is_valid_input(user_input):
    if user_input.isdigit():
        number = int(user_input)
        return number > 0 and number % 2 == 0
    elif user_input.find('.') != -1:
        parts = user_input.split('.')
        return len(parts[1]) == 2
    return False

if is_valid_input(user_input):
    print("输入有效")
```
-----
`微语录：小时候一想到这些倾注着的、渗出似的耀眼的白色颗粒全都是星星，就会无端感到哀伤。抬头仰望着的、这些填满着枝叶间隙的繁星的闪烁。`
