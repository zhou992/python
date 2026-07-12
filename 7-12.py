# 定义函数 phone_book ()，用字典存姓名：手机号
# 菜单循环：
# 1 添加联系人 2 查询手机号 3 退出
# 添加：输入姓名、手机号存入字典
# 查询：输入姓名，存在则打印手机号，不存在提示无该联系人
def phone_book():
    contact = {}
    while True:
        while True:
            try:
                print("菜单如下：")
                print("1 添加联系人 2 查询手机号 3 退出")
                case=int(input("请选择数字："))
                if case in (1,2,3):
                    break
                else:print("请重新选择正确的数字！")

            except ValueError:print("请重新输入！")



        match case:
            case 1:
                name = input("请输入名字：")
                number = input("请输入手机号：")
                contact[name]=number

                print(f"{name}已添加")
            case 2:
                n = input("请输入要查找的联系人：")
                if n in contact:
                    print(contact[n])
                else:print("该联系人不存在！")
            case 3:break

phone_book()