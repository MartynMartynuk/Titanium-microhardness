from tkinter import *
from tkinter.messagebox import showinfo

class MyGui(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.label_depth = Label(text='Введите глубину измерения, мкм', heigh=2, width=50)
        self.label_depth.pack(side=TOP)
        self.entry_depth = Entry(width=50)
        self.entry_depth.pack(side=TOP)
        self.label_hv = Label(text='Введите целевую микротвердость', heigh=2, width=50)
        self.label_hv.pack(side=TOP)
        self.entry_hv = Entry(self, width=50)
        self.entry_hv.pack(side=TOP)
        label1 = Label(self)    #костыль, выполняет функцию пробела между строкой ввода и кнопкой
        label1.pack()
        self.button = Button(self, text='press me!', command=self.push)
        self.button.pack(side=TOP)
        label2 = Label(self)  # костыль, выполняет функцию пробела после кнопки
        label2.pack()

    def push(self):
        #showinfo(message='Zaebis')
        self.aim_depth = self.entry_depth.get()
        self.aim_mean = self.entry_hv.get()
        print(self.aim_depth)
        print(self.aim_mean)