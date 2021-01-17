import os

file_name = 'Numbers.txt'

if os.path.exists(file_name):
    os.remove(file_name)
else:
    print("%s does not exist" % file_name)
