#Display the cube of the number up to a given integer

i = int(input('enter the number : '))

for i in range(1,i+1):
    cube = i**3
    print("current number : ", i ,"and the cube is ", cube)