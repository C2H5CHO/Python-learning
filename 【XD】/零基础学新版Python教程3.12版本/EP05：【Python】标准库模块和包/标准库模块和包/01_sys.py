"""
sys 模块
"""

# （1）获取命令行参数
import sys
print(sys.argv)
# （2）退出程序
# import sys
# if len(sys.argv) < 2:
#     sys.exit("错误：请提供至少一个参数")
# print("程序正常执行")
# （3）获取 Python 解释器信息
import sys
print(f"Python版本：{sys.version}")
print(f"系统平台：{sys.platform}")