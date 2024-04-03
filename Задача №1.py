def read_recipes(filename):
    cook_book = {}
    with open(filename, 'r', encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            ingredients_count = int(file.readline().strip())
            ingredients_list = []
            for _ in range(ingredients_count):
                ingredient_name, quantity, measure = file.readline().strip().split(' | ')
                ingredients_list.append({'ingredient_name': ingredient_name, 'quantity': int(
                    quantity), 'measure': measure})
            cook_book[dish_name] = ingredients_list
            file.readline()
    return cook_book
