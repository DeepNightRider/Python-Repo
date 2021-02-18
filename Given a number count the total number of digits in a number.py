#Given a number count the total number of digits in a number

a=int(input('enter the number : '))
rem = 0
while(a>0):
    a = a // 10
    rem = rem + 1
print(rem)
