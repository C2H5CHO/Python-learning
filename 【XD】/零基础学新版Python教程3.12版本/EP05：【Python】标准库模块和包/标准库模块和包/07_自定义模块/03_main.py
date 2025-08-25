"""
模块在其他目录（添加路径）
"""

import sys
import os

# 获取模块所在目录的绝对路径
module_dir = os.path.abspath("./modules")
# 将目录添加到Python搜索路径
sys.path.append(module_dir)

# 导入模块
import calculator_
print(calculator_.add(1, 2))