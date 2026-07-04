# 定义函数 reverse_num ()
# 用户输入一个正整数，用 try 捕获非数字输入
# 将数字反转输出
# 示例：输入1234，输出4321
# 提示：转字符串切片 [::-1] 或者循环取余都能实现
def reverse_num():
    try:
        n=input("请输入数字: ")


        print(n[::-1])

    except ValueError:
        print("请重新输入!")
reverse_num()










# def reverse_num():
#     try:
#         s = input("请输入数字：")
#         num = int(s)
#         if num <= 0:
#             print("请输入正整数！")
#             return
#         # 字符串反转
#         res = s[::-1]
#         print("反转后数字：", res)
#     except ValueError:
#         print("输入不是合法数字，请重新输入！")
#
# reverse_num()

