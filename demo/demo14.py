# Arbitary Argument Functions, *args

def test(printAll:bool,*courses):
    print(len(courses))
    if printAll:
        for c in courses:
            print(c)
    else:
        print(courses[0])

test(False,"Angulary", "React", "Vue","Python")