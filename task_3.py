"""
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

Под "успешной расстановкой ферзей" в данном контексте подразумевается такая расстановка ферзей на шахматной доске,
в которой ни один ферзь не бьет другого.
Другими словами, ферзи размещены таким образом, что они не находятся на одной вертикали, горизонтали или диагонали.

Список из 4х комбинаций координат сохраните в board_list. Дополнительно печатать его не надо.
"""
from random import randrange
# from task_2 import check_queens


def generate_boards():
    board_list = []
    while len(board_list) < 4:
        board_ = []
        while len(board_) < 8:
            x_ = randrange(1, 9)
            y_ = randrange(1, 9)
            if (x_, y_) not in board_:
                board_.append((x_, y_))
        if board_ not in board_list:  # and check_queens(board_)
            board_list.append(board_)
    return board_list


print(generate_boards())
