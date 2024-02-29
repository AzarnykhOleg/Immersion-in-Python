# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним,
# только если треугольник существует.
def checking_triangle(a, b, c):
    if a == b == c:
        result = 'Треугольник существует\nТреугольник равносторонний'
    elif a > b+c or b > a+c or c > a+b:
        result = 'Треугольник не существует'
    elif a == b or a == c or b == c:
        result = 'Треугольник существует\nТреугольник равнобедренный'
    else:
        result = 'Треугольник существует\nТреугольник разносторонний'
    return result

print(checking_triangle(4, 9, 4))