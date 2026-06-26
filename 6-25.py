# 定义函数 filter_num()
# 用户输入一串混合数字和文字的内容，例如：a12b34c56d7
# 遍历每一个字符，把所有数字挑出来拼成新字符串
# 打印提取出的纯数字
# 示例输入：apple88banana9
# 输出：提取到的数字：889
def filter_num():
    n = ""
    str = input("请输入：")
    for i in str:
        if 48<=ord(i)<=58:
            n+=i
    print(n)


filter_num()


# def filter_num():         #isdigit判断是不是数字
#     res = ""
#     text = input("请输入：")
#     for char in text:
#         if char.isdigit():
#             res += char
#     print("提取到的纯数字：", res)
#
# filter_num()