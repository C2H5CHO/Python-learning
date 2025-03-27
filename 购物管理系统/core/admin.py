"""
管理员视图层
"""

import core
from interface import admin_interface

# 添加账户功能
def add_user():
    is_admin = input("是否添加管理员（y or n）：").strip().lower()
    if is_admin == 'y':
        core.core.register(True)
    else:
        core.core.register()

# 冻结账户功能
def lock_user():
    while True:
        # 1. 接受管理员输入的用户名
        lock_username = input("请输入需要冻结的用户名：").strip()
        is_lock = input("按任意键确认/n退出：").strip().lower()

        # 2. 判断是否想要退出
        if is_lock == 'n':
            break

        # 3. 调用冻结账户的接口层冻结账户
        flag, msg = admin_interface.lock_user_interface(lock_username)
        print(msg)
        if flag:
            break

# 给用户充值
def recharge_to_user():
    username = input("请输入需要充值的用户名：").strip()
    core.core.recharge(username)

func_dic = {
    '0': ('返回首页', ),
    '1': ('添加账户', add_user),
    '2': ('冻结账户', lock_user),
    '3': ('给用户充值', recharge_to_user)
}

# 主程序
def main():
    flag00 = True
    while flag00:
        print("管理员功能".center(20, '='))
        for num in func_dic:
            print(f"{num} {func_dic.get(num)[0]}".center(20, '*'))
        print("我是有底线的".center(20, '='))
        opt = input("请输入功能编号：").strip()
        if opt not in func_dic:
            print("此功能不存在！！")
            continue
        if opt == '0':
            break
        func_dic.get(opt)[1]()
