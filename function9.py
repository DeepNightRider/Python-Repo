# Write a Python function that takes a number as a parameter and check the number is prime or not.
# Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors
# other than 1 and itself.
def prime(num):
    for i in range(2,num//2):
        if num % i == 0:
            print("not prime")
            break
    else:
        print("prime")

num=int(input("enter any number : "))
prime(num)