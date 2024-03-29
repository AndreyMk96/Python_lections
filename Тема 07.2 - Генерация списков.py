"""Тема 7.2 - Генерация списков"""

# Генерация списков - это способ создания списков, содержимое которых подчиняется определенному правилу
cubes = [i**3 for i in range(5)]
print(cubes)

# Генератор списков также может включать оператор if для применения условия к значениям в списке
evens = [i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)