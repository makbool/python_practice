# Random Number Functions(random module)
# random, randrange (Only Integers), shuffle, choice, uniform (decimals supported)

import random


print(random.random())
print(random.random())
print(random.random())
print(random.random())

print(random.randrange(1, 100))
print(random.randrange(1, 100))
print(random.randrange(1, 100))
print(random.randrange(1, 100))

print(random.randrange(3, 97, 5))
print(random.randrange(3, 97, 5))
print(random.randrange(3, 97, 5))
print(random.randrange(3, 97, 5))


numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)

random.shuffle(numbers)
print(numbers)

lang = ['Red', 'Blue', 'Green', 'Yellow', 'Orange']
print(random.choice(lang))
print(random.choice(lang))
print(random.choice(lang))
print(random.choice(lang))


print(random.uniform(20, 60))
print(random.uniform(20, 60))
print(random.uniform(20, 60))

print(random.uniform(1.1, 1.5))
print(random.uniform(1.1, 1.5))
print(random.uniform(1.1, 1.5))


numbers_list = list(range(1, 11))

print(numbers_list)

random.shuffle(numbers_list)

print(numbers_list)
