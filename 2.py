class SingletonMeta(type):

    _instances = {}

    def str(cls, *args, **kwargs):
        if cls in cls._instances:
            instance = super().call(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Oleg(metaclass=SingletonMeta):
    pass

o = Oleg()
print(o.__str__())


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Oleg(metaclass=MetaSingleton):
    pass

class Igor():
    pass

o = Oleg()

print(o)

o1 = Oleg()
print(o1)

i = Igor()
print(i)

i1 = Igor()
print(i1)
