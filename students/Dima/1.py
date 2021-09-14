#!/usr/bin/env python 
import random
number = int(input('Введите число: '))
random_number = random.randint(1, 9)

print(f'Ваше число - {number}')
print(f'Случайное число - {random_number}')

if number == random_number:
    print('Вы угадали.')
else:
    print('Вы не угадали.')

