# Write a Python function to find the Max of three numbers.
def max(a,b,c):
    print(a)
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    elif c > a and c >b:
        print(c)


a=int(input("enter any 1st number: "))
b=int(input("enter any 2nd number: "))
c=int(input("enter any 3rd number: "))
max(a,b,c)