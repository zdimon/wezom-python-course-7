#!/usr/bin/env python3
print('Start')
'''
with open('people.txt', 'r') as file:
    num = 1
    for line in file.readlines():
        # ['1.txt','Vasya']
        line_list = line.split(';')
        print(line_list[1])
        print(':::'.join(line_list))
        # tmp_file = open(f'{num}.txt','w')
        # tmp_file.write(line)
        # tmp_file.close()
        # num = num +1

'''

empty_list = []

#print(dir(empty_list))



user_input = ''

while user_input!='stop':
    user_input = input('Input something:')
    if user_input != 'stop':
        empty_list.append(user_input)
    print(empty_list)

print('End!!!')