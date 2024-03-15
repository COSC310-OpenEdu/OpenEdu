import mysql.connector

class DatabaseManager:
    
    def __init__(self):
        self.cur = None #Cursor that access that database
        self.conn = None
    
    def createConnection(self) -> None:
        db_config = {
                    'user': 'team',
                    'password': 'COSC310Team',
                    'host': '50.98.157.215',
                    'port': '3306',
                    'database': 'openEDU'
                    }
        self.conn = mysql.connector.connect(**db_config) #Creates the cursor. Each method will create a different statement  
        self.cur = self.conn.cursor()
        
    
    def closeConnection(self) -> None:
        self.cur.close()
        self.cur = None
        self.conn.close()
        self.conn = None
             
    #View All Users in Database
    def viewStudents(self) -> list:
        self.createConnection()
        
        statement = "SELECT firstName, lastName from User"
        self.cur.execute(statement)
        
        studentData = self.cur.fetchall()
        self.closeConnection()
        return studentData
    
    #Get all information about one specific user 
    def selectStudent(self, userId) -> tuple:
        
        if not isinstance(userId, int): #Only allow userId to be an integer
            return None
        
        self.createConnection()
        statement = "SELECT * FROM User WHERE userId = %s"
        self.cur.execute(statement, (userId,))
        
        studentData = self.cur.fetchone()
        self.closeConnection()
        return studentData
    
    def checkLogin(self, username, password) -> bool:
        self.createConnection()
        statement = "SELECT * FROM User WHERE username = %s AND password = %s"
        self.cur.execute(statement, (username,password,))
        
        userData = self.cur.fetchone()
        self.closeConnection()

        if userData is None:
            return False
        else:
            return True
        
    def selectStudentUserPass(self, username, password):
        self.createConnection()
        statement = "SELECT * FROM User WHERE username = %s AND password = %s"
        self.cur.execute(statement, (username,password,))
        
        userData = self.cur.fetchone()

        return userData

        


    