
# Write a program to print out all Armstrong numbers between 1 and 500.
# If sum of cubes of each digit of the number is equal to the number itself,
# then the number is called an Armstrong number.
# For example, 153 = ( 1 * 1 * 1 ) + ( 5 * 5 * 5 ) + ( 3 * 3 * 3 )

a = int(input("enter the number : "))
p = a
b = a
rem = 0

while(b > 0):
    b = b // 10
    rem = rem + 1
print(rem)
result = 0
while(p > 0):
    r = p % 10
    result = result + (r ** rem)
    p = p // 10
print(result)

if result == a:
    print("Armstrong number")
else:
    print("not a armstrong number")


