# Use a loop to display elements from a given list which are present at even positions

my_list = [10,20,30,40,50,60,70,80,90,100]
for i in range (1,len(my_list),2):
    # if i % 2 == 1:
    print(my_list[i], end=' ')
    # print()