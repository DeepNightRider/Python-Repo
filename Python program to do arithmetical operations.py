# Python program to do arithmetical operations

# a=int(input("enter 1st number"))
# b=int(input("enter 2nd number"))
# c=int(input('''choose the option
# 1.addition
# 2.subtracction
# 3.multiplication
# 4.division'''))
# if c==1:
#     d=a+b
#     print(d)
# elif c==2:
#     d=a-b
#     print(d)
# elif c==3:
#     d=a*b
#     print(d)
# elif c==4:
#     d=a//b
#     print(d)
# else:
#     print("na")




# using function

def sum(a,b):
    sum=a+b
    return sum

def sub(a,b):
    sub=a-b
    return sub

def mul(a,b):
    mul=a*b
    return mul

def div(a,b):
    div=a//b
    return div

d=1

while(d!=0):
    a = int(input("enter 1st number"))
    b = int(input("enter 2nd  numbber"))
    c = int(input('''choose the option
    1.sum
    2.sub
    3.mul
    4.div'''))
    if c==1:
        print(sum(a,b))
    elif c==2:
        print(sub(a,b))
    elif c==3:
        print(mul(a,b))
    elif c==4:
        print(div(a,b))
    else:
        print("na")

    X=input('do you want to exit(Y/N)')
    if X == 'Y':
        d=1

    elif X=="N":
        d=0
        print()
        print("-------------------------------------------------------")
        print("Thanks for using program")
        print("have a nice day!!!")
        print("-------------------------------------------------------")






