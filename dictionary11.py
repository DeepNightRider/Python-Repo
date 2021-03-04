# Get the key corresponding to the minimum value from the following dictionary
# sampleDict = {
#     'Physics': 82,
#     'Math': 65,
#     'history': 75
# }


sampleDict = {
    'Physics': 82,
    'Math': 15,
    'history': 75
}

print(max(sampleDict, key=sampleDict.get))
print(min(sampleDict, key=sampleDict.get))
# value == 65
# for i in sampleDict:
#     if sampleDict[i] == value:
#         print(i)