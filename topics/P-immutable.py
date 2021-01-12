courses = ['C', 'C++', 'Java', 'Python']

# Share the same reference
new_courses = courses

# Creating a copy
another_new_courses = courses[:]

print(courses)
print(new_courses)
print(another_new_courses)

print(courses is new_courses)
print(courses is another_new_courses)

# Mutable Objects
courses.append('HTML')
new_courses.append('JavaScript')

# Immutable Object
another_new_courses.append('CSS')

print(courses)
print(new_courses)
print(another_new_courses)
