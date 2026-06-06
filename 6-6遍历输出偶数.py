num = int(input("请输入整数："))
total = 0
for i in range(2,num+1,2):      #range的用法（start,stop,step)包括开始start，不包括结束stop
    print(i)
    total +=1
print(f'1到{num}中偶数有{total}个')


# num = int(input("请输入整数："))
# total = 0
# for i in range(1, num+1):
#     if i % 2 == 0:        #使用if判断奇偶
#         print(i)
#         total += 1
# print(f'1到{num}中偶数有{total}个')