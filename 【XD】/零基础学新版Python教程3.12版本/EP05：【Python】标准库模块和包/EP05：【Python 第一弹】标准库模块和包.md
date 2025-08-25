# 一、标准库模块
## 1.1 定义
### 1.1.1 常用模块
- Python标准库是Python内置的一些模块，可以直接导入和使用
- 提供了许多基本的功能和工具，如数学运算、文件操作、日期时间处理等
### 1.1.2 自定义模块
- 将一些相关的函数和变量组织到一个Python文件中，然后在其他Python脚本中导入和使用
### 1.1.3 第三方模块
- 通常是由Python社区开发的，提供了各种扩展功能和工具：
    - `requests`模块发送HTTP请求
    - `numpy`模块进行科学计算
    - `pandas`模块进行数据分析
## 1.2 常用模块
### 1.2.1 `sys`模块
1. 定义：与 Python 解释器交互，提供运行时环境相关的变量和函数，常用于命令行参数处理、程序退出控制等。
2. 常用功能：
	- 获取命令行参数
	- 退出程序
	- 获取 Python 解释器信息
3. 示例：

```python
# （1）获取命令行参数
import sys
print(sys.argv)
# （2）退出程序
import sys
if len(sys.argv) < 2:
    sys.exit("错误：请提供至少一个参数")
print("程序正常执行")
# （3）获取 Python 解释器信息
import sys
print(f"Python版本：{sys.version}")
print(f"系统平台：{sys.platform}")
```
- 运行结果：
```
['D:\\Desktop\\Python-learning\\【Python 第一弹】\\EP05：【Python 第一弹】标准库模块和包\\标准库模块和包\\01_def.py']
错误：请提供至少一个参数
```
```
['D:\\Desktop\\Python-learning\\【Python 第一弹】\\EP05：【Python 第一弹】标准库模块和包\\标准库模块和包\\01_def.py']
Python版本：3.11.7 | packaged by Anaconda, Inc. | (main, Dec 15 2023, 18:05:47) [MSC v.1916 64 bit (AMD64)]
系统平台：win32
```
### 1.2.2 `os`模块
1. 定义：与操作系统交互，提供文件 / 目录操作、环境变量访问等功能，适配多平台（Windows、Linux、macOS）。
2. 常用功能：
	- 目录操作
	- 文件/目录创建与删除
	- 环境变量操作
3. 示例：

```python
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
```
- 运行结果：
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/372a9bb863c7428aaf162f07ae57c9cd.png)
### 1.2.3 `random`模块
1. 定义：生成各种随机数，支持整数、浮点数、序列随机选择等场景。
2. 常用功能：
	- 生成随机数
	- 序列随机操作
	- 固定随机种子
3. 示例：

```python
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
```
- 运行结果：
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/cbac021f42034a9db15677abf00be7ca.png)
### 1.2.4 `datetime`模块
1. 定义：处理日期和时间，提供`datetime`（日期时间）、`date`（日期）、`time`（时间）等类，支持格式化、加减运算等。
2. 常用功能：
	- 获取当前时间
	- 日期时间格式化
	- 日期时间加减
3. 示例：

```python
"""
datetime 模块
"""

# 1. 获取当前时间
from datetime import datetime, date, time
# 当前日期时间
now = datetime.now()
print(now)
# 当前日期
today = date.today()
print(today)

# 2. 日期时间格式化
from datetime import datetime
now = datetime.now()
print(now.strftime("%Y年%m月%d日 %H:%M:%S"))

# 3. 日期时间加减
from datetime import datetime, timedelta
now = datetime.now()
# 3天后
future = now + timedelta(days=3)
print(future.strftime("%Y-%m-%d"))
# 1小时30分钟前
past = now - timedelta(hours=1, minutes=30)
print(past.strftime("%H:%M"))
```
- 运行结果：
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/ebe7327462944637bc58097942cf420d.png)
### 1.2.5 `json`模块
1. 定义：处理 JSON 数据与 Python 对象的相互转换。
2. 常用功能：
	- Python 对象转 JSON 字符串（序列化）
	- JSON 字符串转 Python 对象（反序列化）
	- 文件读写 JSON
3. 示例：

```python
"""
json 模块
"""

# 1. Python 对象转 JSON 字符串（序列化）
import json
data = {
    "name": "张三",
    "age": 25,
    "hobbies": ["读书", "跑步"]
}

json_str = json.dumps(data, ensure_ascii=False, indent=2)
print(json_str)

print('--'*50)

# 2. JSON 字符串转 Python 对象（反序列化）
import json
json_str = '{"name": "李四", "score": 95.5}'
# 转换为Python字典
data = json.loads(json_str)
print(data["name"])
print(type(data["score"]))

print('--'*50)

# 3. 文件读写 JSON
import json
data = {"status": "success", "result": [1, 2, 3]}
# 写入JSON文件
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
# 读取JSON文件
with open("data.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
print(loaded_data["result"])
```
- 运行结果：
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/c1541aef3ebc4dc5a4d6b80ef4f0cf8f.png)
### 1.2.6 `math`模块
1. 定义：提供数学运算相关的函数和常量（如三角函数、对数、幂运算等），适用于科学计算场景。
2. 示例：

