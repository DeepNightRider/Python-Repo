# Create a new dictionary by extracting the following keys from a given dictionary
# Given dictionary:
#
# sampleDict = {
#     "name": "Kelly",
#     "age":25,
#     "salary": 8000,
#     "city": "New york"
#
# }

sampleDict = {
    "name": "Kelly",
    "age":25,
    "salary": 8000,
    "city": "New york"

}

# del sampleDict["age"]
# del sampleDict["city"]
# print(sampleDict)
# print(['name'])

keys=['name','salary']
Dict={k: sampleDict[k] for k in keys}
print(Dict)


