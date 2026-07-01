# 定义函数 grade_level ()
# 输入分数，try 捕获非法输入
# 分级规则：
# 90 及以上：A
# 80~89：B
# 70~79：C
# 60~69：D
# 60 以下：E
# 输出对应等级
def grade_level():

    try:
        s=int(input("请输入分数："))
        if s >= 90:
            print("A")
        elif s >= 80:
            print("B")
        elif s >= 70:
            print("C")
        elif s >= 60:
            print("D")
        elif s < 60:
            print("E")
        else:
            print("请输入有效数字")
    except ValueError:
        print("请输入有效数字！！！")

grade_level()