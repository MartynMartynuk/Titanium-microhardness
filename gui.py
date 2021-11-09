from tkinter import *
from tkinter.messagebox import *

class MyGui(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        frame_left = Frame(self)
        frame_left.pack(fill=Y, side=LEFT)
        self.label_depth = Label(frame_left, text='Введите глубину измерения, мкм', heigh=2, width=50)
        self.label_depth.pack()
        self.entry_depth = Entry(frame_left, width=50)
        self.entry_depth.pack()
        self.label_hv = Label(frame_left, text='Введите целевую микротвердость', heigh=2, width=50)
        self.label_hv.pack()
        self.entry_hv = Entry(frame_left, width=50)
        self.entry_hv.pack()
        label1 = Label(frame_left)    #костыль, выполняет функцию пробела между строкой ввода и кнопкой
        label1.pack()
        self.button = Button(frame_left, text='Calculate', command=self.push)
        self.button.pack()
        frame_right = Frame(self)
        frame_right.pack(fill=Y, side=RIGHT)
        self.output_field = Text(frame_right, heigh=15, width=60)
        self.output_field.pack()


    def push(self):
        #showinfo(message='Zaebis')
        pass
