# Tuple (value,...)
numbers = (1, 2, 3, 4, 5, 6, 5, 7, 4, 2)
items = ('salt', 'sugar', 'Turmeric', 'Chilli Powder', 'sugar', 'salt')

print(numbers)
print(items)
print(items[2])
# Cannot update value
# items[2] = "New Item"
print(items)
print(items[2])

tupleDemo = (11, 22, 33, [4, 5, 6, 5, 4], {6, 7, 8, 9, 66, 777, 8888, 99999}, {
             'name': 'Rahul', 'age': 20})

print(tupleDemo)
print(tupleDemo[0])
print(tupleDemo[1])
print(tupleDemo[2])
print(tupleDemo[3])
print(tupleDemo[4])
print(tupleDemo[5])
print(tupleDemo[5]['name'])


# Tuple Operations
# Empty
# Initialize with values
# Add       -   NO
# Remove    -   NO
# Update    -   NO
# Sort
# Count


empty_tuple = ()
print(empty_tuple)

init_value_tuple = (100, 200)
print(init_value_tuple)

init_value_tuple = (
    10, 20, 30,
    ['C', 'C++', 'JAVA'],
    {'Red', 'Green', 'Blue'},
    {'One': 1, 'Two': 2, 'Three': 3}
)
print(init_value_tuple)

init_value_tuple[3].append('Python')

print(init_value_tuple)

# init_value_tuple[2] = 200

print(len(init_value_tuple))


tuple_pairs = ((1, 'Neha', 323), (3, 'Vahed', 293), (2, 'Riyaz', 313))
print(tuple_pairs)

tuple_pairs_sorted_rollno = sorted(tuple_pairs)
for r in tuple_pairs_sorted_rollno:
    print(r)


def name(value):
    print(f'Name Function: {value} - {value[1]}')
    return value[1]


tuple_pairs_sorted_name = sorted(tuple_pairs, key=name)
for r in tuple_pairs_sorted_name:
    print(r)

print("-----------------------------------------")


def marks(value):
    print(f'Marks Function: {value} - {value[2]}')
    return value[2]


tuple_pairs_sorted_marks = sorted(tuple_pairs, key=marks)
for r in tuple_pairs_sorted_marks:
    print(r)
