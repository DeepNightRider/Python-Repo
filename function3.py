# Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336
def multiple(list):
    mul = 1
    for i in list:
        mul =mul * i
    print(mul)

list=[8,2,3,-1,7]
multiple(list)