from interpolation import *
import matplotlib.pyplot as plt
from gui import *

#finding optimum temperature
def find_max_temp(x, y):
    optimal_hard = 0
    for mean in y:
        if mean > optimal_hard:
            optimal_hard = mean
            optimal_temp = x[y.index(mean)]
    return optimal_temp

#finding nearest in massive
def find_into(x, y, aim):
    for mean in y:
        if aim < mean:
            break
    return x[y.index(mean)], mean

#finding nearest to aim right
def find_right(x_knots, y_mean, aim):
    current_x = x_knots[len(x_knots) - 1]
    current_mean = y_mean[len(y_mean) - 1]
    new_knots = x_knots.copy()
    new_mean = y_mean.copy()
    while aim > current_mean:
        current_x = current_x + 5
        current_mean = lagrange(current_x, x_knots, y_mean)
        new_knots.append(current_x)
        new_mean.append(current_mean)
    x_new = np.linspace(new_knots[0], new_knots[len(new_knots) - 1], len(new_knots) * 20)
    y_new = splyne_interpolation(new_knots, new_mean, x_new)
    answer = 0
    for mean in y_new:
        if mean > aim:
            answer = x_new[y_new.index(mean)]
            break
    return answer, mean, x_new, y_new

#finding nearest to aim left
def find_left(x_knots, y_mean, aim):
    current_x = x_knots[0]
    current_mean = y_mean[0]
    new_knots = x_knots.copy()
    new_means = y_mean.copy()
    while aim < current_mean:
        current_x = current_x - 10
        #current_mean = lagrange(current_x, new_knots, new_means)
        current_mean = linear_interpolate(current_x, x_knots, y_mean)
        new_knots.insert(0, current_x)
        new_means.insert(0, current_mean)
    x_new = np.linspace(new_knots[0], new_knots[len(new_knots) - 1], len(new_knots) * 20)
    y_new = splyne_interpolation(new_knots, new_means, x_new)
    for mean in y_new:
        if mean > aim:
            answer = x_new[y_new.index(mean)]
            break
    return answer, mean, x_new, y_new

#значения эксперимента по вариации времени
time_knots = [5, 10, 20, 30]
time_mean = [859.78, 879.59, 888.29, 893.62]

#значения эксперимента по вариации температур
temp_knots = [650, 700, 800, 850]
temp_mean = [870.09, 904.98, 898.04, 835.41]

#разбиение имеющихся координат по х
x_time = np.linspace(time_knots[0], time_knots[len(time_knots)-1], len(time_knots) * 20)
x_temp = np.linspace(temp_knots[0], temp_knots[len(temp_knots)-1], len(temp_knots) * 20)

time_res = splyne_interpolation(time_knots, time_mean, x_time)
temp_res = splyne_interpolation(temp_knots, temp_mean, x_temp)

#значения микротвердости по глубине измерения
depth_knots = [10, 30, 50, 70, 100, 130, 160, 200, 300, 400]
depth_mean = [0.400, 0.974, 1.140, 1.112, 1.098, 1.079, 1.067, 1.055, 1.029, 1.011]

#значения шероховатости по температуре
harsh_temp = [2.167, 2.036, 2.694, 0.830]
x_harsh_temp = [650, 700, 800, 850]

#значения шероховатости по времени
harsh_time = [0.714, 2.400, 2.411, 3.201]

class NewGui(MyGui):
    def __init__(self):
        MyGui.__init__(self)

    def push(self):
        try:
            self.depth_in = float(self.entry_hv.get())
            assert self.depth_in >= 10 and self.depth_in <= 400, \
                showinfo(message='Ошибка!\n Глубина измерения должна быть от 10 до 400 мкм')
            print('depth = ', self.depth_in)
            self.hv_in = float(self.entry_hv.get())
            assert self.hv_in >= 450, \
                showinfo(message='Ошибка!\n Целевая микротвердость должна быть больше 450')
            print('hv = ', self.hv_in)

        except:
            showinfo(message='Ошибка!\n Пожалуйста повторите ввод')
        calculation(self.hv_in, self.depth_in)

