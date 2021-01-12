# List [value,...]

numbers = [1, 2, 3, 4, 5, 6, 5, 7, 4, 2]
items = ['salt', 'sugar', 'Turmeric', 'Chilli Powder', 'sugar', 'salt']

print(numbers)

print(items)
print(items[2])
items[2] = "New Item"
print(items)
print(items[2])


# List Operations

# List is Ordered

# Empty
# Initialize with values
# Add
# Update
# Remove
# Sort
# Count

empty_list = []
print(empty_list)

init_val_list = [11, 22, 33]
print(init_val_list)

init_val_list.append(55)
print(init_val_list)

# insert (index, value)
init_val_list.insert(3, 44)
print(init_val_list)

init_val_list[2] = 333
print(init_val_list)

del init_val_list[1]
print(init_val_list)

print('Bye')

# program exexution stops when an error occurs
# del init_val_list[10]

print('Hello')

init_val_list.sort()
print(init_val_list)

print(len(init_val_list))

names = ['C', 'CPP', 'JAVA', 'PYTHON']

separator = "-"

result = separator.join(names)

print(result)

