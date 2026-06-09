scores = [85,60,99,75,60,88,60,92]
n = int(input("请输入一个数字"))
count = 0
for i in scores:
    if i ==n:
        count +=1
print(f"数字{n}出现了{count}次")