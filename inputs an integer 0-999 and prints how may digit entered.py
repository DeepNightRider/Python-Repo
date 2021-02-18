
def findlen(d):
    i=0
    while(d!=0):
        d=d//10
        i=i+1
    return i

a=int(input('enter the number'))

print(findlen(a))