# Dictionary{key:value,....}

studentDetails = {
    'name': 'Riyaz',
    'age': 25,
    'gender': 'Male'
}

print(studentDetails)
print(studentDetails['name'])
print(studentDetails['age'])
print(studentDetails['gender'])


# Dictionary Operations
# Empty
# Initialize with values
# Add
# Remove
# Update
# Sort
# Count

empty_dict = {}
print(empty_dict)

init_val_dict = {'name': 'Raj', 'age': 21, 'score': 21}
# init_val_dict = {'name':'Raj', 'age':21,'name':'abc'}
print(init_val_dict)

print(init_val_dict['name'])
print(init_val_dict['age'])

print(init_val_dict.keys())

for key in init_val_dict.keys():
    print(key)

print(init_val_dict.values())

for value in init_val_dict.values():
    print(value)

print(init_val_dict.items())

for key, value in init_val_dict.items():
    print(f'{key} - {value}')

for key in init_val_dict.keys():
    print(f'{key} - {init_val_dict[key]}')


init_val_dict = {'name': 'Raj', 'age': 21, 'score': 21}

init_val_dict['gender'] = 'Male'

print(init_val_dict)

init_val_dict['score'] = 48

print(init_val_dict)

print(len(init_val_dict))

student_totals = {'Neha': 456, 'Vahed': 736, 'Riyaz': 354, 'Raj': 121}

print(sorted(student_totals.keys()))
print(sorted(student_totals.values()))

for key in sorted(student_totals.keys()):
    print(f'{key} - {student_totals[key]}')

student_totals_sorted_keys = sorted(student_totals)
for r in student_totals_sorted_keys:
    print(r, student_totals[r])
print("--------------------------------------")
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
