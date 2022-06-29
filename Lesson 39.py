from random import randint


random_number = randint(1, 50)
lives = 6

while lives > 0:
    guess = int(input("Try to guess the number between 1 and 50: "))
    lives -= 1

    if guess > random_number:
        print('Too high.')
    elif guess > random_number:
        print('Too low.')
    else:
        print("You Won!")
        break

print('Game Over.')