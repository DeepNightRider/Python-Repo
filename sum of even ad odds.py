#Write a program that reads a set of integers, and then prints the sum of the even and odd integers.

list=[11,112,113,4,5,100,101]
j = 0
k = 0

for i in list:
    if i % 2 == 0:
        j = j + i
    else:
        k = k + i
print("sum is :",j)
print("sum is :",k)
