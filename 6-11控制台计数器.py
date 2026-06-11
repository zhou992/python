n = 0
m=0
while m==0:

    s= int(input("请选择操作：1=加1，2=减1，0=退出:"))
    if s==1:
        n+=s
    elif s==2:
        n= n-1
    elif s==0:
        m=1
    else : print("错误输入")
    print(f"当前数值为：{n}")