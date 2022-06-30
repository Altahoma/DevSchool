players_number = int(input('Enter the number of players: '))
sticks = int(input('Enter the number of sticks: '))

players = []
for i in range(1, players_number + 1):
    name = input(f'Print name for the {i} player: ')
    players.append(name)

while sticks > 0:
    for name in players:
        print(f'{name} turn. {sticks} sticks left.')
        choice = int(input('Chose between 1 and 3: '))
        sticks -= choice
        if sticks <= 0:
            print('\tZere sticks left! Player {name} lose!')
            break
