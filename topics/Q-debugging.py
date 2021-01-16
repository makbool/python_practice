# Write a program to create a function which accepts an integer
# displays output based on the below scenarios

# display Fizz if integer value is divisible by 3
# display Buzz if integer value is divisible by 5
# display FizzBuzz if integer value is divisible by 3 and 5
# display the same number if not divisible by 3 or 5


def fizzbuzz(a):
    if(a % 3 == 0 and a % 5 == 0):
        return("FIZZBUZZ")
    elif(a % 5 == 0):
        return("BUZZ")
    elif(a % 3 == 0):
        return("FIZZ")
    else:
        return a


a = int(input('enter a number : '))
print(fizzbuzz(a))


# Step Over  => executes the line of statement and moves debug to Next Statement
# Step Into => debugs into the current statement
# Step out => Comes out of the function which is currently running and moves to the next statement after the function call
