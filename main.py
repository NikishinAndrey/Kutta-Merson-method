import numpy as np
import matplotlib.pyplot as plt

a = 1
b = 2
y_0 = np.exp(1) - 2


def function(x, y, delta):
    return 2 * x * (x ** 2 + y * (1 - delta))


def method(left, right, y_0, func, d, epsilon):
    mas_x = [left]
    mas_y = [y_0]
    mas_error = [0]
    step = 0.25
    value_x = left
    value_y = y_0
    mas_eta = np.zeros((1, 5))[0]
    mas_step = [step]

    def calculate_error(val_x, val_y, st):
        mas_eta[0] = func(val_x, val_y, d)
        mas_eta[1] = func(val_x + st / 3, val_y + st * mas_eta[0] / 3, d)
        mas_eta[2] = func(val_x + st / 3, val_y + st * mas_eta[0] / 6 + st * mas_eta[1] / 6, d)
        mas_eta[3] = func(val_x + st / 2, val_y + st * mas_eta[0] / 8 + 3 * st * mas_eta[1] / 8, d)
        mas_eta[4] = func(val_x + st,
                          val_y + st * mas_eta[0] / 2 - 3 * st * mas_eta[2] / 2 + 2 * st * mas_eta[3], d)
        approx_y = val_y + st * (mas_eta[0] - 3 * mas_eta[2] + 4 * mas_eta[3]) / 2
        val_y = val_y + st * (mas_eta[0] + 4 * mas_eta[3] + mas_eta[4]) / 6
        error_ = 0.2 * abs(val_y - approx_y)
        return error_, val_y

    def test_result(x_, y_, st_):
        test = calculate_error(x_, y_, st_)
        if test[0] < epsilon / 64:
            st_ *= 2
            return x_, y_, st_, test[0]
        elif test[0] < epsilon:
            x_ += st_
            y_ = test[1]
            return x_, y_, st_, test[0]
        else:
            st_ /= 2
            return test_result(x_, y_, st_)

    while value_x < right:
        result = test_result(value_x, value_y, step)
        value_x = result[0]
        value_y = result[1]
        step = result[2]
        mas_step.insert(0, step)
        mas_x.insert(0, result[0])
        mas_y.insert(0, result[1])
        mas_error.insert(0, result[3])
    mas_x.reverse()
    mas_y.reverse()
    mas_error.reverse()
    max_error = max(mas_error)
    min_step = min(mas_step)
    return mas_x, mas_y, mas_error, max_error, min_step


# ------------------------------------------------build_graph_1_2---------------------------------------------------------

result_1 = method(a, b, y_0, function, 0, 1e-1)
result_2 = method(a, b, y_0, function, 0, 1e-2)
result_3 = method(a, b, y_0, function, 0, 1e-3)


plt.figure(1)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('График №1')
x = np.linspace(1, 2, 100)
y = np.exp(x ** 2) - x ** 2 - 1
plt.plot(x, y, label='real')
plt.plot(result_1[0], result_1[1], '--.', label='1e-1')
plt.plot(result_3[0], result_3[1], '--x', label='1e-3')
plt.legend()

plt.figure(2)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('График №2')
plt.plot(result_2[0], result_2[2], '--.', label='1e-2')
plt.plot(result_3[0], result_3[2], '--x', label='1e-3')
plt.legend()


# ------------------------------------------------build_graph_3_4---------------------------------------------------------
def graph_3_4():
    tol = 1e-1
    mas_tol = []
    mas_error = []
    mas_sec = []
    mas_step = []
    step_0 = method(a, b, y_0, function,0, tol)[4]
    error_0 = method(a, b, y_0, function,0, tol)[3]
    mas_error_ = []
    for j in range(13):
        mas_tol.insert(0, tol)
        result = method(a, b, y_0, function,0, tol)
        mas_error.insert(0, result[3])
        mas_error_.insert(0, error_0 / result[3])
        mas_sec.insert(0, result[4])
        step = step_0 / result[4]
        mas_step.insert(0, step)
        tol = 0.1 * tol
    mas_tol.reverse()
    mas_error.reverse()
    mas_sec.reverse()
    mas_step.reverse()
    return mas_tol, mas_error, mas_sec, mas_step, mas_error_


check_2 = graph_3_4()

plt.figure(3)
plt.grid()
plt.yscale('log')
plt.xscale('log')
plt.xlabel('tolerance')
plt.ylabel('error')
plt.title('График №3')
plt.plot(check_2[0], check_2[0], label='exact error')
plt.plot(check_2[0], check_2[1], label='experimental error')
plt.legend()

plt.figure(4)
plt.grid()
plt.xscale('log')
plt.xlabel('tolerance')
plt.ylabel('minimal step')
plt.title('График №4')
plt.plot(check_2[0], check_2[2])

# ------------------------------------------------build_graph_5_6-------------------------------------------------------

def graph_5(tol):
    delta = 0.0
    mas_delta = []
    mas_error = []
    mas_y_real = method(a, b, y_0, function, 0, tol)[1]
    for j in range(5):
        mas_delta.insert(0, delta * 100)
        mas_y_approx = method(a, b, y_0 * (1 - delta), function, 0, tol)[1]
        length = len(mas_y_approx)
        result = np.zeros((1, length))[0]
        for k in range(length):
            result[k] = abs((mas_y_real[k] - mas_y_approx[k]) / mas_y_real[k])
        mas_error.insert(0, max(result) * 100)
        delta += 0.1
    mas_delta.reverse()
    mas_error.reverse()
    return mas_delta, mas_error


check_7_1 = graph_5(1e-1)
check_7_2 = graph_5(1e-6)

plt.figure(5)
plt.suptitle('График №5')
plt.subplot(1, 2, 1)
plt.grid()
plt.plot(check_7_1[0], check_7_1[1], label='tol = 1e-1')
plt.xlabel('start error, %')
plt.ylabel('relative error, %')
plt.legend()
plt.subplot(1, 2, 2)
plt.grid()
plt.plot(check_7_2[0], check_7_2[1], 'r', label='tol = 1e-6')
plt.xlabel('start error, %')
plt.legend()


def graph_6(tol):
    delta_ = 0.0
    mas_delta = []
    mas_error = []
    mas_y_real = method(a, b, y_0, function, 0, tol)[1]
    for j in range(5):
        mas_delta.insert(0, delta_ * 100)
        mas_y_approx = method(a, b, y_0, function, delta_, tol)[1]
        length = len(mas_y_approx)
        result = np.zeros((1, length))[0]
        for k in range(length):
            result[k] = abs((mas_y_real[k] - mas_y_approx[k]) / mas_y_real[k])
        mas_error.insert(0, max(result) * 100)
        delta_ += 0.1
    return mas_delta, mas_error


check_8_1 = graph_6(1e-1)
check_8_2 = graph_6(1e-6)

plt.figure(6)
plt.suptitle('График №6')
plt.subplot(1, 2, 1)
plt.grid()
plt.plot(check_8_1[0], check_8_1[1], label='tol = 1e-1')
plt.xlabel('error in equation, %')
plt.ylabel('relative error, %')
plt.legend()
plt.subplot(1, 2, 2)
plt.grid()
plt.plot(check_8_2[0], check_8_2[1], 'r', label='tol = 1e-6')
plt.xlabel('error in equation, %')
plt.legend()


plt.figure(7)
plt.grid()
plt.xlabel('количество отрезков разбиения')
plt.ylabel('уменьшение абсолютной погрешности')
plt.title('График №7')
check_2[3].pop(2)
check_2[3].pop(8)
plt.plot(np.arange(0, 517, 47), check_2[3])
plt.legend()
plt.show()

