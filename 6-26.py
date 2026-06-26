# 要求
# 定义函数 check_pwd()
# 用户输入密码
# 校验规则：
# 长度必须≥6 位
# 至少包含 1 个数字
# 全部满足打印「密码合格」，否则打印对应失败原因
# # 提示：遍历字符判断是否存在数字，结合len()判断长度
def check_pwd():
    passward = input("请输入密码：")
    if len(passward)>=6 :
        cou=0
        for i in passward:
            if passward.isdigit():
                cou=1
                break



        if cou==1:
            print("密码合格")
    else:print("密码长度不够")

check_pwd()