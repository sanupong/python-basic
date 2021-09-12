# Call Global Variable
tmp1 = "CodeMobiles"

def change():
    tmp1 = "Pong" # Local Variable
    print("tmp1 in change function : " + tmp1 )

def changeGlobal():
    global tmp1
    tmp1 = "Change Global tmp1"    

print(tmp1)
change()
print(tmp1)
changeGlobal()
print(tmp1)