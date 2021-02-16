#Accept number from user and calculate the sum of all number between 1 and given number

x=int(input("enter any number : "))
c=0
for i in range(1,x+1):
    c = c + i
print(c)
