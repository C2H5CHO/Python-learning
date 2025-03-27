"""
购物相关接口
"""

from db import db_handler
from interface import bank_interface

# 查询商品接口
def check_goods_interface(goods_filename):
    goods = db_handler.select_data(goods_filename, is_user=False)
    return goods

# 查看购物车接口
def check_shop_cart_interface(username):
    user_data = db_handler.select_data(username)
    shop_cart_file = user_data.get('shopping_cart')
    return shop_cart_file

# 添加购物车接口
def add_shop_cart_interface(username, shopping_cart):
    # 1. 拿到用户数据里面的购物车数据
    user_data = db_handler.select_data(username)
    shopping_cart_file = user_data['shopping_cart']

    # 2. 添加购物车数据
    for name in shopping_cart.keys():
        if name in shopping_cart_file:
            shopping_cart_file[name]['数量'] += shopping_cart.get(name).get('数量')
        else:
            shopping_cart_file[name] = shopping_cart.get(name)

    # 3. 保存用户数据
    db_handler.save(user_data)

    return True, f"\n购物车添加成功！！"

# 结算接口
def close_account_interface(username, shopping_cart):
    # 1. 计算结算的总金额
    total = 0
    for good_info in shopping_cart.value():
        price = good_info.get('price')
        num = good_info.get('数量')
        total += (price * num)

    flag, msg = bank_interface.pay_interface(username, total)
    return flag, msg, total

# 更新购物车接口
def clear_shop_cart_interface(username, shop_cart={}):
    user_data = db_handler.select_data(username)
    user_data['shopping_cart'] = shop_cart
    db_handler.save(user_data)
    return '\n购物车更新成功！！'
