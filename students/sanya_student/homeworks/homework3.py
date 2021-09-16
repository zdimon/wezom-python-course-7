import random

cnt_good = 0
cnt_bad = 0
is_continue = 'yes'
print('Игра "Угадай число"')

while is_continue != 'no':
    guess = int(input('Введите число от 1 до 5: '))
    random_number = random.randint(1, 5)
    print(f'Ваше число - {guess}')
    print(f'Случайное число - {random_number}')
    if guess == random_number:
        cnt_good += 1
    else:
        cnt_bad += 1
    ask = input('Хотите ли вы продолжить игру?(yes/no): ')
    if ask != 'yes':
        break
    else:
        continue

print(f'Ваш счет:\nУгадал - {cnt_good} раз(a)\nНе угадал - {cnt_bad} раз(a)')

