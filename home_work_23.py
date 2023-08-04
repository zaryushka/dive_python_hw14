# тестирование pytest. 


import math
import pytest


class CalcError(Exception):
    pass
    
class ZeroDivisionError(CalcError):
    def __str__(self):
        return f'Division by zero is not possible.'

class NegativeValueError(CalcError):
    def __str__(self):
        return f'You entered a negative number. It is impossible to get the square root or logarithm.'
    
class TypeError(CalcError):
    def __str__(self):
        return 'Wrong type of arguments.'


class Calculator:
    def __init__(self):
        pass

    def calc(self, operation: str, *args):
        
        list_operation_scientific = ['sin', 'cos', 'tan', 'log', 'sqrt']
        list_operation_simple = ['+', '-', '*', '/']
                

        if operation in list_operation_scientific:
            try:
                num1 = float(args[0])
            except:
                raise TypeError
            result = None
            if operation == 'sin':
                result = math.sin(num1)
            elif operation == 'cos':
                result = math.cos(num1)
            elif operation == 'tan':
                result = math.tan(num1)
            elif operation == 'log':
                if num1 < 0:
                    raise NegativeValueError
                result = math.log(num1)
            elif operation == 'sqrt':
                if num1 < 0:
                    raise NegativeValueError
                result = math.sqrt(num1)

            return f'Результат: {result}'

        if operation in list_operation_simple:
            try:
                num1 = float(args[0])
                num2 = float(args[1])
            except:
                raise TypeError
            result = None

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    raise ZeroDivisionError
                result = num1 / num2

            return f'Результат: {result}'

        if operation not in list_operation_scientific and operation not in list_operation_simple:
            raise TypeError

# my_calc = Calculator()
# my_calc.calc('sqrt', 16)

def test_sgrt(*args):
    my_calc = Calculator()
    my_calc.calc('sqrt', 16) == 4

def test_sub(*args):
    my_calc = Calculator()
    my_calc.calc('-', 16, 10) == 6

def test_div(*args):
    my_calc = Calculator()
    my_calc.calc('/', 16, 4) == 4

def test_div_bad(*args):
    with pytest.raises(ZeroDivisionError):
        my_calc = Calculator()
        my_calc.calc('/', 16, 0)

def test_type_operation(*args):
    with pytest.raises(TypeError):
        my_calc = Calculator()
        my_calc.calc('a', 2, 3)

def test_log(*args):
    my_calc = Calculator()
    my_calc.calc('log', 16, 4) == 2

def test_negative_args(*args):
    with pytest.raises(NegativeValueError):
        my_calc = Calculator()
        my_calc.calc('log', -16, 4)
        my_calc.calc('sqrt', -16)

def test_type_args_scientific(*args):
    with pytest.raises(TypeError):
        my_calc = Calculator()
        my_calc.calc('log', 'a')

def test_type_args_simple(*args):
    with pytest.raises(TypeError):
        my_calc = Calculator()
        my_calc.calc('+', 'a', 2)

if __name__ == '__main__':
    pytest.main(['-v'])

# pytest .\home_work_21.py -vv - запуск в терминале