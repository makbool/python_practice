fw = open ('f1.txt','w')
print(fw.mode)
print()
fw.write('Hi')
fw.write("\n")
fw.write('I am python')
fw.write("\n")
fw.write('I am smart')
fw.write("\n")
fw.close()


fr = open ('f1.txt')
print(fr.mode)
print()
print(fr.read())
fr.close()
# print(fr.readline())


fr2 = open ('f1.txt', 'a')
print(fr2.mode)
print()
fr2.write('You will be Luv\'in It')
fr2.close()

fr1 = open ('f1.txt')
for ln in fr1:
    print(ln, end ='')
fr1.close()



# Mode	    Description
# 'r'       This is the default mode. It Opens file for reading.
# 'w'       This Mode Opens file for writing. 
#           If file does not exist, it creates a new file.
#           If file exists it truncates the file.
# 'x'	    Creates a new file. If file already exists, the operation fails.
# 'a'	    Open file in append mode.
#           If file does not exist, it creates a new file.
# '+'	    This will open a file for reading and writing (updating)


# 't'	    This is the default mode. It opens in text mode.
# 'b'	    This opens in binary mode.
