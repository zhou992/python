l = [10,20,30,40,50]
total =0
for i in l :
    print(i)
    total+=i
avrge = total/len(l)
print(f"总和：{total}")
print(f"平均值：{avrge:.2f}")#保留两位小数位数.2f