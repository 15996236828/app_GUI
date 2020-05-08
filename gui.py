from tkinter  import *
from tkinter.filedialog import *

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

class Classify():
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.new_window()

    def new_window(self):
        window = Toplevel(self)
        window.geometry("400x247")  # 设置窗口大小 注意：是x 不是*
        window.resizable(width=False, height=False)  # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True

        Button(window, text="点击选择csv格式的评论文件", command=getfile).pack()
        label = Label(window, text="请选择文件")
        label.pack()

    def getfile(self, window):
        a = askopenfilename()




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
        cla = Classify(root)
        cla.pack()
    b2 = Button(root, text="分类处理", command=cl)
    b2.place(x=200, y=30, width=100, height=80, bordermode=INSIDE)

    b3 = Button(root, text="聚类处理", command=get_data)
    b3.place(x=200, y=110, width=100, height=80, bordermode=INSIDE)

    # view = View(root)
    # view.place(x = 180, y = 25)
    root.mainloop()