import random
a = 60
b = 20
c = 20

if a > 0:
    print('1. a is a number')
    print('2. a is greater than zero')

if a > 10:
    print('3. a is a number')
print('4. a is greater than zero')
# indentation missing in above statement. This will not come under if block

if a > b:
    print('a greater than b')
else:
    print('a less than or equal to b')

if a > b:
    print('a is greater than b')
    if a > c:
        print('a is greater than b and c')

if b > c:
    print('b greater than c')
elif b == c:
    print('b equal to c')
else:
    print('b less than c')

# if, if/else, nested if, if elif

# ------------------------------------------------

# for, while, nested loops

a = 5
while a <= 10:
    print(a)
    a += 1

for v in range(5):
    print(v)


for v in range(11, 21):
    print(v, end=' ')

print()
