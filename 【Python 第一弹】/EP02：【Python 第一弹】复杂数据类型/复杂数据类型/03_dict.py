"""
字典的常用方法
"""

# 1. 创建字典
student = {
    'name': "李白",
    'age': 25,
    'score': 80,
}
print(student)

# 2. 访问字典
student2 = {
    'name': "杜甫",
    'age': 20,
}

print(student2['name'])
print(student2.get('age', '404'))
print(student2.get('hobby', '404'))
# print(student2['sex'])

# 3. 修改字典
student3 = {
    'name': "苏轼",
    'age': 25,
}
print(student3['age'])
student3['age'] = 18
print(student3['age'])

# 4. 添加字典值
student4 = {
    'name': "王维",
    'age': 18,
}
print(student4)
student4['sex'] = '男'
print(student4)

# 5. 删除字典值
student5 = {
    'name': "李贺",
    'age': "20",
    'sex': "男",
    'hobby': "唱歌",
    'work': "《李凭箜篌引》"
}
print(student5)
del student5['age']
print(student5)
sex = student5.pop('sex')
print(student5)
print(sex)
student5.clear()
print(student5)