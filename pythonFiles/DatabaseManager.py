import mariadb

class DatabaseManager:
    
    def __init__(self):
        self.cur = None #Cursor that access that database
    
    
    def createConnection(self) -> None:

        conn = mariadb.connect(
                user="team",
                password="COSC310Team",
                host="50.98.157.215",
                port=3306,
                database='openEDU'
            )
        
        self.cur = conn.cursor() #Creates the cursor. Each method will create a different statement
    
    
    def closeConnection(self) -> None:
        self.cur.close()
        self.cur = None
        
        
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
        statement = "SELECT * FROM User WHERE userId = ?"
        self.cur.execute(statement, (userId,))
        
        studentData = self.cur.fetchone()
        self.closeConnection()
        return studentData
        
    

    