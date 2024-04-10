from src.Database.Check.DatabaseCheck import DatabaseCheck
from src.Database.DatabaseManager import DatabaseManager
import mysql

class CheckUserIsStudent(DatabaseCheck):
    
    #
    #   Checks if the given userId is an Student
    #   Input:  userId = The user being tests
    #   Ouput:  True if the user is an Student
    #           False otherwise
    #
    
    @classmethod
    def check(self, userId):
        statement = "SELECT userId FROM Student WHERE userId = %s"

        cursor = DatabaseManager.getDatabaseCursor();
        cursor.execute(statement, (userId,))
        userData = cursor.fetchone()
        DatabaseManager.closeConnection();
    
        if userData is None:
            return False
        else:
            return True