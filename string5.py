# Write a Python program to get a string from a given string where all
# occurrences of its first char have been changed to '$',
# except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'


st=input("sample : ")

a = st[0]
s=st.replace(a,"$")
b = a + s
print(b[0:1] + b[2:])


