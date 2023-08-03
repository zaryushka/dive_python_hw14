# Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях.
# Напишите к ним тесты.
# 2-5 тестов на задачу в трёх вариантах:

# тестирование doctest

import math

def square_root(a, b, c):
    """
    функция нахождени корней квадратного уравнения
    >>> square_root(1, 2, 3)
    'уравнение не имеет корней'
    >>> square_root(4, 8, 3)
    (-0.5, -1.5)
    >>> square_root('a', 2, 3)
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for -: 'int' and 'str'
    >>> square_root(1, 2)
    Traceback (most recent call last):
    ...
    TypeError: square_root() missing 1 required positional argument: 'c'
    """
    x1 = x2 = 0
    d = b**2 - 4 * a * c

    if d > 0:
        x1 = (-b  + math.sqrt(d)) / (2*a)
        x2 = (-b  - math.sqrt(d)) / (2*a)
        return x1, x2
    elif d == 0:
        x1 = (-b)/(2*a)
        return f'x1 = x2 = {x1}'
    else:
        return 'уравнение не имеет корней'
    
# print(square_root(1, 2, 3))
# print(square_root(4, 8, 3))
# print(square_root('a', 2, 3))
# print(square_root(1, 2))

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
