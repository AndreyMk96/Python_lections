"""Тема N - ООП - урок 1. Классы и объекты. Атрибуты классов и объектов"""


class Point:
    """Создадим класс Point. По pep - 8 классы именуются в CamelCase"""
    color = "red"  # Переменные внутри класса, называют атрибутами класса или его свойствами
    circle = 2


print(Point.circle)  # Обратиться к атрибуту класса можно через его имя
print(Point.__dict__)  # Все атрибуты класса можно вывести при помощи переменной __dict__

# Создание объекта - экземпляра класса
a = Point()
b = Point()

print(type(a))  # a - это объект класса Point 
print(isinstance(a, Point))  # Проверить принадлежность объекта к классу можно функцией isinstance

print(a.circle)  # Экземпляры берут атрибуты у класса на основе которого они созданы
print(a.__dict__)  # Видно что словарь пустой. У экземпляра а нет своих атрибутов
Point.circle = 1
print(a.circle)  # Если их изменить в исходном классе, они изменятся у экземпляров

a.color = "white"  # В данном случае создается отдельный атрибут для экземпляра
print(Point.color, a.color)  # Видно что значения разные
print(id(Point.color), id(a.color))  # Идентификаторы тоже разные

a.x = 100  # Экземплярам класса, можно добавлять новые атрибуты
setattr(a, "y", 200)  # Также добавлять и изменять атрибуты можно про помощи функции setattr
setattr(a, 'x', 250)
print(a.x, a.y)

print(getattr(a, 'x'))  # Получить значение атрибута можно при помощи функции getattr
print(getattr(Point, 'x', "Такого атрибута нет"))  # В функцию getattr можно задать третий аргумент - исключение

del a.x  # Удалить атрибут можно функцией del
print(a.__dict__)
print(hasattr(a, 'x'), hasattr(a, "y"))  # Проверить принадлежит ли атрибут классу можно функцией hasattr
delattr(a, 'y')  # Также удалить атрибут можно функцией delattr

del a.color  # Если удалить атрибут у экземпляра
print(a.color)  # То атрибут будет браться непосредственно у исходного класса

# Атрибут изначально ищется в исходном пространстве имен,
# А если не находится, то берется из внешнего пространства имен


print(Point.__doc__)  # Описание класса можно вывести при помощи переменной __doc__
