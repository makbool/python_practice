from datetime import datetime;

try: 
    x= int(input("Enter dividend : "));
    y = int (input("Enter divisor : "));
    
    print(x/y);
except ValueError:
    print('Dividend/Divisor is not a valid number');
except ZeroDivisionError as zde:
    print(zde);


try:
    birth_yr = int(input("Enter your Birth Year : "));
    print("Your Age is : ", datetime.now().year - birth_yr);
    
except ValueError as verr:
    print("Birth Year is not a number.", verr);


try:
    name = input("Enter Your Name : ");
    gender = input('Enter Your Gender (M/F/U) : ');
    if(gender == 'M' or gender == 'F' or gender == 'U') :
        print("Hello!!! ", name);
    else :
        raise Exception ('Invalid Gender', gender);
except Exception as ex:
    reason, value = ex.args;
    print(reason, ":", value);
