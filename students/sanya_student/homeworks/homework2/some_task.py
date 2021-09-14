import os
# Перенос файлов из одной папки в другую.
os.replace("/Users/yakubaoleksii/PycharmProjects/python/homework2/first/some.txt",
           "/Users/yakubaoleksii/PycharmProjects/python/homework2/second/some.txt")

os.replace("/Users/yakubaoleksii/PycharmProjects/python/homework2/first/some2.txt",
           "/Users/yakubaoleksii/PycharmProjects/python/homework2/second/some2.txt")

os.replace("/Users/yakubaoleksii/PycharmProjects/python/homework2/first/some3.txt",
           "/Users/yakubaoleksii/PycharmProjects/python/homework2/second/some3.txt")

# Последовательное чтение файлов из папки и создание файла, в который переносится
# содержимое всех прочитаных файлов.
file1 = open('some.txt', 'r')
file2 = open('some2.txt', 'r')
file3 = open('some3.txt', 'r')

for i in file1:
    print(i)

for i in file2:
    print(i)

for i in file3:
    print(i)

file1.close()
file2.close()
file3.close()

with open('newfile.txt', 'w') as file4, open('some.txt', 'r') as some, open('some2.txt', 'r') as some2, open(
        'some3.txt', 'r') as some3:
    for line in some:
        file4.write(line)

    for line in some2:
        file4.write('\n' + line)

    for line in some3:
        file4.write('\n' + line)

# Программа, которая прочитает файл построчно,
# и для каждой строки создаст отдельный файл.
f = open('one_more_file.txt', 'r')
count = 1
for line in f:
    tmp = f'{count}. {line}'
    count += 1
    print(tmp)

f.close()

f1 = open('one_more_file.txt', 'r')
for i, text in enumerate(f1):
    open(str(i + 1) + '.txt', 'w').write(text)

f1.close()


