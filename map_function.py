"""
    Map() Function in Python
"""


def addition(n):
    return n * n


numbers = (1, 2, 3, 4, 5)
result = map(addition, numbers)
print(list(result))



number1 = [1, 2, 3, 4, 5]
number2 = [1, 2, 3, 4, 5]

res = map(lambda x, y: x*y, number1, number2)
print(list(res))
