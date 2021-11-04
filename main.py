from interpolation import *
import matplotlib.pyplot as plt

#значения эксперимента по вариации времени
time_knots = [5, 10, 20, 30]
time_mean = [859.78, 879.59, 888.29, 893.62]

#значения эксперимента по вариации температур
temp_knots = [650, 700, 800, 850]
temp_mean = [870.09, 904.98, 898.04, 835.41]

x_time = np.linspace(time_knots[0], time_knots[len(time_knots)-1], len(time_knots) * 20)
x_temp = np.linspace(temp_knots[0], temp_knots[len(temp_knots)-1], len(temp_knots) * 20)

time_res = splyne_interpolation(time_knots, time_mean, x_time)
temp_res = splyne_interpolation(temp_knots, temp_mean, x_temp)
'''
aim_mean = float(input('Введите целевую микротвердость: '))
aim_dev = [aim_mean - 0.1 * aim_mean, aim_mean + 0.1 * aim_mean]
'''
opt_hard = 0
for i in temp_res:
    if i > opt_hard:
        opt_hard = i
        opt_temp = x_temp[temp_res.index(i)]
print(opt_temp)

time_point = linear_interpolate(35, time_knots[-2:], time_mean[-2:])
time_dop = [35, 45, 50]
#x_new, extra = extrapolation_with_linear(time_knots, time_mean, time_dop)
'''
plt.figure()
plt.title('Time')
#plt.plot(x_new, extra)
plt.plot(time_knots, time_mean, 'x')

'''
plt.figure()
plt.title('Temperature')
plt.plot(x_temp, temp_res)
plt.plot(temp_knots, temp_mean, 'x')

plt.show()
