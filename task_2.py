"""
На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно.
Для проверки своего кода используйте модуль fractions.
"""
from fractions import Fraction


def fractions(frac1: str, frac2: str) -> str:
    """
    This function takes in two fractions in the form of strings and returns their sum and product as strings.
    The fractions are assumed to be in the format a/b, where a and b are integers.
    The function simplifies the fractions before performing the operations.
    The function uses the fractions module from the Python standard library to perform the operations.
    """
    a, b = int(frac1.split('/', 1)[0]), int(frac1.split('/', 1)[1])
    c, d = int(frac2.split('/', 1)[0]), int(frac2.split('/', 1)[1])

    sum_frac = Fraction(a * d + b * c, b * d)
    prod_frac = Fraction(a * c, b * d)

    return f'Sum: {sum_frac}\nProduct: {prod_frac}'


frac1 = "1/2"
frac2 = "1/3"

print(fractions(frac1, frac2))
print(f'Сумма дробей: {Fraction(frac1) + Fraction(frac2)}')
print(f'Произведение дробей: {Fraction(frac1) * Fraction(frac2)}')
