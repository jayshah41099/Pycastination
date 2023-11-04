import getpass

database = {"roy":"582736", "jermie": "689765", "alex": "6574965"}

username = input("Enter your username: ")
password = getpass.getpass(" enter your password: ")
for i in database.keys():

    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Enter your password again: ")
        break

print (" User has been verified! Welcome to the Space!")
