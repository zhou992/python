arr = [5, 18, 3, 26, 9, 41, 32, 7, 14]
ji =[]
ou =[]
for i in arr:
    if i % 2==0:
        ou.append(i)
    else:ji.append(i)
print(f"奇数：{ji}")
print(f"偶数：{ou}")
