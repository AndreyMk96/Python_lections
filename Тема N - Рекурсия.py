"""Тема N - Рекурсия"""


# Пример использования рекурсии при подсчете суммы чисел от 0 до N
def recursion(n):
    if n == 1:
        return 1
    return n + recursion(n - 1)


print(recursion(10))
#  в отличии от цикла рекурсия работает от большего к меньшему

# Определение факториала числа через рекурсию
def factorial(n):
    if n == 0:
       return n
    else:
        return n * factorial(n - 1)
print(factorial(6))

# Исследование дерева с рекурсией
def walk(tree, path=()):
    path = path + (tree['name'],)
    yield path
    for child in tree['children']:
        yield from walk(child, path)

tree = {
    'name': 'Folder 1',
    'children': [
        {'name': 'Folder 2',
         'children': [
              {'name': 'Folder 3',
                'children': []},
              {'name': 'Folder 4',
                'children': []}]}]}

for path in walk(tree):
    print(path)