def calculation(aim_mean, aim_depth):
    dep_coef = splyne_function(depth_knots, depth_mean, aim_depth)
    aim_mean = aim_mean / dep_coef

    if aim_mean > time_mean[len(time_mean) - 1]:
        x_mean, mean, x_new, func_new = find_right(time_knots, time_mean, aim_mean)
        # harsh_answer = lagrange(x_mean, time_knots, harsh_time)
        harsh_answer = linear_interpolate(x_mean, time_knots[-2:], harsh_time[-2:])
        print(
            'Требуемая температура {0}С, требуемое время эксперимента: {1} минут. Прогнозная средняя шероховатость ~ {2}'.
            format(round(find_max_temp(x_temp, temp_res), 1), round(x_mean, 1), round(harsh_answer, 1)))
        plt.figure()
        plt.title('Time')
        plt.plot(x_new, func_new)
        plt.plot(time_knots, time_mean, 'x')
        plt.plot(x_mean, mean, '*')
        plt.show()
    elif aim_mean < time_mean[0]:
        x_mean, mean, x_new, func_new = find_left(temp_knots, temp_mean, aim_mean)
        # harsh_answer = lagrange(x_mean, temp_knots, harsh_time)
        harsh_answer = linear_interpolate(x_mean, temp_knots, harsh_temp)
        print(
            'Требуемая температура {0}С, требуемое время эксперимента: {1} минут. Прогнозная средняя шероховатость ~ {2}'.
            format(round(x_mean, 1), 10, round(harsh_answer, 1)))
        plt.figure()
        plt.title('Temperature')
        plt.plot(x_new, func_new)
        plt.plot(temp_knots, temp_mean, 'x')
        plt.plot(x_mean, mean, '*')
        plt.show()
    else:
        answer, mean = find_into(x_time, time_res, aim_mean)
        harsh_answer = lagrange(answer, time_knots, harsh_time)
        print(
            'Требуемая температура {0}С, требуемое время эксперимента: {1} минут. Прогнозная средняя шероховатость ~ {2}'.
            format(round(find_max_temp(x_temp, temp_res), 1), round(answer, 1), round(harsh_answer, 1)))
        plt.figure()
        plt.title('Time')
        plt.plot(x_time, time_res)
        plt.plot(time_knots, time_mean, 'x')
        plt.plot(answer, mean, '*')
        plt.show()


window = NewGui()
window.pack()
window.mainloop()

'''
try:
    aim_depth = float(input('Введите глубину измерения: '))
    assert aim_depth >= 10 and aim_depth <= 400, print('Глубина измерения должна быть от 10 до 400 мкм')
    aim_mean = float(input('Введите целевую микротвердость: '))
    assert aim_mean >=450, print('Целевая микротвердость должна быть больше 450')
except EOFError:
    print('EOF ERROR, please return input')
    input('Press any key')
except KeyboardInterrupt:
    print('Операция прервана пользователем')
    input('Press any key')
except:
    print('Error, please return input')
    input('Press any key')

#aim_mean = 1200

dep_coef = splyne_function(depth_knots, depth_mean, aim_depth)
aim_mean = aim_mean / dep_coef

if aim_mean > time_mean[len(time_mean)-1]:
    x_mean, mean, x_new, func_new = find_right(time_knots, time_mean, aim_mean)
    #harsh_answer = lagrange(x_mean, time_knots, harsh_time)
    harsh_answer = linear_interpolate(x_mean, time_knots[-2:], harsh_time[-2:])
    print('Требуемая температура {0}С, требуемое время эксперимента: {1} минут. Прогнозная средняя шероховатость ~ {2}'.
          format(round(find_max_temp(x_temp, temp_res), 1), round(x_mean, 1), round(harsh_answer, 1)))
    plt.figure()
    plt.title('Time')
    plt.plot(x_new, func_new)
    plt.plot(time_knots, time_mean, 'x')
    plt.plot(x_mean, mean, '*')
    plt.show()
elif aim_mean < time_mean[0]:
    x_mean, mean, x_new, func_new = find_left(temp_knots, temp_mean, aim_mean)
    #harsh_answer = lagrange(x_mean, temp_knots, harsh_time)
    harsh_answer = linear_interpolate(x_mean, temp_knots, harsh_temp)
    print('Требуемая температура {0}С, требуемое время эксперимента: {1} минут. Прогнозная средняя шероховатость ~ {2}'.
          format(round(x_mean, 1), 10, round(harsh_answer, 1)))
    plt.figure()
    plt.title('Temperature')
    plt.plot(x_new, func_new)
    plt.plot(temp_knots, temp_mean, 'x')
    plt.plot(x_mean, mean, '*')
    plt.show()
else:
    answer, mean = find_into(x_time, time_res, aim_mean)
    harsh_answer = lagrange(answer, time_knots, harsh_time)
    print('Требуемая температура {0}С, требуемое время эксперимента: {1} минут. Прогнозная средняя шероховатость ~ {2}'.
          format(round(find_max_temp(x_temp, temp_res), 1), round(answer, 1), round(harsh_answer, 1)))
    plt.figure()
    plt.title('Time')
    plt.plot(x_time, time_res)
    plt.plot(time_knots, time_mean, 'x')
    plt.plot(answer, mean, '*')
    plt.show()
    '''
