from mysql import connector


class DatabaseManager:
    # User test database if in test mode
    test = False
    currentlyTestMode = False
    
    db_config = {
        'user': 'team',
        'password': 'COSC310Team',
        'host': '50.98.157.215',
        'port': '3306',
        'database': 'openEDU'
    }
    
    db_config_test = {
        'user': 'team',
        'password': 'COSC310Team',
        'host': '50.98.157.215',
        'port': '3306',
        'database': 'openEDUTest'
    }
    
    cur = None
    conn = None

    @classmethod
    def __init__(cls):
        cls.cur = None  # Cursor that access that database
        cls.conn = None

    @classmethod
    def createConnection(cls) -> None:
        # Creates the cursor. Each method will create a different statement
        if cls.test:
            cls.currentlyTestMode = True
            cls.conn = connector.connect(**cls.db_config_test)  # Test Mode
        else:
            cls.currentlyTestMode = False
            cls.conn = connector.connect(**cls.db_config)       # Normal Mode
        cls.cur = cls.conn.cursor()
        cls.conn.autocommit = True
    
    @classmethod
    def closeConnection(cls) -> None:
        cls.cur.close()
        cls.cur = None
        cls.conn.close()
        cls.conn = None

    @classmethod
    def getDatabaseConnection(cls):
        # Creates a new connection if one does not already exist or,
        # Switches to test mode if testmode is requested and the system is not already in test mode or,
        # Switches out of test mode if currently in test mode and system is requesting to use normal mode
        if cls.conn == None or (not cls.currentlyTestMode and cls.test) or (not cls.test and cls.currentlyTestMode):
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
            
            
    @classmethod
    def testMode(cls, boolean):
        cls.test = boolean
