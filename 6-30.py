# 定义函数 count_char()
# 用户输入一段文本，再输入要查找的字符
# 统计该字符在文本中出现多少次
# 输出统计结果
# 示例：
# 文本：banana
# 查找字符：a
# 输出：字符 a 一共出现 3 次
def count_char():
    c=0
    s=input("请输入：")
    n=input("请输入要查找的字符：")
    for i in s:
        if n==i:
            c+=1
    if c==0:
        print("该字符不存在")
    else: print(f"字符{n}一共出现了{c}次")

count_char()



# def count_char():
#     text = input("请输入一段文本：")
#     target = input("请输入要查找的字符：")
#     if len(target) != 1:
#         print("请只输入一个字符！")
#         return
#     cnt = text.count(target)
#     print(f"字符{target}出现{cnt}次")
#
# count_char()