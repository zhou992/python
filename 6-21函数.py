# 定义函数 list_sum(lst)，参数是一个数字列表
# 函数内部循环计算列表所有数字总和，return 总和
# 测试列表 data = [2,5,9,13,6]，调用函数并打印总和
def list_sum(lst):
    s=0
    for i in lst:
        s+=i
    return s


data = [2,5,13,6]

a=list_sum(data)
print(a)

