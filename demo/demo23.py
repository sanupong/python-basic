# Override to String function

class User:
    username = ""
    password = ""

    def __init__(self,username="admin",password="1234"): #constructor
        self.username = username
        self.password = password

    def __str__(self): #Override to (__str__) string function
        return "username: {}, Password: {}".format(self.username,self.password)
        
    def print(self):
        print("created  : {}, {}".format(self.username,self.password))        

# Create an object from above class
user1 = User("Pong","1111")
user1.print()
print(user1)
