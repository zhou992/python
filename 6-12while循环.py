secret = 8
n=0
while n != secret:
    n = int(input("请输数字："))
    if n>secret:
        print("太大了")
    if n<secret:
        print("太小了")
print("猜对了")