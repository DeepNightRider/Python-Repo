# Python program to solve quadratic equation
import cmath
a=int(input('enter the number'))
b=int(input('enter the number'))
c=int(input('ennter the nuumber'))
d=(b**2)-(4*a*c)
print(d)

y1=(-b-cmath.sqrt(d))/(2*a)
y2=(-b+cmath.sqrt(d))/(2*a)
print(y1)
print(y2)