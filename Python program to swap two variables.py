# Python program to swap two variables

# a=8
# b=5
# print('a',a)
# print('b',b)
# c=a
# a=b
# b=c
# print(a,'a')
# print(b,'b')



def swap(a,b):
    c=a
    a=b
    b=c
    return (a,b)
a=int(input('enter the number'))
b=int(input('enter the number'))
a,b = swap(a,b)
print(a)
print(b)


