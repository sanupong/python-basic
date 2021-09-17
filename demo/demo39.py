# ** Double Asterisks (unpack dictional)

def login(username, password):
    print("{0}, {1}".format(username, password))

login("admin","1234")

acc = {"username": "admin", "password": "555"}
login(acc["username"],acc["password"])
login(**acc)
