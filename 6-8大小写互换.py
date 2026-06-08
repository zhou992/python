s = input("请输入一个字符串")
s_new = ''
for i in s:
    if 97<= ord(i) <=122 :
        s_new += chr(ord(i)-32)
    elif 65<= ord(i) <= 90:
        s_new += chr(ord(i)+32)
    else:
        s_new += i

print(s_new)