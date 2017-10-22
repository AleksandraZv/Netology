def read_ingredients():
    all_dishes = dict() # — подготовили пустой словарь
    dish_ingredients = list() # — подготовили пустой список
    with open('ingredients.txt', 'r') as f: # — контекстный менеджер, читаем
        for line in f:
            dish_info = list()
            dish_key = line.strip() # — чтобы не читать построчно взяли лайн
            dish_ingredients.append(dish_key) # — собрали всё что прочли в список
            print(dish_ingredients) # — проверили, что всё ок

            for x in range(dish_ingredients):
                ingredient = f.readline().strip().split(" | ") # — данные в читаемый вид
                i = {'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]), 'measure': ingredient[2]}
                dish_info.append(i)
                f.readline()
                all_dishes.update({dish_key: dish_info})
                print(all_dishes)

    return all_dishes, dish_ingredients

read_ingredients()

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    dishes_all, name_of_the_dish = read_ingredients()
    for dish in dishes:
        for ingredient in dishes_all[dish]:
            new_shop_list_item = dict(ingredient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
        return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)


create_shop_list()
