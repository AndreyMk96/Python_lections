"""Тема 19 - Цикл for и словари (методы перебора словарей)"""
zoo_pets_mass = {
    "lion": 300,
    "skunk": 5,
    "elephant": 5000,
    "horse": 400
}
# Посчитаем общую массу животных
total_mass = 0
for animal in zoo_pets_mass:
    total_mass += zoo_pets_mass[animal]
print(total_mass)

# Метод items возвращает элементы словаря в формате ключ / значение
for animal, mass in zoo_pets_mass.items():
    print("масса " + animal + "(a) = " + str(mass))

# Только значения можно вернуть методом Values()
total_mass = 0
for mass in zoo_pets_mass.values():
    total_mass += mass
print(total_mass)

# Только ключи словаря можно вернуть методом Keys()
for animal in zoo_pets_mass.keys():
    print("У нас в зоопарке есть " + animal)