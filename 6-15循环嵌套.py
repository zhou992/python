
# 题目：打印简单行列图案
# 要求：
# 一共打印 3 行
# 每一行输出 4 个 *

for i in range(3):
    for n in range(4):
        print("*",end="")
    print("")

## while 嵌套写法
# row = 0
# while row < 3:
#     col = 0
#     while col < 4:
#         print("*", end="")
#         col += 1
#     print()  # 换行
#     row += 1