"""
re 模块
"""

# 1. 查找匹配内容
import re
text = "我的手机号是13812345678，另一部是13987654321"
# 匹配手机号（正则规则：1开头，11位数字）
pattern = r"1\d{10}"
# 查找第一个匹配
match = re.search(pattern, text)
print(match.group())
# 查找所有匹配
all_matches = re.findall(pattern, text)
print(all_matches)

# 2. 替换匹配内容
import re
text = "年龄：25，体重：65kg，身高：175cm"
# 隐藏数字（替换为*）
hidden = re.sub(r"\d+", "*", text)
print(hidden)
# 自定义替换（将数字加10）
def add_10(match):
    return str(int(match.group()) + 10)

modified = re.sub(r"\d+", add_10, text)
print(modified)

# 3. 分割字符串
import re
text = "apple, banana; orange| grape"
# 按逗号、分号、竖线分割
parts = re.split(r"[,;|]", text)
print(parts)