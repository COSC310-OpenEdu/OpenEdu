from src.Database.Check.DatabaseCheck import DatabaseCheck
from src.Database.DatabaseManager import DatabaseManager
import mysql

class CheckAssignmentCompletion(DatabaseCheck):
    
    #
    #   Checks whether an assignment is complete
    #   Input:  dataTuple = (courseId, assignmentId, studentId)
    #   Output:    returns solutions if the assignment is complete
    #              False otherwise
    
    
    @classmethod
    def check(self, dataTuple):
        sql = "SELECT questionId, studentAnswer, studentId FROM Solution WHERE courseId=%s and assignmentId=%s and studentId=%s"

        cursor = DatabaseManager.getDatabaseCursor();
        cursor.execute(sql, (dataTuple))
        completion = cursor.fetchall()
        DatabaseManager.closeConnection();
    
        if not completion:
            return False
        else:
            return completion