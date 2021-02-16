a = 1634
c = a
# def lenfind(b):
#     i = 0
#     while(b!=0):
#         i =i +1
#         b = b // 10
#     return i


# def lenfind(b):
#     return len(str(b))



sum = 0
i = len(str(c))
while (a != 0 ):

    s = a %10
    a = a // 10
    sum = sum + (s**i)
print(sum)
if sum == c :
    print('ARMSTRONG')
else:
    print("NOT ARMSTRONG")

# print(lenfind(a))



