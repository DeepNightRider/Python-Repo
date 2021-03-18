a = int(input("enter the number : "))
p = a
b = a
digit = 0

while(b > 0):
    b = b // 10
    digit = digit + 1
print(digit)
result = 0
while(p > 0):
    r = p % 10
    result = result + (r ** digit)
    p = p // 10
print(result)

if result == a:
    print("Armstrong number")
else:
    print("not a armstrong number")