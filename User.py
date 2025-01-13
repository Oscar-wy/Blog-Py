import uuid;
import Server as ServerModule

Database = ServerModule.Database()

class User:
    def __init__(self):
        self.Blogs = {}
        self.UUID = ""
        self.Username = "Test"
        self.Name = ""
        self.Password = ""
        self.SessionID = ""
        self.Server = ServerModule.ServerModule()
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
        if not UserExists:
            return False
        uuiD = uuid.uuid4().hex
        SessionID = uuid.uuid4().hex
        print(uuiD, SessionID)
        if not Database.SearchUser(uuiD):
            return False
        self.LogAssociate(UUID=uuiD, Username=Username, Name=Name, Password=Password, SessionID=SessionID)
        print(self)
        return self.Server.SignUpUser(self)