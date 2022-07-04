board = ['0', '1', '2',
         '3', '4', '5',
         '6', '7', '8']

winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]


def print_board(state):
    for index, val in enumerate(state):
        if (index + 1) % 3 == 0:
            print(f'{val}')
        else:
            print(f'{val} | ', end='')


def make_turn(player):
    choice = int(input(f'Choose a place for {player}: '))
    if choice < 0 or choice > 8:
        print('Choose free place between 0 and 8')
        make_turn(player)
    elif board[choice] == 'X' or board[choice] == 'O':
        print('This place is taken. Choose another one.')
        make_turn(player)
    else:
        board[choice] = player


def is_winner(player, state, combinations):
    for (x, y, z) in combinations:
        if state[x] == player and state[y] == player and state[z] == player:
            return True
    return False


turn = 0
current_player = 'X'
winner = ''
print_board(board)

while turn < 9:
    make_turn(current_player)
    turn += 1
    print_board(board)

    if is_winner(current_player, board, winning_combinations):
        winner = current_player
        break
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

if winner:
    print(f'Player {winner} won!')
else:
    print('Draw!')
