# Delete Object


class User:
    username = ""
    password = ""

    def __init__(self,username="admin",password="1234"): #constructor
        self.username = username
        self.password = password
        self.print()

    def print(self):
        print("created  : {}, {}".format(self.username,self.password))        

# Create an object from above class

user1 = User("Pong","1111")

print(user1.username)
# del user1.username   
# del user1.password
# print("After delete object :", user1.username)
del user1
user1.print()


