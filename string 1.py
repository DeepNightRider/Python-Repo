# write a program that takes a string with multiple words and then capitalize the first letter
# of each word and forms a new string out of it.


st = input("Write anything : ")
b = st.split()
a =""
for i in b:
    a = a + " " +i.capitalize()
print(a[1:])


