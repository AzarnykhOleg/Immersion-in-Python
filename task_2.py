"""
Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
имена str, ставка int, премия str с указанием процентов вида 10.25%.
В результате result получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
"""

names = ["Grace", "John", "Linda"]
salary = [6200, 5800, 7500]
bonus = ["9%", "3%", "12%"]


def premium_calculation(names, salary, bonus):
    my_calculation_dict = {}
    for name, pay, extra in zip(names, salary, bonus):
        my_calculation_dict[name] = pay * float(extra.strip('%')) / 100
    return my_calculation_dict


result = {name: pay * float(extra.strip('%')) / 100 for name, pay, extra in zip(names, salary, bonus)}

print(premium_calculation(names, salary, bonus))
print(result)
