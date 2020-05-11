# [5,3,3,2,3,1,3,4,2,4]

# 1 - 5

# rep        2, 3, 4
# non-rep    5, 1

# repetition count
# 1 - 1
# 2 - 2
# 3 - 4
# 4 - 2
# 5 - 1

num_list = [5,3,3,2,3,1,3,4,2,4]
sorted_num_list = num_list[:]
sorted_num_list.sort()

print(num_list)
print(sorted_num_list)

rep_count = {}

for val in sorted_num_list :
    if(val in rep_count) :
        rep_count[val] = rep_count[val] + 1
    else:
        rep_count[val] = 1

print(rep_count)

dup_list = []
non_dup_list = []

for key in rep_count.keys() :
    if(rep_count[key] > 1) :
        dup_list.append(key)
    else :
        non_dup_list.append(key)
    
print(dup_list)
print(non_dup_list)

