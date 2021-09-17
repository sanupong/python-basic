# * Asterisks  (unpack array) / Destructoring

numbers =[1,2,3]
anotherNumbers = [4,5,6]
allNumbers = [*numbers, *anotherNumbers]
print(allNumbers)

colorSet1 = {"Red": "#F00", "Green":"#0F0"}
colorSet2 = {"Yellow": "#FF0", "Blue":"#00F"}
allColors ={**colorSet1, **colorSet2}
print(allColors["Red"]) #Retreive Value

print(allNumbers)
print(*allNumbers)

def show(msg1, msg2, msg3):
    print(msg1)
    print(msg2)
    print(msg3)

show(*["Angular", "VueJS", "React"])

def test(*messages):
    print(len(messages))
    print(messages[1])

test("pong", "ning", "dontone")


