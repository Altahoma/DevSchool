def coffee_shop():
    cups = int(input("How many coffee cups do you wish? "))
    bonus_cups = int(cups / 6)
    print(f'You bought {cups} of coffee and got {bonus_cups} cups for free.')


def distance():
    x1 = float(input('Enter x1: '))
    y1 = float(input('Enter y1: '))
    x2 = float(input('Enter x2: '))
    y2 = float(input('Enter x2: '))
    dist = round(((x1 - x2)**2 + (y1 - y2)**2)**0.5, 3)
    print(dist)


def sum_of_legs():
    chickens = int(input('Chickens: '))
    cows = int(input('Cows: '))
    pigs = int(input('Pigs: '))
    legs = chickens*2 + cows*4 + pigs*4
    print(legs)


# coffee_shop()
# distance()
# sum_of_legs()
