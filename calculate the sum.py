# Write a program to calculate the sum of following series where n is input by user.
# 1 + 1/2 + 1/3 + 1/4 + 1/5 +…………1/n

a =int(input("enter the number : "))
c =  0
for i in range(1,a+1):
    c = c + 1/i
print(c)