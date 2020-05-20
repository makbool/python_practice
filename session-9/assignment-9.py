# Write a program to find an integer from a list of integers.
# if found return the index of the value found else return -1
# don't use any predefined functions


# [66, 22, 88, 33, 67, 99, 4, 3]

# input
# 66
# Output
# 0

# input
# 67
# Output
# 4

# input
# 999
# Output
# -1

b = int(input("enter your number:"))
a = [34, 53, 65, 23, 76, 96, 86, 74]
# x = a.index(b)
# print(f"index of {b} is {x}")

if b in a:
    x = a.index(b)
    print(f"index of {b} is {x}")
else:
    print(f"index of {b} is {-1}")
