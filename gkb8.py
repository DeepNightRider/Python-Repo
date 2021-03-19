# Python program to check whether a number is Prime or not

i = int(input())
if  i ==2 or i ==3:
    print("prime number")
elif i % 2 != 0 and  i % 3 !=0:
    print("prime Number")
else:
    print("Not a Prime Number")