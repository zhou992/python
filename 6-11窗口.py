import tkinter as tk
windows = tk.Tk()
from tkinter import messagebox
#定义函数
def click():
    input_text = input_box.get()
    # 检查是否为空
    if input_text == "":
        messagebox.showwarning("提示", "请输入内容")
        return

    try:
        # 转为整数
        number = int(input_text)

        if number > 0:
            messagebox.showinfo("结果", "这是一个正数")
        elif number < 0:
            messagebox.showinfo("结果", "这是一个负数")
        else:
            messagebox.showinfo("结果", "这是0")
    except ValueError:
        messagebox.showerror("错误", "请输入一个整数")


#设置窗口大小
windows.geometry("300x200")


#添加输入框
input_box = tk.Entry(windows)# 创建输入框

input_box.pack()    # 添加


#添加按钮

button = tk.Button(windows, text="输入",command=click,   bg="blue", fg="white"
   )
button.pack()  # 自动按顺序排列



windows.mainloop()


# import tkinter as tk
#
# windows = tk.Tk()
#
#
# # 定义函数
# def click():
#     input_text = input_box.get()
#
#     # 检查是否为空
#     if input_text == "":
#         result_label.config(text="请输入内容", fg="red")
#         return
#
#     try:
#         # 转为整数
#         number = int(input_text)
#
#         if number > 0:
#             result_label.config(text="这是一个正数", fg="green")
#         elif number < 0:
#             result_label.config(text="这是一个负数", fg="blue")
#         else:
#             result_label.config(text="这是0", fg="black")
#     except ValueError:
#         result_label.config(text="请输入一个整数", fg="red")
#
#
# # ... existing code ...
#
# # 设置窗口大小
# windows.geometry("300x200")
#
# # 添加输入框
# input_box = tk.Entry(windows)
# input_box.pack()
#
# # 添加结果显示标签
# result_label = tk.Label(windows, text="", font=("宋体", 12))
# result_label.pack(pady=10)
#
# # 添加按钮
# button = tk.Button(windows, text="输入", command=click, bg="blue", fg="white")
# button.pack()
#
# windows.mainloop()