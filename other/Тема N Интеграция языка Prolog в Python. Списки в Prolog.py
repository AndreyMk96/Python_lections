"""Тема N Интеграция языка Prolog в Python при помощи библиотеки PySwip
Часть 3 списки в Prolog"""
from pyswip import Prolog
p = Prolog()
fruits = ['слива']
#f = str(fruits)
p.assertz(f"фрукты({fruits})")  # Задаем список
p.assertz("result(X) :- фрукты(L), member(X, L)")  # Задаем правило для проверки вхождения в список
print(list(p.query("result('слива').")))  # Выполняем запрос, если список не пустой, значит true
"""
# Попробуем добавить правило проверки вхождения двух элементов в список
p.assertz("result2(X,Y):- fruits(L), member(X, L), member(Y, L)")
print(list(p.query("result2(apple, orange).")))

# Создадим правило проверки вхождения одного из нескольких операторов в список
p.assertz("result3(X,Y):- fruits(L), member(X, L); fruits(L), member(Y, L)")
print(list(p.query("result3(aaqpple, oarange).")))

# Создадим правило проверки вхождения одного из операторов в несколько списков. Для этого оптимальным решением
# будет объединить списки и проверить вхождение элемента в объединенный список
p.assertz("fruits2([melon, pineapple, cranberry])")
p.assertz("result(X) :- fruits(L), member(X, L); fruits2(K), member(X, K)")
print(list(p.query("result(melon).")))"""
