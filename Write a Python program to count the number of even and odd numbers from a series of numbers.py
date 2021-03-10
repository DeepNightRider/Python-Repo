#Write a Python program to count the number of even and odd numbers from a series of numbers

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
j = 0
k =0
for i in range(1,len(numbers)+1):
    if i % 2 == 0:
        j = j + 1

    else:
        k = k + 1

print(j,"even nos ",k ,"odd nos")
