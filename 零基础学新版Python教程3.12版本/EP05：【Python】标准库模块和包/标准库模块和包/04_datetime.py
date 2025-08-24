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