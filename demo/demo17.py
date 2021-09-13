# Dictionary

dictData ={"dog": "หมา", "cat": "แมว", "cat": "แมวแมว"}
print(dictData)
print(dictData["cat"])
print(dictData.get("dog"))
print(dictData.keys())
print(dictData.values())
print(len(dictData))

dictData["bird"] = "นก"
print(dictData)

dictData.pop("bird")
del dictData["dog"]
print(dictData)


