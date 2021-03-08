# Write a Python function to check whether a number is in a given range.
def check(num):
    if num >= 15 and num < 21:
        print("true")
    else:
        print("false")
num=int(input("enter any number : "))
check(num)