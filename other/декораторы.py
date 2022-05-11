"""Декораторы"""

def make(func):
    def wrapper(x, y):
        print(x)
        func()
        print(y)
    return wrapper

@make
def print_name():
    print("Andrey")

#make(print_name)
#print_name = make(print_name)
#таким образом мы изменили функцию print name. Это можно сделать проще, при помощи декоратора
print_name(10,20)
#это изпользуется
#в ботах телеграм/дискорд, ассинхронном программировании