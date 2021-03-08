# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12
def calculate(string):
    countu = 0
    countl = 0
    for i in string:

        if i.isupper():
            countu = countu + 1

        elif i.islower():
            countl = countl + 1

    print(countu)
    print(countl)

string=input("sample string : ")
calculate(string)