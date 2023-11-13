spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [element['name'] for element in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [element for element in spicy_foods if element['heat_level']>5]

def print_spicy_foods(spicy_foods):
    for element in spicy_foods:
        element_name = element['name']
        number_of_pep = element['heat_level'] * '🌶'
        print(f"{element_name} ({element['cuisine']}) | Heat Level: {number_of_pep}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine']==cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    new_list =[food for food in spicy_foods if food['heat_level']>5]
    print_spicy_foods(new_list)

def get_average_heat_level(spicy_foods):
    return sum([food['heat_level'] for food in spicy_foods])/len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    