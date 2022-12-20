
"""
Для исправления требуется добавить в условие if пропущенную переменную number,
идущую на вход lambda функции
"""
even_or_odd = lambda number: "Even" if number % 2 == 0 else "Odd"


if __name__ == '__main__':
    print(__doc__)
    for i in range(-10, 10):
        print(i, ' -> ', even_or_odd(i))
