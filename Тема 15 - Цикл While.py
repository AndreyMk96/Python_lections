"""Тема 15 - Цикл While"""

# Цикл - это неоднократное повторение одного и того же участка кода

"""Цикл while позволяет выполнять последовательность действий, пока проверяемое условие истинно. Условие записывается
до тела цикла и проверяется до выполнения тела цикла. Как правило, цикл while используется, когда невозможно определить 
точное значение проходов исполнения цикла"""

# while <условие>:
#     <блок кода>

print("Здравствуйте")
i = 0  # переменная цикла должна меняться внутри цикла
while i < 10:
    print(i)
    i += 1
print("До свидания")

# Последовательность Фибоначчи при помощи цикла While
f1, f2 = 1, 1
while f2 < 1000:
    print(f2)
    f1, f2 = f2, f1 + f2

# Операторы в цикле:
# else
# break
# continue

# While else
i = 10
while i < 10:
    print(i)
    i *= 2
else:
    print("i >= 10 ")

# Оператор break
my_pets = ["dog", "cat", "hamster"]
i = 0
while i < len(my_pets):
    print("Проверяем " + my_pets[i])
    if my_pets[i] == "cat":
        print("Ура, кот найден!!")
        break
    i += 1
else:
    print("не нашли.....")

# Оператор continue
my_pets2 = ["lion", "dog", "cat", "skunk", "hamster", "monkey"]
i = -1
while i < len(my_pets2):
    i += 1
    if i == 2:
        continue
    if my_pets2[i] == "cat":
        print("Ура! Кот найден!")
        break
else:
    print("Ничего не найдено")

# Бесконечный цикл:
while True:
    print("Hello World")