# required
def add(x, y):
    return x + y

# print(add(10, 20))

# Error
# print(add(10))


# default
def incr(current_value, increment_value=1):
    return current_value + increment_value


# a = 100

# a = incr(a, 20)

# a = incr(a)

# print(a)


# keyword
# def greet_user_by_gender(user_name, gender):
#     if(gender == 'M'):
#         print('Mr.' + user_name)
#     else:
#         print("Miss." + user_name)


# greet_user_by_gender("Raj", "M")
# greet_user_by_gender("Jennifer", "F")


# greet_user_by_gender(gender="M", user_name="Raj")
# greet_user_by_gender(gender="F", user_name="Jennifer")

# variable-length arguments (* - tuple)


# def all_sum(a, b, *c):
#     print(a)
#     print(b)
#     print(c)
#     sum = a+b
#     print("looping variable args (tuple)")
#     for x in c:
#         sum += x
#     return sum


# print("-------------------------")
# print(all_sum(10, 20, 30))
# print("-------------------------")
# print(all_sum(10, 20, 30, 40))
# print("-------------------------")
# print(all_sum(10, 20, 30, 40, 50))
# print("-------------------------")


# keyworded variable-length arguments (** - name = value pairs)

# emp = {'name': 'Antony', 'age': 30,
#        'branch': 'Testing', 'location': 'Hyderabad'}

# print(emp)


# def update_emp(emp, **new_emp_det):
#     print(new_emp_det)
#     for key, value in new_emp_det.items():
#         # print(key, value)
#         emp[key] = value


# update_emp(emp, name='Akbar', age="45", location="Vizag")


# print(emp)


# function returns multiple values as a tuple

# def get_prev_next_items(num_list, el):
#     if el in num_list:
#         index = num_list.index(el)
#         if(index < len(num_list) - 1):
#             return (num_list[index - 1], num_list[index + 1])
#         else:
#             return (num_list[index - 1], num_list[0])
#     else:
#         return('Element Not in list')


# tens_list = [10, 20, 30, 40, 50]

# print(get_prev_next_items(tens_list, 30))

# print(get_prev_next_items(tens_list, 50))

# print(get_prev_next_items(tens_list, 10))

# print(get_prev_next_items(tens_list, 100))

# None value

result = print('Hello')

print(result)


def say_hello(name):
    print('Hello!!! ' + name)


def say_hello_2(name):
    print('Hello!!! ' + name)
    return None


say_hello("Vahed")

print(say_hello("Vahed"))

say_hello_2("Vahed")

print(say_hello_2("Vahed"))
