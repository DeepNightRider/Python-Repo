#Display Fibonacci series up to 10 terms

n= 10
a = 0
b = 1
print(a,end=' ')
print(b,end=' ')
for i in range(0,n-2):
    c = a + b
    a = b
    b = c
    print(c,end=' ')