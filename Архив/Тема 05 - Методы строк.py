"""Тема 5 - Методы строк"""
my_str = "Toyota Rav - 4"
print(my_str.find('a'))  # Метод find возвращает позицию первого вхождения подстроки в строку
print(my_str.rfind('a'))  # Метод rfind возвращает позицию посленего вхождения подстроки в строку
my_str = my_str.replace('a', '*')  # Метод replace выполняет замену шаблона
print(my_str)
my_str = my_str.upper()  # Метод upper приводит строку к верхнему регистру
print(my_str)
my_str = my_str.lower()  # Метод lower приводит строку к нижнему регистру
print(my_str)
print(my_str.isalpha())  # Метод isalpha возвращает True, если строка состоит только из букв. Иначе возвр. False
print(my_str.isnumeric())  # Метод isnumeric возвращает True, если строка состоит только из цифр
# Левый Ctrl, превращает функцию в ссылку на библиотеку с этой функцией (особенность PyCharm)
# остальные функции дописать самостоятельно
