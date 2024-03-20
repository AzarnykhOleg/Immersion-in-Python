"""
Напишите код, решающий задачу о 8 ферзях, включающий в себя
функцию is_attacking(q1,q2), проверяющую, бьют ли ферзи друг друга и
check_queens(queens), которая проверяет все возможные пары ферзей.

Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.

Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь. Не забудьте напечатать результат.
"""


def overlapping_fields(x, y):
    overlapping_fields_set_x = {(x, i) for i in range(1, 9)}
    overlapping_fields_set_y = {(k, y) for k in range(1, 9)}
    overlapping_fields_set = overlapping_fields_set_x.union(overlapping_fields_set_y)
    x_, y_ = x, y
    while x_ < 8 and y_ < 8:
        x_ += 1
        y_ += 1
        overlapping_fields_set.add((x_, y_))
    x_, y_ = x, y
    while x_ > 1 and y_ > 1:
        x_ -= 1
        y_ -= 1
        overlapping_fields_set.add((x_, y_))
    x_, y_ = x, y
    while x_ < 8 and y_ > 1:
        x_ += 1
        y_ -= 1
        overlapping_fields_set.add((x_, y_))
    x_, y_ = x, y
    while x_ > 1 and y_ < 8:
        x_ -= 1
        y_ += 1
        overlapping_fields_set.add((x_, y_))
    return overlapping_fields_set


def is_attacking(q1, q2):
    if q1 in overlapping_fields(q2[0], q2[1]):
        return True
    else:
        return False


def check_queens(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if is_attacking(queens[i], queens[j]):
                return False
            else:
                continue
    return True


if __name__ == "__main__":
    print(overlapping_fields(8, 1))

    q1 = (1, 1)
    q2 = (4, 2)
    print(is_attacking(q1, q2))

    queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6)]
    print(check_queens(queens))
