number = int(input())  # 121

number_copy = number
reversed_number = 0
while number_copy > 0:
    reversed_number *= 10
    reversed_number += number_copy % 10
    number_copy //= 10

if number == reversed_number:
    print('Palindrome')
else:
    print('No Palindrome')
