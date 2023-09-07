x = 10
def factorial(value):
    result = 1
    for i in range(1, value):
        result += result * i
    print(result)
factorial(x)
