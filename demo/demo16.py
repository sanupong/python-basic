# List

dataList1 = ["Angular","VueJS","React"] #implicit
dataList2: list = ["Angular","VueJS","React"] #explicit
dataList3 = list(("Angular","VueJS","React")) #constructor


print(dataList1)
print(dataList2)
print(type(dataList2))
print(dataList3)

extraArray =["Raspberry Pi", "Flutter"]
dataList1.append("Python")
dataList1.extend(extraArray)
print(dataList1)
dataList1.insert(1,"C#")
print(dataList1)
dataList1.remove("C#")
print(dataList1)
dataList1.pop() # เอาตัวท้ายออก
dataList1.pop()
print(dataList1)
dataList1.clear()
print(dataList1)
#del dataList2

print(dataList2[0])








