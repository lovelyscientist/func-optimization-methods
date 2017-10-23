def calculate(goal_function, a, b, epsilon, delta):
    x = 0

    while (b - a) > epsilon:
        lamda = (a + b - delta)/2
        mu = (a + b + delta)/2

        if goal_function(lamda) < goal_function(mu):
            b = mu
            x = lamda
        else:
            a = lamda
            x = mu

    return x

