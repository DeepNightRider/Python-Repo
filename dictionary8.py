# Delete set of keys from Python Dictionary
# Given:
#
# sampleDict = {
#     "name": "Kelly",
#     "age":25,
#     "salary": 8000,
#     "city": "New york"
#
# }
# keysToRemove = ["name", "salary"]

sampledict = {
    "name": "Kelly",
    "age":25,
    "salary": 8000,
    "city": "New york"

}
keys=['age','salary']
dict={k: sampledict[k] for k in keys}
print(dict)