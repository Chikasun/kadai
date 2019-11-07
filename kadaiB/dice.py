# サイコロの面の数は?: 8
# 何回振りますか?: 20
# [6, 6, 8, 5, 1, 6, 4, 4, 3, 4, 7, 5, 7, 1, 4, 2, 5, 7, 1, 7]


import random

face = int(input('サイコロの面の数は? : '))
count = int(input('何回振りますか? : '))
number_list = []
for a in range(count):
    number_list.append(random.randint(1, face + 1))
print(number_list)

