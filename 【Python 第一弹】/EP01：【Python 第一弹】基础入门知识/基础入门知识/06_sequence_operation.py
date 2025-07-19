"""
序列操作
"""

# 1. 创建字符串
str1 = "Hello"
str2 = 'World'
str3 = """
Hello
World
"""
print(f"str1：{str1}")
print(f"str2：{str2}")
print(f"str3：{str3}")

print('--'*50)

# 2. 通过索引获取字符
print(f"第一个字符：{str1[0]}")
print(f"最后一个字符：{str1[-1]}")

print('--'*50)

# 3. 通过切片获取字符
# 取首略尾
print(f"取首略尾：{str1[1:3]}")
# 默认到尾
print(f"默认到尾：{str1[1:]}")
# 从头开始
print(f"从头开始：{str1[:4]}")
# 从左向右
print(f"从左向右：{str1[1:4:1]}")
# 隔1取1
print(f"隔1取1：{str1[1:4:2]}")
# 反向截取
print(f"反向截取：{str1[3:1:-1]}")

print('--'*50)

# 4. 拼接字符串
concat1 = str1 + " " + str2
concat2 = "".join([str1, " ", str2])
print(f"concat1：{concat1}")
print(f"contact：{concat2}")

print('--'*50)

# 5. 计算字符串长度
print(f"str1的长度：{len(str1)}")
print(f"str3的行数：{len(str3.splitlines())}")

print('--'*50)

# 6. 判断某个字符或子字符串是否存在
print(f"存在判断: 'e' 在 {str1} 中: {'e' in str1}")
print(f"子串判断: 'lo' 在 {str1} 中: {str1.find('lo') != -1}")