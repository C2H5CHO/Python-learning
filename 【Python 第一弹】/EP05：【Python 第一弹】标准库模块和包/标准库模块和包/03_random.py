"""
random 模块
"""

# 1. 生成随机数
import random
# 生成[0.0, 1.0)之间的随机浮点数
print(random.random())
# 生成[a, b]之间的随机整数
print(random.randint(1, 10))
# 生成[a, b)之间的随机浮点数
print(random.uniform(2.5, 5.5))

# 2. 序列随机操作
import random
fruits = ["苹果", "香蕉", "橙子"]
# 随机选择一个元素
print(random.choice(fruits))
# 打乱序列（原地修改）
random.shuffle(fruits)
print(fruits)
# 随机选择多个元素（可重复）
print(random.choices(fruits, k=2))

# 3. 固定随机种子
import random
random.seed(42)
print(random.randint(1, 10))
random.seed(42)
print(random.randint(1, 10))