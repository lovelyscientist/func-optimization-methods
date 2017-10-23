PHI = 1.6180339887499
PSI = -0.61803398871499
REVERSE_SQUARE_ROOT_FIVE = 0.447213595499958


def fibonacci_number(n):
    return (PHI**n - PSI**n)*REVERSE_SQUARE_ROOT_FIVE


def calculate(goal_function, a, b, epsilon):
    x = 0
    n = 100

    while (b - a) > epsilon or n != 1:
        lamda = a + (b - a)*(fibonacci_number(n-2)/fibonacci_number(n))
        mu = a + (b - a)*(fibonacci_number(n-1)/fibonacci_number(n))

        if goal_function(lamda) <= goal_function(mu):
            b = mu
            x = lamda
        else:
            a = lamda
            x = mu

        n -= 1

    if n == 1:
        return (mu + lamda) / 2

    return x

