import tkinter
from tkinter import ttk  # 导入内部包
from tkinter import *
import csv
import re


def readdata():
    """逐行读取文件"""

    # 读取gbk编码文件，需要加encoding='utf-8'
    f = open(r"D:\classify\app_reviews.csv" , 'r')
    line = f.readline()
    while line:
        yield line
        line = f.readline()
    f.close()


win = tkinter.Tk()
tree = ttk.Treeview(win)  # 表格
scr = Scrollbar(win)

tree.config(yscrollcommand=scr.set)
scr.config(command=tree.yview)
tree["columns"] = ("评论", "类别")
tree.column("#0",minwidth=0,width=0, stretch=NO)
tree.column("评论", width=400)  # 表示列,不显示
tree.column("类别", width=50)



tree.heading("评论", text="评论")  # 显示表头
tree.heading("类别", text="类别")


op = readdata()
while 1:
    try:
        line = next(op)
    except StopIteration as e:
       break
    else:
        line = line.split(",")
        tree.insert('','end',values=[line[1],line[0]])


tree.pack(side=LEFT, fill=Y)
scr.pack(side=RIGHT, fill=Y)
win.mainloop()
