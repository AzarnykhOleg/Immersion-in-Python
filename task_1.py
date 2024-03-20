"""
Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем.
На вход будет подаваться дата в формате "день.месяц.год".
Ваша задача - создать программу, которая проверяет, является ли введенная дата корректной или нет.

Ваша программа должна предоставить ответ "True" (дата корректна) или "False" (дата некорректна)
в зависимости от результата проверки.
"""

DAYS_ORDINARY_YEAR = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
LEAP_YEAR_DAYS = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
NUMBER_OF_MONTHS = 12


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def syntax_validation(string):
    try:
        day, month, year = string.split('.')
        return int(day), int(month), int(year)
    except ValueError:
        return False


def date_validation(date_to_prove):
    if syntax_validation(str(date_to_prove)):
        day, month, year = syntax_validation(date_to_prove)
        if (is_leap_year(year) and month in range(1, NUMBER_OF_MONTHS + 1)
                and day in range(1, LEAP_YEAR_DAYS[month] + 1) and year in range(1, 10000)):
            return True
        else:
            if month in range(1, NUMBER_OF_MONTHS + 1) and day in range(1, DAYS_ORDINARY_YEAR[
                                                                               month] + 1) and year in range(1, 10000):
                return True
            else:
                return False
    else:
        return False


date_to_prove = '15.4.2023'
print(date_validation(date_to_prove))
