import mariadb

class DatabaseManager:
    
    def __init__(self):
        self.cur = None #Cursor that access that database
    
    
    def createConnection(self):

        conn = mariadb.connect(
                user="team",
                password="COSC310Team",
                host="50.98.157.215",
                port=3306,
                database='openEDU'
            )
        
        self.cur = conn.cursor() #Creates the cursor. Each method will create a different statement
    
    def closeConnection(self):
        self.cur.close()
        self.cur = None
        
    
    def viewStudents(self):
        self.createConnection()
        
        statement = "SELECT firstName, lastName from User"
        self.cur.execute(statement)
        
        
    

    