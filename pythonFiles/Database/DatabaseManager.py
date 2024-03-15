from mysql import connector


class DatabaseManager:
    db_config = {
        'user': 'team',
        'password': 'COSC310Team',
        'host': '50.98.157.215',
        'port': '3306',
        'database': 'openEDU'
    }
    cur = None
    conn = None

    @classmethod
    def __init__(cls):
        cls.cur = None  # Cursor that access that database
        cls.conn = None

    @classmethod
    def createConnection(cls) -> None:
        cls.conn = connector.connect(
            **cls.db_config)  # Creates the cursor. Each method will create a different statement
        cls.cur = cls.conn.cursor()
    
    @classmethod
    def closeConnection(cls) -> None:
        cls.cur.close()
        cls.cur = None
        cls.conn.close()
        cls.conn = None

    @classmethod
    def getDatabaseConnection(cls):
        if (cls.conn == None):
            cls.createConnection();
        return cls.conn;

    @classmethod
    def getDatabaseCursor(cls):
        if (cls.cur == None):
            cls.createConnection();
        return cls.cur;

    @classmethod
    def commit(cls) -> None:
        if (cls.conn != None):
            cls.conn.commit();
