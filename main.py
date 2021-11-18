import matplotlib.pyplot as plt
from gui import *
from functions import *

#значения эксперимента по вариации времени
time_knots = [5, 10, 20, 30]
time_mean = [553.08, 622.09, 470.43, 478.23]

#значения эксперимента по вариации температур
temp_knots = [600, 700, 800, 850]
temp_mean = [439.73, 474.82, 468.49, 500.19]

#разбиение имеющихся координат по х
x_time = np.linspace(time_knots[0], time_knots[len(time_knots)-1], len(time_knots) * 20)
x_temp = np.linspace(temp_knots[0], temp_knots[len(temp_knots)-1], len(temp_knots) * 20)

time_res = splyne_interpolation(time_knots, time_mean, x_time)
temp_res = splyne_interpolation(temp_knots, temp_mean, x_temp)

#значения микротвердости по глубине измерения
depth_knots = [10, 30, 50, 70, 100, 130, 160, 200, 300, 400, 500, 600, 700, 800]
depth_mean = [1.302,	1.12,	1.088,	1.038,	1.019,	0.998,	0.975,	0.951,
              0.923,	0.875,	0.818,	0.802,	0.799,	0.771]

#значения шероховатости по температуре
harsh_temp = [2.549, 3.086, 2.368, 2.609]
x_harsh_temp = [600, 700, 800, 850]

#значения шероховатости по времени
harsh_time = [0.714, 2.400, 2.411, 3.201]

class NewGui(MyGui):
    def __init__(self):
        super().__init__()
        self.i = 0
        self.xplot = []
        self.yplot = []
        self.xknots = []
        self.yknots = []
        self.xans = 100500
        self.yans = 100500
        self.tittle = ''

    def push(self):
        try:
            self.depth_in = float(self.entry_depth.get())
            #print('depth = ', self.depth_in)
            assert self.depth_in >= 10 and self.depth_in <= 800, \
                showerror(title='Микротвердость титана', message='Ошибка!\n Глубина измерения должна быть от 10 до 400 мкм')
            self.hv_in = float(self.entry_hv.get())
            #print('hv = ', self.hv_in)
            assert self.hv_in >= 450, \
                showerror(title='Микротвердость титана', message='Ошибка!\n Целевая микротвердость должна быть больше 450')
        except EOFError:
            showerror(title='Микротвердость титана', message='Ошибка "конец ввода"!\n . Повторите ввод')
        except:
            showerror(title='Микротвердость титана', message='Ошибка!\n Пожалуйста повторите ввод')
        self.i += 1
        answer, self.xplot, self.yplot, self.xknots, self.yknots, self.xans, self.yans, self.tittle\
            = calculation(self.hv_in, self.depth_in)

        self.output_field.insert(END, '\n {0}) {1}; \n'.format(str(self.i), answer))

    def graph(self):
        if self.xans == 100500 and self.yans == 100500:
            showerror(title='Микротвердость титана', message='Ошибка!\n Сначала выполните раcсчет')
        else:
            plt.figure()
            plt.title(self.tittle)
            plt.plot(self.xplot, self.yplot)
            plt.plot(self.xknots, self.yknots, 'x')
            plt.plot(self.xans, self.yans, '*')
            plt.show()

def calculation(aim_mean, aim_depth):
    dep_coef = splyne_function(depth_knots, depth_mean, aim_depth)
    aim_mean = aim_mean * dep_coef
    if aim_mean > time_mean[len(time_mean) - 1]:
        x_mean, mean, x_new, func_new = find_right(time_knots, time_mean, aim_mean)
        # harsh_answer = lagrange(x_mean, time_knots, harsh_time)
        harsh_answer = linear_interpolate(x_mean, time_knots[-2:], harsh_time[-2:])
        output = 'Требуемая температура {0}С, требуемое время эксперимента: {1} минут. Прогнозная средняя шероховатость ~ {2}'\
            .format(round(find_max_temp(x_temp, temp_res), 1), round(x_mean, 1), round(harsh_answer, 1))
        xPlot = x_new
        yPlot = func_new
        xKnots = time_knots
        yKnots = time_mean
        xAns = x_mean
        yAns = mean
        title = 'Время'
    elif aim_mean < time_mean[0]:
        x_mean, mean, x_new, func_new = find_left(temp_knots, temp_mean, aim_mean)
        # harsh_answer = lagrange(x_mean, temp_knots, harsh_time)
        harsh_answer = linear_interpolate(x_mean, temp_knots, harsh_temp)
        output = 'Требуемая температура {0}С, требуемое время эксперимента: {1} минут. Прогнозная средняя шероховатость ~ {2}'\
            .format(round(x_mean, 1), 10, round(harsh_answer, 1))
        xPlot = x_new
        yPlot = func_new
        xKnots = temp_knots
        yKnots = temp_mean
        xAns = x_mean
        yAns = mean
        title = 'Температура'
    else:
        answer, mean = find_into(x_time, time_res, aim_mean)
        harsh_answer = lagrange(answer, time_knots, harsh_time)
        output = 'Требуемая температура {0}С, требуемое время эксперимента: {1} минут. Прогнозная средняя шероховатость ~ {2}'\
            .format(round(find_max_temp(x_temp, temp_res), 1), round(answer, 1), round(harsh_answer, 1))
        xPlot = x_time
        yPlot = time_res
        xKnots = time_knots
        yKnots = time_mean
        xAns = answer
        yAns = mean
        title = 'Время'
    return output, xPlot, yPlot, xKnots, yKnots, xAns, yAns, title

window = NewGui()
window.title('')
window.mainloop()
plt.close()