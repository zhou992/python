i = 1
while i<=20:
    if i%2!=0:
        i += 1  # 跳过奇数
        continue
    if i==18:
        break

    print(i)

    i+=1