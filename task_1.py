"""
Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""

file_path_1 = "C:/Users/User/Documents/example.txt"
file_path_2 = 'file_in_current_directory.txt'


def get_file_info(file_path):
    if file_path.count('/'):
        q = file_path.rpartition('/')
        w = q[2].rpartition('.')
        return f'{q[0]}/', f'{w[0]}', f'.{w[2]}'
    else:
        q = file_path.rpartition('.')
        return '', f'{q[0]}', f'.{q[2]}'


print(get_file_info(file_path_1))
print(get_file_info(file_path_2))