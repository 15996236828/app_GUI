from tkinter  import *
from tkinter.filedialog import *
from tkinter import ttk  # 导入内部包
from tkinter import messagebox
import os
import threading
import time
import re

# class View(Frame):
#     count = 0
#     def __init__(self, *args, **kwargs):
#         Frame.__init__(self, *args, **kwargs)
#         h = 2
#         w = 10
#         b1 = Button(self, text="获取数据", command=self.new_window,height = h, width = w)
#         b1.pack()
#
#         b2 = Button(self, text="分类处理", command=self.new_window,height = h, width = w)
#         b2.pack()
#
#         b3 = Button(self, text="聚类+评级", command=self.new_window,height = h, width = w)
#         b3.pack()
#
#     def new_window(self):
#         self.count += 1
#         id = "New window #%s" % self.count
#         window = Toplevel(self)
#         label = Label(window, text=id)
#         label.pack()
#         b1 = Button(self, text="获取数据", command=self.new_window)
#         b1.pack()
#         window.mainloop()

class Getdata(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.new_window()

    def new_window(self):
        window = Toplevel(self)
        window.geometry("400x247")  # 设置窗口大小 注意：是x 不是*
        window.resizable(width=False, height=False)  # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True


        # label = Label(window, text=id)
        # label.pack()
        window.mainloop()


class Classify(object):
    def __init__(self):
        self.window = None
        self.tree = None
        self.new_window()

    def new_window(self):
        self.window = Toplevel()
        self.window.geometry("800x494")  # 设置窗口大小 注意：是x 不是*
        self.window.resizable(width=False, height=False)  # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True

        Button(self.window, text="点击选择数据文件夹",
               command=self.getfile).place(x=15, y=10, width=160, height=30, bordermode=INSIDE)

        self.tree = ttk.Treeview(self.window)  # 表格
        scr = Scrollbar(self.window)

        self.tree.config(yscrollcommand=scr.set)
        scr.config(command=self.tree.yview)
        self.tree["columns"] = ("评论", "类别")
        self.tree.column("#0", minwidth=0, width=0, stretch=NO)
        self.tree.column("评论", width=550)  # 表示列,不显示
        self.tree.column("类别", width=50)
        self.tree.heading("评论", text="评论")  # 显示表头
        self.tree.heading("类别", text="类别")

        self.tree.place(x=15, y=60, width=600, height=400, bordermode=INSIDE)
        scr.place(x=615, y=60, width=15, height=400)

        self.window.protocol("WM_DELETE_WINDOW", self.tuichu)   #重定义窗口关闭事件
        self.window.mainloop()

    def getfile(self):
        a = askdirectory()
        lable4=Label(self.window,text='runing......')
        lable4.place(x=190, y=10, width=160, height=30, bordermode=INSIDE)
        if a != "":
            order = "python ./bert/run_classifier.py --task_name=mytask --do_predict=true --data_dir="  + a +\
                    " --vocab_file=./bert/chinese_L-12_H-768_A-12/vocab.txt " \
                    "--bert_config_file=./bert/chinese_L-12_H-768_A-12/bert_config.json " \
                    "--init_checkpoint=./bert/mytask_output --max_seq_length=128 --output_dir=./bert/mrpc_output"
            os.system(order)
            order2 = "python get_result.py"
            os.system(order2)

        op = self.readdata()
        while 1:
            try:
                line = next(op)
            except StopIteration as e:
                break
            else:
                line = line.split(",")
                self.tree.insert('', 'end', values=[line[3], line[5]])
        # lable4.place_forget()

    def readdata(self):
        """逐行读取文件"""
        f = open(r"bert\glue\result.csv", 'r')
        # f = open(r"D:\classify\app_reviews.csv", 'r')
        line = f.readline()
        while line:
            yield line
            line = f.readline()
        f.close()

    def tuichu(self):
        self.window.quit()
        self.window.destroy()




if __name__ == "__main__":
    root = Tk()
    root.title("Comment Analysis")  # 设置窗口标题
    root.geometry("400x247")  # 设置窗口大小 注意：是x 不是*
    root.resizable(width=False, height=False)  # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True

    def get_data():
        data = Getdata(root)
        data.pack()
    b1 = Button(root, text="获取数据", command=get_data)
    b1.place(x=90,y=30,width=100,height=161,bordermode=INSIDE)

    def cl():
        root.withdraw()
        # root.update()
        cla = Classify()
        print("jieshu ")
        root.update()
        root.deiconify()
    b2 = Button(root, text="分类处理", command=cl)
    b2.place(x=200, y=30, width=100, height=80, bordermode=INSIDE)

    b3 = Button(root, text="聚类处理", command=get_data)
    b3.place(x=200, y=110, width=100, height=80, bordermode=INSIDE)

    # view = View(root)
    # view.place(x = 180, y = 25)
    root.mainloop()