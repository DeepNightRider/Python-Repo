#Write a Python program to get the Fibonacci series between 0 to 50

fib=int(input("enter any number : "))
a = 0
b = 1
print("0",end=" ")
print("1",end=" ")
for i in range(2,fib+1):
    c = a + b
    a = b
    b = c
    print(c,end=" ")



