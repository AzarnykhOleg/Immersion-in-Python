"""
На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в качестве значения.

Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
Предметы не должны дублироваться.

Результат должен быть в виде словаря {предмет:вес} с вещами в рюкзаке и сохранен в переменную backpack.

Достаточно получить один допустимый вариант и сохранить в переменную backpack. Не выводите backpack на экран.
"""

items = {
    "спальник": 2.0,
    "палатка": 3.5,
    "термос": 0.8,
    "карта": 0.2,
    "фонарик": 0.5,
    "котелок": 1.0,
    "еда": 3.0,
    "одежда": 1.8,
    "обувь": 1.0,
    "нож": 0.3
}
max_weight = 10.0

def get_backpack(items: dict[str, float], max_weight: float):
    backpack = {}
    backpack_weight = 0
    for item, weight in items.items():
        if weight + backpack_weight <= max_weight:
            backpack[item] = weight
            backpack_weight += weight
    return backpack


print(get_backpack(items, max_weight))
