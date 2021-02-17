# n=5
# fact=1
# for i in range(n,0,-1):
#     if i==1:
#         fact=fact*1
#     else:
#         fact=fact*i

# print(fact)


def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
x=fact(5)
print(x)
