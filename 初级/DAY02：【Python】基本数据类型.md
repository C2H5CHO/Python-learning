# 一、数字类型
## 1.1 数字类型的组成
### 1.1.1 整数
#### （1）十进制，二进制0b，八进制0o，十六进制0x

```python
print(16 == 0b10000 == 0o20 == 0x10)
# 输出：True
```
#### （2）十进制转其他进制

```python
a = bin(16)
b = oct(16)
c = hex(16)
print(a, b, c)
# 输出：0b10000 0o20 0x10
```
> 注意：上述输出结果为==字符串类型==

```python
print(a == b == c)
# 输出：False
print(type(a), type(b), type(c))
# 输出：<class 'str'> <class 'str'> <class 'str'>
```
#### （3）其他进制转十进制

```python
l = int(a, 2)
m = int(b, 8)
n = int(c, 16)
print(l, m, n)
# 输出：16 16 16
```
### 1.1.2 浮点数
#### （1）不确定小数问题

```python
print((0.1 + 0.2) == 0.3)
# 输出：False
print(0.1 + 0.2)
# 输出：0.30000000000000004
```
#### （2）计算机采用二进制小数表示浮点数的小数部分
> 注意：
> 1. 部分小数不能用二进制小数完全表示
>  2. 通常情况，不影响计算精度
>  3. 四舍五入可获得精确解

```python
a = 0.1 + 0.7
print(a)
# 输出：0.7999999999999999

b = round(a, 1)
print(b)
# 输出：0.8
print(b == 0.8)
# 输出：True
```
### 1.1.3 复数
#### （1）j or J

```python
print(3+4j)
# 输出：(3+4j)
print(3+4J)
# 输出：(3+4j)
```
#### （2）若虚部系数为1，则需要显式写出

```python
print(3+J)
# 输出：NameError: name 'J' is not defined
print(3+1j)
# 输出：(3+1j)
```
## 1.2 数字类型的运算操作符
### 1.2.1 加减乘除

```python
print((1+2-3*4) / 5)
# 输出：-1.8
```
### 1.2.2 取反

```python
x = 3
print(-x)
# 输出：-3
```
### 1.2.3 乘方

```python
print(2**3)
# 输出：8
```
### 1.2.4 整数商和模

```python
print(11 // 2)
# 输出：5
print(11 % 2)
# 输出：2
```
> 注意：
> 1. 整数和浮点数的运算结果为浮点数
> 2. 除法的运算结果为浮点数

```python
print(1+2.5)
# 输出：3.5
print(5/2)
# 输出：2.5
print(4.0/2)
# 输出：2.0
```
## 1.3 整数类型的运算操作函数
### 1.3.1 绝对值——abs()

```python
print(abs(-3))
# 输出：3
print(abs(3+4j))  # 对复数，执行求模运算
# 输出：5.0
```
### 1.3.2 幂次方——pow(x, n)

```python
print(pow(2, 3))  # 执行 2**3
# 输出：8
print(pow(2, 3, 4))  # 执行 2^3%4
# 输出：0
```
### 1.3.3 四舍五入——round(x, n)

```python
a = 314.159
print(round(a))  # 默认整数
# 输出：314
print(round(a, 2))  # 四舍五入保留两位小数
# 输出：314.16
print(round(a, 8))  # 位数不足时，无需补足
# 输出：314.159
print(round(a, -2))  # 四舍五入保留100的倍数
# 输出：300.0
```
### 1.3.4 整数商和模——divmod(x, y)

```python
print(divmod(9, 2))
# 输出：(4, 1)
# 返回二元元组：(9//2, 9%2)
```
### 1.3.5 序列最大值/最小值——max(), min()

```python
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("max：", max(lst))
# 输出：max： 10
print("min：", min(lst))
# 输出：min： 1
```
### 1.3.6 求和——sum()

```python
print(sum((1, 3, 5, 7, 9)))
# 输出：25
```
### 1.3.7 科学计算库
#### （1）math

