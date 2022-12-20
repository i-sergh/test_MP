"""
Для исправления требуется:
    1. в тернарном операторе if переместить n в позицию перед if:
            if n < 10 n else    ->    n if n < 10 else
    2. исправить имя функции sum (убрать двойное m):
            summ    ->    sum
"""

def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))


if __name__ == '__main__':

    def strSequense():
        st = ''
        def inner(var=''):
            nonlocal st
            st += str(var)
            return st
        return inner

    print(__doc__)

    newSeq = strSequense()
    for i in range(6):
        print(newSeq(i), ' -> ', digital_root(int(newSeq())))
