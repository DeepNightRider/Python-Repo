# python program to convert Celsius to Fahrenheit
def celsius(C):
    F=C*9/5+32
    return F

C=int(input('enter the celsius'))
s = celsius(C)
print(s)
