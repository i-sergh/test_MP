"""
Для починки требуется:
    1. начинать с первого элемента в первом split
            re.split('_|-', text)[1]    ->    re.split('_|-', text)[0]
        это избавит от ошибки IndexError: list index out of range
        Причина ошибки: при невозможности разбиения более чем на 2 элемента, мы не можем обратиться ко второму
            
    2. внутри выражения for внутри итерируемого split нужно убрать кавычки, обособляющие text
            for word in re.split('_|-', 'text')[1::]    ->    for word in re.split('_|-', text)[1::]
        В изначальном варианте мы проходимся по строке 'text'
        В исправленном - по строке, находящейся в переменной text
    """


import re


def to_camel_case(text):
    return re.split('_|-', text)[0] + ''.join(word.title() for word in re.split('_|-', text)[1::])


if __name__ == '__main__':
    print(__doc__)

    print(
        to_camel_case('oneword'),
        to_camel_case('two-words'),
        to_camel_case('four_words_WiTH_underscore'),
        sep='\n')