```python
import math

# 1.幂运算
print("2 的 3 次方:", math.pow(2, 3))
# 输出：2 的 3 次方: 8.0

# --------------------------------------------------

# 2.对数运算
print("log(100, 10):", math.log(100, 10))  # 以 10 为底 100 的对数
# 输出：log(100, 10): 2.0
print("自然对数 log(e):", math.log(math.e))  # 自然对数
# 输出：自然对数 log(e): 1.0

# --------------------------------------------------

# 3.平方根
print("sqrt(16):", math.sqrt(16))
# 输出：sqrt(16): 4.0

# --------------------------------------------------

# 4.角度转弧度
angle_in_degrees = 45
angle_in_radians = math.radians(angle_in_degrees)

# --------------------------------------------------

# 5.正弦、余弦、正切
print(f"{angle_in_degrees} 度的正弦值: {math.sin(angle_in_radians)}")
# 输出：45 度的正弦值: 0.7071067811865476
print(f"{angle_in_degrees} 度的余弦值: {math.cos(angle_in_radians)}")
# 输出：45 度的余弦值: 0.7071067811865476
print(f"{angle_in_degrees} 度的正切值: {math.tan(angle_in_radians)}")
# 输出：45 度的正切值: 0.9999999999999999

# --------------------------------------------------

# 6.反三角函数
print("arcsin(0.7071):", math.degrees(math.asin(0.7071)))  # 结果转换为角度
# 输出：arcsin(0.7071): 44.99945053347443

# --------------------------------------------------

# 7.双曲正弦、双曲余弦、双曲正切
x = 1
print(f"x={x} 的双曲正弦值: {math.sinh(x)}")
# 输出：x=1 的双曲正弦值: 1.1752011936438014
print(f"x={x} 的双曲余弦值: {math.cosh(x)}")
# 输出：x=1 的双曲余弦值: 1.5430806348152437
print(f"x={x} 的双曲正切值: {math.tanh(x)}")
# 输出：x=1 的双曲正切值: 0.7615941559557649

# --------------------------------------------------

# 8.阶乘
n = 5
print(f"{n} 的阶乘: {math.factorial(n)}")
# 输出：5 的阶乘: 120

# --------------------------------------------------

# 9.伽马函数
print("gamma(3):", math.gamma(3))  # gamma(n) = (n-1)!
# 输出：gamma(3): 2.0

# --------------------------------------------------

# 10.常数
print("π:", math.pi)
# 输出：π: 3.141592653589793
print("e:", math.e)
# 输出：e: 2.718281828459045
```
#### （2）scipy
- Optimize (==优化==)：提供了多种优化算法，包括最小化(最大化)函数、曲线拟合等

```python
from scipy import optimize
import numpy as np

def f(x):
    return x**2 + 10 * np.sin(x)

# 使用 minimize 方法寻找函数最小值
result = optimize.minimize(f, 0)
print("找到的最小值点:", result.x)
# 输出：找到的最小值点: [-1.30644012]
```
- Integrate (==积分==和==微分==方程求解)：提供了多种数值积分方法以及 ODE 求解器

```python
from scipy import integrate

# 定义被积函数
def integrand(x):
    return np.exp(-x**2)

# 计算积分
result, _ = integrate.quad(integrand, -np.inf, np.inf)
print("积分结果:", result)
# 输出：积分结果: 1.7724538509055159
```
- Linalg (==线性代数==)：扩展了 NumPy 的线性代数能力，提供了更多高级功能

```python
from scipy import linalg
import numpy as np

# 创建两个随机矩阵
A = np.random.randn(3, 3)
B = np.random.randn(3, 1)

# 解线性方程 Ax = B
solution = linalg.solve(A, B)
print("Ax=B 的解:", solution)
# 输出：Ax=B 的解: [[-0.07803842]
#                 [ 0.23422888]
#                 [ 0.19536865]
#                ]
```
- Signal (==信号处理==)：提供了一系列工具用于信号处理，如滤波、卷积等

