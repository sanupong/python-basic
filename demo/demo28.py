# self and static method

class User:
    username = "" 
    password = ""

    def __init__(self, username="admin", password="1234"):
        self.username = username
        self.password = password

    @staticmethod # บอกว่า function นี้เป็น static method
    def test():
        print("5678")

User.test() # เรียกตรง ๆ ได้เลย ไม่ต้องประกาศ Object

user = User()
print(user.username)