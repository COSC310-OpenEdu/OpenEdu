import mysql.connector
from mysql import connector, cursor, MySqlConnector;

class DatabaseManager:
    db_config = {
                'user': 'team',
                'password': 'COSC310Team',
                'host': '50.98.157.215',
                'port': '3306',
                'database': 'openEDU'
                }
    
    def __init__(cls):
        cls.cur = None #Cursor that access that database
        cls.conn = None

    def createConnection(cls) -> None:
        cls.conn = mysql.connector.connect(**cls.db_config) #Creates the cursor. Each method will create a different statement  
        cls.cur = cls.conn.cursor()
        

    def closeConnection(cls) -> None:
        cls.cur.close()
        cls.cur = None
        cls.conn.close()
        cls.conn = None

    def getDatabaseConnection(cls) -> MySqlConnector:
        if (cls.conn == None):
            cls.createConnection();
        return cls.conn;
    
    def getDatabaseCursor(cls) -> cursor:
        if (cls.cur == None):
            cls.createConnection();
        return cls.cur;
            
    
    def checkLogin(self, username, password) -> bool:
        
        
    def selectStudentUserPass(self, username, password):
        self.createConnection()
        statement = "SELECT * FROM User WHERE username = %s AND password = %s"
        self.cur.execute(statement, (username,password,))
        
        userData = self.cur.fetchone()

        return userData

        


    