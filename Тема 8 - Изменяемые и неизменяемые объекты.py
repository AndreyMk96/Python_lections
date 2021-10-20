"""Тема 8 - изменяемыи и неизменяеые объекты"""
# Список - изменяемый объект
my_list = [1, 2, 3, 4, 5]
second_list = my_list
my_list.append(100)
print(second_list)  # Связанный список меняется так же как и исходный
# Строка - неизменяемый объект
my_str = "Andrey"
# my_str[1] = '*'
# print(my_str) # Будет выдана ошибка
my_str.replace('n', '*')
print(my_str)  # Результат не изментится
my_str = my_str.replace('n', '*')
print(my_str)  # Чтобы строка изменилась, ее надо перезаписывать
# Число - неизменяемый объект
valve = 42
print(id(valve))
mass = valve
print(id(mass))
mass += 1
print(id(mass))  # Видно, что при изменении mass становится другим объектом
# Строка байтов - неизменяемый объект
# Кортеж - тоже что и список, только неизменяемый
my_tuple = (1, 2, 3)
print(my_tuple, type(my_tuple))
my_tuple += (4, 5, 6)  # При сложении кортежей происходит их перезапись
print(my_tuple)
