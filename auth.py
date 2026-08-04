import getpass
from logger import logger

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

def login():
    username = input("Enteer User name:")
    password = getpass.getpass("Enter Password:")

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("login Successful")
        logger.info("Admin logged in successfully.")
        return True
    else:
        print("Invalid Username or Password!")
        logger.warning("Failed login attempt.")
        return False     
