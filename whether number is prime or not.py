#Write a program that prompts the user to input a positive integer. It should then output a message indicating whether the number is a prime number.


a = int(input("enter any number : "))
k =1
if a < 2:
    k = 0

elif a == 2:
    k = 1
else:
    for i in range(2,a//2):
        if a % i == 0:
            k = 0
            break
        else:
            k= 1

if k == 1:
    print("prime")
elif k == 0:
    print('not prime')