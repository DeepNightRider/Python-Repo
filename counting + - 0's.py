# Write a program to enter the numbers till the user wants and at the end
# it should display the count of positive,
# negative and zeros entered.



c = 0
p = 0
z = 0
take ="y"
while take=="y":
    a = int(input("enter any number: "))
    if a > 0:
        c = c + 1
    elif a < 0:
        p = p + 1
    elif a == 0:
        z = z + 1

    take =input("do you want again(y,n):")
print("positive",c,"negative",p,"zeros",z)

