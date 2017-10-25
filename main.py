import dichotomy_method
import golden_section_method
import fibonacci_method
import plots
import math


def goal_function(x): return x**4-4*x**2-4*x+1
epsilon = 0.00001
delta = epsilon/1000
a = -10
b = 10
n = 100

x_min_dichotomy = dichotomy_method.calculate(goal_function, a, b, epsilon, delta)
x_min_golden_section = golden_section_method.calculate(goal_function, a, b, epsilon)
x_min_fibonacci = fibonacci_method.calculate(goal_function, a, b, epsilon)

print(x_min_golden_section)
print(x_min_dichotomy)
print(x_min_fibonacci)

plots.draw(goal_function, a, b, x_min_golden_section, x_min_dichotomy, x_min_fibonacci)
