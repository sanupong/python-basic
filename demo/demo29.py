# Private function & Public Function

class User:
    username = "" 
    password = ""

    def __init__(self, username="admin", password="1234"): # Constructor
        self.username = username
        self.password = password
    
    def clear(self): #public function
        print("clear")
        self.__privateClear()
    
    def __privateClear(self): #private function
        print("private clear")

user = User()
user.clear()
