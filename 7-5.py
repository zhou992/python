# 定义函数 is_palindrome ()
# 输入正整数，异常捕获非法输入
# 判断数字是否是回文（正读、反读一样，如 121、1331）
# 打印 “是回文数” 或 “不是回文数”
def is_palindrome():
    try:
        n=(input("请输入数字："))
        s = int(n)
        if s<= 0:
                print("请输入正整数！")
                return
        s= n[::-1]
        if n==s:
            print("是回文数")
        else:print("不是回文数")
    except ValueError:print("请输入整数！！！")
is_palindrome()
