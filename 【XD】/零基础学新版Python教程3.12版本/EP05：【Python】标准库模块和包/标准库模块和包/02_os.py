"""
os 模块
"""

# 1. 目录操作
import os
# 获取当前工作目录
print(os.getcwd())
# 切换工作目录
os.chdir("D:\Desktop\Python-learning\【Python 第一弹】\EP05：【Python 第一弹】标准库模块和包\标准库模块和包")
# 列出目录内容
print(os.listdir("."))

# 2. 文件/目录创建与删除
import os
# 创建目录（支持多级目录）
os.makedirs("data/reports", exist_ok=True)
# 删除文件
if os.path.exists("temp.txt"):
    os.remove("temp.txt")
# 删除空目录
os.rmdir("data/reports")

# 3. 环境变量操作
import os
# 获取环境变量
print(os.environ.get("PATH"))
# 设置临时环境变量
os.environ["MY_VAR"] = "test_value"
print(os.environ["MY_VAR"])