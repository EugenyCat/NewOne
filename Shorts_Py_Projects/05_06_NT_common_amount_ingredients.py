"""
Given a recipe book with information on how many ingredients are needed for cooking a dish per serving.
Write a program that will ask the user the number of portions for the preparation of these dishes
and display information on the total number of ingredients required in the specified form.
"""


def calculate_common_amount_ingredients(cook_dict:dict, amount:int) -> dict:
    """Method calculate common amount of ingredients for dishes multiply on amount:int.
    Important that measure can be different"""
    common_amount = { }
    for dish in cook_dict.values():
        for ingredient in dish:
            if common_amount.get(ingredient.get('ingredient_name') + ingredient.get('measure')) is None:
                common_amount[ingredient.get('ingredient_name') + ingredient.get('measure')] = [ingredient.get('ingredient_name'), ingredient.get('measure'), ingredient.get('quantity')*amount]
            else:
                common_amount.get(ingredient.get('ingredient_name') + ingredient.get('measure'))[2] += ingredient.get('quantity')*amount
    return common_amount

def print_common_amount_ingredients(cook_dict:dict, amount:int) -> None:
    """Print dictionary from method calculate_common_amount_ingredients()"""
    common_amount = calculate_common_amount_ingredients(cook_book, 3)
    for item in common_amount.values():
        print(f'{item[0]}: {item[2]} {item[1]}')

cook_book = {
  'salat': [
     {'ingredient_name': 'cheese', 'quantity': 50, 'measure': 'gr'},
     {'ingredient_name': 'tomatoes', 'quantity': 2, 'measure': 'pc.'},
     {'ingredient_name': 'cucumbers', 'quantity': 20, 'measure': 'gr'},
     {'ingredient_name': 'olives', 'quantity': 10, 'measure': 'gr'},
     {'ingredient_name': 'olive oil', 'quantity': 20, 'measure': 'ml'},
     {'ingredient_name': 'salat', 'quantity': 10, 'measure': 'gr'},
     {'ingredient_name': 'pepper', 'quantity': 20, 'measure': 'gr'}
    ],
  'pizza': [
     {'ingredient_name': 'cheese', 'quantity': 20, 'measure': 'gr'},
     {'ingredient_name': 'sausage', 'quantity': 30, 'measure': 'gr'},
     {'ingredient_name': 'bacon', 'quantity': 30, 'measure': 'gr'},
     {'ingredient_name': 'olives', 'quantity': 10, 'measure': 'gr'},
     {'ingredient_name': 'tomatoes', 'quantity': 20, 'measure': 'gr'},
     {'ingredient_name': 'dough', 'quantity': 100, 'measure': 'gr'},
    ],
  'lemonade': [
     {'ingredient_name': 'lemon', 'quantity': 1, 'measure': 'ml'},
     {'ingredient_name': 'water', 'quantity': 200, 'measure': 'ml'},
     {'ingredient_name': 'sugar', 'quantity': 10, 'measure': 'gr'},
     {'ingredient_name': 'lime', 'quantity': 20, 'measure': 'gr'},
    ]
}

print_common_amount_ingredients(cook_book, 3)