#!/usr/bin/env python3
print('Test script')

# content = file.read()
# print(content)

'''
c подобные языки (с java php js)

for(i=1,i<10,i=i+2) {
    i 
}

for i in [1,2,3,4,5,6]:

'''
#d = [1,2,3,4,5,6]
# for counter in range(6,80,2):
#     print(counter)
file = open('people.txt','r')
cnt = 1
for line in file:
    #print(cnt)
    #print(line)
    #tmp = str(cnt)+'.'+line
    #tmp = '%s -------- %s' % (cnt, line)
    tmp = f'{cnt}:{line}'

    # JS `${var_name}...`

    cnt += 1
    print(tmp)