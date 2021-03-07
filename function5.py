# Write a Python function to calculate the factorial of a number (a non-negative integer).
# The function accepts the number as an argument.
def fact(num):
    if num == 0:
        print("1")
    elif num ==1:
        print("1")
    else:
        fac=1
        for i in range(2,num + 1):
            fac = fac * i
        print(fac)

num = int(input("enter the number : "))
fact(num)

