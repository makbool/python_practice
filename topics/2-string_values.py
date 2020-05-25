# string functions/manipulations

name = "Python Language"

print(name)
print(len(name))

print(name[1])
print(name[-1])
print(name[0:6])
print(name[2:-2])
print(name[4:])
print(name[:])


numbers = "9876543210"

# [start_index, end_index, step or index_increment]

print(numbers[::2])
print(numbers[1::2])

print(numbers[::-1])

print(numbers[::-2])

print(numbers[::2][::-1])

print(numbers[-2::-2])

SQS = 'Single \nQuoted'
DQS = "Double Quoted"
TQS = '''Triple
Quoted
New Line String

    Courses
        C
        C++
        Java


Spaces Gap


Hello
'''

print(SQS)
print(DQS)
print(TQS)

name = "Python"

print('th' in name)
print('ht' in name)
print('Hell' not in name)


print(" %*% " * 5)
print(" %*% " * 4)
print(" %*% " * 3)
print(" %*% " * 2)
print(" %*% ")
