#Write a program to calculate the sum of first 10 natural number.

n = int(input("enter any number : "))
sum = 0
for i in range(1,n+1):
    sum = sum + i
print(sum)