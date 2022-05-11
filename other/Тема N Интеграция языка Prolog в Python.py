"""Тема N Интеграция языка Prolog в Python при помощи библиотеки PySwip
Часть 1 задание предикатов"""
from pyswip import Prolog
p = Prolog()

# Задаем правила
p.assertz("father(michael, gina)")  # Михаэль приходится отцом Джине
p.assertz("father(michael, john)")  # Михаэль приходится отцом Джону
p.assertz("father(michael, lauren)")  # Михаэль приходится отцом Лорен

# Выводим список детей Михаэля
print(list(p.query("father(michael,X).")))

# Укажем пол каждого ребенка
p.assertz("gender(gina, woman)")
p.assertz("gender(john, man)")
p.assertz("gender(lauren, woman)")

# Выводим список детей Михаэля, у которых пол Женский
print(list(p.query("father(michael,X), gender(X,woman).")))

# Укажем возраст каждого ребенка
p.assertz("age(gina, 10)")
p.assertz("age(john, 12)")
p.assertz("age(lauren, 15)")

# Выведем список детей, чей возраст меньше введенного пользователем с клавиатуры
child_age = int(input("Введите возраст ребенка: "))
print(list(p.query("father(michael,X), age(X,Y), Y < %s." %(child_age))))

# Зададим правила брат и сестра
# Братом является человек, с которым у которого такой же отец, и пол - мужской
# Сестрой является человек, с которым у него такой же отец, и пол - женский
p.assertz("brother(X,Y):- father(Z,X),father(Z,Y),X\=Y,gender(X, man)")
p.assertz("sister(X,Y):- father(Z,X),father(Z,Y),X\=Y,gender(X, woman)")

# Выведем на печать братьев Джины и сестер Джона
print(list(p.query("brother(X, gina).")))
print(list(p.query("sister(X, john).")))
