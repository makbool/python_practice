# time
# immutable
# functions


import time
import calendar

# # 1970 January 1 12:00 AM - epoch
# print(time.time())
# print(time.localtime())
# # print(time.localtime(time.time()))

# print(time.asctime(time.localtime()))

# may_2020 = calendar.month(2020, 5)

# print(may_2020)

# print(time.process_time())

# start_time = time.process_time()

# result = ""
# for i in range(1,10001) :
#     result += str(i) + " - "

# print(result)

# end_time = time.process_time()

# print()
# print(f'Time Taken in seconds : + {end_time - start_time}')

print("Start : %s" % time.ctime())
result = ""
for i in range(1, 6):
    time.sleep(1)
    result += str(i) + " - "

print(result)
print("End : %s" % time.ctime())
