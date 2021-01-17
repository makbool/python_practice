f = open('Numbers.txt', 'w')

f.write('1')
f.write('2')
f.write('3')
f.write('\n')
f.writelines(['4', '5', '6'])
f.close()

f = open('Numbers.txt', 'a')
f.write('7')
f.write('8')
f.write('9')
f.write('\n')
f.writelines(['Numbers 1-9\n',
              'Have a great day\n',
              'Python Fundamentals Complete!!!\n'])
f.close()

