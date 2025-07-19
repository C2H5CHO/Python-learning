"""
判断学生成绩
"""

# 1. 双分支语句
score = int(input('请输入分数:'))
if score >= 60:
    print('及格')
else:
    print('不及格')

# 2. 多分支语句
score = int(input('请输入分数:'))
if score >= 90:
    print('优秀')
elif score >= 80:
    print('良好')
elif score >= 70:
    print('中等')
elif score >= 60:
    print('及格')
else:
    print('不及格')