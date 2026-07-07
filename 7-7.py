# 定义函数 count_prime ()
# 接收用户输入一个大于 1 的整数 n，捕获非法输入
# 统计 2 ~ n 之间所有素数并打印，最后输出素数总个数
# 素数定义：只能被 1 和自身整除，2 是最小素数
# 示例：输入 10，素数为 2,3,5,7，一共 4 个
def countL_prime():
    try:
        n= int(input("请输入一个大于1的整数："))
        if n<=1:
            print("请重新输入！！")
            return
        else:

            count = 0
            s = []
            for i in range(2, n+1):

                for j in range(2, i):
                    if i % j == 0:
                        break
                    else:

                        if i not in s:
                            count += 1
                            s.append(i)

        print(f"输入 {n}，素数为 {s}，一共 {count} 个")
    except ValueError:print("输入错误请重新输入")
countL_prime()


# def count_prime():
#     try:
#         n = int(input("请输入一个大于1的整数："))
#         if n <= 1:
#             print("数字必须大于1，请重新输入！")
#             return
#
#         prime_list = []
#         # 遍历2 ~ n所有数字
#         for i in range(2, n + 1):
#             is_prime = True
#             # 只需要判断2 ~ i-1
#             for j in range(2, i):
#                 if i % j == 0:
#                     is_prime = False只要有一个有余数就不是素数了
#                     break
#             # 全部循环结束仍为True，才是素数
#             if is_prime:
#                 prime_list.append(i)
#
#         print(f"输入 {n}，素数为 {prime_list}，一共 {len(prime_list)} 个")
#     except ValueError:
#         print("输入错误请重新输入")
#
# count_prime()


