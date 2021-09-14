#!/usr/bin/env python3
print('Start')

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
