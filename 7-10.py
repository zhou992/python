# 函数 bubble_sort()
# 循环输入数字，输入 - 1 结束；输入文字捕获异常提示重输
# 手写冒泡排序从小到大
# 打印原列表、排序后列表
def bubble_sort():

        s = []

        while True:
            try:
                n = int(input("请输入数字："))
                if n == -1:
                    break
                else:s.append(n)
            except ValueError:
                print("输入错误，请重新输入")
        print("原列表：",s)
        for i in s:
            for j in range(len(s) - 1):
                if s[j] > s[j + 1]:
                    s[j], s[j + 1] = s[j + 1], s[j]

        print("排序后列表：",s)


bubble_sort()