"""
    Passing Function as Arguments in other function
"""


def uppr(text):
    return text.upper()


def lowr(text):
    return text.lower()


def greet(func):
    greeting = func('Hello World')
    return greeting


print(greet(uppr))
print(greet(lowr))
