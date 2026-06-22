def calc_sum():
    n=1
    s = 0
    while n!=0:

        try:
            n=int(input("请输入数字："))
            s+=n
        except ValueError:
            print("输入错误，请输入整数！")
    return s
a = calc_sum()
print(a)



# def calc_sum():
#     s = 0
#     while True:
#         try:
#             num = int(input("请输入数字："))
#             if num == 0:
#                 # 输入0，直接退出循环，不参与累加
#                 break
#             s += num
#         except ValueError:
#             print("输入错误，请输入整数！")
#     return s
#
# a = calc_sum()
# print("所有数字总和：", a)