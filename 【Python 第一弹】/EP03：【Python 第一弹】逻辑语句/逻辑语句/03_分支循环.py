# 1. 打印1-9的整数
count = 0
while count < 10:
    print(count)
    count += 1

# 2. 打印字符串的每个字符
for item in '黄鹤楼送孟浩然之广陵':
        print(item)

# 3. 随机生成验证码
import random
import string
str1 = ''
for i in range(4):
    random_char = random.choice(string.ascii_uppercase)
    str1 += random_char
print(str1)
