def sumfun_old (x, y) : 
    return x+ y;

sumfun = lambda x, y : x + y;

print(sumfun_old(10,20));

print(sumfun(10,20));


num_list = [1,2,3,4,5,6,7,8,9];


def even_filter (x) :
    return x%2 == 0;

def square_mapper (x) :
    return x*x;


print(list(filter(even_filter, num_list)));

print(list(map(square_mapper,num_list)));



print(list(filter(lambda x: x%2 == 0, num_list)));

print(list(map(lambda x: x*x,num_list)));

