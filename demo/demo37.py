# Elipsis (...) or tripple dots เทียบเท่า ใด ๆ 

def test():
    ... #แทน pass

def login(account:...) ->...: 
    print(account)
    print(account["username"])
    return {"result": "success"}

print("Hi")
acc = {"username": "admin", "password": "1234"}
login(acc)
result = login(acc)
print(result)



