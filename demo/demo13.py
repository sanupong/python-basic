# Functions
def test1():
    print("call test")

def test2(x,y,z):
    print(x,y,z)

# Only Python3
def test3(x:int,y:str,z:bool):
    print(str(x),str(y),str(z))

def test4(a:int,b:int) -> float:
    return float(a+b), "ok"

test1()

test2(1,2,3)
test2(x=1,z=3,y=2)
test3(x=3, z=True,  y="ok")
print(test4(2,3))

data, result = test4(4,5)
print(data, result)