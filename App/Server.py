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
                      SELECT Username FROM User()
                      WHERE Username = ? OR UUID = ?;
                    """
              cursor.execute(sql, Values)
              result, = cursor.fetchone()
              if result == Field:
                  return True
              else:
                  return False
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
            

class Server:
    def __init__(self):
        self.Users = {}
    def SignUpUser(self, User):
        print(User.UUID)
    