name = "Vahed"
age = 17

name_2 = "Neha"
age_2 = 6

# My name is Vahed and my age is 17

# print('My name is ' + name + ' and my age is ' + age)
print('My name is ' + name + ' and my age is ' + str(age))

print(f'My name is {name} and my age is {age}')

# Not Recommended
print('My name is {0} and my age is {1}'.format(name, age))

print('My name is {v1} and my age is {v2}'.format(v1=name, v2=age))
print('My name is {v1} and my age is {v2}'.format(v1=name_2, v2=age_2))


average = 12.5679

print(average)

print("%d" % (average))

print("%f" % (average))

print("%.2f" % (average))
print("%08.2f" % (average))
print("%8.2f" % (average))

p1 = 121.67
p2 = 1.65
p3 = 1267.9
p4 = 0.23
p5 = 1.1
p6 = 10.67

print("%f" % (p1))
print("%f" % (p2))
print("%f" % (p3))
print("%f" % (p4))
print("%f" % (p5))
print("%f" % (p6))

print("%8.2f" % (p1))
print("%8.2f" % (p2))
print("%8.2f" % (p3))
print("%8.2f" % (p4))
print("%8.2f" % (p5))
print("%8.2f" % (p6))
