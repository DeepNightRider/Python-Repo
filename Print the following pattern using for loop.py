#Print the following pattern using for loop
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

for i in range(6):
    k = 5-i
    for j in range(1,6-i):
        print(k,end=' ')
        k = k-1
    print()