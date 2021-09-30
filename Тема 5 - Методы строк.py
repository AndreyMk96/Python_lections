"""Тема 5 - Методы строк"""
my_str = "Toyota Rav - 4"
print(my_str.find('a'))  # Метод find возвращает позицию первого вхождения подстроки в строку
print(my_str.rfind('a'))  # Метод rfind возвращает позицию посленего вхождения подстроки в строку
my_str = my_str.replace('a', '*')  # Метод replace выполняет замену шаблона
print(my_str)