```python
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体或其他中文字体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号 '-' 显示为方块的问题

# 创建一个简单的正弦波信号
t = np.linspace(0, 1, 500)
x = np.sin(2 * np.pi * 3 * t) + 0.5 * np.random.randn(t.size)

# 设计一个低通滤波器并应用到信号上
b, a = signal.butter(3, 0.05)
filtered_x = signal.filtfilt(b, a, x)

plt.plot(t, x, label='原始信号')
plt.plot(t, filtered_x, label='过滤后的信号')
plt.legend()
plt.show()
```
> 结果：
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/9c71926ce6814805bccdaa87158f637c.png#pic_center)
- Stats (==统计==分布和函数)：提供了广泛的统计分布模型和统计测试

```python
from scipy import stats
import numpy as np

# 生成一组随机数据
data = np.random.normal(loc=0, scale=1, size=1000)

# 计算描述性统计量
mean = np.mean(data)
median = np.median(data)
mode = stats.mode(data)  # 需要注意的是，对于连续分布的数据，模式可能不适用或需要进行分箱处理
std_dev = np.std(data)

print(f"Mean: {mean}, Median: {median}, Standard Deviation: {std_dev}")
# 输出：Mean: 0.035383601211682034, Median: 0.06455716819180869, Standard Deviation: 0.9858768770120637
```
#### （3）numpy

```python
import numpy as np

# 1.创建数组
# 从列表创建一维数组
a = np.array([1, 2, 3])
print("一维数组:", a)
# 输出：一维数组: [1 2 3]

# 从列表创建二维数组
b = np.array([[1, 2], [3, 4]])
print("二维数组:\n", b)
# 输出：二维数组:
#             [[1 2]
#             [3 4]]

# 使用内置函数创建特定形状的数组
c = np.zeros((3, 3))  # 创建一个3x3的零矩阵
print("零矩阵:\n", c)
# 输出：零矩阵:
#            [[0. 0. 0.]
#            [0. 0. 0.]
#            [0. 0. 0.]]

# --------------------------------------------------

# 2.数组操作
# 数组的形状和大小
print("数组b的形状:", b.shape)
# 输出：数组b的形状: (2, 2)
print("数组b的维度:", b.ndim)
# 输出：数组b的维度: 2
print("数组b的元素总数:", b.size)
# 输出：数组b的元素总数: 4

# 数组重塑
d = b.reshape(1, 4)  # 将二维数组b重塑为1行4列的一维数组
print("重塑后的数组:\n", d)
# 输出：重塑后的数组:
#                   [[1 2 3 4]]

# --------------------------------------------------

# 3.广播机制
e = np.array([1, 2, 3])
f = np.array([2, 2, 2])

# 利用广播机制进行加法运算
g = e + f
print("广播加法结果:", g)
# 输出：广播加法结果: [3 4 5]

# 标量与数组的加法
h = e + 2
print("标量加法结果:", h)
# 输出：标量加法结果: [3 4 5]

# --------------------------------------------------

# 4.线性代数运算
i = np.array([[1, 2], [3, 4]])
j = np.array([[5, 6], [7, 8]])

# 矩阵乘法
k = np.dot(i, j)
print("矩阵乘法结果:\n", k)
# 输出：矩阵乘法结果:
#                 [[19 22]
#                  [43 50]]

# 计算行列式
det_i = np.linalg.det(i)
print("行列式i:", det_i)
# 输出：行列式i: -2.0000000000000004

# --------------------------------------------------

# 5.傅里叶变换
signal = np.array([0, 1, 0, 1])
fourier = np.fft.fft(signal)
print("傅里叶变换结果:", fourier)
# 输出：傅里叶变换结果: [ 2.+0.j  0.+0.j -2.+0.j  0.+0.j]

# --------------------------------------------------

# 6.随机数生成
# 生成标准正态分布的随机数
random_numbers = np.random.randn(5)
print("随机数:", random_numbers)
# 输出：随机数: [ 0.91515599 -0.74805686  0.90227149  0.2376813   2.70840746]

# 生成指定范围内的整数随机数
random_integers = np.random.randint(0, 10, size=5)
print("整数随机数:", random_integers)
# 输出：整数随机数: [7 0 4 7 7]
```
# 二、字符串类型
## 2.1 字符串的表达

