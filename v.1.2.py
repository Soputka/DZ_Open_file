from pprint import pprint

file_name = 'recipes.txt'

def recipies_book(recipies):
    with open(recipies, encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            line = line.strip()
            if line.isdigit() or line == '':
                continue
            elif '|' in line:
                ingredient_name, quantity, measure = map(str.strip, line.split('|'))
                cook_book[dish].append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure})
            else:
                dish = line
                cook_book[dish] = []
        return cook_book



def get_shop_list_by_dishes(dishes, person_count):
    cook_dict = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredients in cook_book[dish]:
                ingredient, quantity, measure = ingredients
                if ingredients[ingredient] in cook_dict:
                    cook_dict[ingredients[ingredient]]['quantity'] += ingredients[quantity]*person_count
                else:
                    cook_dict[ingredients[ingredient]] = {'measure': ingredients[measure],
                                                             'quantity': ingredients[quantity]*person_count}
        else:
            print(f'Блюда "{dish}" нет в книге рецептов.')
    return cook_dict


cook_book = recipies_book(file_name)
pprint(cook_book, sort_dicts=False)
goods = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Перепёлка в сливках'], 2)
pprint(goods)