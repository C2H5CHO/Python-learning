"""
银行相关接口
"""

from db import db_handler
from conf import settings
from datetime import datetime

# 充值接口
def recharge_interface(username, amount):
    # 1. 获取用户数据
    user_data = db_handler.select_data(username)

    if not user_data:
        return True, f"\n用户：{username}不存在！！"

    # 2. 给user_data里面的balance做加钱操作
    user_data['balance'] += amount

    # 3. 记录流水
    msg = (f"\n{datetime.now()}用户：{username}成功充值：{amount}元！！"
           f"\n当前余额为：{user_data.get('balance')}元！！")
    user_data['flow'].append(msg)

    # 4. 调用数据处理层，保存修改之后的数据
    db_handler.save(user_data)

    return True, msg

# 提现接口
def withdraw_interface(username, amount):
    # 1. 获取用户数据
    user_data = db_handler.select_data(username)
    balance = user_data.get('balance')

    # 2. 计算手续费，并判断用户金额是否充足
    service_fee = settings.RATE * amount
    if balance < (service_fee + amount):
        return False, '\n当前账户余额不足！！'

    # 3. 给user_data里面的balance做扣钱操作
    user_data['balance'] -= (service_fee + amount)

    # 4. 记录流水
    msg = (f"\n{datetime.now()}用户：{username}成功提现：{amount}元！！"
           f"\n手续费为：{service_fee}元！！"
           f"\n当前余额为：{user_data.get('balance')}元！！")
    user_data['flow'].append(msg)

    # 5. 调用数据处理层，保存修改后的数据
    db_handler.save(user_data)

    return True, msg

# 查看余额接口
def check_balance_interface(username):
    user_data = db_handler.select_data(username)
    balance = user_data.get('balance')

    return True, f"\n用户：{username}当前余额为：{balance}元！！"

# 转账接口
def transfer_interface(username, to_username, amount):
    # 1. 获取两个用户的用户数据
    user_data = db_handler.select_data(username)
    to_user_data = db_handler.select_data(to_username)

    # 2. 判断to_user_data是否存在
    if not to_user_data:
        return False, f"\n目标用户：{to_username}不存在！！"

    # 3. 判断当前用户的金额是否充足
    if user_data.get('balance') < amount:
        return False, f"\n当前账户余额不足，转账失败！！"

    # 4. 开始转账，给当前用户减钱，给目标用户加钱
    user_data['balance'] -= amount
    to_user_data['balance'] += amount

    # 5. 记录流水
    msg = (f"\n{datetime.now()}用户：{username}成功给用户：{to_username}转账：{amount}元！！"
           f"\n当前余额为：{user_data.get('balance')}元！！")
    user_data['flow'].append(msg)

    to_msg = (f"\n{datetime.now()}用户：{to_username}成功收到用户：{username}转账：{amount}元！！"
              f"\n当前余额为：{to_user_data.get('balance')}元！！")
    to_user_data['flow'].append(to_msg)

    # 6. 保存用户数据
    db_handler.save(user_data)
    db_handler.save(to_user_data)

    return True, msg

# 查看流水接口
def check_flow_interface(username):
    user_data = db_handler.select_data(username)
    flow_list = user_data.get('flow')
    return True, flow_list

# 支付接口
def pay_interface(username, total):
    # 1. 拿到用户数据
    user_data = db_handler.select_data(username)

    # 2. 判断用户余额是否充足
    if user_data.get('balance') < total:
        return False, f"\n用户：{username}余额不足，支付：{total}元失败！！"

    # 3. 支付
    user_data['balance'] -= total

    # 4. 添加流水
    msg = f"\n{datetime.now()}用户：{username}消费：{total}元，当前余额为：{user_data.get('balance')}"
    user_data['flow'].append(msg)

    # 5. 保存用户数据
    db_handler.save(user_data)

    return True, msg

