# Set {value,...}
# No Duplicates

numbers = {8888, 1, 2, 3, 4, 5, 6, 5, 7, 4, 2, 66, 77, 888, 9999}
items = {'salt', 'sugar', 'Turmeric', 'Chilli Powder', 'sugar', 'salt'}

print(numbers)
print(items)
items.add('Jaggery')
items.add('Ghee')
print(items)


courses = {'C', 'C++', 'Java', 'Python'}

print('Java' in courses)

print('HTML' not in courses)


# Set Operations
# Set is unorderd
# Empty
# Initialize with values
# Add
# Remove
# Update
# Sort
# Count

empty_set = set()
print(empty_set)

num_list = {11, 3, 4, 4, 5, 5, 8}
unique = set(num_list)
print(unique)

init_val_set = {10, 20, 30}
print(init_val_set)

empty_set.add(10)
print(empty_set)

init_val_set.add(3)
print(init_val_set)

init_val_set.remove(20)
print(init_val_set)

sorted_set = sorted(init_val_set)
print(init_val_set)
print(sorted_set)

print(len(init_val_set))
