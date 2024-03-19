from src.Database.Check.DatabaseCheck import DatabaseCheck
from src.Database.DatabaseManager import DatabaseManager
import mysql

class CheckUserIsInstructor(DatabaseCheck):
    @classmethod
    def check(self, userId):
        statement = "SELECT userId FROM Instructor WHERE userId = %s"

        cursor = DatabaseManager.getDatabaseCursor();
        cursor.execute(statement, (userId,))
        userData = cursor.fetchone()
        DatabaseManager.closeConnection();
    
        if userData is None:
            return False
        else:
            return True