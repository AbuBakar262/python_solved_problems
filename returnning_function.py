def create_adder(x):

    def adder(y, z):
        return x + y + z
    return adder


add = create_adder(10)
print(add(5, 4))
