
a= input("eneter numbers : ")
n = a.split(',')

p =0
t=0
z=0
for i in n:
    if int(i) > 0:
        p = p + 1
    elif int(i) < 0:
        t = t + 1
    else:
        z = z + 1


print("+ve",p,"-ve",t,"zeros",z)




