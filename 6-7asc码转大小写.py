s = input("请输入一个字符串")

new_s = ''
for i in s:
    if 97<= ord(i) <=122 :
        new_chr = chr(ord(i)-32)    #ord:取出字符的 ASCII 码
    else:                           #chr:获取 ASCII 码对应的字符
        new_chr = i
    new_s = new_s + new_chr
print(new_s)