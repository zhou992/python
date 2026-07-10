# 定义函数 binary_search ()
# 先录入一组数字（输入 - 1 结束），用冒泡排序升序
# 输入要查找的目标数字，使用二分查找
# 找到输出下标，找不到输出 “不存在该数字”
###错误案例
# def binary_search():
#     num=[]
#     while True:
#         n=int(input("请输入数字："))
#         if n!=-1:
#             num.append(n)
#         else:break
#     print(f"原数据：{num}")
#
#     for i in range(len(num)):
#         for j in range(len(num)-1):
#             if num[j]>num[j+1]:
#                 num[j],num[j+1]=num[j+1],num[j]
#     print(f"排序后数据：{num}")
#     s=int(input("请输入要查找的数字："))
#     left=0
#     right=len(num)-1
#     des=0
#
#     while num[des]!=s:
#         if num[right]==s:
#             des=right
#             break
#         des = (left + right) // 2
#         if num[des]>s:
#             right=des
#         else:left=des
#
#     print(des)
#
# binary_search()


def binary_search():
    num = []
    # 录入数字 + 异常捕获
    while True:
        try:
            n = int(input("请输入数字："))
            if n == -1:
                break
            num.append(n)
        except ValueError:
            print("请输入合法整数！")

    print(f"原数据：{num}")
    length = len(num)
    # 冒泡排序
    for i in range(length):
        for j in range(length - 1 - i):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j], num[j]
    print(f"排序后数据：{num}")

    # 输入查找目标
    try:
        target = int(input("请输入要查找的数字："))
    except ValueError:
        print("查找值必须是整数")
        return

    # 标准二分查找
    left = 0
    right = length - 1
    find_idx = -1

    while left <= right:
        mid = (left + right) // 2
        if num[mid] == target:
            find_idx = mid
            break
        elif num[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if find_idx == -1:
        print("不存在该数字")
    else:
        print(f"目标数字下标：{find_idx}")

binary_search()