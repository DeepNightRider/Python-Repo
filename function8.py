# Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]
def unique_elements(list):
    new =[]
    for i in list:
        if i not in new:
            new.append(i)
    print(new)
list=[1,2,3,3,3,3,4,5]
unique_elements(list)