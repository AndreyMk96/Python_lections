"""Тема N - Механизм полиморфизма"""
# Полиморфизм - это возможность работать с разными объектами единым образом(через единый интерфейс)


class Geom:
    def get_pr(self):
        #return "Для данной фигуры определить периметр невозможно"
        raise NotImplementedError("Нет метода get_pr")


class Rectangle(Geom):
    """Создадим класс прямоугольник"""
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_rect_pr(self):
        """Функция возвращающая периметр прямоугольника"""
        return (self.w + self.h) * 2

    def get_pr(self):
        return (self.w + self.h) * 2


class Square(Geom):
    """Создадим класс квадрат"""
    def __init__(self, a):
        self.a = a

    def get_sq_pr(self):
        """Функция возвращающая периметр квадрата"""
        return self.a * 4

    def get_pr(self):
        return self.a * 4


class Triangle(Geom):
    """Создадим класс Треугольник"""
    def __init__(self, a , b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_tr_pr(self):
        return self.a + self.b + self.c

    def get_pr(self):
        return self.a + self.b + self.c

# Создадим экземпляры классов
r1 = Rectangle(1,2)
r2 = Rectangle(3,4)
s1 = Square(5)
s2 = Square(10)

# Вызовем функцию возвращающую периметр
print(r1.get_rect_pr(), r2.get_rect_pr())
print(s1.get_sq_pr(), s2.get_sq_pr())

# Занесем экземпляры в список
figures = [r1, r2, s1, s2]
# Попробуем вывести площать для всех элементов списка
# Решение в лоб
for f in figures:
    if isinstance(f, Rectangle):
        print(f.get_rect_pr())
    if isinstance(f, Square):
        print(f.get_sq_pr())

# Добавим треугольники
t1 = Triangle(1,2,3)
t2 = Triangle(4,5,6)
figures.append(t1)
figures.append(t2)

# в цикле прописывать проверку на каждый тип данных неудобно
# нет ни красоты, ни гибкости
# можно в каждом классе создать метод возвращающий периметр, и назвать его единым образом
for f in figures:
    print(f.get_pr())

# Каждая ссылка списка ведет строго на свой объект
# Однако если в каком либо классе не реализовать такой геттер, то  это приведет к ошибке
# Избавиться от этого можно созданием базового класса (в нашем случае класс Geom)
# Однако это тоже не самое лучшее решение
# Лучше добавить исключение NotImplementedError, читая это исключение мы сразу поймем в чем проблема



