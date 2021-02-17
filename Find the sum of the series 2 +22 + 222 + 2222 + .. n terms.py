#Find the sum of the series 2 +22 + 222 + 2222 + .. n terms

n= int(input('number_of_terms = '))
a = 0
b = 10
sum = 0
for i in range(0,n):
    a = (2 * (b ** i) + a)
    sum = sum + a
print(sum)