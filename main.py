from interpolation import *
import matplotlib.pyplot as plt
import scipy.interpolate

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
    print('Dodelat')
    for mean in y:
        if aim < mean:
            break
    return x[y.index(mean)], mean

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


#aim_mean = float(input('Введите целевую микротвердость: '))
aim_mean = 890

current_mean = 0
current_time = 0
new_time_knots = time_knots
new_time_mean = time_mean

if aim_mean > time_mean[len(time_mean)-1]:
    current_time = time_knots[len(time_knots)-1]
    current_mean = time_mean[len(time_mean)-1]
    while aim_mean > current_mean:
        current_time = current_time + 5
        current_mean = lagrange(current_time, new_time_knots, new_time_mean)
        new_time_knots.append(current_time)
        new_time_mean.append(current_mean)
    x_new = np.linspace(time_knots[0], time_knots[len(time_knots)-1], len(new_time_knots) * 20)
    func_new = splyne_interpolation(new_time_knots, new_time_mean, x_new)
    for mean in func_new:
        if mean > aim_mean:
            x_mean = x_new[func_new.index(mean)]
            break
    print('Требуемая температура {0}С, требуемое время эксперимента: {1} минут'.
          format(round(find_max_temp(x_temp, temp_res), 1), round(x_mean, 1)))
    plt.figure()
    plt.title('Time')
    plt.plot(x_new, func_new)
    plt.plot(new_time_knots, new_time_mean, 'x')
    plt.plot(x_mean, mean, '*')
elif aim_mean < time_mean[0]:
    for i in temp_res:

     '''   
    current_time = time_knots[0]
    current_mean = time_mean[0]
    while aim_mean < current_mean and current_time > 0:
        new_time_knots.insert(current_time, 0)
        print(new_time_knots)
        #new_time_mean.insert(lagrange(current_time, time_knots, time_mean), 0)
    print('Такой возможности не предусмотрено, свяжитесь с разработчиком')'''
else:
    answer, mean = find_into(x_time, time_res, aim_mean)
    print('Требуемая температура {0}С, требуемое время эксперимента: {1} минут'.
          format(round(find_max_temp(x_temp, temp_res), 1), round(answer, 1)))

    plt.figure()
    plt.title('Time')
    plt.plot(x_time, time_res)
    plt.plot(new_time_knots, new_time_mean, 'x')
    plt.plot(answer, mean, '*')

'''
plt.figure()
plt.title('Temperature')
plt.plot(x_temp, temp_res)
plt.plot(temp_knots, temp_mean, 'x')

plt.show()
'''