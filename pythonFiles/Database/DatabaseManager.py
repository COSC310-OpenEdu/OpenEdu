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
    
    def commit(cls) -> None:
        if (cls.conn != None):
            cls.conn.commit();