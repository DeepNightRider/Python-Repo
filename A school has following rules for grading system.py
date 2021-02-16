#A school has following rules for grading system

M = int(input('enter the marks : '))

if M > 80:
    print('A')
elif M > 60 and M <= 80:
    print('B')
elif M >50 and M <= 60:
    print('C')
elif M >45 and M <=50:
    print('D')
elif M >25 and M <=45:
    print('E')
else:
    print('F')