import uuid;
import Server as ServerModule

Database = ServerModule.Database()
Server = ServerModule.Server()

class User:
    def __init__(self):
        self.Blogs = {}
        self.UUID = ""
        self.Username = "Test"
        self.Name = ""
        self.Password = ""
        self.SessionID = ""
        self.Server = Server
        self.Database = Database
    def LogAssociate(self, UUID, Username, Name, Password, SessionID):
        self.UUID = UUID
        self.Username = Username
        self.Name = Name
        self.Password = Password
        self.SessionID = SessionID
        self.Blogs = Database.GetUserBlogs(self.UUID)
    def Signup(self, Username, Name, Password):
        UserExists = Database.SearchUser(Username)
        if UserExists:
            return False
        uuiD = uuid.uuid4().hex
        SessionID = uuid.uuid4().hex
        print(uuiD, SessionID)
        if Database.SearchUser(uuiD):
            return False
        self.LogAssociate(UUID=uuiD, Username=Username, Name=Name, Password=Password, SessionID=SessionID)
        Server.SignUpUser(self)