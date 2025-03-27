"""
公共方法
"""

# 登录认证装饰器
def login_auth(func):
    def wrapper(*args, **kwargs):
        from core import core
        if core.logged_user:
            res = func(*args, **kwargs)
            print(res)
        else:
            print("\n当前账户未登录！！")
            core.login()
    return wrapper

# 密码加密
def pwd_to_sha256(password):
    import hashlib
    sha = hashlib.sha256()
    sha.update(password.encode('utf-8'))
    sha.update("洗刷刷洗刷刷".encode('gbk'))
    return sha.hexdigest()