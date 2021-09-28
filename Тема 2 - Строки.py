a = "Andrey"
b = """asadsad
asdadsad
sdfdfsdfs"""
print(a, b)
print("hello" * 2)
print("hello" + " " + "world")
print("abc" == "abc")
print("a" > "A", "a" > "c")

"""Индексация строк"""
print("qwerty"[0])
print("qwerty"[-1])  # негативный индекс
print("qwerty"[2:4])  # срез
print("qwerty"[2:-2])  # так тоже можно
print("qwerty"[-4:-1])  # и даже так можно
print("qwerty"[:4])  # если правый индекс не указан то начентся с нуля, если левый то до конца
print("qwertyuiop"[0:10:2])  # срез с шагом
print("qwertyuiop"[10:0:-2])  # шаг может быть отрицательным
print("qwertyuiop"[::-1])  # так можно перевернуть строку
