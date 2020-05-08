#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter.tix import Tk, Control, ComboBox #升级的组合控件包
from tkinter.messagebox import showinfo, showwarning, showerror #各种类型的提示框
from tkinter.filedialog import *

root = Tk()  # 创建窗口对象的背景色
root.title("Comment Analysis") # 设置窗口标题
root.geometry("400x500") # 设置窗口大小 注意：是x 不是*
root.resizable(width=True, height=True) # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
root.tk.eval('package require Tix') #引入升级包，这样才能使用升级的组合控件

def test():
    with askopenfile(title="上传文件",initialdir="d:",filetypes=[("文本文件",".txt")]) as f:
        show["text"]=f.read()

Button(root,text="选择读取的文本文件",command=test).pack()


# lable.pack(side=TOP)

# button=Button(root,text='QUIT',command=root.quit,activeforeground="black",activebackground='blue',bg='red',fg='white')
# button.pack(fill=Y,expand=1)

# def resize(ev=None):
#     lable.config(font='Helvetica -%d bold'%scale.get())
# scale=Scale(root,from_=10,to=40,orient=HORIZONTAL,command=resize)
# scale.set(12)
# scale.pack()

# ct=Control(root,label='Number:',integer=True,max=12,min=2,value=2,step=2)
# ct.label.config(font='Helvetica 14 bold')
# ct.pack()

# cb=ComboBox(root,label='Type:',editable=True)
# for animal in ('dog','cat','hamster','python'):
#     cb.insert(END,animal)
# cb.pack()

# def click():
#     print("点击了一次")
# menubar=Menu(root)
# root.config(menu=menubar)
# filemenu=Menu(menubar,tearoff=0)
# menubar.add_cascade(label='文件',menu=filemenu)
# filemenu.add_command(label='新建...',command=click())
# filemenu.add_command(label='打开...',command=click())
# filemenu.add_command(label='保存',command=click())
# filemenu.add_command(label='关闭填写',command=root.quit)

# frame1 =Frame(root)
# frame1.pack(fill=X)
# lable1=Label(frame1,text='您的花名： ')
# lable1.grid(row=15,column=10)
#
# frame2=Frame(root)
# frame2.pack(fill=X)
# lable2=Label(frame2,text='您的性别： ')
# lable2.grid(row=1,column=0)
# sex=StringVar()
# sex_male=Radiobutton(frame2,text='男',fg='blue',variable=sex,value='男')
# sex_male.grid(row=1,column=2)
# sex_female=Radiobutton(frame2,text='女',fg='red',variable=sex,value='女')
# sex_female.grid(row=1,column=4)
#
# frame4 =Frame(root)
# frame4.pack(fill=X)
# lable4=Label(frame4,text='4、请删除您不会的变成语言： ')
# lable4.grid(row=1,column=0)
# listbox=Listbox(frame4)
# listbox.grid(row=1,column=1)
# for item in ["C","C++","JAVA","PYTHON","R","SQL","JS"]:
#     listbox.insert(END,item)
# DELETE=Button(frame4,text="删除",command=lambda listbox=listbox:listbox.delete(ANCHOR))
# DELETE.grid(row=1,column=2)
# language=Button(frame4,text="确定")
# language.grid(row=2,column=1)


root.mainloop()  # 进入消息循环