# Write a Python program to count the number of strings where the string length
# is 2 or more and the first and last character are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

a=[b for b in input("enter the number : ").split(' ') ]
print(a)
x = 0
for i in a:
    if len(i) > 2 and i[0] == i[-1]:
        x = x + 1

    else:
        print("try again")

print(x)