"""Solve and graph quadratic equations entered by the user."""

import math

import matplotlib.pyplot as plt


while True:
    try:
        a_text = input("Enter a: ")
    except EOFError:
        break

    # Pressing ENTER without typing a value ends the program.
    if a_text.strip() == "":
        break

    a = float(a_text)
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        print("no real solutions")

        # Center the graph at the parabola's vertex.
        x_opt = -b / (2 * a)
        x_min = x_opt - 5
        x_max = x_opt + 5
    elif math.isclose(discriminant, 0.0, abs_tol=1e-12):
        x1 = -b / (2 * a)
        print(f"one solution: {x1:.5f}")

        # Put space on both sides of the repeated root.
        x_min = x1 - 5
        x_max = x1 + 5
    else:
        square_root = math.sqrt(discriminant)
        x1 = (-b - square_root) / (2 * a)
        x2 = (-b + square_root) / (2 * a)
        print(f"two solutions: x1={x1:.5f} x2={x2:.5f}")

        # Add a margin around the two roots so both are clearly visible.
        root_span = abs(x2 - x1)
        margin = max(2.0, root_span / 2)
        x_min = min(x1, x2) - margin
        x_max = max(x1, x2) + margin

    # Plot the quadratic function using exactly 150 x-values.
    step = (x_max - x_min) / 149
    x_values = [x_min + i * step for i in range(150)]
    y_values = [a * x**2 + b * x + c for x in x_values]

    plt.figure()
    plt.plot(x_values, y_values, label=f"{a:g}x^2 + {b:g}x + {c:g}")
    plt.axhline(0, color="black", linewidth=0.8)
    plt.axvline(0, color="black", linewidth=0.8)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Quadratic Function")
    plt.grid(True)
    plt.legend()
    plt.show()
