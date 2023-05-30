"""
    Function 1 to use as a decorator
"""


def attach_data(func):
    func.data = "Attach Data 1"
    return func


"""
    Function 2 to use as a decorator
"""


def attach_data2(func):
    func.value = "Attach Data 2"
    return func


"""
    Function 1 to use as a decorator
"""


def attach_data3(func):
    func.stri = "Attach Data 3"
    return func

name = "umair"

print(name)
name = "ali"


number = [1, 2, 3, 4, 5]

def funct(number):
    return number

# Object.freeze(abc)
num_dict = {
    "one": 1,
    "two": 2
}
print('dict',num_dict.popitem())
@attach_data3
@attach_data2
@attach_data
def add(x, y):
    return x + y


print(add(3, 2))
print(add.data)
print(add.value)
print(add.stri)
