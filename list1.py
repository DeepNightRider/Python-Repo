# Write a Python program to sum all the items in a list

a=[int(i) for i in input( ).split()]
print(a)
sum=0
for i in a:
    sum = sum + i
print(sum)