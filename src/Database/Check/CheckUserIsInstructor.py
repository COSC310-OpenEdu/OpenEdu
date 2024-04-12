from src.Database.Check.DatabaseCheck import DatabaseCheck
from src.Database.DatabaseManager import DatabaseManager
import mysql

class CheckUserIsInstructor(DatabaseCheck):
    
    #
    #   Checks if the given userId is an Instructor
    #   Input:  userId = The user being tests
    #   Ouput:  True if the user is an Instructor
    #           False otherwise
    #
 
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