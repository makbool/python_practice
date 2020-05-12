# Tuple Operations
# Empty
# Initialize with values
# Add       -   NO
# Remove    -   NO
# Update    -   NO
# Sort
# Count


# empty_tuple = ()
# print(empty_tuple)

# init_value_tuple = (100, 200)
# print(init_value_tuple)

# init_value_tuple = (
#     10, 20, 30,
#     ['C', 'C++', 'JAVA'],
#     {'Red', 'Green', 'Blue'},
#     {'One': 1, 'Two': 2, 'Three': 3}
# )
# print(init_value_tuple)

# init_value_tuple[3].append('Python')

# print(init_value_tuple)

# # init_value_tuple[2] = 200

# print(len(init_value_tuple))


tuple_pairs =  ( (1,'Neha', 323), (3,'Vahed', 293), (2,'Riyaz', 313) )
# print(tuple_pairs)

# tuple_pairs_sorted_rollno = sorted(tuple_pairs)
# for r in tuple_pairs_sorted_rollno:
#     print(r)

# def name(value):
#     print(f'Name Function: {value} - {value[1]}')
#     return value[1]

# tuple_pairs_sorted_name = sorted(tuple_pairs, key=name)
# for r in tuple_pairs_sorted_name:
#     print(r)

print("-----------------------------------------")

def marks(value):
    print(f'Marks Function: {value} - {value[2]}')
    return value[2]

tuple_pairs_sorted_marks = sorted(tuple_pairs, key=marks)
for r in tuple_pairs_sorted_marks:
    print(r)

