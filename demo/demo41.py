# None, Null, Undefined

tmp1 = True
tmp2 = False
# tmp3 = True
tmp4 = None

print(tmp1)
print(tmp2)

try:
    print(tmp3)
except:
    print("tmp3 undefined")

if tmp4 != None:
    print("tmp4 not is None")
else:
    print(tmp4)

print(type(tmp4))