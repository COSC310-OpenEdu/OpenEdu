from src.Database.Check.DatabaseCheck import DatabaseCheck
from src.Database.DatabaseManager import DatabaseManager
import pytest

class CheckAddQuestion(DatabaseCheck):
    
    #
    #   Check If a question exists in the database
    #   Input:  dataTuple = (questionId, assignmentId, courseId)
    #   Ouput:  If the question exists
    #
    
    @classmethod 
    def check(cls, dataTuple) -> bool:
        cursor = DatabaseManager.getDatabaseCursor()
        sql = "SELECT COUNT(questionId) FROM CourseRequests WHERE questionId = %s AND assignmentId = %s AND courseId = %s"
        cursor.execute(sql, dataTuple)
        
        return cursor.fetchone()[0] == 1;
        