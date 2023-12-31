# тестирование doctest

import math


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
        """
        Класс калькулятор
        >>> my_calc.calc('sqrt', 16)
        Результат: 4.0
        >>> my_calc.calc('log', 16, 4)
        Результат: 2.772588722239781
        >>> my_calc.calc('log', -16, 4)
        Traceback (most recent call last):
        ...
        NegativeValueError: You entered a negative number. It is impossible to get the square root or logarithm.
        >>> my_calc.calc('sqrt', -16)
        Traceback (most recent call last):
        ...
        NegativeValueError: You entered a negative number. It is impossible to get the square root or logarithm.
        >>> my_calc.calc('log', 'a')
        Traceback (most recent call last):
        ...
        TypeError: Wrong type of arguments.
        >>> my_calc.calc('+', 'a', 2)
        Traceback (most recent call last):
        ...
        TypeError: Wrong type of arguments.
        >>> my_calc.calc('-', 16, 10)
        Результат: 6.0

        """
        
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

            print(f'Результат: {result}')

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

            print(f'Результат: {result}')

        if operation not in list_operation_scientific and operation not in list_operation_simple:
            raise TypeError

my_calc = Calculator()


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)