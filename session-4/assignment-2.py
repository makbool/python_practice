import random

number_list = []

print(f'Initial Size : {len(number_list)}')

while(len(number_list) != 5):
    random_num = random.randrange(1, 6)
    print(f'Random Number {random_num}')
    if(random_num not in number_list):
        number_list.append(random_num)
        print(f'New Number List {number_list}')

print(f'Final Size : {len(number_list)}')

print(number_list)
