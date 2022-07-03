import math


prices = {"Strawberries": 1.5, "Banana": 0.5, "Mango": 2.5, "Blueberries": 1,
          "Raspberries": 1, "Apple": 1.75, "Pineapple": 3.5}


class Pizza:
    orders = 0

    def __init__(self, ingredients):
        Pizza.orders += 1
        self.order_number = Pizza.orders
        self.ingredients = ingredients

    @classmethod
    def hawaiian(cls):
        return cls(['ham', 'pineapple'])

    @classmethod
    def meat_festival(cls):
        return cls(['beef', 'meatball', 'bacon'])

    @classmethod
    def garden_feast(cls):
        return cls(['spinach', 'olives', 'mushroom'])


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi*self.radius**2

    def get_perimeter(self):
        return math.pi*self.radius*2


class Beverage:
    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.cost = sum([prices[ingr] for ingr in self.ingredients])

    def get_cost(self):
        return f'${self.cost:.2f}'

    def get_price(self):
        return f'${round(self.cost * 2.5, 2):.2f}'

    def get_name(self):
        ingr_names = f'{" ".join(sorted(self.ingredients)).replace("berries", "berry")}'
        if len(self.ingredients) == 1:
            return ingr_names + ' Smoothie'
        else:
            return ingr_names + ' Fusion'
