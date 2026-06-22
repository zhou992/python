try:
    n = int(input("请输入一个数字："))
    print(f"你输入的数字是：{n}")
except ValueError:
    print("请重新输入整数")