"""
用户相关接口
"""

from db import db_handler

# 注册接口
def register_interface(username, password, is_admin=False, balance=0):
    """
    注册接口
    :param username: 用户名 str
    :param password: 密码 str
    :param is_admin: 是否是管理员 boolean
    :param balance: 初始余额 int
    :return: (boolean, str)
    """
    # 1. 调用数据处理层，查看用户是否已存在
    if db_handler.select_data(username, False):
        return False, '\n该用户名已存在！！'

    # 2. 组织用户数字字典
    user_data = {
        "username": username,
        "password": password,
        "balance": balance,
        "shopping_cart": {},
        "flow": [],
        "is_admin": is_admin,
        "locked": False,
    }

    # 3. 调用数据处理层，保存用户数据
    db_handler.save(user_data)

    return True, f'\n恭喜用户：{username}注册成功！！'

# 登录接口
def login_interface(username, password):
    # 1. 调用数据处理层，查看用户是否已存在
    user_data = db_handler.select_data(username)
    if not user_data:
        return False, f'\n该用户：{username}不存在，请重新输入！！', False

    # 2. 若用户存在，继续校验密码是否正确
    if password != user_data.get('password'):
        return False, '\n用户名或密码错误！！', False

    # 3. 若密码正确，继续校验用户是否冻结
    if user_data.get('locked'):
        return False, f'\n该用户：{username}已被冻结！！', False

    return True, f'\n用户：{username}登录成功！！', user_data.get('is_admin')
