class A:
    x = 10

    def __init__(self):
        self.name = "Sonata"
        self._model = 2024
        self.__make = 'Hyndai'

    def get_public(self):
        return self.__make

objA = A()
print(objA.x)
print(objA.name)
print(objA._model)
print(objA.get_public())