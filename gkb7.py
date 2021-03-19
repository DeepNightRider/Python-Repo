# Python program to print all Prime numbers in an Interval

n = int(input())
if n >=2:
    print("2")
    print("3")
    for i in range(4,n+1):
        if i % 2 !=0 and i % 3 != 0:
            print(i)

