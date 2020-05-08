# write a program to fill a list with 1-10 numbers randomly

# numbers_list = [6,8,4,10,9,7,2,1,3,5]

import random

numbers_list = []

for x in range(1,11):
    # print(x)
    numbers_list.append(x)

# print(numbers_list)

random.shuffle(numbers_list)

print(numbers_list)

