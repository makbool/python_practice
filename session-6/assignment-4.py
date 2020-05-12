names = ['C','CPP','JAVA','PYTHON']

# output : C$$$CPP$$$JAVA$$$PYTHON


# for name in names:  
#     print(name, end="-")


separator = "-"

# str=""
# for name in names:
#     str += name + separator

# str = str[:-1 * len(separator)]

# print(str)

result = separator.join(names)

print(result)


