from tkinter import *
from tkinter.messagebox import *

class MyGui(Tk):
    def __init__(self):
        Tk.__init__(self)
        label_ttl = Label(self, text='Оптимизация катодного электролитно-плазменного азотирования'
                                     'титановых сплавов\n для управления микротвердостью '
                                     'поверхностного слоя математическими методами')
        label_ttl.pack()
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
        self.button = Button(frame_left, text='Рассчитать', width=35, command=self.push)
        self.button.pack()
        label2 = Label(frame_left, heigh='1')
        label2.pack()
        self.button_graph = Button(frame_left, text='Показать график', width=35, command=self.graph)
        self.button_graph.pack()
        frame_right = Frame(self)
        frame_right.pack(fill=Y, side=RIGHT)
        self.output_field = Text(frame_right, heigh=15, width=60)
        self.output_field.pack()

    def push(self):
        pass

    def graph(self):
        pass