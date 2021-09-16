#!/usr/bin/env python 
import random

def game():
	print('Лабораторная работа')
	cmt_good = 0
	cmt_bad =0
	contiune = 'yes'
	while contiune !='no':
		gess = input(('Введите число от 1 до 5','r'))
		i = random.randint(1, 5)
		#tmp = f'{gess}:{str}'
		print(f'Ваше число ')
		print(f'Число компьютера')
		if gess == i :
			cmt_good =+1
		contiune = input('Введите "yes" или "no"')
	print('Игра окончена')
  
