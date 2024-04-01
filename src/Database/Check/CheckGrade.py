from src.Database.Check.DatabaseCheck import DatabaseCheck
from src.Database.DatabaseManager import DatabaseManager
import mysql

class CheckGrade(DatabaseCheck):
    
    #
    #   Checks if a question with the specified information exists is in the database
    #   Input:      dataTuple = (grade, courseId, questionId, assignmentId, studentId)
    #   Output:     True if the grade exists
    #               False if the grade does not exist
    #
    @classmethod
    def check(cls, dataTuple):
        cursor = DatabaseManager.getDatabaseCursor()
        sql = "SELECT COUNT(grade) FROM Grades WHERE grade = %s AND courseId = %s AND questionId = %s AND assignmentId = %s AND studentId = %s"
        cursor.execute(sql, dataTuple)
        
        return cursor.fetchone()[0] != 0  