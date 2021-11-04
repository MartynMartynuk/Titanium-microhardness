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

time_point = lagrange(35, time_knots, time_mean)

plt.figure()
plt.title('Time')
plt.plot(x_time, time_res)
plt.plot(time_knots, time_mean, 'x')

plt.figure()
plt.title('Temperature')
plt.plot(x_temp, temp_res)
plt.plot(temp_knots, temp_mean, 'x')

plt.show()
