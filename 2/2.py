"""
Для исправления требуется:
    1. перегружать метод __call__, а не создавать метод str
            def str(cls, *args, **kwargs)    ->     def __call__(cls, *args, **kwargs)
            
    2. в операторе ветвления мы должны проверять отсутствие экземпляра
            if cls in cls._instances    ->    if cls not in cls._instances
            
    3. через функцию super мы должны доставать метод __call__ из родителя
            super().call(*args, **kwargs)    ->    super().__call__(*args, **kwargs)
"""


class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


if __name__ == '__main__':
    print(__doc__)
    
    class Oleg(metaclass=SingletonMeta):
        pass

    class Igor():
        pass

    o1 = Oleg()
    o2 = Oleg()
    
    i1 = Igor()
    i2 = Igor()

    print('o1 ->', o1)
    print('o2 ->', o2)
    print('i1 ->', i1)
    print('i2 ->', i2)
    print('o1 is o2 -> ', o1 is o2)
    print('i1 is i2 -> ', i1 is i2)
    print('Потому что Игорей может быть много, \n а Олег один')
