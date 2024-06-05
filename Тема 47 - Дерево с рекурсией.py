"""Тема 29 - Дерево с рекурсией"""

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

# Еще один пример(екомендуется выполнить пошагово
html_dom = {
    'html': {
        'head': {
            'title': 'Колобок', 'title2' : 'Сказка'
        },
        'body': {
            'h2': 'Привет!',
            'div': 'Хочешь, я расскажу тебе сказку?',
            'p': 'Жили-были старик со старухой...',
        }
    }
}


def find_element(tree, element_name):
    if element_name in tree:  # Если ключ есть, мы его возвращаем, и выходим из функции
        return tree[element_name]
    for key, sub_tree in tree.items(): # Если ключа нет, то мы перебираем словарь по парам ключ - значение
        print(key, sub_tree)
        if isinstance(sub_tree, dict):  # Если под - дерево является словарем
            result = find_element(tree=sub_tree, element_name=element_name)  # Заново вызываем функцию, в которую передаем вложенный словарь
            if result:  # Если результат найден - выходим из функции (а если нет, переходим на следующий элемент словаря)
                break
    else:
        result = None
    return result


res = find_element(tree=html_dom, element_name='title2')
print(res)
