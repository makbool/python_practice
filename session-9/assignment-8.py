# Write a program to find the smallest integer among a list of positive integers.
# smallest integer in an Integer list
# don't use any predefined functions


def smallest_int(num_list):
    small_int = num_list[0]
    print(small_int)

    for i in range(1, len(num_list)):
        if(small_int > num_list[i]):
            small_int = num_list[i]

    return small_int


my_list = [47, 88, 33, 44, 22, 55, 77]

print('Smallest Integer in list {int_list} is {smallest}'.format(
    int_list=my_list, smallest=smallest_int(my_list)))
