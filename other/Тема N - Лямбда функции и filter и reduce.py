"""Тема N. Функции Filter и Reduce"""
import functools
"""filter() возвращает элементы итерации, для которых функция возвращает True. Если вы передадите None в функцию, 
тогда filter() будет использовать функцию идентификации. Это означает, что filter() проверяет значение истинности 
каждого элемента в итерации и отфильтровывает все элементы, которые являются ложными."""

L = [1, -2, 3, -4, 5]
print(list(filter(lambda x: x > 0, L)))

L2 = ["One", "Two", "Three", "Four", "Five"]
print(list(filter(lambda x: len(x) > 3, L2)))

"""Reduce() — еще один основной функциональный инструмент в Python, который полезен, когда вам нужно применить функцию 
к итерируемому объекту и уменьшить его до одного накопительного значения. Этот вид операции обычно известен как 
сокращение или складывание"""


def f(x, y):
    print(x, y)
    return x + y


L3 = functools.reduce(f, L)  # Находим сумму всех элементов списк при помощи reduce
print(L3)

L4 = functools.reduce(lambda x, y: x + y, L)  # Тоже самое, но при помощи лямбда функции
print(L4)