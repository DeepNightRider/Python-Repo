# Write a Python program to remove the nth index character from a nonempty string

a=input("sample: ")
n=int(input("nth number"))
c=a[0:n]+a[n+1:]
print(c)

