from interpolation import *

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