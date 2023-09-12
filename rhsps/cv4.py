# pylint: disable=missing-module-docstring,missing-function-docstring
x = 10
def factorial(value):
    result = 1
    for i in range(1, value):
        result += result * i
    return result
factorial(x)
