import sqlite3

DATABASE = "./Backend/Data.db"

with sqlite3.connect(DATABASE) as db:
    cursor = db.cursor()
    sql = """
            CREATE TABLE IF NOT EXISTS User(
            UUID text UNIQUE,
            Username text,
            Name varchar(20),
            Password text,
            SessionIDs text,
            Primary key(UUID));
          """
    cursor.execute(sql)

class Database:
    def SearchUser(self, Field):
        try:
            Values = (Field, Field)
            with sqlite3.connect(DATABASE) as db:
                cursor = db.cursor()
                sql = """
                        SELECT Username FROM User
                        WHERE Username = ? OR UUID = ?;
                      """
                cursor.execute(sql, Values)
                result = cursor.fetchone()
                print(result)
                if result == Field:
                    return False
                else:
                    return True
        except sqlite3.Error as err:
            print(err)
            return False
    def GetUserBlogs(self, Field):
        try:
            Values = (Field, Field)
            with sqlite3.connect(DATABASE) as db:
                cursor = db.cursor()
                sql = """
                        SELECT Blogs FROM User
                        WHERE Username = ? OR UUID = ?;
                      """
                cursor.execute(sql, Values)
                result, = cursor.fetchone()
                return result
        except:
            return False
    def CreateUser(self, user):
        try:
            Values = (user.UUID, user.Username, user.Name, user.Password, user.SessionID)
            with sqlite3.connect(DATABASE) as db:
                cursor = db.cursor()
                sql = """
                        INSERT INTO User(UUID, Username, Name, Password, SessionIDs)
                        Values(?, ?, ?, ?, ?)
                      """
                cursor.execute(sql, Values)
                return True
        except sqlite3.Error as err:
            print(err)
            return False
            
class ServerModule:
    def __init__(self):
        self.Users = {}
        self.Db = Database()
    def SignUpUser(self, User):
        if self.Db.CreateUser(User):
            return True
        else:
            return False
    def SearchUser(self, Field):
        return self.Db.SearchUser(Field)