#Python program to display all the prime numbers within a range
x = 25
y =50
for i in range(x , y):
    if i == 2:
        print(i, 'Prime no')
    for j in range(2,i):

        if i % j == 0:
            k = 1
            break
        else:

