#Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish

n = int(input("enter the number : "))
sum = 0
for i in range(1,n+1):
    sum = sum + i
print(sum)
avg = sum//n
print(avg)