from pythonFiles.Database.Check.DatabaseCheck import DatabaseCheck
from pythonFiles.Database.DatabaseManager import DatabaseManager
import mysql

class UsernamePasswordCheck(DatabaseCheck):
    @classmethod
    def check(cls, dataTuple) -> bool:
        statement = "SELECT * FROM User WHERE username = %s AND password = %s"
        username, password = dataTuple;

        cursor = DatabaseManager.getDatabaseCursor();
        cursor.execute(statement, (username, password,))
        userData = cursor.fetchone()
        DatabaseManager.closeConnection();

        if userData is None:
            return False
        else:
            return True
