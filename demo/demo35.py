# Enum

import enum

class Course(enum.Enum):
    EnumAngular = "Angular + NodeJS"
    EnumVue = "VueJS + NodeJS"
    EnumReact = "ReactJS + Golang"

def register(course: Course):
    print("Register :" + course.value)

course: Course = Course.EnumAngular #สร้างตัวแปรรับ Enum
print(course.value)
course = course.EnumVue
print(course.value)
register(course)

if hasattr(Course,"EnumVue"): # hasattr เป็นการเช็คค่าใน Set ของ Enum
    print("Yes")
else:
    print("No")


