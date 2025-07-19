"""
字典推导式
"""

# 1. 基础用法
keys = ['name', 'age', 'city']
values = ['Alice', 30, 'New York']
person = {keys[i]: values[i] for i in range(len(keys))}
print(person)

# 2. 条件过滤
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares)

# 3. 转换现有字典
original = {'a': 'apple', 'b': 'banana', 'c': 'cherry'}
upper_dict = {k: v.upper() for k, v in original.items()}
print(upper_dict)

# 4. 交换键值对
original = {'name': 'Alice', 'age': '30'}
swapped = {v: k for k, v in original.items()}
print(swapped)

# 5. 处理字符串
text = 'hello world'
char_count = {char: text.count(char) for char in text if char != ' '}
print(char_count)
