import random
from App import User as UserModule

User = UserModule.User()

def Signup():
    NoUser = False
    while not NoUser:
        Username = input("Enter A Username: ")
        NoUser = User.Server.SearchUser(Username)
        if NoUser:
            print("Username Exists")
    Name = input("Enter Name: ")
    Password = input("Enter Password: ")
    User.Signup(Username, Name, Password)