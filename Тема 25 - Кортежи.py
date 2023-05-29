"""Тема 25 - Кортежи"""

# Кортеж - это список, объекты в котором неизменяемы
words = ("spam", "eggs", "sausages")
print(words, type(words))

# К элементу кортежа можно обратиться по индексу, также как в списках
print(words[1])

# Кортежи можно создавать без круглых скобок, разделяя значения запятыми
my_tuple = "one", "two", "three"
print(my_tuple[0])

# Распаковка кортежа позволяет присвоить каждый элемент кортежа переменной
numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)

# Если при распаковке кортежа перед какой либо переменной стоит *, то в нее занесутся все значения не вязтые
# в другие переменные
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)