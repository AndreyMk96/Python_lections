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
print("qwerty"[-1])  # Негативный индекс
print("qwerty"[2:4])  # Срез
print("qwerty"[2:-2])  # Так тоже можно
print("qwerty"[-4:-1])  # И даже так можно
print("qwerty"[:4])  # Если правый индекс не указан то начентся с нуля, если левый то до конца
print("qwertyuiop"[0:10:2])  # Срез с шагом
print("qwertyuiop"[10:0:-2])  # Шаг может быть отрицательным
print("qwertyuiop"[::-1])  # Так можно перевернуть строку
