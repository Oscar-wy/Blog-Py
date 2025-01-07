import uuid;
import Server

Database = Server.Database()

class User:
    def __init__(self):
        self.Blogs = {}
        self.UUID = ""
        self.Username = "Test"
        self.Name = ""
        self.Password
        self.SessionID = ""
    def LogAssociate(self, UUID, Username, Name, Password, SessionID):
        self.UUID = UUID
        self.Username = Username
        self.Name = Name
        self.Password = Password
        self.SessionID = SessionID
        self.Blogs = Database.GetUserBlogs()
    def Signup(self, Username, Name, Password):
        UserExists = Database.SearchUser(Username)
        if UserExists:
            return False
        uuiD = uuid.uuid4().hex
        SessionID = uuid.uuid4().hex
        print(uuiD, SessionID)
        if Database.SearchUser(uuiD):
            return False
        self.LogAssociate(uuiD, Username, Name, Password, SessionID)
        Server.SignUpUser(self)
        
tempUser = User
tempUser.Signup(tempUser, "Username", "Name", "Password")