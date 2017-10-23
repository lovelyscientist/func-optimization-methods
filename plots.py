import matplotlib.pyplot as plt
import numpy as np


def draw(goal_function, a, b, x_min_dichotomy, x_min_golden_section, x_min_fibonacci):
    x = np.linspace(a, b, 100)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # Move left y-axis and bottim x-axis to centre, passing through (0,0)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')

    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')

    # Eliminate upper and right axes
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # Show ticks in the left and lower axes only
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    plt.plot(x, goal_function(x), color="violet")
    plt.plot([x_min_fibonacci], [goal_function(x_min_fibonacci)], marker='s', markersize=8, color="red", label="fibonacci")
    plt.plot([x_min_golden_section], [goal_function(x_min_golden_section)], marker='o', markersize=6, color="yellow", label="golden section")
    plt.plot([x_min_dichotomy], [goal_function(x_min_dichotomy)], marker='x', markersize=4, color="green", label="dichotomy")
    plt.title("Minimum of F(x) by dichotomy, golden section and fibonacci methods")
    plt.legend()
    plt.show()

