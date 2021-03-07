# Write a Python function to check whether a number is perfect or not.
def perfect(num):
    sum = 0
    k = 0
    for i in range(1,num//2 + 1):
        if num % i == 0:
            print(i)
            sum = sum + i
            if num == sum:
                k =0
                pass
            else:
                k = 1
    if k == 0:
        print("perfect number")
    elif k == 1:
        print("not a perfect number")
num = int(input("enter the number : "))
perfect(num)