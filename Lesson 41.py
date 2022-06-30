from random import choice

rsp = ['r', 's', 'p']
winning_combinations = [('r', 's'), ('s', 'p'), ('p', 'r')]
game_over = False
while not game_over:
    comp_choice = choice(rsp)
    user_choice = input(f'Make your choice {rsp}: ').lower()

    if user_choice not in rsp:
        print('Incorrect input.')
        continue

    if comp_choice == user_choice:
        print('Draw!')
    elif (user_choice, comp_choice) in winning_combinations:
        print('You Won!')
    else:
        print('You lose!')

    should_continue = input('Want to continue? Type Y or N: ').lower()
    if should_continue != 'y':
        game_over = True
