#Write a program that prompts the user to input an integer and then outputs the number with the digits reversed. For example, if the input is 12345, the output should be 54321.

x=int(input("INPUT : "))
rev = 0
while(x>0):
    rem = x % 10
    rev = (rev * 10) + rem
    x = x // 10
print(rev)