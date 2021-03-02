#Write a loop to find the factorial of any number

fact = int(input("enter the factorial of : "))
sum = 1
while (fact>0):
    if fact==0:
        print("1")
    sum = sum * fact
    fact = fact - 1
print(sum)

