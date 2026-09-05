import math

import matplotlib.pyplot as plt


def plot_function(fun_str, domain, ns):
    xmin, xmax = domain
    step = (xmax - xmin) / (ns - 1)

    xs = []
    ys = []

    for i in range(ns):
        x = xmin + i * step
        xs.append(x)
        y = eval(fun_str)
        ys.append(y)

    print()
    print("{:>15} {:>15}".format("x", "y"))
    print("{:>15} {:>15}".format("-" * 15, "-" * 15))

    for x, y in zip(xs, ys):
        print("{:15.5f} {:15.5f}".format(x, y))

    plt.figure()
    plt.plot(xs, ys)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("y = " + fun_str)
    plt.grid(True)
    plt.show()


function_string = input("Enter function with variable x: ")
x_min = float(input("Enter xmin: "))
x_max = float(input("Enter xmax: "))
number_of_samples = int(input("Enter number of samples: "))

plot_function(function_string, (x_min, x_max), number_of_samples)
