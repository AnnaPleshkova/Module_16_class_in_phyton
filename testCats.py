import json

from cats import Cat

with open('Pet_List.json', encoding='utf8') as f:
    templates = json.load(f)

print(templates)


def find_cat(elem, item):
    if elem[item]['code'] == 'cat':
        return True


for elem in templates['results']:
    for item in elem:
        if item == 'species' and find_cat(elem, item):
            obj_cat = Cat(elem['name'], elem['gender']['name'], elem['age'])
            print(obj_cat.name)
            print(obj_cat.gender)
            print(obj_cat.age)
        else:
            print(False)