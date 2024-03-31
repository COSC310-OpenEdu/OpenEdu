from src.Database.Check.DatabaseCheck import DatabaseCheck
from src.Database.DatabaseManager import DatabaseManager
import mysql

class CheckAssignmentExists(DatabaseCheck):

    #
    # Checks if an assignment exists.
    # Input : dataTuple = (courseId, assignmentId)
    # Output : False if assignment doesnt exists. True if it does.
    #

    @classmethod
    def check(self, dataTuple):
        statement = "SELECT assignmentId FROM Assignment WHERE courseId=%s and assignmentId=%s"

        cursor = DatabaseManager.getDatabaseCursor();
        cursor.execute(statement, (dataTuple))
        assignment = cursor.fetchall()
        DatabaseManager.closeConnection();
    
        if assignment is None:
            return False
        else:
            return True