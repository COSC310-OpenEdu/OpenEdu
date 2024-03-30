from src.Database.Check.DatabaseCheck import DatabaseCheck
from src.Database.DatabaseManager import DatabaseManager
import mysql

class CheckAssignmentCompletion(DatabaseCheck):
    @classmethod
    def check(self, dataTuple):
        sql = "SELECT questionId, studentAnswer FROM Solution WHERE courseId=%s and assignmentId=%s and studentId=%s"

        cursor = DatabaseManager.getDatabaseCursor();
        cursor.execute(sql, (dataTuple))
        completion = cursor.fetchall()
        DatabaseManager.closeConnection();
    
        if not completion:
            return False
        else:
            return completion