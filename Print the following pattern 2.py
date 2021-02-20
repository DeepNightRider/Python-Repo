# Print the following pattern

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
for i in range(6):
    for j in range(1,i+1):
        print('*',end=' ')
    print()
for i in range(5):
    for j in range(1,5-i):
        print('*',end=' ')
    print()