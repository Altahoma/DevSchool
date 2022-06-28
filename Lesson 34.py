def print_stairs():
    length = int(input('Enter the length of the stairs: '))
    for i in range(1, length+1):
        print('*' * i)


def even_or_odd():
    num = int(input('Enter the number: '))
    for i in range(num+1):
        if i % 2 == 0:
            print(f'{i} in even')
        else:
            print(f'{i} is odd')


# print_stairs()
# even_or_odd()
