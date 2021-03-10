#Write a Python program that prints each item and its corresponding type from the following list.

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

for i in range (len(datalist)):
    print(str(type(datalist[i]))[8:-2],"   " ,datalist[i])

print(type(datalist))