# Tuple -> (), List -> [] , Set -> {} , Dectionary { "Field": "Value"}

colors = ["Red", "Green", "Blue"]
print(colors)
colors[0] = "Yellow"
print(colors)

courses = ("Angular", "VueJS", "React", "Python", "Python")
print(courses)
print(courses[0])
try:
    courses[0] = "NodeJS"
except TypeError:
    print("'tuple' object does not support item assignment")

print(len(courses))

courses2 = tuple(("Angular", "VueJS", "React", "Python", "Python"))
print(courses2)




