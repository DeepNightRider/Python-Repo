# Write a Python program to remove the characters which have odd index values of a given string

st=input("enter string: ")
b=len(st)
c =''
for i in range(b):
    if i % 2 == 0:
        c = c + st[i]
d=c[1:]
print(d)
