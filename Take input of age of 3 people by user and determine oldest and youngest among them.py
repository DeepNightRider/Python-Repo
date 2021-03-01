#Take input of age of 3 people by user and determine oldest and youngest among them

a=int(input('enter the age : '))
b=int(input('enter the age : '))
c=int(input('enter the age : '))

if a > b and a >c:
    if  b < c:
        print(b,'youngest one')
    else:
        print(c,'youngest one')
    print(a,'oldest one')

elif b > a and b > c:
    if  c < a:
        print(c,'youngest one')
    else:
        print(a,'youngest one')
    print(b,'oldesst one')


elif c > a and c > b:
    if  b < a:
        print(b,'youngest one')
    else:
        print(a,'youngest one')
    print(c,'oldesst one')
