#Write a program to find the factorial value of any number entered through the keyboard
n=5
fact=1
for i in range(0,n,-1):
    if i==1 or i==0:
        fact=fact*1
    else:
        fact=fact*i

print(fact)