def hello():
    print('Hello Python')


hello()


def greet_user(user_name):
    print(f'Hi {user_name}!!!. How are you doing?')


greet_user('Raj')
greet_user('Maxi')


def add_num(x, y):
    return x + y


print(add_num(10, 20))


def add_five(y):
    y += 5
    print(y)


x = 5

print(x)

add_five(x)

print(x)


def square(x):
    return x*x


a = 10

print(a)

print(square(a))

print(a)

b = square(a)

print(b)


def greetName(name, gender):
    if(gender == 'M'):
        return "Mr. " + name
    else:
        return "Mrs. " + name


userA = 'Gary'
userB = 'Kathy'

print(userA, userB)

print(greetName(userA, 'M'))
print(greetName(userB, 'F'))

print(userA, userB)


def add_value(num_list, value):
    num_list.append(value)


my_list = [10, 20]
print(my_list)

add_value(my_list, 30)
print(my_list)

add_value(my_list, 40)
print(my_list)


def display_squares(num_list):
    for i in num_list:
        print(i*i, end=" ")


num_list = [1, 2, 3]

display_squares(num_list)


def get_squares(num_list):
    for i in range(len(num_list)):
        num_list[i] = num_list[i] ** 2


num_list = [1, 2, 3, 4, 5]

print(num_list)

get_squares(num_list)

print(num_list)


def get_squares_2(num_list):
    num_list_new = num_list[:]
    for i in range(len(num_list_new)):
        num_list_new[i] = num_list_new[i] ** 2
    return num_list_new


num_list = [1, 2, 3, 4, 5]

print(num_list)

squares_list = get_squares_2(num_list)

print(squares_list)


# recursive functions


def decrement_num(x):
    if x > 0:
        print(x, end=" ")
        x -= 1
        decrement_num(x)


decrement_num(5)

# Call By Value


def add_five_cbv(y):
    y += 5
    print(y)


x = 5

print(x)

add_five_cbv(x)

print(x)


def add_exclamation(y):
    y += "!!!!!"
    print(y)


name = "Python"

print(name)

add_exclamation(name)

print(name)


# Call By Reference


def add_value_cbr(num_list, value):
    num_list.append(value)


my_list = [10, 20]
print(my_list)

add_value_cbr(my_list, 30)
print(my_list)

add_value_cbr(my_list, 40)
print(my_list)


def add_value_cbr_2(num_list, value):
    new_num_list = num_list[:]
    new_num_list.append(value)
    print("a", new_num_list)


my_list = [10, 20]
print("x", my_list)

add_value_cbr_2(my_list, 30)
print("y", my_list)

add_value_cbr_2(my_list, 40)
print("z", my_list)
