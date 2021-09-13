# Constructor

class User:
    username = ""
    password = ""

    def __init__(self): #constructor
        self.username = "admin"
        self.password = "1234"
        self.print()

    def __init__(self,username="admin",password="1234"): #constructor
        self.username = username
        self.password = password
        self.print()

    def print(self):
        print("created  : {}, {}".format(self.username,self.password))        

# Create an object from above class
user1 = User()
user2 = User("Pong","1111")






