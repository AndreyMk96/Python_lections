"""Тема 18 - Цикл for подробнее"""
zoo_pets = ["lion", "hamster", "cat", "tiger", "cheetah", "dolphin"]
# Enumerate - возвращает номер и значение элемента в списке
for i, animal in enumerate(zoo_pets):
    print(i, animal)

# Списки можно перебирать также по срезам
# но так не очень хорошо с точки зрения памяти, так как создается еще один список
for animal in zoo_pets[::2]:
    print(animal)

# В Python так лучше не делать
for i in range(len(zoo_pets)):
    print(zoo_pets[i])

# Генерация целочисленных последовательностей
for i in range(100, 500, 50):  # Параметры start, stop, step
    print(i)

# Вложенные циклы
for animal in zoo_pets:  # Перебираем сначала по элементам
    for char in animal:  # А потом элемент по буквам
        print(char)