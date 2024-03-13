"""
Напишите функцию для транспонирования матрицы transposed_matrix:
принимает в аргументы matrix, и возвращает транспонированную матрицу.
"""

matrix = [[1, 2], [3, 4]]


def transposed_matrix(matrix):
    return [list(row) for row in zip(*matrix)]


print(transposed_matrix(matrix))
