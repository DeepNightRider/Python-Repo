# Python Program for factorial of a number
factorial=int(input())
if factorial ==0:
    print("1")
elif factorial == 1:
    print("1")
else:
    fact=1
    for i in range(1,factorial + 1):
        fact = fact * i
    print(fact)




