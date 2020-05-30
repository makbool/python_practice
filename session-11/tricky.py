# # All Primitive Types are immutable

# a = 10
# b = a
# c = 10

# print(a, id(a), b, id(b), c, id(c))

# b = 20
# c = 20

# print(a, id(a), b, id(b), c, id(c))

# print("-----------------------------------------------")

# x = "hello"
# y = x
# z = "hello"

# print(x, id(x), y, id(y), z, id(z))

# y = "Bye"
# z = "Bye"

# print(x, id(x), y, id(y), z, id(z))


# print("-----------------------------------------------")

# a = 10
# b = a
# print(a, b)  # 20, 20 - 10, 10

# b = 20
# print(a, b)  # 20, 20


# x = "Hello"
# y = x

# print(x, y)

# y = "Bye"

# print(x, y)


# print("-----------------------------------------------")

# List is mutable

# num_list = [10, 20, 30]

# print(num_list, id(num_list))

# num_list.append(40)

# print(num_list, id(num_list))

# new_list = num_list[:]
# # Copy

# new_list.append(50)

# print(num_list, id(num_list), new_list, id(new_list))


# print("-----------------------------------------------")


# truthy falsy values

# print(bool(0), bool(""), bool([]), bool(None))

# print(bool(1), bool(-1),
#       bool("True"), bool("False"), bool(" "),
#       bool(["True"]), bool(["False"]))


# temp = [10, 20]

# if temp:
#     print(temp)
# else:
#     print("List is empty")

# x = ""

# if x:
#     print(x)
# else:
#     print("x is empty")

# print("-----------------------------------------------")


# for else block
# names = ['Abdul', 'Raju', 'Sheela', 'Rahman', 'Prasad', 'Kumar']

# search_crit = 'Z'

# result = ''
# for name in names:
#     if name.startswith(search_crit):
#         result = name
#         break
# else:
#     result = 'This will be printed if loop doesn\'t  break. <Name Not Found>'
# print(result)


# # else is not required here
# for x in range(5):
#     print(x, end=" ")
# # else:
# #     print("Loop is completed")

# print("Loop is completed")


# lambda (function without name)

# syntax lambda args : expression

def adder2(x, y): return x + y

print(adder2(10, 20))

