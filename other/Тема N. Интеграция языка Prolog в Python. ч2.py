"""Тема N Интеграция языка Prolog в Python при помощи библиотеки PySwip
Часть 2 работа с вопросами"""
from pyswip import Prolog
p = Prolog()

p.assertz("man :- verify(man)")
p.assertz("great_driver :- verify(great_driver)")
p.assertz("more_money :- verify(have_a_more_money)")
p.assertz("sport_car :- verify(like_a_sport_car)")
p.assertz("ask(Question) :- write('Please, enter yes or no You:  '), write(Question), write('? '),read(Response),nl,"
          "( (Response == yes ; Response == y)->assert(yes(Question)) ;assert(no(Question)), fail)")
p.assertz("verify(S) :- (yes(S)->true ;(no(S)->fail ;ask(S)))")

print(list(p.query("man(X).")))