# List Operations

# List is Ordered

# Empty
# Initialize with values
# Add
# Update
# Remove
# Sort
# Count

# empty_list = []
# print(empty_list)

# init_val_list = [11,22,33]
# print(init_val_list)

# init_val_list.append(55)
# print(init_val_list)

# # insert (index, value)
# init_val_list.insert(3,44)
# print(init_val_list)

# init_val_list[2] = 333
# print(init_val_list)

# del init_val_list[1]
# print(init_val_list)

# print('Bye')

# # program exexution stops when an error occurs
# # del init_val_list[10]

# print('Hello')

# init_val_list.sort()
# print(init_val_list)

# print(len(init_val_list))


# Set Operations
# Set is unorderd
# Empty
# Initialize with values
# Add
# Remove
# Update
# Sort
# Count

# empty_set = set()
# print(empty_set)

# num_list = {11,3,4,4,5,5,8}
# unique = set(num_list)
# print(unique)

# init_val_set = {10,20,30}
# print(init_val_set)

# empty_set.add(10)
# print(empty_set)

# init_val_set.add(3)
# print(init_val_set)

# init_val_set.remove(20)
# print(init_val_set)

# sorted_set = sorted(init_val_set)
# print(init_val_set)
# print(sorted_set)

# print(len(init_val_set))


# Dictionary Operations
# Empty
# Initialize with values
# Add
# Remove
# Update
# Sort
# Count

# empty_dict = {}
# print(empty_dict)

# init_val_dict = {'name': 'Raj', 'age': 21, 'score': 21}
# # init_val_dict = {'name':'Raj', 'age':21,'name':'abc'}
# print(init_val_dict)

# print(init_val_dict['name'])
# print(init_val_dict['age'])

# print(init_val_dict.keys())

# for key in init_val_dict.keys():
#     print(key)

# print(init_val_dict.values())

# for value in init_val_dict.values():
#     print(value)

# print(init_val_dict.items())

# for key, value in init_val_dict.items():
#     print(f'{key} - {value}')

# for key in init_val_dict.keys():
#     print(f'{key} - {init_val_dict[key]}')


# init_val_dict = {'name': 'Raj', 'age': 21, 'score': 21}

# init_val_dict['gender'] = 'Male'

# print(init_val_dict)

# init_val_dict['score'] = 48

# print(init_val_dict)

# print(len(init_val_dict))

student_totals = {'Neha': 456, 'Vahed': 736, 'Riyaz': 354, 'Raj': 121}

# print(sorted(student_totals.keys()))
# print(sorted(student_totals.values()))

# for key in sorted(student_totals.keys()):
#     print(f'{key} - {student_totals[key]}')

# student_totals_sorted_keys = sorted(student_totals)
# for r in student_totals_sorted_keys:
#     print(r, student_totals[r])
# print("--------------------------------------")
student_totals_sorted_keys_rev = sorted(student_totals, reverse=True)

print(student_totals_sorted_keys_rev)

for r in student_totals_sorted_keys_rev:
    print(r, student_totals[r])
# print("--------------------------------------")
# student_totals_sorted_values = sorted(
#     student_totals, key=student_totals.get)
# for r in student_totals_sorted_values:
#     print(r, student_totals[r])
# print("--------------------------------------")
# Display student names sorted by marks desc
student_totals_sorted_values_rev = sorted(
    student_totals, key=student_totals.get, reverse=True)

print(student_totals_sorted_values_rev)

for r in student_totals_sorted_values_rev:
    print(r, student_totals[r])
