def get_avg():
    s = 0
    cou = 0
    m = 0
    min = 999999
    while True:

        try:

            n = int(input("请输入分数"))
            if n== -1:
                break
            s+=n

            cou+=1
            if n>m:
                m=n
            if n<min:
                min=n
        except ValueError:
            print("请输入整数！")
    print(f"总分{s},平均分{s/cou},最高分{m} ，最低分{min}")
get_avg()