```python
"""
math 模块
"""

# 1. 基础数学运算
import math
# 平方根
print(math.sqrt(25))
# 幂运算（等价于2**3，但精度更高）
print(math.pow(2, 3))
# 向下取整、向上取整
print(math.floor(3.7))
print(math.ceil(3.2))

# 2. 特殊常量
import math
print(math.pi)
print(math.e)

# 3. 三角函数
import math
print(math.sin(math.pi/2))
print(math.log(100, 10))
```
- 运行结果：
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/ead387fc94c64e449d3cb87188166be6.png)
### 1.2.7 `re`模块
1. 定义：提供正则表达式操作，用于字符串的匹配、查找、替换、分割等。
2. 常用功能：
	- 查找匹配内容
	- 替换匹配内容
	- 分割字符串
3. 示例：

```python
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
```
- 运行结果：
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/9eb9ed6bce7a4d77bcc42b20a9615215.png)
## 1.3 自定义模块
### 1.3.1 定义
一个以.py为扩展名的 Python 文件，文件名即为模块名。
### 1.3.2 内容
可包含函数、类、变量、可执行语句等。
### 1.3.3 作用
- 实现代码复用（多个程序可共享模块功能）
- 避免命名冲突（不同模块中的同名函数/变量互不影响）
- 使代码结构更清晰（按功能拆分模块）
### 1.3.4 代码实操——`calculator`模块

```python
"""
calculator 模块
"""

# 定义变量
PI = 3.1415926

# 定义函数
def add(a, b):
    """返回两个数的和"""
    return a + b


def multiply(a, b):
    """返回两个数的积"""
    return a * b

# 定义类
class Circle:
    """圆的类，计算周长和面积"""

    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        """计算周长"""
        return 2 * self.PI * self.radius

    def area(self):
        """计算面积"""
        return self.PI * self.radius ** 2

# 模块内的可执行代码（导入模块时会执行）
if __name__ == "__main__":
    # 仅在当前模块作为主程序运行时执行（测试代码）
    print("模块自测：")
    print(add(2, 3))
    print(Circle(2).area())
```
1. 模块与主程序在同一目录：
```
project/
├── calculator.py  # 自定义模块
└── main.py        # 主程序
```

```python
"""
模块与主程序在同一目录
"""

# 方式1：导入整个模块，通过"模块名.成员"访问
import calculator
print(calculator.add(5, 3))
print(calculator.PI)

# 方式2：导入模块中的特定成员，直接使用成员名
from calculator import add, Circle
print(add(10, 20))
circle = Circle(3)
print(circle.perimeter())

# 方式3：导入模块所有成员（不推荐，可能引发命名冲突）
from calculator import *
print(multiply(4, 5))
```
- 运行结果：
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/214bf15e2cfe4d7db4451d0955b30d4d.png)
2. 模块在子目录中（包结构）：
```
project/
├── main.py
└── utils/                  # 包目录
    ├── __init__.py         # 包初始化文件（可空）
    └── calculator.py       # 自定义模块
```

```python
"""
模块在子目录中（包结构）
"""

# 方式1：通过包名.模块名导入
from utils.calculator import add
print(add(2, 8))

# 方式2：导入整个模块
import utils.calculator as calc
print(calc.multiply(3, 7))
```
- 运行结果：
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/b1865de074de45fdae389d74866c0bcf.png)
3. 模块在其他目录（添加路径）：
```
project/
├── main.py
└── modules/
    └── calculator_.py  # 自定义模块（路径：/path/to/project/modules/calculator_.py）
```

```python
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
```
- 运行结果：
```
3
```

# 二、包
## 2.1 定义
**包是一个包含多个模块的目录**，目录中必须包含一个特殊文件`__init__.py`（Python 3.3+允许为空，但建议保留）。
## 2.2 作用
  - 避免模块名冲突（不同包中可存在同名模块）
  - 提供层次化的代码组织结构（如`package.module.function`）
  - 便于代码复用和维护
## 2.3 包 vs 模块 vs 库
| 术语       | 定义                                  | 示例                     |
|------------|---------------------------------------|--------------------------|
| **模块**   | 单个Python文件（`.py`）               | `math.py`、`utils.py`    |
| **包**     | 包含`__init__.py`的目录，可包含多个模块 | `mypackage/`（含多个`.py`） |
| **库**     | 一组相关的包和模块的集合              | `requests`、`numpy`      |
## 2.4 基本结构
### 2.4.1 简单包结构
```
mypackage/
├── __init__.py    # 包标识文件（可空）
├── module1.py     # 模块1
└── module2.py     # 模块2
```
### 2.4.2 嵌套包结构（多级目录）
```
webapp/
├── __init__.py
├── models/        # 子包：数据模型
│   ├── __init__.py
│   ├── user.py    # 用户模型
│   └── product.py # 产品模型
├── utils/         # 子包：工具函数
│   ├── __init__.py
│   └── fileio.py  # 文件操作工具
└── main.py        # 主程序入口
```

----
==微语录：我的理想永不醉落，它会以我的生命为燃料，永远高飞天际！——《文豪野犬》==
