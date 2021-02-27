# Write a Python program to change a given string to a new string where the first and last chars have been exchanged

st=input()
a=st[:1]
b=st[-1:]
x= b + st[1:-1] + a
print(x)