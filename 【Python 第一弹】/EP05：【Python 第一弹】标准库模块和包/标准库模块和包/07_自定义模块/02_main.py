"""
模块在子目录中（包结构）
"""

# 方式1：通过包名.模块名导入
from utils.calculator import add
print(add(2, 8))

# 方式2：导入整个模块
import utils.calculator as calc
print(calc.multiply(3, 7))