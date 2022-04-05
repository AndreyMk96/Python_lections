"""Тема 16 - Цикл For"""
"""Цикл for используется для перебора какой либо последовательности"""
# for <переменная> in <список>:
#    <блок кода>
zoo_pets = ["tiger", "horse", "cheetah", "skunk", "mouse"]
for pet in zoo_pets:
    print(pet)

# Оператор break прерывает цикл
for pet in zoo_pets:
    if pet == "cheetah":
        break
    print(pet)

# В цикле for также может быть оператор else.
# Он срабатывает при выходе из цикла
for pet in zoo_pets:
    if pet == "elephant":
        break
else:
    print("Слона в списке нет")