```python
print("hello", 'world')
# 输出：hello world
```
### 2.1.1 双中有单

```python
print("I'm a test")
# 输出：I'm a test
```
### 2.1.2 单中有双

```python
print('I am a "test"')
# 输出：I am a "test"
```
### 2.1.3 双中有双/单中有单

```python
print('I\'m a test')
# 输出：I'm a test
```
### 2.1.4 转移符用来换行继续输入

```python
st = "py\
thon"
print(st)
# 输出：python
```
## 2.2 字符串的性质
### 2.2.1 字符串的索引——变量名[位置编号]

```python
s = "my name is <NAME>"

# 正向索引
print(s[0])
# 输出：m
print(s[3])
# 输出：n
print(s[9])
# 输出：s

# 反向索引
print(s[-1])
# 输出：>
print(s[-2])
# 输出：E
print(s[-6])
# 输出：<
```
### 2.2.2 字符串的切片——变量名[开始位置:结束位置:切片间隔]

```python
print(s[0:6])
# 输出：my nam
print(s[0:6:2])
# 输出：m a
print(s[:6])  # 开始位置为0时，可省略
# 输出：my nam
print(s[:])  # 结束位置省略时，则表示取到最后一个字符
# 输出：my name is <NAME>
print(s[-3:])  # 也可以使用反向索引
# 输出：ME>
print(s[-1:-9:-1])  # 反向切片
# 输出：>EMAN< s
```
## 2.3 字符串的操作符
### 2.3.1 字符串的拼接

```python
a = "my name "
b = "is Tom"
print(a + b)
# 输出：my name is Tom
```
### 2.3.2 字符串的成倍复制

```python
c = a+b
print(c)
# 输出：my name is Tom
print(c*3)
# 输出：my name is Tommy name is Tommy name is Tom
```
### 2.3.3 字符串的成员运算
- 子集 in 全集——任何一个连续的切片都是原字符串的子集

```python
singers = "Tom, Tina, Time"
print("Tom" in singers)
# 输出：True
```
- for 字符 in 字符串——遍历字符串

```python
for s in "python":
    print(s)
# 输出：p
#      y
#      t
#      h
#      o
#      n
```
## 2.4 字符串的处理函数
### 2.4.1 字符串的长度——len()

```python
s = "python"
print(len(s))
# 输出：6
```
### 2.4.2 字符编码
> 1. 定义：将字符（字母、数字、符号等）映射为计算机可以处理的二进制数
> 2. 特点：
> &emsp;&emsp;（1）每个单一字符对应一个==唯一==的==不可重复==的二进制编码
> &emsp;&emsp;（2）Python中使用Unicode编码
#### （1）字符转Unicode码——ord(字符)

```python
print(ord("1"))
# 输出：49
print(ord("a"))
# 输出：97
print(ord("."))
# 输出：46
print(ord("中"))
# 输出：20013
```
#### （2）Unicode码转字符——chr(Unicode码)

```python
print(chr(1000))
# 输出：8
print(chr(1010))
# 输出：c
print(chr(12345))
# 输出：〹
```
## 2.5 字符串的处理方法
> 特点：
> &emsp;&emsp;1. 返回的结果为一个列表
> &emsp;&emsp;2. 原字符串不变

### 2.5.1 字符串的分割——字符串.split(分割字符)

```python
st = "my name is Tom"
st_lst = st.split(" ")
print(st)
# 输出：my name is Tom
print(st_lst)
# 输出：['my', 'name', 'is', 'Tom']
```
### 2.5.2 字符串的聚合——"聚合字符".join(可迭代数据类型)
> 可迭代类型：
> &emsp;&emsp;1. 列表（list）：有序的、可变的数据集合
> &emsp;&emsp;2. 元组（tuple）：有序的、不可变的数据集合
> &emsp;&emsp;3. 字符串（str）：字符的有序集合，也是不可变的
> &emsp;&emsp;4. 字典（dict）：键值对的无序集合，迭代时默认遍历键
> &emsp;&emsp;5. 集合（set）：无序且不重复元素的集合

