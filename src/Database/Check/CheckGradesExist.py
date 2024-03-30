from src.Database.Check.DatabaseCheck import DatabaseCheck
from src.Database.DatabaseManager import DatabaseManager
import mysql

class CheckGradesExist(DatabaseCheck):
    @classmethod
    def check(self, dataTuple):
        sql = "SELECT studentId FROM Grades WHERE courseId=%s and questionId=%s and assignmentId=%s and studentId=%s"

        cursor = DatabaseManager.getDatabaseCursor();
        cursor.execute(sql, (dataTuple))
        check = cursor.fetchall()
        DatabaseManager.closeConnection();
    
        return check