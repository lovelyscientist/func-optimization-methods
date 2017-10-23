PHI = 1.6180339887499
REVERSED_PHI = 1/PHI


def calculate(goal_function, a, b, epsilon):
    x = 0

    while (b - a) > epsilon:
        lamda = b - (b - a)*REVERSED_PHI
        mu = a + (b - a)*REVERSED_PHI

        if goal_function(lamda) <= goal_function(mu):
            b = mu
            x = lamda
        else:
            a = lamda
            x = mu

    return x

