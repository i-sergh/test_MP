## Для исправления требуется:
1. перегружать метод `__call__`, а не создавать метод `str`
```
def str(cls, *args, **kwargs)    ->     def __call__(cls, *args, **kwargs)
```

2. в операторе ветвления мы должны проверять отсутствие экземпляра
```
if cls in cls._instances    ->    if cls not in cls._instances
```

3. через функцию `super` мы должны доставать метод `__call__` из родителя
```
super().call(*args, **kwargs)    ->    super().__call__(*args, **kwargs)
```
