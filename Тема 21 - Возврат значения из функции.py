"""Тема 21 - Возврат значения из функции"""


# Функция возвращает значения при помощи ключевого слова return

def power(number, pow):
    return number ** pow


print(power(2, 5))

my_list = [1, 2, 3, 4, 5]
for n, p in enumerate(my_list):
    print(power(number=p, pow=n))

# Если не указать возвращаемое значение, функция вернет None

# Функция может возвращать несколько значений
def create_default_user():
    name = "Василий"
    age = 27
    return name, age


user_name, user_age = create_default_user()
print(user_name, user_age)

# Также в языке Python есть встроенные(предопределенные функции),(builtins) - эти функции встроены в сам язык
# (например print)
