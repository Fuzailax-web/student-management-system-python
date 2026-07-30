import getpass

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

def login():
    username = input("Enteer User name:")
    password = getpass.getpass("Enter Password:")

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("login Successful")
        return True
    else:
        print("Invalid Username or Password!")
        return False     
