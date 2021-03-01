#Take two int values from user and print greatest among them.

a = int(input('enter the number : '))
b = int(input('enter the number : '))

if a > b:
    print(a,'is greater than',b)
elif b > a:
    print(b,'is greater than',a)
else:
    print(a, 'equal to',b)