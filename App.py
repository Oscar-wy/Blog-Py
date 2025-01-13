import random
import User as userModule

if __name__ == "__main__":
    User = userModule.User()

    def Signup():
        NoUser = False
        while not NoUser:
            Username = input("Enter A Username: ")
            NoUser = User.Server.SearchUser(Username)
            if not NoUser:
                print("Username Exists")
        Name = input("Enter Name: ")
        Password = input("Enter Password: ")
        print(User.Signup(Username, Name, Password))
    
    Signup()