import copy


class Developer():
    _count = 0
    def __new__(cls, *args, **kwargs):
        cls._count += 1
        if cls._count > 3:
            raise TypeError("3 objects already created.")
        cls.name = kwargs.get("name")


dev_obj  = Developer("Abubakar")
dev1 = Developer("Ali")
dev2 = Developer("Baber")
dev3 = Developer("BaberIbrar")
dev4 = Developer("BaberIbrar")
dev5 = Developer("BaberIbrar")
dev6 = copy.deepcopy(dev3)


print(dev_obj, dev1, dev2, dev5, dev4)