"""
Дан список повторяющихся элементов lst. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
"""

lst = [1, 4, 1, 2, 2, 4, 4, 4, 3, 3]


def recurring_element(lst):
    sorted_lst = sorted(lst)
    unique_list = []
    for i in range(len(lst) - 1):
        if sorted_lst[i] == sorted_lst[i + 1]:
            unique_list.append(sorted_lst[i])
    recurring_elements_set = set(unique_list)
    recurring_elements_list = list(recurring_elements_set)

    return recurring_elements_list


print(recurring_element(lst))
