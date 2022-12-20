
"""
Для исправления требуется добавить аргумент n в lambda функцию
"""

count_bits = lambda n: bin(n).count('1')


if __name__ == '__main__':
    print(__doc__)
    for i in range(0, 10):
        print(i, '\r\n  bin -> ', bin(i), '\r\n  count ->', count_bits(i), end='\n\n')
