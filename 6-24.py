from os.path import split


def word_count():

    st = input("请输入一段英文句子：")
    s = st.split()
    n=len(s)
    print(f"单词总数为:{n},分别为: ")
    for i in s:
        print(i)

word_count()