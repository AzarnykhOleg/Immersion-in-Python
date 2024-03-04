"""
Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""
num = 344
BASE = 16


def converts_numbers_by_base(number: int, base=BASE) -> str:
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36, inclusive")

    number_str = '0123456789abcdefghijklmnopqrstuvwxyz'
    if number == 0:
        return ''
    elif number < base:
        return number_str[number]

    return ("{0}{1}".format(converts_numbers_by_base(number // base, base), number_str[number % base])).upper()


print(f'Шестнадцатеричное представление числа: {converts_numbers_by_base(num)}')
print(f'Проверка результата: {hex(num)}')