```python
words = ["Hello", "world", "from", "Python"]
sentence = " ".join(words)
print(sentence)
# 输出: Hello world from Python

numbers = [1, 2, 3]
joined_numbers = " - ".join(str(n) for n in numbers)
print(joined_numbers)
# 输出: 1 - 2 - 3
```
### 2.5.3 删除两端待定字符——字符串.strip(删除字符)

```python
s = "------my name is Tom------"
print(s.strip("-"))
# 输出：my name is Tom
print(s.rstrip("-"))
# 输出：------my name is Tom
print(s.lstrip("-"))
# 输出：my name is Tom------
print(s)
# 输出：------my name is Tom------

st = "      my name is Tom      "
print(st.strip(" "))  # strip()从两侧开始搜索，遇到指定字符则删除，遇到非指定字符则停止
# 输出：my name is Tom
```
### 2.5.4 字符串的替换——字符串.replace("被替换", "替换成")

```python
s = "my name is Tom"
s1 = s.replace("Tom", "Time")
print(s1)
# 输出：my name is Time
```
### 2.5.5 字符串的字母大小写

```python
s = "pyThon"
print(s.upper())  # 全部大写
# 输出：PYTHON
print(s.lower())  # 全部小写
# 输出：python
print(s.capitalize())  # 字符串首字母大写
# 输出：Python
print(s.title())  # 单词首字母大写
# 输出：Python
print(s.swapcase())  # 大小写转写
# 输出：PYtHON
```
# 三、布尔类型
## 3.1 作为逻辑运算的结果

```python
a = 3
print(a > 1)
# 输出：True
print(a == 3)
# 输出：True
print(a < 2)
# 输出：False
print(any([False, 1, 0, None]))
# 输出：True
print(all([False, 1, 0, None]))
# 输出：False
```
## 3.2 作为指示条件

```python
m = 3
while True:
    n = eval(input("请输入一个正整数："))
    if m == n:
        print("猜对啦！")
    elif m > n:
        print("猜小了。")
    else:
        print("猜大了。")
```
## 3.3 作为掩码

```python
import numpy as np
x = np.array([[1, 3, 2, 5, 7]])
print(x > 3)
# 输出：[[False False False  True  True]]
print(x[x > 3])
# 输出：[5 7]
```
# 四、类型判别与转换
## 4.1 类型判别
### 4.1.1 type(变量)

```python
age = 20
print(type(age))
# 输出：<class 'int'>
```
### 4.1.2 isinstance(变量, 预测类型)

```python
print(isinstance(age, int))
# 输出：True
print(isinstance(age, float))
# 输出：False
print(isinstance(age, object))
# 输出：True
```
### 4.1.3 字符串的检查方法
#### （1）数字组成——字符串.isdigit()

```python
# 数字组成--字符串.isdigit()
age = "20"
age1 = "18 岁"
print(age.isdigit())
# 输出：True
print(age1.isdigit())
# 输出：False
```
#### （2）字母组成——字符串.isalpha()

```python
name = "Tom"
print(age.isalpha())
# 输出：False
print(name.isalpha())
# 输出：True
```
#### （3）数字和字母组成——字符串.isalnum()

```python
print("Tom2025".isalnum())  # 一般用于判断用户名是否合法
# 输出：True
```
## 4.2 类型转换
### 4.2.1 数字转字符串——str(数字类型)

```python
age = 20
print("my age is " + str(age))
# 输出：my age is 20
```
### 4.2.2 字符串转数字

```python
s1 = "20"
s2 = "21.5"
print(int(s1))
# 输出：20
print(float(s2))
# 输出：21.5
print(eval(s1))
# 输出：20
print(eval(s2))
# 输出：21.5
```
-------
`微语录：书上说，天下没有不散的宴席。不要怕，书上还说了，人生何处不相逢。`
