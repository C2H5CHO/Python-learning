# 1. 全局变量
global_var = "全局的变量"

def print_global_var():
    print(global_var)

print_global_var()
print(global_var)

# 2. 局部变量
def print_local_var():
    local_var = '局部变量'
    print(local_var)

print_local_var()
# print(local_var)