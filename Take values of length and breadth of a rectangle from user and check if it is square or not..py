#Take values of length and breadth of a rectangle from user and check if it is square or not.

length = int(input('enter the number : '))
breadth = int(input('enter the number : '))

if length == breadth:
    print('square')
else:
    print('rectangle')