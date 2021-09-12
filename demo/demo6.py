# Multiple variable assignment declaration

def getData():
    return 10, 20, 30


x = y = z = 0
x1, y1, z1 = getData()

courses = ["Angular", "Python", "React"]
angulartitle, pythonTitle, reacttitle = courses

print(x, y, z)
print(x1, y1, z1)
print(angulartitle, pythonTitle, reacttitle)  # unpack array
