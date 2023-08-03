# Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях.
# Напишите к ним тесты.
# 2-5 тестов на задачу в трёх вариантах:

# тестирование pytest. 
# pytest .\home_work_13.py -vv - запуск в терминале

import math
import pytest


def test_not_root(*args, **kwargs):
    assert square_root(1, 2, 3) == 'уравнение не имеет корней'

def test_root(*args, **kwargs):
    assert square_root(4, 8, 3) == (-0.5, -1.5)

def test_type(*args, **kwargs):
    assert pytest.raises(TypeError, square_root, 'a', 2, 3) 

def test_missing_arg(*args, **kwargs):
    assert pytest.raises(TypeError, square_root, 1, 2)


def square_root(a, b, c):
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

if __name__ == '__main__':
    pytest.main(['-v'])